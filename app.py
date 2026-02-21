import streamlit as st
import random
from questions import get_questions_by_level

# ──────────────────────────────────────────
# ページ設定
# ──────────────────────────────────────────
st.set_page_config(page_title="ことばクイズ", page_icon="📚", layout="centered")

# ──────────────────────────────────────────
# セッション状態の初期化
# ──────────────────────────────────────────
def init_state():
    """session_state に必要なキーがなければ初期値をセットする"""
    defaults = {
        "screen": "top",        # top / quiz / result
        "level": None,          # easy / normal / hard
        "questions": [],        # 出題する問題リスト（シャッフル済み）
        "current": 0,           # 現在の問題番号（0始まり）
        "score": 0,             # 正解数
        "answers": [],          # ユーザーの回答履歴 {"question":..., "answer":..., "correct":...}
        "shuffled_choices": [], # 現在の問題の選択肢（シャッフル済み）
        "answered": False,      # 今の問題に回答済みか
        "last_correct": None,   # 直前の回答が正解だったか
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

init_state()

# ──────────────────────────────────────────
# ヘルパー関数
# ──────────────────────────────────────────
LEVEL_LABELS = {
    "easy":   "⭐ やさしい（1〜2年生）",
    "normal": "⭐⭐ ふつう（2〜3年生）",
    "hard":   "⭐⭐⭐ むずかしい（3〜4年生）",
}

def start_quiz(level: str):
    """レベルを選んでクイズを開始する"""
    qs = get_questions_by_level(level)
    random.shuffle(qs)
    st.session_state.level = level
    st.session_state.questions = qs
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.answered = False
    st.session_state.last_correct = None
    _set_choices(qs[0])
    st.session_state.screen = "quiz"

def _set_choices(q: dict):
    """問題の選択肢をシャッフルして session_state に保存する"""
    choices = q["choices"][:]
    random.shuffle(choices)
    st.session_state.shuffled_choices = choices

def answer(selected: str):
    """回答ボタンが押されたときの処理"""
    if st.session_state.answered:
        return
    q = current_question()
    correct = selected == q["answer"]
    if correct:
        st.session_state.score += 1
    st.session_state.answers.append({
        "question": q,
        "selected": selected,
        "correct": correct,
    })
    st.session_state.answered = True
    st.session_state.last_correct = correct

def next_question():
    """次の問題へ進む（最後なら結果画面へ）"""
    st.session_state.current += 1
    if st.session_state.current >= len(st.session_state.questions):
        st.session_state.screen = "result"
    else:
        q = st.session_state.questions[st.session_state.current]
        _set_choices(q)
        st.session_state.answered = False
        st.session_state.last_correct = None

def current_question() -> dict:
    return st.session_state.questions[st.session_state.current]

def reset():
    """トップ画面に戻る"""
    st.session_state.screen = "top"

# ──────────────────────────────────────────
# 画面1: トップ画面
# ──────────────────────────────────────────
def show_top():
    st.title("📚 ことばクイズ")
    st.write("レベルを えらんで、スタート！")
    st.markdown("---")

    for level, label in LEVEL_LABELS.items():
        if st.button(label, use_container_width=True, key=f"btn_{level}"):
            start_quiz(level)
            st.rerun()

# ──────────────────────────────────────────
# 画面2: クイズ画面
# ──────────────────────────────────────────
def show_quiz():
    q = current_question()
    total = len(st.session_state.questions)
    current_idx = st.session_state.current  # 0始まり

    # ── 進捗バー・ヘッダー ──
    st.progress((current_idx) / total)
    col_l, col_r = st.columns([3, 1])
    with col_l:
        st.write(f"**もんだい {current_idx + 1} / {total}**　"
                 f"レベル：{LEVEL_LABELS[st.session_state.level]}")
    with col_r:
        st.write(f"✅ {st.session_state.score}もん せいかい")

    st.markdown("---")

    # ── 絵文字・ヒント ──
    if q["emoji"]:
        st.markdown(f"<div style='font-size:80px; text-align:center'>{q['emoji']}</div>",
                    unsafe_allow_html=True)
    st.markdown(f"### {q['hint']}")
    st.markdown("")

    # ── 選択肢ボタン ──
    answered = st.session_state.answered
    for choice in st.session_state.shuffled_choices:
        # 回答済みのとき：正解は緑、不正解の選択肢は赤でハイライト
        if answered:
            if choice == q["answer"]:
                st.success(f"⭕ {choice}")
            elif choice == st.session_state.answers[-1]["selected"] and not st.session_state.last_correct:
                st.error(f"❌ {choice}")
            else:
                st.button(choice, disabled=True, key=f"choice_{choice}", use_container_width=True)
        else:
            if st.button(choice, key=f"choice_{choice}", use_container_width=True):
                answer(choice)
                st.rerun()

    # ── 正誤フィードバック → 次へボタン ──
    if answered:
        st.markdown("---")
        if st.session_state.last_correct:
            st.markdown("## 🎉 せいかい！")
        else:
            st.markdown(f"## 😢 ざんねん…　こたえは **{q['answer']}** だよ！")

        label = "つぎの もんだいへ →" if current_idx + 1 < total else "けっかを みる 🏁"
        if st.button(label, use_container_width=True, type="primary"):
            next_question()
            st.rerun()

# ──────────────────────────────────────────
# 画面3: 結果画面
# ──────────────────────────────────────────
def show_result():
    total = len(st.session_state.questions)
    score = st.session_state.score
    ratio = score / total

    st.title("🏁 けっか はっぴょう！")
    st.markdown(f"## {score} / {total} もん せいかい")

    if ratio == 1.0:
        st.balloons()
        st.success("🌟 ぜんもん せいかい！ すごい！！")
    elif ratio >= 0.7:
        st.success("👏 よく できました！")
    elif ratio >= 0.4:
        st.warning("💪 もう すこし！ もう いちど チャレンジ してみよう！")
    else:
        st.error("📖 もんだいを よく よんで、もう いちど チャレンジ してみよう！")

    st.markdown("---")
    st.markdown("### 📋 こたえ あわせ")

    for i, rec in enumerate(st.session_state.answers):
        q = rec["question"]
        mark = "⭕" if rec["correct"] else "❌"
        with st.expander(f"{mark} もんだい{i+1}：{q['hint'][:20]}…"):
            if q["emoji"]:
                st.write(q["emoji"])
            st.write(f"**ヒント：** {q['hint']}")
            st.write(f"**あなたの こたえ：** {rec['selected']}")
            st.write(f"**せいかい：** {q['answer']}")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 もう いちど おなじ レベルで", use_container_width=True):
            start_quiz(st.session_state.level)
            st.rerun()
    with col2:
        if st.button("🏠 レベル えらびに もどる", use_container_width=True):
            reset()
            st.rerun()

# ──────────────────────────────────────────
# 画面の切り替え
# ──────────────────────────────────────────
screen = st.session_state.screen

if screen == "top":
    show_top()
elif screen == "quiz":
    show_quiz()
elif screen == "result":
    show_result()
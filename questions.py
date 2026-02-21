# questions.py
# ことばクイズ　問題データ
# キー一覧:
#   emoji       : 絵文字（やさしい・ふつうレベルで表示）
#   hint        : ヒント文（プレーンテキスト）
#   hint_ruby   : フリガナ付きヒント文（HTMLのrubyタグ使用）
#   answer      : 正解の文字列
#   choices     : 選択肢4つのリスト（正解を含む）
#   choices_ruby: 選択肢に（フリガナ）を付けた辞書 {"元の選択肢": "表示文字列"}
#   level       : "easy" / "normal" / "hard"

QUESTIONS = [

    # ──────────────────────────────────────────
    # やさしい（1〜2年生）
    # ひらがな中心・フリガナ不要
    # ──────────────────────────────────────────
    {
        "emoji": "🐘",
        "hint": "はなが とても ながい どうぶつは？",
        "hint_ruby": "はなが とても ながい どうぶつは？",
        "answer": "ぞう",
        "choices": ["ぞう", "きりん", "うま", "くま"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "🍎",
        "hint": "あかくて あまい くだものは？",
        "hint_ruby": "あかくて あまい くだものは？",
        "answer": "りんご",
        "choices": ["りんご", "みかん", "ぶどう", "もも"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "🌸",
        "hint": "はるに さく ピンクの はなは？",
        "hint_ruby": "はるに さく ピンクの はなは？",
        "answer": "さくら",
        "choices": ["さくら", "たんぽぽ", "あさがお", "ひまわり"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "🐟",
        "hint": "みずの なかを およぐ いきものは？",
        "hint_ruby": "みずの なかを およぐ いきものは？",
        "answer": "さかな",
        "choices": ["さかな", "かめ", "かえる", "とり"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "🌙",
        "hint": "よるの そらに ひかる まるい ものは？",
        "hint_ruby": "よるの そらに ひかる まるい ものは？",
        "answer": "つき",
        "choices": ["つき", "ほし", "たいよう", "くも"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "🚌",
        "hint": "おおぜいの ひとを はこぶ おおきな くるまは？",
        "hint_ruby": "おおぜいの ひとを はこぶ おおきな くるまは？",
        "answer": "バス",
        "choices": ["バス", "タクシー", "トラック", "でんしゃ"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "✏️",
        "hint": "じを かくときに つかう ほそながい ものは？",
        "hint_ruby": "じを かくときに つかう ほそながい ものは？",
        "answer": "えんぴつ",
        "choices": ["えんぴつ", "はさみ", "のり", "じょうぎ"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "🐸",
        "hint": "みずの ちかくに いて「ケロケロ」と なく いきものは？",
        "hint_ruby": "みずの ちかくに いて「ケロケロ」と なく いきものは？",
        "answer": "かえる",
        "choices": ["かえる", "へび", "とかげ", "やもり"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "☂️",
        "hint": "あめの ひに さして つかう ものは？",
        "hint_ruby": "あめの ひに さして つかう ものは？",
        "answer": "かさ",
        "choices": ["かさ", "ぼうし", "てぶくろ", "マフラー"],
        "choices_ruby": {},
        "level": "easy",
    },
    {
        "emoji": "🍙",
        "hint": "のりで まいた、ごはんの たべものは？",
        "hint_ruby": "のりで まいた、ごはんの たべものは？",
        "answer": "おにぎり",
        "choices": ["おにぎり", "すし", "パン", "うどん"],
        "choices_ruby": {},
        "level": "easy",
    },

    # ──────────────────────────────────────────
    # ふつう（2〜3年生）
    # ──────────────────────────────────────────
    {
        "emoji": "🚒",
        "hint": "火事のとき かけつけて、水を かける 赤い 車は？",
        "hint_ruby": "<ruby>火事<rt>かじ</rt></ruby>のとき かけつけて、<ruby>水<rt>みず</rt></ruby>を かける <ruby>赤<rt>あか</rt></ruby>い <ruby>車<rt>くるま</rt></ruby>は？",
        "answer": "消防車",
        "choices": ["消防車", "救急車", "パトカー", "ごみ収集車"],
        "choices_ruby": {
            "消防車":   "消防車（しょうぼうしゃ）",
            "救急車":   "救急車（きゅうきゅうしゃ）",
            "ごみ収集車": "ごみ収集車（しゅうしゅうしゃ）",
        },
        "level": "normal",
    },
    {
        "emoji": "🦋",
        "hint": "いもむしが さなぎに なって、羽が はえた 虫は？",
        "hint_ruby": "いもむしが さなぎに なって、<ruby>羽<rt>はね</rt></ruby>が はえた <ruby>虫<rt>むし</rt></ruby>は？",
        "answer": "チョウ",
        "choices": ["チョウ", "トンボ", "セミ", "カブトムシ"],
        "choices_ruby": {},
        "level": "normal",
    },
    {
        "emoji": "🌊",
        "hint": "海や 川で 水が 高く もり上がって おしよせる ものは？",
        "hint_ruby": "<ruby>海<rt>うみ</rt></ruby>や <ruby>川<rt>かわ</rt></ruby>で <ruby>水<rt>みず</rt></ruby>が <ruby>高<rt>たか</rt></ruby>く もり<ruby>上<rt>あ</rt></ruby>がって おしよせる ものは？",
        "answer": "なみ",
        "choices": ["なみ", "かわ", "みずうみ", "たき"],
        "choices_ruby": {},
        "level": "normal",
    },
    {
        "emoji": "🍦",
        "hint": "冷たくて 甘い、コーンに のせて 食べる おやつは？",
        "hint_ruby": "<ruby>冷<rt>つめ</rt></ruby>たくて <ruby>甘<rt>あま</rt></ruby>い、コーンに のせて <ruby>食<rt>た</rt></ruby>べる おやつは？",
        "answer": "アイスクリーム",
        "choices": ["アイスクリーム", "プリン", "ゼリー", "ケーキ"],
        "choices_ruby": {},
        "level": "normal",
    },
    {
        "emoji": "🔭",
        "hint": "遠くの 星や 月を 大きく 見るための 道具は？",
        "hint_ruby": "<ruby>遠<rt>とお</rt></ruby>くの <ruby>星<rt>ほし</rt></ruby>や <ruby>月<rt>つき</rt></ruby>を <ruby>大<rt>おお</rt></ruby>きく <ruby>見<rt>み</rt></ruby>るための <ruby>道具<rt>どうぐ</rt></ruby>は？",
        "answer": "ぼうえんきょう",
        "choices": ["ぼうえんきょう", "けんびきょう", "カメラ", "めがね"],
        "choices_ruby": {},
        "level": "normal",
    },
    {
        "emoji": "🌋",
        "hint": "山の 上から 火や ようがんが 出て くる 山は？",
        "hint_ruby": "<ruby>山<rt>やま</rt></ruby>の <ruby>上<rt>うえ</rt></ruby>から <ruby>火<rt>ひ</rt></ruby>や ようがんが <ruby>出<rt>で</rt></ruby>て くる <ruby>山<rt>やま</rt></ruby>は？",
        "answer": "火山",
        "choices": ["火山", "高原", "丘", "砂漠"],
        "choices_ruby": {
            "火山": "火山（かざん）",
            "高原": "高原（こうげん）",
            "丘":   "丘（おか）",
            "砂漠": "砂漠（さばく）",
        },
        "level": "normal",
    },
    {
        "emoji": "🐫",
        "hint": "砂漠に すんでいて、せなかに こぶが ある 動物は？",
        "hint_ruby": "<ruby>砂漠<rt>さばく</rt></ruby>に すんでいて、せなかに こぶが ある <ruby>動物<rt>どうぶつ</rt></ruby>は？",
        "answer": "ラクダ",
        "choices": ["ラクダ", "シマウマ", "キリン", "サイ"],
        "choices_ruby": {},
        "level": "normal",
    },
    {
        "emoji": "🧲",
        "hint": "鉄を 引き付ける ふしぎな 力を もつ ものは？",
        "hint_ruby": "<ruby>鉄<rt>てつ</rt></ruby>を <ruby>引<rt>ひ</rt></ruby>き<ruby>付<rt>つ</rt></ruby>ける ふしぎな <ruby>力<rt>ちから</rt></ruby>を もつ ものは？",
        "answer": "じしゃく",
        "choices": ["じしゃく", "でんち", "スイッチ", "はり金"],
        "choices_ruby": {
            "はり金": "はり金（がね）",
        },
        "level": "normal",
    },
    {
        "emoji": "🌈",
        "hint": "雨上がりの 空に かかる、7色の 帯は？",
        "hint_ruby": "<ruby>雨上<rt>あめあ</rt></ruby>がりの <ruby>空<rt>そら</rt></ruby>に かかる、7<ruby>色<rt>いろ</rt></ruby>の <ruby>帯<rt>おび</rt></ruby>は？",
        "answer": "にじ",
        "choices": ["にじ", "かみなり", "雲", "夕焼け"],
        "choices_ruby": {
            "雲":   "雲（くも）",
            "夕焼け": "夕焼け（ゆうやけ）",
        },
        "level": "normal",
    },
    {
        "emoji": "🪴",
        "hint": "根・茎・葉・花が あって、光合成を する 生き物は？",
        "hint_ruby": "<ruby>根<rt>ね</rt></ruby>・<ruby>茎<rt>くき</rt></ruby>・<ruby>葉<rt>は</rt></ruby>・<ruby>花<rt>はな</rt></ruby>が あって、<ruby>光合成<rt>こうごうせい</rt></ruby>を する <ruby>生<rt>い</rt></ruby>き<ruby>物<rt>もの</rt></ruby>は？",
        "answer": "植物",
        "choices": ["植物", "動物", "昆虫", "細菌"],
        "choices_ruby": {
            "植物": "植物（しょくぶつ）",
            "動物": "動物（どうぶつ）",
            "昆虫": "昆虫（こんちゅう）",
            "細菌": "細菌（さいきん）",
        },
        "level": "normal",
    },

    # ──────────────────────────────────────────
    # むずかしい（3〜4年生）
    # ──────────────────────────────────────────
    {
        "emoji": "",
        "hint": "地球の まわりを 回っている、大きな 岩の 天体は？",
        "hint_ruby": "<ruby>地球<rt>ちきゅう</rt></ruby>の まわりを <ruby>回<rt>まわ</rt></ruby>っている、<ruby>大<rt>おお</rt></ruby>きな <ruby>岩<rt>いわ</rt></ruby>の <ruby>天体<rt>てんたい</rt></ruby>は？",
        "answer": "月",
        "choices": ["月", "太陽", "彗星", "小惑星"],
        "choices_ruby": {
            "月":   "月（つき）",
            "太陽": "太陽（たいよう）",
            "彗星": "彗星（すいせい）",
            "小惑星": "小惑星（しょうわくせい）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "水を 熱すると 出てくる 気体で、冷えると 水に もどる ものは？",
        "hint_ruby": "<ruby>水<rt>みず</rt></ruby>を <ruby>熱<rt>ねつ</rt></ruby>すると <ruby>出<rt>で</rt></ruby>てくる <ruby>気体<rt>きたい</rt></ruby>で、<ruby>冷<rt>さ</rt></ruby>えると <ruby>水<rt>みず</rt></ruby>に もどる ものは？",
        "answer": "水蒸気",
        "choices": ["水蒸気", "酸素", "二酸化炭素", "窒素"],
        "choices_ruby": {
            "水蒸気":   "水蒸気（すいじょうき）",
            "酸素":     "酸素（さんそ）",
            "二酸化炭素": "二酸化炭素（にさんかたんそ）",
            "窒素":     "窒素（ちっそ）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "植物が 日光を 使って、でんぷんと 酸素を 作る はたらきは？",
        "hint_ruby": "<ruby>植物<rt>しょくぶつ</rt></ruby>が <ruby>日光<rt>にっこう</rt></ruby>を <ruby>使<rt>つか</rt></ruby>って、でんぷんと <ruby>酸素<rt>さんそ</rt></ruby>を <ruby>作<rt>つく</rt></ruby>る はたらきは？",
        "answer": "光合成",
        "choices": ["光合成", "呼吸", "蒸散", "発芽"],
        "choices_ruby": {
            "光合成": "光合成（こうごうせい）",
            "呼吸":   "呼吸（こきゅう）",
            "蒸散":   "蒸散（じょうさん）",
            "発芽":   "発芽（はつが）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "国を 代表して 外国と 話し合いを する 人を 何と 言う？",
        "hint_ruby": "<ruby>国<rt>くに</rt></ruby>を <ruby>代表<rt>だいひょう</rt></ruby>して <ruby>外国<rt>がいこく</rt></ruby>と <ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>いを する <ruby>人<rt>ひと</rt></ruby>を <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "大使",
        "choices": ["大使", "大臣", "知事", "市長"],
        "choices_ruby": {
            "大使": "大使（たいし）",
            "大臣": "大臣（だいじん）",
            "知事": "知事（ちじ）",
            "市長": "市長（しちょう）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "地面の 下で プレートが ずれて、大地が ゆれる 現象は？",
        "hint_ruby": "<ruby>地面<rt>じめん</rt></ruby>の <ruby>下<rt>した</rt></ruby>で プレートが ずれて、<ruby>大地<rt>だいち</rt></ruby>が ゆれる <ruby>現象<rt>げんしょう</rt></ruby>は？",
        "answer": "地震",
        "choices": ["地震", "津波", "台風", "洪水"],
        "choices_ruby": {
            "地震": "地震（じしん）",
            "津波": "津波（つなみ）",
            "台風": "台風（たいふう）",
            "洪水": "洪水（こうずい）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "空気中の 水分が 冷えて 小さな 水のつぶに なり、空に 浮かんでいる ものは？",
        "hint_ruby": "<ruby>空気中<rt>くうきちゅう</rt></ruby>の <ruby>水分<rt>すいぶん</rt></ruby>が <ruby>冷<rt>さ</rt></ruby>えて <ruby>小<rt>ちい</rt></ruby>さな <ruby>水<rt>みず</rt></ruby>のつぶに なり、<ruby>空<rt>そら</rt></ruby>に <ruby>浮<rt>う</rt></ruby>かんでいる ものは？",
        "answer": "雲",
        "choices": ["雲", "霧", "霜", "露"],
        "choices_ruby": {
            "雲": "雲（くも）",
            "霧": "霧（きり）",
            "霜": "霜（しも）",
            "露": "露（つゆ）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "電気を 通しやすい 物質の ことを 何と 言う？",
        "hint_ruby": "<ruby>電気<rt>でんき</rt></ruby>を <ruby>通<rt>とお</rt></ruby>しやすい <ruby>物質<rt>ぶっしつ</rt></ruby>の ことを <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "導体",
        "choices": ["導体", "絶縁体", "半導体", "磁石"],
        "choices_ruby": {
            "導体":   "導体（どうたい）",
            "絶縁体": "絶縁体（ぜつえんたい）",
            "半導体": "半導体（はんどうたい）",
            "磁石":   "磁石（じしゃく）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "法律を 作る 権限を もつ、国の 最高 機関は？",
        "hint_ruby": "<ruby>法律<rt>ほうりつ</rt></ruby>を <ruby>作<rt>つく</rt></ruby>る <ruby>権限<rt>けんげん</rt></ruby>を もつ、<ruby>国<rt>くに</rt></ruby>の <ruby>最高<rt>さいこう</rt></ruby> <ruby>機関<rt>きかん</rt></ruby>は？",
        "answer": "国会",
        "choices": ["国会", "内閣", "裁判所", "県庁"],
        "choices_ruby": {
            "国会":   "国会（こっかい）",
            "内閣":   "内閣（ないかく）",
            "裁判所": "裁判所（さいばんしょ）",
            "県庁":   "県庁（けんちょう）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "川や 雨水が 長い 年月を かけて 岩を 削って できた 深い 谷は？",
        "hint_ruby": "<ruby>川<rt>かわ</rt></ruby>や <ruby>雨水<rt>あまみず</rt></ruby>が <ruby>長<rt>なが</rt></ruby>い <ruby>年月<rt>ねんげつ</rt></ruby>を かけて <ruby>岩<rt>いわ</rt></ruby>を <ruby>削<rt>けず</rt></ruby>って できた <ruby>深<rt>ふか</rt></ruby>い <ruby>谷<rt>たに</rt></ruby>は？",
        "answer": "峡谷",
        "choices": ["峡谷", "平野", "盆地", "台地"],
        "choices_ruby": {
            "峡谷": "峡谷（きょうこく）",
            "平野": "平野（へいや）",
            "盆地": "盆地（ぼんち）",
            "台地": "台地（だいち）",
        },
        "level": "hard",
    },
    {
        "emoji": "",
        "hint": "生き物が 長い 年月を かけて 少しずつ 変化して いく ことを 何と 言う？",
        "hint_ruby": "<ruby>生<rt>い</rt></ruby>き<ruby>物<rt>もの</rt></ruby>が <ruby>長<rt>なが</rt></ruby>い <ruby>年月<rt>ねんげつ</rt></ruby>を かけて <ruby>少<rt>すこ</rt></ruby>しずつ <ruby>変化<rt>へんか</rt></ruby>して いく ことを <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "進化",
        "choices": ["進化", "成長", "変態", "繁殖"],
        "choices_ruby": {
            "進化": "進化（しんか）",
            "成長": "成長（せいちょう）",
            "変態": "変態（へんたい）",
            "繁殖": "繁殖（はんしょく）",
        },
        "level": "hard",
    },
]


def get_questions_by_level(level: str) -> list:
    """指定したレベルの問題だけを返す関数"""
    return [q for q in QUESTIONS if q["level"] == level]
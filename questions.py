# questions.py
# ことばクイズ　問題データ
# キー一覧:
#   emoji       : 絵文字
#   hint        : ヒント文（プレーンテキスト）
#   hint_ruby   : フリガナ付きヒント文（rubyタグ）
#   answer      : 正解
#   choices     : 選択肢4つ
#   choices_ruby: 選択肢フリガナ辞書 {"元の文字": "文字（よみ）"}
#   level       : "easy" / "normal" / "hard"
#   category    : "どうぶつ" / "しぜん" / "たべもの" / "のりもの" / "はたらき" / "スポーツ" など

QUESTIONS = [

    # ════════════════════════════════════════
    # やさしい（1〜2年生）
    # ════════════════════════════════════════

    # ── どうぶつ ──
    {
        "emoji": "🐘", "hint": "はなが とても ながい どうぶつは？",
        "hint_ruby": "はなが とても ながい どうぶつは？",
        "answer": "ぞう", "choices": ["ぞう", "きりん", "うま", "くま"],
        "choices_ruby": {}, "level": "easy", "category": "どうぶつ",
    },
    {
        "emoji": "🐸", "hint": "みずの ちかくに いて「ケロケロ」と なく いきものは？",
        "hint_ruby": "みずの ちかくに いて「ケロケロ」と なく いきものは？",
        "answer": "かえる", "choices": ["かえる", "へび", "とかげ", "やもり"],
        "choices_ruby": {}, "level": "easy", "category": "どうぶつ",
    },
    {
        "emoji": "🐟", "hint": "みずの なかを およぐ いきものは？",
        "hint_ruby": "みずの なかを およぐ いきものは？",
        "answer": "さかな", "choices": ["さかな", "かめ", "かえる", "とり"],
        "choices_ruby": {}, "level": "easy", "category": "どうぶつ",
    },
    {
        "emoji": "🐦", "hint": "そらを とぶ、はねの ある いきものは？",
        "hint_ruby": "そらを とぶ、はねの ある いきものは？",
        "answer": "とり", "choices": ["とり", "むし", "さかな", "かえる"],
        "choices_ruby": {}, "level": "easy", "category": "どうぶつ",
    },
    {
        "emoji": "🐱", "hint": "「ニャー」と なく、いえで かう どうぶつは？",
        "hint_ruby": "「ニャー」と なく、いえで かう どうぶつは？",
        "answer": "ねこ", "choices": ["ねこ", "いぬ", "うさぎ", "はむすたー"],
        "choices_ruby": {}, "level": "easy", "category": "どうぶつ",
    },

    # ── しぜん ──
    {
        "emoji": "🌸", "hint": "はるに さく ピンクの はなは？",
        "hint_ruby": "はるに さく ピンクの はなは？",
        "answer": "さくら", "choices": ["さくら", "たんぽぽ", "あさがお", "ひまわり"],
        "choices_ruby": {}, "level": "easy", "category": "しぜん",
    },
    {
        "emoji": "🌙", "hint": "よるの そらに ひかる まるい ものは？",
        "hint_ruby": "よるの そらに ひかる まるい ものは？",
        "answer": "つき", "choices": ["つき", "ほし", "たいよう", "くも"],
        "choices_ruby": {}, "level": "easy", "category": "しぜん",
    },
    {
        "emoji": "⛄", "hint": "ふゆに そらから ふってくる しろい ものは？",
        "hint_ruby": "ふゆに そらから ふってくる しろい ものは？",
        "answer": "ゆき", "choices": ["ゆき", "あめ", "かぜ", "くも"],
        "choices_ruby": {}, "level": "easy", "category": "しぜん",
    },
    {
        "emoji": "🌻", "hint": "なつに さく、おおきくて きいろい はなは？",
        "hint_ruby": "なつに さく、おおきくて きいろい はなは？",
        "answer": "ひまわり", "choices": ["ひまわり", "さくら", "たんぽぽ", "あじさい"],
        "choices_ruby": {}, "level": "easy", "category": "しぜん",
    },
    {
        "emoji": "🌊", "hint": "うみや かわで みずが うごく ものは？",
        "hint_ruby": "うみや かわで みずが うごく ものは？",
        "answer": "なみ", "choices": ["なみ", "かわ", "いけ", "たき"],
        "choices_ruby": {}, "level": "easy", "category": "しぜん",
    },

    # ── たべもの ──
    {
        "emoji": "🍎", "hint": "あかくて あまい くだものは？",
        "hint_ruby": "あかくて あまい くだものは？",
        "answer": "りんご", "choices": ["りんご", "みかん", "ぶどう", "もも"],
        "choices_ruby": {}, "level": "easy", "category": "たべもの",
    },
    {
        "emoji": "🍙", "hint": "のりで まいた、ごはんの たべものは？",
        "hint_ruby": "のりで まいた、ごはんの たべものは？",
        "answer": "おにぎり", "choices": ["おにぎり", "すし", "パン", "うどん"],
        "choices_ruby": {}, "level": "easy", "category": "たべもの",
    },
    {
        "emoji": "🍌", "hint": "きいろくて ながい、さるが すきな くだものは？",
        "hint_ruby": "きいろくて ながい、さるが すきな くだものは？",
        "answer": "バナナ", "choices": ["バナナ", "りんご", "みかん", "もも"],
        "choices_ruby": {}, "level": "easy", "category": "たべもの",
    },
    {
        "emoji": "🍜", "hint": "ながい めんを つゆで たべる たべものは？",
        "hint_ruby": "ながい めんを つゆで たべる たべものは？",
        "answer": "うどん", "choices": ["うどん", "ラーメン", "スパゲッティ", "そば"],
        "choices_ruby": {}, "level": "easy", "category": "たべもの",
    },
    {
        "emoji": "🍰", "hint": "たんじょうびに たべる、あまくて まるい たべものは？",
        "hint_ruby": "たんじょうびに たべる、あまくて まるい たべものは？",
        "answer": "ケーキ", "choices": ["ケーキ", "プリン", "アイス", "チョコ"],
        "choices_ruby": {}, "level": "easy", "category": "たべもの",
    },

    # ── のりもの ──
    {
        "emoji": "🚌", "hint": "おおぜいの ひとを はこぶ おおきな くるまは？",
        "hint_ruby": "おおぜいの ひとを はこぶ おおきな くるまは？",
        "answer": "バス", "choices": ["バス", "タクシー", "トラック", "でんしゃ"],
        "choices_ruby": {}, "level": "easy", "category": "のりもの",
    },
    {
        "emoji": "✈️", "hint": "そらを とんで とおくへ いく のりものは？",
        "hint_ruby": "そらを とんで とおくへ いく のりものは？",
        "answer": "ひこうき", "choices": ["ひこうき", "ふね", "でんしゃ", "バス"],
        "choices_ruby": {}, "level": "easy", "category": "のりもの",
    },
    {
        "emoji": "🚲", "hint": "ペダルを こいで すすむ のりものは？",
        "hint_ruby": "ペダルを こいで すすむ のりものは？",
        "answer": "じてんしゃ", "choices": ["じてんしゃ", "バイク", "くるま", "スケボー"],
        "choices_ruby": {}, "level": "easy", "category": "のりもの",
    },

    # ── はたらき ──
    {
        "emoji": "👨‍⚕️", "hint": "びょうきや けがを なおしてくれる ひとは？",
        "hint_ruby": "びょうきや けがを なおしてくれる ひとは？",
        "answer": "おいしゃさん", "choices": ["おいしゃさん", "せんせい", "けいかん", "しょうぼうし"],
        "choices_ruby": {}, "level": "easy", "category": "はたらき",
    },
    {
        "emoji": "👩‍🏫", "hint": "がっこうで べんきょうを おしえてくれる ひとは？",
        "hint_ruby": "がっこうで べんきょうを おしえてくれる ひとは？",
        "answer": "せんせい", "choices": ["せんせい", "おいしゃさん", "けいかん", "うんてんし"],
        "choices_ruby": {}, "level": "easy", "category": "はたらき",
    },

    # ── スポーツ ──
    {
        "emoji": "⚽", "hint": "あしで ボールを けって あそぶ スポーツは？",
        "hint_ruby": "あしで ボールを けって あそぶ スポーツは？",
        "answer": "サッカー", "choices": ["サッカー", "やきゅう", "バスケ", "テニス"],
        "choices_ruby": {}, "level": "easy", "category": "スポーツ",
    },
    {
        "emoji": "🏊", "hint": "みずの なかで およぐ スポーツは？",
        "hint_ruby": "みずの なかで およぐ スポーツは？",
        "answer": "すいえい", "choices": ["すいえい", "やきゅう", "サッカー", "たいそう"],
        "choices_ruby": {}, "level": "easy", "category": "スポーツ",
    },

    # ── どうぐ ──
    {
        "emoji": "✏️", "hint": "じを かくときに つかう ほそながい ものは？",
        "hint_ruby": "じを かくときに つかう ほそながい ものは？",
        "answer": "えんぴつ", "choices": ["えんぴつ", "はさみ", "のり", "じょうぎ"],
        "choices_ruby": {}, "level": "easy", "category": "どうぐ",
    },
    {
        "emoji": "☂️", "hint": "あめの ひに さして つかう ものは？",
        "hint_ruby": "あめの ひに さして つかう ものは？",
        "answer": "かさ", "choices": ["かさ", "ぼうし", "てぶくろ", "マフラー"],
        "choices_ruby": {}, "level": "easy", "category": "どうぐ",
    },


    # ════════════════════════════════════════
    # ふつう（2〜3年生）
    # ════════════════════════════════════════

    # ── どうぶつ ──
    {
        "emoji": "🦋", "hint": "いもむしが さなぎに なって、羽が はえた 虫は？",
        "hint_ruby": "いもむしが さなぎに なって、<ruby>羽<rt>はね</rt></ruby>が はえた <ruby>虫<rt>むし</rt></ruby>は？",
        "answer": "チョウ", "choices": ["チョウ", "トンボ", "セミ", "カブトムシ"],
        "choices_ruby": {}, "level": "normal", "category": "どうぶつ",
    },
    {
        "emoji": "🐫", "hint": "砂漠に すんでいて、せなかに こぶが ある 動物は？",
        "hint_ruby": "<ruby>砂漠<rt>さばく</rt></ruby>に すんでいて、せなかに こぶが ある <ruby>動物<rt>どうぶつ</rt></ruby>は？",
        "answer": "ラクダ", "choices": ["ラクダ", "シマウマ", "キリン", "サイ"],
        "choices_ruby": {}, "level": "normal", "category": "どうぶつ",
    },
    {
        "emoji": "🐧", "hint": "南極に すんでいて、空は 飛べないが 泳ぐのが 得意な 鳥は？",
        "hint_ruby": "<ruby>南極<rt>なんきょく</rt></ruby>に すんでいて、<ruby>空<rt>そら</rt></ruby>は <ruby>飛<rt>と</rt></ruby>べないが <ruby>泳<rt>およ</rt></ruby>ぐのが <ruby>得意<rt>とくい</rt></ruby>な <ruby>鳥<rt>とり</rt></ruby>は？",
        "answer": "ペンギン", "choices": ["ペンギン", "フラミンゴ", "ダチョウ", "カモ"],
        "choices_ruby": {}, "level": "normal", "category": "どうぶつ",
    },
    {
        "emoji": "🦈", "hint": "海に すむ、大きくて 歯が するどい 魚は？",
        "hint_ruby": "<ruby>海<rt>うみ</rt></ruby>に すむ、<ruby>大<rt>おお</rt></ruby>きくて <ruby>歯<rt>は</rt></ruby>が するどい <ruby>魚<rt>さかな</rt></ruby>は？",
        "answer": "サメ", "choices": ["サメ", "クジラ", "イルカ", "タコ"],
        "choices_ruby": {}, "level": "normal", "category": "どうぶつ",
    },

    # ── しぜん ──
    {
        "emoji": "🌋", "hint": "山の 上から 火や ようがんが 出て くる 山は？",
        "hint_ruby": "<ruby>山<rt>やま</rt></ruby>の <ruby>上<rt>うえ</rt></ruby>から <ruby>火<rt>ひ</rt></ruby>や ようがんが <ruby>出<rt>で</rt></ruby>て くる <ruby>山<rt>やま</rt></ruby>は？",
        "answer": "火山",
        "choices": ["火山", "高原", "丘", "砂漠"],
        "choices_ruby": {"火山": "火山（かざん）", "高原": "高原（こうげん）", "丘": "丘（おか）", "砂漠": "砂漠（さばく）"},
        "level": "normal", "category": "しぜん",
    },
    {
        "emoji": "🌈", "hint": "雨上がりの 空に かかる、7色の 帯は？",
        "hint_ruby": "<ruby>雨上<rt>あめあ</rt></ruby>がりの <ruby>空<rt>そら</rt></ruby>に かかる、7<ruby>色<rt>いろ</rt></ruby>の <ruby>帯<rt>おび</rt></ruby>は？",
        "answer": "にじ", "choices": ["にじ", "かみなり", "雲", "夕焼け"],
        "choices_ruby": {"雲": "雲（くも）", "夕焼け": "夕焼け（ゆうやけ）"},
        "level": "normal", "category": "しぜん",
    },
    {
        "emoji": "🌊", "hint": "海や 川で 水が 高く もり上がって おしよせる ものは？",
        "hint_ruby": "<ruby>海<rt>うみ</rt></ruby>や <ruby>川<rt>かわ</rt></ruby>で <ruby>水<rt>みず</rt></ruby>が <ruby>高<rt>たか</rt></ruby>く もり<ruby>上<rt>あ</rt></ruby>がって おしよせる ものは？",
        "answer": "なみ", "choices": ["なみ", "かわ", "みずうみ", "たき"],
        "choices_ruby": {}, "level": "normal", "category": "しぜん",
    },
    {
        "emoji": "🧲", "hint": "鉄を 引き付ける ふしぎな 力を もつ ものは？",
        "hint_ruby": "<ruby>鉄<rt>てつ</rt></ruby>を <ruby>引<rt>ひ</rt></ruby>き<ruby>付<rt>つ</rt></ruby>ける ふしぎな <ruby>力<rt>ちから</rt></ruby>を もつ ものは？",
        "answer": "じしゃく", "choices": ["じしゃく", "でんち", "スイッチ", "はり金"],
        "choices_ruby": {"はり金": "はり金（がね）"},
        "level": "normal", "category": "しぜん",
    },

    # ── たべもの ──
    {
        "emoji": "🍦", "hint": "冷たくて 甘い、コーンに のせて 食べる おやつは？",
        "hint_ruby": "<ruby>冷<rt>つめ</rt></ruby>たくて <ruby>甘<rt>あま</rt></ruby>い、コーンに のせて <ruby>食<rt>た</rt></ruby>べる おやつは？",
        "answer": "アイスクリーム", "choices": ["アイスクリーム", "プリン", "ゼリー", "ケーキ"],
        "choices_ruby": {}, "level": "normal", "category": "たべもの",
    },
    {
        "emoji": "🍣", "hint": "酢飯の 上に 魚などを のせた 日本の 料理は？",
        "hint_ruby": "<ruby>酢飯<rt>すめし</rt></ruby>の <ruby>上<rt>うえ</rt></ruby>に <ruby>魚<rt>さかな</rt></ruby>などを のせた <ruby>日本<rt>にほん</rt></ruby>の <ruby>料理<rt>りょうり</rt></ruby>は？",
        "answer": "すし", "choices": ["すし", "てんぷら", "そば", "うどん"],
        "choices_ruby": {}, "level": "normal", "category": "たべもの",
    },
    {
        "emoji": "🧁", "hint": "小麦粉・卵・砂糖を まぜて 焼いた、やわらかい 洋菓子は？",
        "hint_ruby": "<ruby>小麦粉<rt>こむぎこ</rt></ruby>・<ruby>卵<rt>たまご</rt></ruby>・<ruby>砂糖<rt>さとう</rt></ruby>を まぜて <ruby>焼<rt>や</rt></ruby>いた、やわらかい <ruby>洋菓子<rt>ようがし</rt></ruby>は？",
        "answer": "ケーキ", "choices": ["ケーキ", "せんべい", "まんじゅう", "もち"],
        "choices_ruby": {}, "level": "normal", "category": "たべもの",
    },
    {
        "emoji": "🥕", "hint": "オレンジ色で 土の 中に できる 野菜は？",
        "hint_ruby": "オレンジ<ruby>色<rt>いろ</rt></ruby>で <ruby>土<rt>つち</rt></ruby>の <ruby>中<rt>なか</rt></ruby>に できる <ruby>野菜<rt>やさい</rt></ruby>は？",
        "answer": "にんじん", "choices": ["にんじん", "だいこん", "さつまいも", "かぶ"],
        "choices_ruby": {}, "level": "normal", "category": "たべもの",
    },

    # ── のりもの ──
    {
        "emoji": "🚒", "hint": "火事のとき かけつけて、水を かける 赤い 車は？",
        "hint_ruby": "<ruby>火事<rt>かじ</rt></ruby>のとき かけつけて、<ruby>水<rt>みず</rt></ruby>を かける <ruby>赤<rt>あか</rt></ruby>い <ruby>車<rt>くるま</rt></ruby>は？",
        "answer": "消防車",
        "choices": ["消防車", "救急車", "パトカー", "ごみ収集車"],
        "choices_ruby": {"消防車": "消防車（しょうぼうしゃ）", "救急車": "救急車（きゅうきゅうしゃ）", "ごみ収集車": "ごみ収集車（しゅうしゅうしゃ）"},
        "level": "normal", "category": "のりもの",
    },
    {
        "emoji": "🚢", "hint": "海の 上を 走る、大きな のりものは？",
        "hint_ruby": "<ruby>海<rt>うみ</rt></ruby>の <ruby>上<rt>うえ</rt></ruby>を <ruby>走<rt>はし</rt></ruby>る、<ruby>大<rt>おお</rt></ruby>きな のりものは？",
        "answer": "ふね", "choices": ["ふね", "ひこうき", "でんしゃ", "バス"],
        "choices_ruby": {}, "level": "normal", "category": "のりもの",
    },

    # ── はたらき ──
    {
        "emoji": "👨‍🍳", "hint": "レストランで 料理を 作る 人は？",
        "hint_ruby": "レストランで <ruby>料理<rt>りょうり</rt></ruby>を <ruby>作<rt>つく</rt></ruby>る <ruby>人<rt>ひと</rt></ruby>は？",
        "answer": "コック（シェフ）", "choices": ["コック（シェフ）", "いしゃ", "けいかん", "うんてんし"],
        "choices_ruby": {}, "level": "normal", "category": "はたらき",
    },
    {
        "emoji": "👮", "hint": "町を パトロールして 安全を 守る 人は？",
        "hint_ruby": "<ruby>町<rt>まち</rt></ruby>を パトロールして <ruby>安全<rt>あんぜん</rt></ruby>を <ruby>守<rt>まも</rt></ruby>る <ruby>人<rt>ひと</rt></ruby>は？",
        "answer": "警察官",
        "choices": ["警察官", "消防士", "医者", "弁護士"],
        "choices_ruby": {"警察官": "警察官（けいさつかん）", "消防士": "消防士（しょうぼうし）", "医者": "医者（いしゃ）", "弁護士": "弁護士（べんごし）"},
        "level": "normal", "category": "はたらき",
    },
    {
        "emoji": "🌿", "hint": "根・茎・葉・花が あって、光合成を する 生き物は？",
        "hint_ruby": "<ruby>根<rt>ね</rt></ruby>・<ruby>茎<rt>くき</rt></ruby>・<ruby>葉<rt>は</rt></ruby>・<ruby>花<rt>はな</rt></ruby>が あって、<ruby>光合成<rt>こうごうせい</rt></ruby>を する <ruby>生<rt>い</rt></ruby>き<ruby>物<rt>もの</rt></ruby>は？",
        "answer": "植物",
        "choices": ["植物", "動物", "昆虫", "細菌"],
        "choices_ruby": {"植物": "植物（しょくぶつ）", "動物": "動物（どうぶつ）", "昆虫": "昆虫（こんちゅう）", "細菌": "細菌（さいきん）"},
        "level": "normal", "category": "しぜん",
    },

    # ── スポーツ ──
    {
        "emoji": "⚾", "hint": "バットで ボールを 打って 塁を まわる スポーツは？",
        "hint_ruby": "バットで ボールを <ruby>打<rt>う</rt></ruby>って <ruby>塁<rt>るい</rt></ruby>を まわる スポーツは？",
        "answer": "野球",
        "choices": ["野球", "サッカー", "バスケ", "テニス"],
        "choices_ruby": {"野球": "野球（やきゅう）"},
        "level": "normal", "category": "スポーツ",
    },
    {
        "emoji": "🏀", "hint": "バスケットに ボールを 入れて 点を 取る スポーツは？",
        "hint_ruby": "バスケットに ボールを <ruby>入<rt>い</rt></ruby>れて <ruby>点<rt>てん</rt></ruby>を <ruby>取<rt>と</rt></ruby>る スポーツは？",
        "answer": "バスケットボール", "choices": ["バスケットボール", "バレーボール", "ラグビー", "サッカー"],
        "choices_ruby": {}, "level": "normal", "category": "スポーツ",
    },
    {
        "emoji": "🔭", "hint": "遠くの 星や 月を 大きく 見るための 道具は？",
        "hint_ruby": "<ruby>遠<rt>とお</rt></ruby>くの <ruby>星<rt>ほし</rt></ruby>や <ruby>月<rt>つき</rt></ruby>を <ruby>大<rt>おお</rt></ruby>きく <ruby>見<rt>み</rt></ruby>るための <ruby>道具<rt>どうぐ</rt></ruby>は？",
        "answer": "ぼうえんきょう", "choices": ["ぼうえんきょう", "けんびきょう", "カメラ", "めがね"],
        "choices_ruby": {}, "level": "normal", "category": "どうぐ",
    },


    # ════════════════════════════════════════
    # むずかしい（3〜4年生）
    # ════════════════════════════════════════

    # ── しぜん・理科 ──
    {
        "emoji": "", "hint": "地球の まわりを 回っている、大きな 岩の 天体は？",
        "hint_ruby": "<ruby>地球<rt>ちきゅう</rt></ruby>の まわりを <ruby>回<rt>まわ</rt></ruby>っている、<ruby>大<rt>おお</rt></ruby>きな <ruby>岩<rt>いわ</rt></ruby>の <ruby>天体<rt>てんたい</rt></ruby>は？",
        "answer": "月",
        "choices": ["月", "太陽", "彗星", "小惑星"],
        "choices_ruby": {"月": "月（つき）", "太陽": "太陽（たいよう）", "彗星": "彗星（すいせい）", "小惑星": "小惑星（しょうわくせい）"},
        "level": "hard", "category": "しぜん",
    },
    {
        "emoji": "", "hint": "水を 熱すると 出てくる 気体で、冷えると 水に もどる ものは？",
        "hint_ruby": "<ruby>水<rt>みず</rt></ruby>を <ruby>熱<rt>ねつ</rt></ruby>すると <ruby>出<rt>で</rt></ruby>てくる <ruby>気体<rt>きたい</rt></ruby>で、<ruby>冷<rt>さ</rt></ruby>えると <ruby>水<rt>みず</rt></ruby>に もどる ものは？",
        "answer": "水蒸気",
        "choices": ["水蒸気", "酸素", "二酸化炭素", "窒素"],
        "choices_ruby": {"水蒸気": "水蒸気（すいじょうき）", "酸素": "酸素（さんそ）", "二酸化炭素": "二酸化炭素（にさんかたんそ）", "窒素": "窒素（ちっそ）"},
        "level": "hard", "category": "しぜん",
    },
    {
        "emoji": "", "hint": "植物が 日光を 使って、でんぷんと 酸素を 作る はたらきは？",
        "hint_ruby": "<ruby>植物<rt>しょくぶつ</rt></ruby>が <ruby>日光<rt>にっこう</rt></ruby>を <ruby>使<rt>つか</rt></ruby>って、でんぷんと <ruby>酸素<rt>さんそ</rt></ruby>を <ruby>作<rt>つく</rt></ruby>る はたらきは？",
        "answer": "光合成",
        "choices": ["光合成", "呼吸", "蒸散", "発芽"],
        "choices_ruby": {"光合成": "光合成（こうごうせい）", "呼吸": "呼吸（こきゅう）", "蒸散": "蒸散（じょうさん）", "発芽": "発芽（はつが）"},
        "level": "hard", "category": "しぜん",
    },
    {
        "emoji": "", "hint": "地面の 下で プレートが ずれて、大地が ゆれる 現象は？",
        "hint_ruby": "<ruby>地面<rt>じめん</rt></ruby>の <ruby>下<rt>した</rt></ruby>で プレートが ずれて、<ruby>大地<rt>だいち</rt></ruby>が ゆれる <ruby>現象<rt>げんしょう</rt></ruby>は？",
        "answer": "地震",
        "choices": ["地震", "津波", "台風", "洪水"],
        "choices_ruby": {"地震": "地震（じしん）", "津波": "津波（つなみ）", "台風": "台風（たいふう）", "洪水": "洪水（こうずい）"},
        "level": "hard", "category": "しぜん",
    },
    {
        "emoji": "", "hint": "空気中の 水分が 冷えて 小さな 水のつぶに なり、空に 浮かんでいる ものは？",
        "hint_ruby": "<ruby>空気中<rt>くうきちゅう</rt></ruby>の <ruby>水分<rt>すいぶん</rt></ruby>が <ruby>冷<rt>さ</rt></ruby>えて <ruby>小<rt>ちい</rt></ruby>さな <ruby>水<rt>みず</rt></ruby>のつぶに なり、<ruby>空<rt>そら</rt></ruby>に <ruby>浮<rt>う</rt></ruby>かんでいる ものは？",
        "answer": "雲",
        "choices": ["雲", "霧", "霜", "露"],
        "choices_ruby": {"雲": "雲（くも）", "霧": "霧（きり）", "霜": "霜（しも）", "露": "露（つゆ）"},
        "level": "hard", "category": "しぜん",
    },
    {
        "emoji": "", "hint": "電気を 通しやすい 物質の ことを 何と 言う？",
        "hint_ruby": "<ruby>電気<rt>でんき</rt></ruby>を <ruby>通<rt>とお</rt></ruby>しやすい <ruby>物質<rt>ぶっしつ</rt></ruby>の ことを <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "導体",
        "choices": ["導体", "絶縁体", "半導体", "磁石"],
        "choices_ruby": {"導体": "導体（どうたい）", "絶縁体": "絶縁体（ぜつえんたい）", "半導体": "半導体（はんどうたい）", "磁石": "磁石（じしゃく）"},
        "level": "hard", "category": "しぜん",
    },
    {
        "emoji": "", "hint": "生き物が 長い 年月を かけて 少しずつ 変化して いく ことを 何と 言う？",
        "hint_ruby": "<ruby>生<rt>い</rt></ruby>き<ruby>物<rt>もの</rt></ruby>が <ruby>長<rt>なが</rt></ruby>い <ruby>年月<rt>ねんげつ</rt></ruby>を かけて <ruby>少<rt>すこ</rt></ruby>しずつ <ruby>変化<rt>へんか</rt></ruby>して いく ことを <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "進化",
        "choices": ["進化", "成長", "変態", "繁殖"],
        "choices_ruby": {"進化": "進化（しんか）", "成長": "成長（せいちょう）", "変態": "変態（へんたい）", "繁殖": "繁殖（はんしょく）"},
        "level": "hard", "category": "しぜん",
    },

    # ── 社会・はたらき ──
    {
        "emoji": "", "hint": "国を 代表して 外国と 話し合いを する 人を 何と 言う？",
        "hint_ruby": "<ruby>国<rt>くに</rt></ruby>を <ruby>代表<rt>だいひょう</rt></ruby>して <ruby>外国<rt>がいこく</rt></ruby>と <ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>いを する <ruby>人<rt>ひと</rt></ruby>を <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "大使",
        "choices": ["大使", "大臣", "知事", "市長"],
        "choices_ruby": {"大使": "大使（たいし）", "大臣": "大臣（だいじん）", "知事": "知事（ちじ）", "市長": "市長（しちょう）"},
        "level": "hard", "category": "はたらき",
    },
    {
        "emoji": "", "hint": "法律を 作る 権限を もつ、国の 最高 機関は？",
        "hint_ruby": "<ruby>法律<rt>ほうりつ</rt></ruby>を <ruby>作<rt>つく</rt></ruby>る <ruby>権限<rt>けんげん</rt></ruby>を もつ、<ruby>国<rt>くに</rt></ruby>の <ruby>最高<rt>さいこう</rt></ruby> <ruby>機関<rt>きかん</rt></ruby>は？",
        "answer": "国会",
        "choices": ["国会", "内閣", "裁判所", "県庁"],
        "choices_ruby": {"国会": "国会（こっかい）", "内閣": "内閣（ないかく）", "裁判所": "裁判所（さいばんしょ）", "県庁": "県庁（けんちょう）"},
        "level": "hard", "category": "はたらき",
    },
    {
        "emoji": "", "hint": "裁判を 行う 権限を もつ 国の 機関は？",
        "hint_ruby": "<ruby>裁判<rt>さいばん</rt></ruby>を <ruby>行<rt>おこな</rt></ruby>う <ruby>権限<rt>けんげん</rt></ruby>を もつ <ruby>国<rt>くに</rt></ruby>の <ruby>機関<rt>きかん</rt></ruby>は？",
        "answer": "裁判所",
        "choices": ["裁判所", "国会", "内閣", "警察"],
        "choices_ruby": {"裁判所": "裁判所（さいばんしょ）", "国会": "国会（こっかい）", "内閣": "内閣（ないかく）", "警察": "警察（けいさつ）"},
        "level": "hard", "category": "はたらき",
    },

    # ── ちり・地理 ──
    {
        "emoji": "", "hint": "川や 雨水が 長い 年月を かけて 岩を 削って できた 深い 谷は？",
        "hint_ruby": "<ruby>川<rt>かわ</rt></ruby>や <ruby>雨水<rt>あまみず</rt></ruby>が <ruby>長<rt>なが</rt></ruby>い <ruby>年月<rt>ねんげつ</rt></ruby>を かけて <ruby>岩<rt>いわ</rt></ruby>を <ruby>削<rt>けず</rt></ruby>って できた <ruby>深<rt>ふか</rt></ruby>い <ruby>谷<rt>たに</rt></ruby>は？",
        "answer": "峡谷",
        "choices": ["峡谷", "平野", "盆地", "台地"],
        "choices_ruby": {"峡谷": "峡谷（きょうこく）", "平野": "平野（へいや）", "盆地": "盆地（ぼんち）", "台地": "台地（だいち）"},
        "level": "hard", "category": "ちり",
    },
    {
        "emoji": "", "hint": "山や 丘に 囲まれた、低くて 平らな 土地は？",
        "hint_ruby": "<ruby>山<rt>やま</rt></ruby>や <ruby>丘<rt>おか</rt></ruby>に <ruby>囲<rt>かこ</rt></ruby>まれた、<ruby>低<rt>ひく</rt></ruby>くて <ruby>平<rt>たい</rt></ruby>らな <ruby>土地<rt>とち</rt></ruby>は？",
        "answer": "盆地",
        "choices": ["盆地", "平野", "台地", "峡谷"],
        "choices_ruby": {"盆地": "盆地（ぼんち）", "平野": "平野（へいや）", "台地": "台地（だいち）", "峡谷": "峡谷（きょうこく）"},
        "level": "hard", "category": "ちり",
    },
    {
        "emoji": "", "hint": "海に 向かって 細長く 突き出た 陸地の 部分を 何と 言う？",
        "hint_ruby": "<ruby>海<rt>うみ</rt></ruby>に <ruby>向<rt>む</rt></ruby>かって <ruby>細長<rt>ほそなが</rt></ruby>く <ruby>突<rt>つ</rt></ruby>き<ruby>出<rt>で</rt></ruby>た <ruby>陸地<rt>りくち</rt></ruby>の <ruby>部分<rt>ぶぶん</rt></ruby>を <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "半島",
        "choices": ["半島", "岬", "島", "湾"],
        "choices_ruby": {"半島": "半島（はんとう）", "岬": "岬（みさき）", "島": "島（しま）", "湾": "湾（わん）"},
        "level": "hard", "category": "ちり",
    },

    # ── スポーツ ──
    {
        "emoji": "", "hint": "4年に 1度 開かれる、世界最大の スポーツ 大会は？",
        "hint_ruby": "4<ruby>年<rt>ねん</rt></ruby>に 1<ruby>度<rt>ど</rt></ruby> <ruby>開<rt>ひら</rt></ruby>かれる、<ruby>世界最大<rt>せかいさいだい</rt></ruby>の スポーツ <ruby>大会<rt>たいかい</rt></ruby>は？",
        "answer": "オリンピック",
        "choices": ["オリンピック", "ワールドカップ", "インターハイ", "アジア大会"],
        "choices_ruby": {"アジア大会": "アジア大会（たいかい）"},
        "level": "hard", "category": "スポーツ",
    },
    {
        "emoji": "", "hint": "柔道や 剣道のように、日本で 生まれた 武道を まとめて 何と 言う？",
        "hint_ruby": "<ruby>柔道<rt>じゅうどう</rt></ruby>や <ruby>剣道<rt>けんどう</rt></ruby>のように、<ruby>日本<rt>にほん</rt></ruby>で <ruby>生<rt>う</rt></ruby>まれた <ruby>武道<rt>ぶどう</rt></ruby>を まとめて <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>う？",
        "answer": "武道",
        "choices": ["武道", "体操", "格闘技", "スポーツ"],
        "choices_ruby": {"武道": "武道（ぶどう）", "体操": "体操（たいそう）", "格闘技": "格闘技（かくとうぎ）"},
        "level": "hard", "category": "スポーツ",
    },

    # ── たべもの ──
    {
        "emoji": "", "hint": "大豆を 発酵させて 作る、日本の 伝統的な 調味料は？",
        "hint_ruby": "<ruby>大豆<rt>だいず</rt></ruby>を <ruby>発酵<rt>はっこう</rt></ruby>させて <ruby>作<rt>つく</rt></ruby>る、<ruby>日本<rt>にほん</rt></ruby>の <ruby>伝統的<rt>でんとうてき</rt></ruby>な <ruby>調味料<rt>ちょうみりょう</rt></ruby>は？",
        "answer": "みそ",
        "choices": ["みそ", "しょうゆ", "酢", "みりん"],
        "choices_ruby": {"酢": "酢（す）"},
        "level": "hard", "category": "たべもの",
    },
    {
        "emoji": "", "hint": "牛乳を 乳酸菌で 発酵させて 作る 食品は？",
        "hint_ruby": "<ruby>牛乳<rt>ぎゅうにゅう</rt></ruby>を <ruby>乳酸菌<rt>にゅうさんきん</rt></ruby>で <ruby>発酵<rt>はっこう</rt></ruby>させて <ruby>作<rt>つく</rt></ruby>る <ruby>食品<rt>しょくひん</rt></ruby>は？",
        "answer": "ヨーグルト",
        "choices": ["ヨーグルト", "バター", "チーズ", "アイス"],
        "choices_ruby": {},
        "level": "hard", "category": "たべもの",
    },
]


def get_questions_by_level(level: str) -> list:
    """指定したレベルの問題だけを返す関数"""
    return [q for q in QUESTIONS if q["level"] == level]


def get_questions_by_category(category: str) -> list:
    """指定したカテゴリーの問題だけを返す関数（将来の拡張用）"""
    return [q for q in QUESTIONS if q["category"] == category]
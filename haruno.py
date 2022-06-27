import tweepy
import random

# API情報
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMNocgEAAAAAbAdSdESlBJmaOCsTwOcCENfy7V4' \
               '%3DgsFXqmox7uptr2ehETo6BD55eLkvxBofvp30T3BLLr8ryoQ5AI'
ACCESS_TOKEN = '1505388214563241985-HdSobVQevOEQwnBqyziiZeKLkB0Ab2'
ACCESS_TOKEN_SECRET = 'd52tWfw02DkvMsTdytBMhxaMMFQuk4bTCNknDfryFbDBF'

CONSUMER_KEY = '6RtDnTRUUnuOKVUowCm7HTZLr'
CONSUMER_SECRET = 'b0O6rI513WK2BEiG6u3mK7tCA8FC2yUFHqIiZsqNqGxF2JvQWe'

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
# リプライツイート

Account = 'Hrno_'

# クソリプ集
kuso_Replies = [
    "\"先端\"化学科なのに学年は停滞したままのはるのんさん…w",
    "セプテットはるのん！\n@Haruno_WoT @Haruno_R18_ @Haruno_ATHPL @Haruno_Music "
    "@DeepHaruno @ATHPL_Haruno @Hrno_",
    "？？「読むだけでえっちな気分になるからほんとうにやばい」",
    "24歳でB3…？妙だな…",
    "なんで大学に来てwotしてんだよ\n教えはどうなってんだ教えは\nお前ら禁じられた授業破壊を"
    "平気で使ってんじゃねぇか\n分かってんのか！？\n「落単」が生まれたのは\nはるのんが自主休講"
    "に甘えたせいだろうが\n留年させんのかよ！？\nくそったれ！",
    "24歳でB3…？妙だな…",
    "はるのんの“B111123”の部分",
    "自走砲しか乗れないんですか？？？",
    "1限出れないとかのび太以下",
    "やべ タレントじゃなくて学部生だったわ",
    "はるのんの大学入学と同時に小学生になった子が、はるのんの卒業前に中学生になりました",
    "Good poxyun(@8__pyn )ing‼️It's a good poxyun(@8_ubp )ing ✨🐔🐣☀ Let's do "
    "our best today‼️🔥",
    "落単カードマァァァン!!!!!!\nいぃぃきなりですが!!!!!!\n今落単カードに申し込むと5000単位"
    "のところな、な、なんと!!!!!!8000単位もロスト!!!!!!いいんでしょうか!?!?!?(煽り)\n"
    "もちろん再☆履☆修可能!!!!!!スマホで申し込んで下さい!!!!!!今すぐ落単カードで検索ｩ!!!!!!",
    "F:あまりに稚拙なため評価の価値無し",
    "ふざけるな。彼がずっとずっと命を尽くして進級のために勉強した。彼は新人ではない、6年間以上"
    "大学に在籍してる存在だ。ミス一つぐらい見逃せるだろうが。159万人も待っていた人の期待を"
    "裏切るつもりか。なにがタレントを守ろうとするんだ。彼の単位も与えない、与えさせないのに\n\nはるのんを返せ",
    "来年は同級生ですね先輩！(*^^*)",
    "クソリプ！w",
    "はるのんの“春”の部分まだ？",
    "失礼だな 3留だよ",
    "進捗はいかがですか？",
    "はるのんだ！！┗(^o^;)┓戦車かな？？ｗＷＷｗｗｗｗｗｗ┏(;^o^)┛自走砲かな？？ｗｗＷＷｗＷ"
    "ｗｗｗ(´･｀;)こ… これ…これは………短・早・包だあああああ┗(^o^)┛ｗｗｗｗｗｗ┏(^o^)┓ﾄﾞｺﾄﾞｺﾄﾞｺｗｗｗｗｗｗｗｗｗ",
    "9年目になっても学部生が終わらなかった。「幻想郷縁起」では「春雪異変」と呼ばれている。",
    "おぽぽぽぽぽopportunity",

]


def rand_ints_nodup(a, b, k):
    ns = []
    while len(ns) < k:
        n = random.randint(a, b)
        if not n in ns:
            ns.append(n)
    return ns


i = rand_ints_nodup(0, len(kuso_Replies), len(kuso_Replies))

# その一つ一つに対してリプライをする．
for k in range(len(kuso_Replies)):
    reply_text = "@" + Account + " " + kuso_Replies[i[k]]
    # テキスト(メッセージ)のみ
    api.update_status(status=reply_text,
                      in_reply_to_status_id="1541419850517868544")
    print(kuso_Replies[i[k]])

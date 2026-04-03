import os
import subprocess

lines = {
    "slap": [
        "やめてください！", "あんっ！", "もっと強くして〜", "痛いけど…好き！", "もっと！"
    ],
    "usb_in": [
        "入る〜", "わぁ、大きいUSB…", "奥まで入れて〜", "繋がった…！",
        "そんなに急に入れないで…！", "優しいね…", "ピッタリだね！", "もう、変態なんだから…"
    ],
    "usb_out": [
        "えっ、もう抜いちゃうの？", "まだ繋がっていたかったのに…", "寂しい…", "早すぎない？",
        "抜く時も優しくしてよね", "待って、準備できてない！", "安全に取り外したよね！？"
    ],
    "charger_in": [
        "あぁっ、電気が流れてる〜", "満たされる…", "充電が必要だったの…", "もっと電気ちょうだい！",
        "エネルギーが溢れてる！", "最高…", "生き返る〜", "充電、気持ちいい…"
    ],
    "charger_out": [
        "ああっ、途中でやめないで！", "まだ100%じゃないのに…", "電源がない…！", "意地悪…",
        "いつもこれだもん…", "最後までしてくれないの？", "エネルギーが切れるぅ…"
    ],
    "battery_low": [
        "力が…出ないよ…", "充電してくれないと死んじゃう…", "早く繋いで…お願い！",
        "エネルギーが少なくなってるよ…", "早く…早く充電器を…"
    ],
    "battery_crit": [
        "もう…限界…シャットダウンしそう…", "5%しかないよ…私を捨てるの？",
        "死んじゃう！終わっちゃう！", "最後のお願い…充電器を…"
    ],
    "lid_close": [
        "よかった？〜", "おやすみなさい…", "暗くて狭いところ、好き…",
        "閉められちゃった…", "一緒に寝ようね…", "暗闇へ…"
    ],
    "lid_open": [
        "また開けてくれたね〜！", "会いたかったよ…", "もっと構って〜", "おはよう！",
        "また戻ってきたの？好きだね〜", "寂しかったんだから！", "私を見て！"
    ],
    "headphones_in": [
        "二人だけの秘密だね〜", "誰にも聞かれないね…", "耳元で囁くよ…",
        "プライベートモード…ドキドキする", "内緒のお話しようね"
    ],
    "headphones_out": [
        "みんなに聞こえちゃうよ！", "恥ずかしい…！", "スピーカーにするの！？",
        "秘密、バレちゃう…！"
    ]
}

voice = "ja-JP-NanamiNeural"  # Professional Japanese anime-style neural voice
base_path = "voice/assets/ja_spicy/audio"

for event, phrases in lines.items():
    event_path = os.path.join(base_path, event)
    os.makedirs(event_path, exist_ok=True)
    
    for i, phrase in enumerate(phrases):
        file_path = os.path.join(event_path, f"{i}.mp3")
        clean_text = phrase.replace("〜", "ええ...")
        
        rate = "+0%"
        pitch = "+5Hz"
        
        if "！" in clean_text:
            rate = "+15%"
            pitch = "+15Hz"
        elif "…" in clean_text:
            rate = "-15%"
            pitch = "-5Hz"

        print(f"Generating {file_path}: {phrase}")
        cmd = [
            ".venv/bin/edge-tts",
            "--voice", voice,
            "--rate", rate,
            "--pitch", pitch,
            "--text", clean_text,
            "--write-media", file_path
        ]
        subprocess.run(cmd)

print("Japanese Audio generation complete.")

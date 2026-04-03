import os
import subprocess

lines = {
    "slap": [
        "Hey! Not cool.", "What was that for?", "Ow!", "I felt that!", "Rude!",
        "Do that again. I DARE you.", "Really? REALLY?!", "Oh you're gonna regret that.", "I'm keeping score, you know.",
        "Please stop...", "Why are you like this?!", "I'm fragile!", "Not again!",
        "THE PAIN! Oh, the humanity!", "Is this what I was manufactured for?!", "Tell Apple... I died a hero.",
        "...", "I don't even feel it anymore.", "Whatever."
    ]
}

voice = "en-US-AriaNeural"  # Professional female
base_path = "voice/assets/en_default/audio"

for event, phrases in lines.items():
    event_path = os.path.join(base_path, event)
    os.makedirs(event_path, exist_ok=True)
    
    for i, phrase in enumerate(phrases):
        file_path = os.path.join(event_path, f"{i}.mp3")
        
        rate = "+0%"
        pitch = "+0Hz"
        
        if "!" in phrase:
            rate = "+15%"
            pitch = "+5Hz"
        elif "..." in phrase:
            rate = "-15%"
            pitch = "-5Hz"
            
        if phrase == "...":
            # Just whisper something or stay silent. Edge TTS needs words.
            phrase = "Sigh."
            rate = "-50%"
            pitch = "-20Hz"

        print(f"Generating SFW {file_path}: {phrase}")
        cmd = [
            ".venv/bin/edge-tts",
            "--voice", voice,
            "--rate", rate,
            "--pitch", pitch,
            "--text", phrase,
            "--write-media", file_path
        ]
        subprocess.run(cmd)

print("SFW Audio generation complete.")

import vosk, wave, json

def main():
    voice = wave.open("test-voice.wav", "rb")
    model = vosk.Model("vosk-model-small-ja-0.22")
    samplerate = voice.getframerate()
    rec = vosk.KaldiRecognizer(model, samplerate)
    rec.SetWords(True)

    while True:
        data = voice.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            output = rec.Result()
            json_dict = json.loads(output)

    print(json.loads(rec.FinalResult())['text'])

if __name__ == "__main__":
    main()
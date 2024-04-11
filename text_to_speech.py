from TTS.api import TTS


def generate_audio(text, speaker_wav="output.wav", language="en", file_path="result.wav"):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # "It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent."
    tts.tts_to_file(text=text,
                file_path=file_path,
                speaker_wav=speaker_wav,
                language="en")

    return file_path
from llm_client import ask_llm
from play_audio import play_audio
from record_audio import record_and_save_audio
from speech_recognition import transcribe_audio
from text_to_speech import generate_audio
from util import make_short_answer

user_input = "user_input"


def main():
    mp3_file = record_and_save_audio(filename=user_input)
    print(f"Recording saved as {mp3_file}")
    transcribed_text = transcribe_audio(mp3_file)
    print(transcribed_text)
    response = ask_llm(transcribed_text, api_choice='ollama')
    response = make_short_answer(response)
    print(response)
    response_voice_file = generate_audio(
        response, file_path="response.wav", 
        speaker_wav=user_input+".wav"
        )
    play_audio(response_voice_file)


if __name__ == "__main__":
    main()

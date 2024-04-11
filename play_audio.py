import simpleaudio as sa

def play_audio(filename):
    """
    Play a WAV audio file.

    Args:
        filename (str): The path to the WAV file to be played.
    """
    try:
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done() 
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

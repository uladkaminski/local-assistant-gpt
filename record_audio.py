import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import threading

def record_and_save_audio(sample_rate=44100, threshold=0.01, silence_duration=3, filename="output"):
    """
    Records audio from the default microphone until silence is detected, then saves it as an MP3 file.

    :param sample_rate: Sampling rate in Hz.
    :param threshold: Amplitude threshold to consider as silence.
    :param silence_duration: Duration of silence in seconds to trigger the end of recording.
    :param filename: Base filename for the output files (without extension).
    :return: Name of the saved MP3 file.
    """
    device_info = sd.query_devices(sd.default.device, 'input')
    channel_count = device_info['max_input_channels']
    print(f"Recording audio from {device_info['name']} ({channel_count} channels)")

    recorded_audio = []
    silent_frames = 0
    recording_finished = threading.Event()

    def callback(indata, frames, time, status):
        nonlocal silent_frames
        max_amplitude = np.max(np.abs(indata))
        if max_amplitude < threshold:
            silent_frames += frames
            if silent_frames > sample_rate * silence_duration:
                recording_finished.set()
        else:
            silent_frames = 0
        recorded_audio.append(indata.copy())

    with sd.InputStream(callback=callback, samplerate=sample_rate, channels=channel_count, dtype='float32'):
        recording_finished.wait()

    # Concatenate and normalize the recorded audio
    recorded_audio = np.concatenate(recorded_audio, axis=0)
    recorded_audio_normalized = np.int16(recorded_audio / np.max(np.abs(recorded_audio)) * 32767)

    # Save as WAV
    wav_filename = f"{filename}.wav"
    write(wav_filename, sample_rate, recorded_audio_normalized)

    # Convert to MP3
    mp3_filename = f"{filename}.mp3"
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(mp3_filename, format="mp3")

    return mp3_filename


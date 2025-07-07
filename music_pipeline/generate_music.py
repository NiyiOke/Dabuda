from pydub import AudioSegment
from pydub.generators import Sine
import random


def generate_music(filename="output.mp3", length_seconds=60):
    """Generate a simple random melody and export as mp3."""
    segment = AudioSegment.silent(duration=0)
    for _ in range(length_seconds):
        freq = random.randint(200, 800)
        tone = Sine(freq).to_audio_segment(duration=1000)
        segment += tone
    segment.export(filename, format="mp3")


if __name__ == "__main__":
    generate_music()

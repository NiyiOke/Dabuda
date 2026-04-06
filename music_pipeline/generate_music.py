"""Generate a chill Amapiano-inspired track."""

from pydub import AudioSegment
from pydub.generators import Sine
import random

TEMPO = 110
BEAT_MS = int(60000 / TEMPO)


def _chord(frequencies, duration):
    chord = Sine(frequencies[0]).to_audio_segment(duration=duration)
    for f in frequencies[1:]:
        chord = chord.overlay(Sine(f).to_audio_segment(duration=duration))
    return chord


CHORDS = [
    (164.81, 207.65, 261.63),  # Em
    (185.00, 233.08, 293.66),  # F#m
    (196.00, 246.94, 311.13),  # G
    (174.61, 220.00, 277.18),  # F
]


def _bar():
    chord = random.choice(CHORDS)
    harmony = _chord(chord, BEAT_MS * 4)
    beat = AudioSegment.silent(duration=0)
    for _ in range(4):
        kick = Sine(55).to_audio_segment(duration=100).apply_gain(-3)
        beat += kick + AudioSegment.silent(duration=BEAT_MS - 100)
    return harmony.overlay(beat)


def generate_music(filename="output.mp3", minutes=60):
    """Generate a one-hour chill Amapiano-style track."""
    track = AudioSegment.silent(duration=0)
    bars = int(minutes * 60 / 4)
    for _ in range(bars):
        track += _bar()
    track.export(filename, format="mp3")


if __name__ == "__main__":
    generate_music()

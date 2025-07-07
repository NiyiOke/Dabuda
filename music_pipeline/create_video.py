import subprocess
from PIL import Image
import random


def create_cover(path='cover.png'):
    """Generate a simple colored cover image."""
    img = Image.new(
        'RGB',
        (1280, 720),
        (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ),
    )
    img.save(path)


def create_video(audio_file='output.mp3', video_file='output.mp4', cover_file='cover.png'):
    """Create a video from a static image and audio using ffmpeg."""
    create_cover(cover_file)
    cmd = [
        'ffmpeg',
        '-y',
        '-loop',
        '1',
        '-i',
        cover_file,
        '-i',
        audio_file,
        '-c:v',
        'libx264',
        '-c:a',
        'aac',
        '-shortest',
        video_file,
    ]
    subprocess.run(cmd, check=True)


if __name__ == '__main__':
    create_video()

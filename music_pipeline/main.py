import datetime
from generate_music import generate_music
from create_video import create_video
from upload_to_youtube import upload


def main():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    audio_file = f'music_{timestamp}.mp3'
    video_file = f'video_{timestamp}.mp4'
    generate_music(audio_file, length_seconds=60)
    create_video(audio_file, video_file)
    upload(video_file, title=f'Automated Track {timestamp}')


if __name__ == '__main__':
    main()

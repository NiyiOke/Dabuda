# Automated YouTube Music Pipeline

This folder contains a minimal example of generating music, creating a video, and uploading it to YouTube automatically.

## Requirements
- Python 3
- ffmpeg installed and available in your PATH
- `pydub`, `Pillow`, `google-api-python-client`, `google-auth-oauthlib`

Install dependencies:
```bash
pip install pydub Pillow google-api-python-client google-auth-oauthlib
```

## Setup
1. Create a Google Cloud project and enable the YouTube Data API.
2. Download `credentials.json` for OAuth and place it in this directory.
3. Run `python upload_to_youtube.py` once to complete OAuth. A `token.pickle` file will be created for future authentication.

## Usage
Run `python main.py` to generate a one-minute track, create a video and upload it to your YouTube channel. The script can be scheduled daily using cron or any scheduler.

```bash
0 0 * * * /usr/bin/python /path/to/main.py
```

This is a simple demo. You can extend the music generation and video creation logic as needed.

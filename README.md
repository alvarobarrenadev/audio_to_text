# Audio to Text Transcriber

This project allows you to download audio from a YouTube or TikTok video, transcribe it to text using OpenAI's Whisper model, and save the transcription to a text file.

## Requirements

- Python 3.10
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/download)

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/alvarobarrenadev/audio_to_text.git
    cd audio_to_text
    ```

2. Create a virtual environment with Miniconda or Conda and activate it:
    ```sh
    conda create -n transcriber python=3.10
    conda activate transcriber
    ```

3. Install the necessary dependencies:
    ```sh
    pip install openai-whisper yt_dlp
    ```

## Usage

1. Run the *`app.py`* script:
    ```sh
    python3 app.py
    ```

2. Enter the URL of the YouTube or TikTok video when prompted.

3. The script will download the audio, transcribe it, and save the transcription to a file named *`transcripcion.txt`*.

## Files

- *`app.py`*: Main script that downloads the audio, transcribes it, and saves the transcription.
- *`.gitignore`*: Files and directories ignored by Git.

## Notes

- Ensure you have enough disk space to download and process the audio files.
- The downloaded audio file will be automatically deleted after transcription to save space.

## Whisper Models

Whisper offers several models with different levels of accuracy and speed. Below are the available options:

- **tiny**: The smallest and fastest model, but with lower accuracy. Ideal for devices with limited resources.
- **base**: Slightly larger than the tiny model, offering a balance between speed and accuracy.
- **small**: Intermediate-sized model, with better accuracy than the tiny and base models, but still relatively fast.
- **medium**: Larger than the small model, with significantly improved accuracy, suitable for tasks requiring higher precision.
- **large**: The largest and most accurate model, but also the slowest and most resource-intensive.
- **large-v2**: An improved version of the large model, with additional adjustments to enhance accuracy.

## Warnings

- The script ignores `FutureWarning` warnings to avoid unnecessary messages during execution.

## Contributing

Contributions are welcome. If you want to improve this project, feel free to fork it and create a pull request.
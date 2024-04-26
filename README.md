# dramasub
Extract timestamp subtitles from drama series videos

## Algorithm steps

1. Extract audio from the source file 
2. Voice activity detection (VAD)
3. Convert speech regions into flac to be sent to Google Web Speech API
4. Transcription (ASR)
5. Translation (if source language is different from destination language)

## Install
* create and activate a shell with python ^3.11
* install poetry: `pip install poetry`
* init the environment: `poetry shell`
* install the dependencies `poetry install --no-root`
* Install **ffmpeg**, used for converting video and audio has never been so easy: `sudo apt-get update & sudo apt install -y ffmpeg`
* Quickly check that it works: 
   - transcription from English to English (WITHOUT translation): `pytest tests/functional/test_on_short_audio.py::test_en2en_from_console`
   - transcription from French to English (WITH translation): `pytest tests/functional/test_on_short_audio.py::test_fr2en_from_console`
* Comprehensively checks that everything works well: `pytest -v`
* To transcribe a video: 
    - whole usage help: `python -m dramasub -h`
    - list of supported subtitle formats: `python -m dramasub --list-formats`
    - list of supported languages: `python -m dramasub --list-languages`
    - example: `python -m dramasub -o data/zh-playing_house.e21.360p.en_sub.srt -F srt -S zh-CN -D en data/zh-playing_house.e21.360p.mp4`
    - example: `python -m dramasub -o data/ko-the.limit.2022.360p.en_sub.srt -F srt -S ko -D en data/ko-the.limit.2022.360p.mp4`

## Good points
- `dramasub` is very fast: less than 5 min to transcribe and translate a 1h30 movie from korean to english
  - 4sec for VAD
  - 4min for ASR
  - the remaining for translation
  - Not sure whether we can keep this pace in a standalone deployment on a single PC or mobile (with or without GPU)
      - to check when moving to `whisper-large-v3` and `whisper-tiny`

## Issues and limits

- no speaker diarization: no distinction of the speakers
- a lot of speech regions are not transcribed
    - are they detected? 
    - might need a dedicated model for VAD (as a tokenizer)
- a lot of inaccurate translation
    - might need to check how accurate is the result of the ASR
- texts in videos are transcribed
    - annotations describing a particular expression, word, person, place, etc.
    - credits at the beginning and the end
- No informative font:
    - the speaker is not the one facing in the screen now
    - speech that is kept in mind (dream, thinking, etc.)
    - lyrics of background songs (usually in italic with some characters like music notes)
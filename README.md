# dramasub
Extract timestamp subtitles from drama series videos

## Install
* create and activate a shell with python ^3.11
* install poetry: `pip install poetry`
* install the dependencies `poetry install --no-root`
* Install **ffmpeg**, used for converting video and audio has never been so easy: `sudo apt-get update & sudo apt install -y ffmpeg`
* Check that everything works fine:
    - run this
    ```commandline
    wget https://eslyes.com/easydialogs/audio/dailylife002.mp3 -O data/i_have_a_honda.mp3
    python -m dramasub -C 1 -o data/i_have_a_honda.srt -F srt -S en -D en data/i_have_a_honda.mp3
    ```
    - you should get something like this
    ```
Converting speech regions to FLAC files: 100% |##################################################################################################################################################################| Time:  0:00:00
Performing speech recognition: 100% |############################################################################################################################################################################| Time:  0:00:12
Subtitles file created at data/i_have_a_honda.srt
    ```


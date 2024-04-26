import os


def test_en2en_from_console():
    """
    python -m dramasub -C 1 -o data/i_have_a_honda.srt -F srt -S en -D en data/i_have_a_honda.mp3 > data/i_have_a_honda.log 2>&1
    """
    input_url = "https://eslyes.com/easydialogs/audio/dailylife002.mp3"
    basename = "en-i_have_a_honda"
    input_path = f"data/{basename}.mp3"
    output_format = "srt"
    output_path = f"data/{basename}.{output_format}"
    log_path = f"data/{basename}.log"
    source_language = "en"
    dest_language = "en"
    os.system(f"wget {input_url} -O {input_path}")
    assert os.path.exists(input_path)
    os.system(f"python -m dramasub -C 1 -o {output_path} -F {output_format} -S {source_language} -D {dest_language}"
              f" {input_path} > {log_path} 2>&1")
    assert os.path.exists(log_path)
    assert os.path.exists(output_path)


def test_fr2en_from_console():
    """pytest tests/functional/test_on_short_audio.py::test_fr2en_from_console"""
    input_url = "https://www.podcastfrancaisfacile.com/wp-content/uploads/files/boulangerie1.mp3?_=1"
    basename = "fr-boulangerie.mp3"
    input_path = f"data/{basename}.mp3"
    output_format = "srt"
    output_path = f"data/{basename}.{output_format}"
    log_path = f"data/{basename}.log"
    source_language = "fr"
    dest_language = "en"
    os.system(f"wget {input_url} -O {input_path}")
    assert os.path.exists(input_path)
    os.system(f"python -m dramasub -C 1 -o {output_path} -F {output_format} -S {source_language} -D {dest_language}"
              f" {input_path} > {log_path} 2>&1")
    assert os.path.exists(log_path)
    assert os.path.exists(output_path)

def test_translate_fr2en():
    """pytest tests/functional/test_translator.py::test_translate_fr2en"""
    from dramasub import Translator
    Translator(src="fr", dst="en")("Qu’est-ce que vous avez comme tartes ?")

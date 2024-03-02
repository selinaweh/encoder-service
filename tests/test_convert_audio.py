import os
import tempfile

from pydub.utils import mediainfo

from src.service.encoder_service import convert_audio

relative_path = os.path.join(os.path.dirname(__file__), '..', 'tests', 'resources')


def create_tempfile(content):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(content)
        temp_file_path = temp_file.name
        return temp_file_path


def test_convert_audio_to_wav():
    with open(os.path.join(relative_path, 'HORST WESSEL LIED (DIE FAHNE HOCH - GROSSES BLAS ORCHESTER.mp3'),
              "rb") as file:
        content = file.read()
    converted_content = convert_audio(content, 'mp3', 'wav')
    temp_path = create_tempfile(converted_content)
    info = mediainfo(temp_path)
    assert info['format_name'] == 'wav'


def test_convert_audio_to_ogg():
    with open(os.path.join(relative_path, 'HORST WESSEL LIED (DIE FAHNE HOCH - GROSSES BLAS ORCHESTER.mp3'),
              "rb") as file:
        content = file.read()
    converted_content = convert_audio(content, 'mp3', 'ogg')
    temp_path = create_tempfile(converted_content)
    info = mediainfo(temp_path)
    assert info['format_name'] == 'ogg'


def test_convert_audio_to_flac():
    with open(os.path.join(relative_path, 'HORST WESSEL LIED (DIE FAHNE HOCH - GROSSES BLAS ORCHESTER.mp3'),
              "rb") as file:
        content = file.read()
    converted_content = convert_audio(content, 'mp3', 'flac')
    temp_path = create_tempfile(converted_content)
    info = mediainfo(temp_path)
    assert info['format_name'] == 'flac'

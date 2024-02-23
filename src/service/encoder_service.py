from io import BytesIO
from pydub import AudioSegment


def convert(filename: str, from_format: str, to_format: str):
    """Converts audio file from one format to another and exports it
    Params:
        filename: name of original file
        from_format: format of og audio file
        to_format: desired format"""
    raw_audio = AudioSegment.from_file(f"{filename}.{from_format}", format=from_format)
    converted_file = raw_audio.export(f"{filename}.{to_format}", format=to_format)
    return converted_file


def convert_audio(content: bytes, from_format: str, to_format: str) -> bytes:
    """Converts audio content from one format to another and returns it as bytes"""
    input_audio = AudioSegment.from_file(BytesIO(content), format=from_format)
    buffer = BytesIO()
    input_audio.export(buffer, format=to_format)
    return buffer.getvalue()




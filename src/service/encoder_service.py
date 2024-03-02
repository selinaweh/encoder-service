from io import BytesIO

from pydub import AudioSegment


def convert_audio(content: bytes, from_format: str, to_format: str) -> bytes:
    """
    Converts audio content from one format to another and returns it as bytes
    """
    input_audio = AudioSegment.from_file(BytesIO(content), format=from_format)
    buffer = BytesIO()
    input_audio.export(buffer, format=to_format)
    return buffer.getvalue()

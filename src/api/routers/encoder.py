from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette.responses import Response
from src.api.myapi.conversion_model import ConversionResponse
from src.service.encoder_service import convert_audio
from src.settings.error_messages import FILE_CONVERSION_ERROR, UNSUPPORTED_FORMAT_ERROR

router = APIRouter(
    prefix="/api/encoder", tags=["Encoder Service"]
)


@router.post("/convert", response_model=ConversionResponse, response_model_exclude_none=True)
def convert_audio_endpoint(src_format: str, target_format: str, file: UploadFile = File(...)):
    valid_target_formats = ["wav", "flac", "ogg"]
    if target_format not in valid_target_formats:
        raise HTTPException(status_code=400, detail=UNSUPPORTED_FORMAT_ERROR)

    try:
        input_data = file.file.read()
        output_data = convert_audio(input_data, src_format, target_format)
        return Response(content=output_data, media_type=f"audio/{target_format}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{FILE_CONVERSION_ERROR}: {str(e)}")

from fastapi import APIRouter, UploadFile, File, HTTPException, Form
import base64
from src.api.myapi.conversion_model import ConversionResponse, InputModel
from src.service.encoder_service import convert_audio
from src.settings.error_messages import FILE_CONVERSION_ERROR, UNSUPPORTED_FORMAT_ERROR

router = APIRouter(
    prefix="/api/encoder", tags=["Encoder Service"]
)


@router.post("/convert", response_model=ConversionResponse)
def convert_audio_endpoint(input_model: InputModel, file: UploadFile = File(...)):      #src_format: str, target_format: str
    valid_target_formats = ["wav", "flac", "ogg"]
    if input_model.target_format not in valid_target_formats:
        raise HTTPException(status_code=400, detail=UNSUPPORTED_FORMAT_ERROR)

    try:
        input_data = file.file.read()
        print(f"input_data:{input_data}")
        output_data = convert_audio(input_data, input_model.src_format, input_model.target_format)
        print(f"output_data: {output_data}")
        base64_encoded_output = base64.b64encode(output_data).decode('utf-8')
        conversion_response = ConversionResponse(file_type=input_model.target_format, content=base64_encoded_output)
        return conversion_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{FILE_CONVERSION_ERROR}: {str(e)}")

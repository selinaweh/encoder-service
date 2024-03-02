# Encoder Service

## Description

This Service converts a given audio file (Upload file) to a different format. The supported formats are MP3, WAV, FLAC, and OGG.


## Dependencys (outside Docker)
The Python module pydub is dependent on the ffmpeg package. When using the service within Docker, this package is loaded automatically. As the package in turn requires various dependencies, the build of the container can take a few minutes.
If used outside the container, the package must be downloaded manually and placed in the folder of the executing Python file (encoder_service.py):
https://www.ffmpeg.org/download.html


## Test

For testing purpose a mp3-file was added to the folder resources.

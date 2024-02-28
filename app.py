from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from generate_audio import generate_audio


app = FastAPI()

AUDIO_DIRECTORY = 'audio'


@app.get('/generate')
def make_audio(prompt: str):
    if prompt != '':
        generate_audio(prompt, AUDIO_DIRECTORY)
    return "Audio generated"


@app.get('/audio/{filename}')
async def get_audio(filename: str):
    return FileResponse(f"{AUDIO_DIRECTORY}/{filename}")


#if __name__ == "__main__":
#    uvicorn.run(app, port=8000, host='0.0.0.0')
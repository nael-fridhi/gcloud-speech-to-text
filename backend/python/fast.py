from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from google.cloud import speech_v1
import io
import json
import os

app = FastAPI()

client = speech_v1.SpeechAsyncClient()

streaming_config = speech_v1.StreamingRecognitionConfig(
    config=speech_v1.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    ),
    interim_results=True
)

CHUNK_SIZE = 8192  # Define the size of each chunk (e.g., 8 KB)

async def request_generator(buffer):
    yield speech_v1.StreamingRecognizeRequest(streaming_config=streaming_config)
    while True:
        chunk = buffer.read(CHUNK_SIZE)  # Await the read operation
        if not chunk:
            break
        yield speech_v1.StreamingRecognizeRequest(audio_content=chunk)

async def recognize(requests):
    full_transcript = ""
    # Open a streaming request
    async for response in await client.streaming_recognize(requests):
        for result in response.results:
            #if result.is_final:
            #    full_transcript += result.alternatives[0].transcript
            data = {
                'alternatives': [{
                    'transcript': alternative.transcript,
                    'confidence': alternative.confidence
                } for alternative in result.alternatives],
                'is_final': result.is_final
            }
            yield f"{json.dumps(data)}\n"
        #yield json.dumps({"transcript": full_transcript})
    


@app.post("/transcribe")
async def sse_endpoint(file: UploadFile = File(...)):
    buffer = io.BytesIO(await file.read())
    requests = request_generator(buffer)
    
    return StreamingResponse(recognize(requests), media_type="application/stream+json", headers={'Transfer-Encoding': 'chunked'})

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get("PORT", 3000))
    uvicorn.run(app, host='0.0.0.0', port=port)
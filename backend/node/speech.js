const express = require('express');
const fs = require('fs');
const speech = require('@google-cloud/speech');

const app = express();
const port = process.env.PORT || 3000;

const client = new speech.SpeechClient();

app.post('/transcribe', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'application/stream+json',
    'Transfer-Encoding': 'chunked'
  })
  const encoding = "LINEAR16";
  const sampleRateHertz = 16000;
  const languageCode = "en-US";

  const request = {
    config: {
      encoding: encoding,
      sampleRateHertz: sampleRateHertz,
      languageCode: languageCode,
    },
    interimResults: true,
  };

  const recognizeStream = client
    .streamingRecognize(request)
    .on('error', (err) => {
      console.error('Error during transcription:', err);
      res.status(500).send({ error: 'Transcription failed' });
    })
    .on('data', (data) => {
      res.write(JSON.stringify(data))
    })
    .on('end', () => { 
      res.end(); 
    });

  req.pipe(recognizeStream);
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

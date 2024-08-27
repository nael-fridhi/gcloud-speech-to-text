# gcloud-speech-to-text
This project provides a comprehensive solution for utilizing Google Cloud's Speech-to-Text API in streaming mode at scale. 
It includes backend implementations, scaling strategies, and a frontend application for a seamless user experience.

![GIF showing speech to text use case in real world](./docs/teaser.gif)


## Backend 

This folder contains backend developeed using two different programming language:

1. **Node.js:**  Leveraging the Express.js framework for a robust and efficient Node.js implementation.
   - [Learn more about the Node.js backend](./docs/node.md)
2. **Python:** Utilizing the FastAPI framework for a modern and asynchronous Python backend.
   - [Explore the Python FastAPI backend](./docs/python.md)


## Scale 

This project includes Python scripts designed to test the scalability of the backend and measure latencies.

- [Dive into the scaling strategies and analysis](./docs/scale.md)

## Frontend

Frontend application using nextJS to consume the API [Here](./docs/frontend.md)

**WIP**


## Resources 

**Python**

- [Socket Programming in Python](https://ismatsamadov.medium.com/an-introduction-to-socket-programming-in-python-ea5480ff658e)
- [ASGI vs WSGI](https://ismatsamadov.medium.com/asgi-vs-wsgi-87ba76d24365)
- [Gunicorn vs Uvicorn](https://ismatsamadov.medium.com/gunicorn-vs-uvicorn-369635b92809)

**Google Cloud Speech-to-Text API**

- [Google Cloud Speech-to-Text Documentation](https://cloud.google.com/speech-to-text/docs)
- [Speech-to-Text API Reference](https://cloud.google.com/speech-to-text/docs/reference/rest)
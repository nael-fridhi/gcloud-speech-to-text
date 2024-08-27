# Frontend to consume the backend API

This repository contains nextjs application that uses websocket to collected audio streams and send them to our backend which will use Speech to Text API in streaming mode in order to give us the text.


## Getting Started

- **locally:**
```
npm install
npm run dev
```


- **Google Cloud:**

```
# Configure gcloud in your laptop
gcloud auth application-default login

# Configure Docker with Artifact Registry credentials
gcloud auth configure-docker us-central1-docker.pkg.dev

# Build the docker image
docker build -t  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPOSITORY/YOUR_IMAGE_NAME:TAG .

# Push the docker image to Artifact Registry
docker push  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPOSITORY/YOUR_IMAGE_NAME:TAG

# Deploy to Google Cloud Run

gcloud run deploy \
  SERVICE_NAME \
  --image  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPOSITORY/YOUR_IMAGE_NAME \ 
  --port 3000 \
  --region us-central1 \
  --allow-unauthenticated

```


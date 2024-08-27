# Node Express JS Implementation

This is an implentation using Express JS Framework 


## Run the application locally
```
npm install
node speech.js
```
## Run the application in the cloud 
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

# Python FastAPI Implementation

This is an implentation using FAST API Framework 


## Run the application locally
```
# Create a virtual environment
python3 -m venv venv 
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# Launch the application
uvicorn fast:app --host 0.0.0.0 --port 8000

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

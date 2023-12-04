# https://cloud.google.com/sdk/gcloud/reference/run/deploy
export GOOGLE_CLOUD_PROJECT=<YOUR_PROJECT_ID>
gcloud config set project $GOOGLE_CLOUD_PROJECT
export SERVICE_NAME=<YOUR_SERVICE_NAME>
export ARTIFACT_REGISTRY_NAME=<YOUR_ARTIFACT_REGISTRY_NAME>
export REGION=<YOUR_REGION>

# Service Account
export SERVICE_ACCOUNT_EMAIL=<YOUR_SERVICE_ACCOUNT_EMAIL>

# Build and Deploy

# Artifact Registry
gcloud builds submit --tag $REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$ARTIFACT_REGISTRY_NAME/$SERVICE_NAME:latest

gcloud run deploy $SERVICE_NAME \
--image $REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$ARTIFACT_REGISTRY_NAME/$SERVICE_NAME:latest \
--platform managed \
--allow-unauthenticated \
--region=$REGION \
--ingress=all \
--min-instances=0 \
--concurrency=20 \
--service-account=$SERVICE_ACCOUNT_EMAIL \
--execution-environment=gen2    \
--cpu-boost \
--cpu=4 \
--memory=8Gi \


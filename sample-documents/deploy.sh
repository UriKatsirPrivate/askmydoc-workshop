# https://cloud.google.com/sdk/gcloud/reference/run/deploy
export GOOGLE_CLOUD_PROJECT=landing-zone-demo-341118
gcloud config set project $GOOGLE_CLOUD_PROJECT
export SERVICE_NAME=experts-hub-demo
export ARTIFACT_REGISTRY_NAME=cloud-run-source-deploy
export REGION=europe-west4
export SERVICE_ACCOUNT_EMAIL=experts-hub-demo@landing-zone-demo-341118.iam.gserviceaccount.com

# Artifact Registry
gcloud builds submit --tag $REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$ARTIFACT_REGISTRY_NAME/$SERVICE_NAME:latest

gcloud run deploy $SERVICE_NAME \
--image $REGION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/$ARTIFACT_REGISTRY_NAME/$SERVICE_NAME:latest \
--platform managed \
--allow-unauthenticated \
--region=$REGION \
--ingress=all \
--min-instances=1 \
--concurrency=20 \
--service-account=$SERVICE_ACCOUNT_EMAIL \
--execution-environment=gen2    \
--cpu-boost \
--cpu=1 \
--memory=1Gi \

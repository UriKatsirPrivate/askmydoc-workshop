# FROM python:3.10-slim
FROM python:3.10

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Optional: Upgrade pip version
# RUN pip3 install --upgrade pip
ENV SYSTEM_VERSION_COMPAT=1

# Install required libraries
RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
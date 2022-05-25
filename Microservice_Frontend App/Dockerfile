# lightweight python
FROM public.ecr.aws/docker/library/python:3.7-slim

# Copy local code to the container image.
COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

# Run the streamlit on container startup
CMD [ "streamlit", "run","--server.enableCORS","false","imgwebapp.py" ]

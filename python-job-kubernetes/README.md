#Buld docker with a local tag:
docker build -f Dockerfile -t hello-python:0.1 .

#Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE: docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]:
docker tag hello-python:0.1 jsrfntd/demo:v5

#Push the image to Dockerhub:
docker push jsrfntd/demo:v5
Clone the repository.

#build the docker file
docker build .

#check for the images
docker images

run the image with the Image ID by passing the python file
docker run -i -t <IMAGE ID> python omdbapi.py

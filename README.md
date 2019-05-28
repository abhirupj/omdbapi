Clone the repository.

git clone https://github.com/abhirupj/omdbapi.git

#build the docker file

docker build .

#check for the images

docker images

#run the image with the Image ID by passing the python file

docker run -i -t <IMAGE ID> python omdbapi.py

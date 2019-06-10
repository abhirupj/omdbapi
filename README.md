Git repo: https://github.com/abhirupj/omdbapi.git

1) To run the image directly from my image

I have added a repository in my docker hub.

# Pull the image

docker pull abhirup/omdb_api

#see the image listed

docker images abhirup/omdb_api

# run the docker image 

docker run -i -t abhirup/omdb_api python omdbapi.py

2) If you want to build your own image

# Clone the repo

git clone https://github.com/abhirupj/omdbapi.git

#build the docker file

docker build .

#check for the images

docker images

#run the image with the Image ID by passing the python file

docker run -i -t <IMAGE ID> python omdbapi.py

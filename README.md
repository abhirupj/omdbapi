Git repo: https://github.com/abhirupj/omdbapi.git

# To run the image directly from my image

I have added a repository in my docker hub.

1) Pull the image

docker pull abhirup/omdb_api

2) see the image listed

docker images abhirup/omdb_api

3) run the docker image 

docker run -i -t abhirup/omdb_api python omdbapi.py

# If you want to build your own image

1) Clone the repo

git clone https://github.com/abhirupj/omdbapi.git

2) build the docker file

docker build .

3) check for the images

docker images

4) run the image with the Image ID by passing the python file

docker run -i -t <IMAGE ID> python omdbapi.py

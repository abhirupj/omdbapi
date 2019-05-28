import requests
import json


def movie():
    movie_name = input("please enter the movie name: ")
    movie_year = input("please enter the movie year if you remember :")
    movie_database = "www.omdbapi.com"
    movie_apikey = "d8543567"
    movie_url = "http://{}/?apikey={}&t={}&y={}&plot=full&r=json".format(movie_database, movie_apikey, movie_name, movie_year)
    response = requests.get(movie_url)
    json_data = json.loads(response.text)
    x = json_data
    print('\n')
    print("################################# Final Result #################################")
    print('\n')
    print("Name : " + x['Title'])
    print("year :" + x['Year'])
    print("Cast :" + x['Actors'])
    print("Runtime : " + x['Runtime'])
    print("Rotten Tomatoes Rating : " + x['Ratings'][1]['Value'])
    print('\n')
    print('\n')


def main():
    try:
        movie()
    except KeyError as error:
        print("Could not get in the database please try again ")
        movie()
    except Exception as exception:
        print("Could not get in the database please try again ")
        print('\n')
        movie()


if __name__ == "__main__":
    main()


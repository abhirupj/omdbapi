import requests
import json
from termcolor import colored, cprint

def movie():
    try:
        movie_name = input("please enter the movie name: ")
        movie_year = input("please enter the movie year if you remember :")
        if movie_name == "":
            cprint('\ndo not enter empty string for movie name', 'red', attrs=['blink'])
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
        return 0;
        quit()
    except (KeyError, KeyboardInterrupt, NameError, EOFError) as error:
        cprint('Could not get in the database please try again','green', attrs=['blink'])
    except IndexError as error:
        cprint('something wrong while fetching the details','magenta',attrs=['blink'])

def main():
    movie()
if __name__ == "__main__":
    main()

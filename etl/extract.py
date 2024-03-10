# import libraries
import requests
import pandas as pd
from datetime import datetime

def extract_data(api_key, nb_page_to_load=10):
    # initialize a list to append the extracted data
    final_list = []
    n=0
    while n<nb_page_to_load:
        n+=1
        # sorted by popularity
        url = f"https://api.themoviedb.org/3/discover/movie?&sort_by=popularity.desc&offest=20&page={n}&api_key={api_key}"
        
        # Make the GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the list of movies
            results = data['results']
            # Append to the initial list
            final_list.extend(results)
        else:
            # If the request was not successful, print the error message and return None
            print(f"Failed to fetch data: {response.status_code}")
            return None
        
    return pd.DataFrame(final_list)
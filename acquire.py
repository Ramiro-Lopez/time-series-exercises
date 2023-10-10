import pandas as pd
import numpy as np 
import math
import requests

# =========================================================================================================

def get_people(response = requests.get('https://swapi.dev/api/people/')) -> pd.DataFrame:
    data = response.json() 
    people_df = pd.DataFrame(data['results'])
    next_page = data['next'] 

    while next_page:
        # Make a request to the API using the current next_page URL
        response = requests.get(next_page)
    
        # Check status code 
        if response.status_code == 200:
            data = response.json()
        
            # get information 
            number_of_people = data['count']
            next_page = data['next']
            previous_page = data['previous']
            number_of_results = len(data['results'])
            max_page = math.ceil(number_of_people / number_of_results)
        
            # Concat the results to the DataFrame
            people_df = pd.concat([people_df, pd.DataFrame(data['results'])]).reset_index(drop=True)
        
            # Print information about the current page
            print(f'{number_of_people=}')
            print(f'next_page: {next_page}')
            print(f'previous_page: {previous_page}')
            print(f'number_of_results: {number_of_results}')
            print(f'max_page: {max_page}')
        else:
            # Handle the case where the request was not successful (e.g., handle errors)
            print(f"Request failed with status code {response.status_code}")
        break  # Exit the loop if there's an issue with the request
    return(people_df)

# =========================================================================================================

def get_planets(response = requests.get('https://swapi.dev/api/planet/')) -> pd.DataFrame:
    data = response.json() 
    planet_df = pd.DataFrame(data['results'])
    next_page = data['next'] 

    while next_page:
        # Make a request to the API using the current next_page URL
        response = requests.get(next_page)
    
        # Check status code 
        if response.status_code == 200:
            data = response.json()
        
            # get information 
            number_of_people = data['count']
            next_page = data['next']
            previous_page = data['previous']
            number_of_results = len(data['results'])
            max_page = math.ceil(number_of_people / number_of_results)
        
            # Concat the results to the DataFrame
            people_df = pd.concat([people_df, pd.DataFrame(data['results'])]).reset_index(drop=True)
        
            # Print information about the current page
            print(f'{number_of_people=}')
            print(f'next_page: {next_page}')
            print(f'previous_page: {previous_page}')
            print(f'number_of_results: {number_of_results}')
            print(f'max_page: {max_page}')
        else:
            # Handle the case where the request was not successful (e.g., handle errors)
            print(f"Request failed with status code {response.status_code}")
        break  # Exit the loop if there's an issue with the request
    return(planet_df)

# =========================================================================================================

def get_starship(response = requests.get('https://swapi.dev/api/starships/')) -> pd.DataFrame:
    data = response.json() 
    starship_df = pd.DataFrame(data['results'])
    next_page = data['next'] 

    while next_page:
        # Make a request to the API using the current next_page URL
        response = requests.get(next_page)
    
        # Check status code 
        if response.status_code == 200:
            data = response.json()
        
            # get information 
            number_of_people = data['count']
            next_page = data['next']
            previous_page = data['previous']
            number_of_results = len(data['results'])
            max_page = math.ceil(number_of_people / number_of_results)
        
            # Concat the results to the DataFrame
            people_df = pd.concat([people_df, pd.DataFrame(data['results'])]).reset_index(drop=True)
        
            # Print information about the current page
            print(f'{number_of_people=}')
            print(f'next_page: {next_page}')
            print(f'previous_page: {previous_page}')
            print(f'number_of_results: {number_of_results}')
            print(f'max_page: {max_page}')
        else:
            # Handle the case where the request was not successful (e.g., handle errors)
            print(f"Request failed with status code {response.status_code}")
        break  # Exit the loop if there's an issue with the request
    return(starship_df)

# =========================================================================================================

def get_solar_data(solar_df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')) -> pd.DataFrame:
    solar_df.Date = pd.to_datetime(solar_df.Date)
    solar_df = solar_df.set_index("Date").sort_index()
    solar_df['Year'] = solar_df.index.year  
    solar_df['Month'] = solar_df.index.month
    solar_df.bfill()
    return(solar_df)
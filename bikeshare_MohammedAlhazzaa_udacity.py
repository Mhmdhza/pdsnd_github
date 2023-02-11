
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None.
    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Initializing an empty city variable to store city choice from user
    
    city = ''
   
    while city not in CITY_DATA:
        print("welcome, choose the city: chicago, new york city or washinton? ")
        
        city = input().lower()

        if city not in CITY_DATA:
            print("please try again")

    print("You have chosen: " ,{city.title()} )

    #Creating a dictionary to store all the months including the 'all' option
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in months.keys():
        print("Please choose january to june or all")
        month = input().lower()

    print("You have chosen: " ,{month.title()})

    #Creating a list to store all the days including the 'all' option
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = ''
    while day not in days:
        print("Please choose any days of week or all")
        day = input().lower()

    print(f"\nYou have chosen: ", {day.title()})
    
    print('-'*78)
    #Returning the city, month and day selections
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        param1 (str): name of the city to analyze
        param2 (str): name of the month to filter by, or "all" to apply no month filter
        param3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    #Load data for city
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday

    #Filter by month if applicable
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day) + 1 
        df = df[df['weekday'] == day]

 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    start_time = time.time()

    #Uses mode method to find the most popular month
    month_common = df['month'].mode()[0]

    print(" most popular month is: ", month_common)

    #Uses mode method to find the most popular day
    day_common = df['weekday'].mode()[0]

    print("most popular day is: ", day_common)

    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    #Uses mode method to find the most popular hour
    hour_common = df['hour'].mode()[0]

    print("most popular hour is: ", hour_common)

   
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*78)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    start_time = time.time()

    #Uses mode method to find the most common start station
    common_s_station = df['Start Station'].mode()[0]

    print("most popular start station is: ", common_s_station)

    #Uses mode method to find the most common end station
    common_e_station = df['End Station'].mode()[0]

    print("most popular end station is: ", common_e_station)

    #Assigns the result to a new column 'Start To End'
  
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'])
    s_to_e = df['Start To End'].mode()[0]

    print("most frequant combination is: ", s_to_e)

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*78)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    start_time = time.time()

    #Uses sum method to calculate the total trip duration
    total_duration = df['Trip Duration'].sum()
    #Finds out the duration in minutes and seconds format
    minute, second = divmod(total_duration, 60)
    #Finds out the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, and {minute} minutes and {second} seconds. ")

    #Calculating the average trip duration using mean method
    average_duration = round(df['Trip Duration'].mean())
    #Finds the average duration in minutes and seconds format
    mins, sec = divmod(average_duration, 60)
  
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"The average trip duration is {hour} hours, {mins} minutes and {sec} seconds. ")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*78)

#Function to calculate user statistics
def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    start_time = time.time()

    #The total users are counted using value_counts method
   
    type_user = df['User Type'].value_counts()

    print(" the type user is: " , type_user)
 
    try:
        gender = df['Gender'].value_counts()
        print(" this gender is: " , gender)
    except:
        print("No gender for this file. sorry ")

    if city.lower() != "washington":
        earliest_date = int(df['Birth Year'].min())
        recent_date = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"earliest date is {earliest_date}, recent date is {recent_date}")
        print(f"and common year is {common_year}")
    else:
        print("No earliest and recent date with common year for this file")
   
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*78)

def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    print(df.head())
    start_point = 0
    while True:
        demo_data = input(" Do you want to see 5 row of this data? answer yes or no")
        if demo_data.lower() != 'yes':
            return
        start_point = start_point + 5
        print(df.iloc[start_point : start_point + 5])
      
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*78)

#Main function to call all the previous functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input(" do you want to restart this? yes or no? ")
        if restart.lower() != 'yes':
            break
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    print(df.head())
    start_point = 0
    while True:
        demo_data = input(" Do you want to see 5 row of this data? answer yes or no")
        if demo_data.lower() != 'yes':
            return
        start_point = start_point + 5
        print(df.iloc[start_point : start_point + 5])
      
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*78)

#Main function to call all the previous functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input(" do you want to restart this? yes or no? ")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # First I want to create lists for cities, months and days.  I'll use those to cycle over
    # with a WHILE loop for the user inputs
    cities = ['chicago', 'washington', 'new york city']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'All']
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'All']
    
    # Here I'm initializing the below to nulls    
    city = ""
    month = ""
    day = ""
       
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Use a while loop to handle invalid inputs in order to 
	# get user input for the city (chicago, new york city, washington). 
    while city.lower() not in cities:
        city = input(("Enter either Chicago, New York City, or Washington:\n"))
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while month.lower() not in months:
        month = input(("Enter a month (Please spell out the full month, or specify 'All' if you want all months):\n"))
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day.lower() not in days:
        day = input(("Enter a day (Please spell out the full day, or specify 'All' if you want all days):\n"))
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'octover', 'november', 'december',                         'all']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month.  Print out the most common month
    print("The most common month is: ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day is: ", df['day'].mode()[0], "\n")

    # TO DO: display the most common start hour
    # load data file into a dataframe
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    print("The most popular hour is: ", df['hour'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used START station is: ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used END station is: ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    # ?????  create a new column for 'Station Combination'
    # ?????  concatinate start and end stations, and then find the mode (below)
    # HERE, I need to create a station combination for start/end.
    print("The most frequent combination of start station and end station trip is: ", df['Station Combination'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: ", int(df['Trip Duration'].sum()), "seconds\n")

    # TO DO: display mean travel time
    print("The average travel time is: ", int(df['Trip Duration'].mean()), "seconds\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # practice problem 2
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    gender = df['gender'].value_counts()
    print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    # Use min, max, mode, after extracting year from year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

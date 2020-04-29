import time
import pandas as pd
import numpy as np
from statistics import mode
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\nEnter the name of city from chicago, new york city, washington to explore bike share data: ").lower()

    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input( "entered invalid city name, please enter a valid city name: ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("enter the name of month from January, February, March, April, May, June :").lower()

    while month.lower() not in ['january','february','march','april','may','june']:
        month = input('entered month is invalid, please enter a valid month').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("enter the day from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday :").lower()

    while day.lower() not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input('entered day is invalid, please enter a valid day').lower()

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
    df = pd.read_csv(CITY_DATA[city])
    # convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from start time to create new  columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #fillter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    #filter by day of week
    if day !=  'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]-1
    print('Most common month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = mode(df['hour'])
    print('Most common Start hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most popular start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most popular end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip_combination'] = df['Start Station'] + ' to ' + df['End Station']
    print('\nThe most common start and end station is : {}\n'.format(df['trip_combination'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('\nTotal Travel time : {}'.format(total))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('\nAverage travel time : {}'.format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_total = df['User Type'].value_counts()
    print('\nCount of user by types: \n{} '.format(user_types_total))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\n count of gender by categories: \n{} '.format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
        recent_Year = df['Birth Year'].max()
        print('\nRecent Year:', recent_Year)
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

	#asking user if they want to view the raw data
    raw_data_view = input('To view the raw data enter Yes or no:')
    raw_data_view.lower()

    if raw_data_view == 'yes':
        print(df.head(5))
        raw_data(df)
    else:
        print("Thanks for viewing the Raw data")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

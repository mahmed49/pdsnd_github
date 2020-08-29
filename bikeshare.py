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
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\nWhich city would you like to learn about? Chicago, New York City or Washington? Type the name below\n")
        city = city.lower()
        if city not in ('chicago','new york city','washington'):
            print("Sorry, please type in from the choices in the question below")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nWhich month would you like to see the data from? Please type in from the following choices: January, February, March, April, May, June or All\n")
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Sorry, please type in from the choices in the question below")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nWhich day would you like to see the data from? Please type in from the following choices: Sunday, Monday, Tuesday, Wednesday, Thursday, Firday, Saturday or All\n")
        day = day.lower()
        if day not in('sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'):
            print ("Sorry, please type in from the choices in the question below")
            continue
        else:
            break

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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day of week if applicable
    if day != 'all':

        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:",common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day is:",common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is:",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print("The most popular start station is: ",popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print("The most popular end station is: ",popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_stations'] = df['Start Station'] + " - " + df['End Station']
    popular_start_end = df['start_end_stations'].mode()[0]
    print("The most popular starting and ending stations are: ",popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time in hours is: ", round(total_travel_time/3600,2))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time in minutes is: ", round(mean_travel_time/60,2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Types of users:\n", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("\nBreakdown of gender:\n",gender)
    else:
        print("\nGender data is not available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print("\nThe earliest birth year is: ", int(earliest_birth))
        print("The most recent birth year is: ", int(recent_birth))
        print("The most common birth year is: ",int(common_birth))
    else:
        print("\nBirth year data is not available for this city")

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

        #displays 5 rows of raw data, if user iputs yes, will continue to display additional 5 rows of data until user inputs no
        index = 0
        while True:
            display_rawdata = input("Would you like to view 5 rows of raw data?\n")
            display_rawdata = display_rawdata.lower()
            if display_rawdata == 'yes':
                raw_data=df.iloc[index:index+5]
                print(raw_data)
                index+=5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

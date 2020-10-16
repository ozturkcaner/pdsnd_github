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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter name of the city to analyze (chicago, new york city, washington) : " ).lower()
    while city not in ('washington' ,'chicago' , 'new york city'):
      print('Opss! It wasnt right format !')
      city = input("Please enter name of the city to analyze (chicago, new york city, washington) : " ).lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter name of the month to filter by (january, february, ... , june), or ""all"" to apply no month filter : " ).lower()
    while month not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
        print('Opss! It wasnt right format !')
        month = input("Please enter name of the month to filter by (january, february, ... , june), or ""all"" to apply no month filter : " ).lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter name of the day of week to filter by (monday, tuesday, ... sunday), or ""all"" to apply no day filter: " ).lower()
    while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all'):
          print('Opss! It wasnt right format !')
          day = input("Please enter name of the day of week to filter by (monday, tuesday, ... sunday), or ""all"" to apply no day filter: " ).lower()
    
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month :', df['month'].mode()[0])
    
    # TO DO: display the most common day of week
    print('Most common day of week :', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('Most common start hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station :', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used start station :', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df1 = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print('Most commonly used start / end station : {} , Count : {}'.format( ' / '.join(df1.index[0]) , df1.iloc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time :' , pd.to_timedelta(df['Trip Duration'].sum() , unit = 's'))

    # TO DO: display mean travel time
    print('Mean Travel Time : ' , pd.to_timedelta(df['Trip Duration'].mean(), unit = 's'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    count_of_ut = df['User Type'].value_counts()
    print('The counts of user types :')
    print('{}'.format(count_of_ut))
    print('\n')
    # TO DO: Display counts of gender
    try:
       count_of_gd = df['Gender'].value_counts()
       print('The counts of gender :')
       print('{}'.format(count_of_gd))
       print('\n')
    except KeyError:
          print('No Gender Data for the filtered city')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth :', df['Birth Year'].min())
        print('The earliest year of birth :', df['Birth Year'].max())
        print('The most common year of birth :', df['Birth Year'].mode()[0])
    except KeyError:
        print('No Birth Year Data for the filtered city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def display_rdata(df):
    answer = input('Would you like to see raw data (Y/N) :').lower()
    counter = 0
    while answer not in ('y','n'):
        print('Opss! It wasnt right format !')
        answer = input('Would you like to see raw data (Y/N) :').lower()
    if answer == 'y':
        print(df.head())
            
    while answer == 'y':
        answer = input('Would you like to see more data (Y/N) :').lower()
        counter +=5
        if answer == 'y':
            print(df[counter:counter+5])
        else:
            break
  
    print('-'*40)
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

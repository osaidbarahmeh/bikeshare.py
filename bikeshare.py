import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print(" Let explore some US bikeshare data")

    while True:
        city = input(" let a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
             print("Oops!, Invalid city. Please try again.")

    months = ['january', 'february', 'march', 'april', 'may', 'junne', 'all']
    while True:
        month = input("Choose a month (january to june) or 'all': ").lower()
        if month in months:
             break
        else:
             print("Invalid month.should be try again.")

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day of week or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid day.please try again.")



    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = months.index(month) + 1
        df = df[df['month'] == month_num]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day.lower()]



    return df




def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = int(df['month'].mode()[0])
    print(f"Most common month (number): {most_common_month}")

    most_common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {most_common_day}")

    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = int(df['hour'].mode()[0])
    print(f"Most common start hour: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {start_station}")

    end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {end_station}")

    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print(f"Most frequent trip: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = np.sum(df['Trip Duration'])
    print(f"Total travel time: {total_travel_time} seconds")

    mean_travel_time = np.mean(df['Trip Duration'])
    print(f"Mean travel time: {mean_travel_time:.2f} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)





def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("User Types:")
    print(user_types)

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nGender Counts:")
        print(gender_counts)
    else:
        print("\nNo gender data available for this city.")

    if 'Birth Year' in df.columns:
        earliest = int(np.min(df['Birth Year']))
        most_recent = int(np.max(df['Birth Year']))
        most_common = int(df['Birth Year'].mode()[0])

        print("\nBirth Year Stats:")
        print(f"Earliest year of birth: {earliest}")
        print(f"Most recent year of birth: {most_recent}")
        print(f"Most common year of birth: {most_common}")
    else:
        print("\nNo birth year data available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

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

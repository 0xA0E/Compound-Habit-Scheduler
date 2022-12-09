#!/bin/python3

from datetime import date, timedelta
    
def get_date(jump):
    considered_day = (date.today() + timedelta(days=jump)).strftime("%a %d %b")
    return considered_day
    
def generate_schedule(start, end, increase):
    current_time_spent = start
    prev_time_spent = current_time_spent
    current_day = 1
    while current_time_spent < end:
        hours, minutes = (int(x) for x in divmod(current_time_spent, 60))
        added = int(current_time_spent - prev_time_spent)
        date = get_date(current_day)
        day = [f'(Day {current_day}) ', f'{date}: ', f'{hours}H {minutes}MIN', f'Added {added}MIN']
        prev_time_spent = current_time_spent
        current_time_spent *= (1 + increase)
        current_day += 1
        yield day

def print_day(day):
        print("{: <10}  {: <15}  {: <15}  {: <15}".format(*day))

if __name__ == '__main__':
    current_time_spent = int(input("Enter the amount of time you currently spend on this habit (or want to start spending) (in min): "))
    compound_percent = float(input("Enter a daily interest for your habits (between 0-1): "))
    goal = int(input("What's your end goal for this habit (in min): "))
    schedule = generate_schedule(current_time_spent, goal, compound_percent)
    print('\n\n\n')
    for day in schedule:
        print_day(day)
        if(day[1][0:3] == 'Sun'):
            break
    day_counter = 0
    for day in schedule:
        if day_counter % 7 == 0:
            print(f'WEEK {int(day_counter/7)}')
        print_day(day)
        if day_counter % 7 == 6:
            print()
        day_counter += 1

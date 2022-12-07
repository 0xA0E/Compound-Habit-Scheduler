#!/bin/python3

from datetime import date, timedelta
    
def get_date(jump):
    considered_day = (date.today() + timedelta(days=jump)).strftime("%a %d %b")
    return considered_day
    
def make_Schedule(start, end, increase):
    days_list = []
    current = start
    prev = current
    current_day = 1
    while current < end:
        hours, minutes = divmod(current, 60) 
        hours = int(hours)
        minutes = int(minutes)
        jump = int(current- prev)
        date = get_date(current_day)
        days_list += [[f'Day {current_day} ', f'{date}: ', f'{hours}H {minutes}MIN', f'Added {jump}MIN']]
        prev = current
        current += current*increase
        current_day += 1
    return days_list

def print_Schedule(schedule):
    for i in range(len(schedule)):
        if(i % 7 == 0):
            week = int(i/7) + 1;
            print(f'WEEK {week}')
        print("{: <10} {: <10} {: <10} {: <10}".format(*schedule[i]))
        if(i % 7 == 6):
            print()

def main():
    current_time_spent = int(input("Enter the amount of time you currently spend on this habit (or want to start spending) (in min): "))
    compound_percent = float(input("Enter a daily interest for your habits: "))
    goal = int(input("What's your end goal for this habit (in min): "))
    schedule = make_Schedule(current_time_spent, goal, compound_percent)
    print_Schedule(schedule)
    
main()

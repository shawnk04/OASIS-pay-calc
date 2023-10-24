"""
OASIS Workstudy Pay Allotment Calculator
Terminal Version

by Shawn Khandia, for Spring '23 semester
"""

import re, time, sys, os, math

if __name__ == "__main__":
    # Clear terminal if needed
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Pay rate: $13.50/hr
    rate = 13.50
    
    print("Welcome to the UNC OASIS Workstudy pay allotment calculator!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nThis calculator prints our relevant information about your pay and current allotment left in a semester, such as total pay so far, how much allotment you have left, and more!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    print("To get started, please type in the following: \n - Your original allotment amount (can be found on financial aid letter in ConnectCarolina)\n - Total number of hours you have worked so far this semester (see instructions below)\n - The number of weeks left in the semester (minus any breaks/weeks you WON'T be working for MOST of the week, such as Thanksgiving break)\n\nTo find the total number of hours you've been paid for, go to ConnectCarolina > Self Service > My Pay and Taxes > View Paycheck. Then view the number of hours from your past paychecks this semester and add them all up.\nNext, to get the number of hours you haven't been paid for yet, go to TIM (unctim.unc.edu) and look at the Previous Pay Period.\nAdd your PAID hours worked AND your YET-TO-BE-PAID hours worked to get the total current hours to date.\n")
    # Input loop and ensure inputs are valid numbers
    while True:
        allotment_raw = input("Original allotment amount: ")
        HTD_raw = input("Current hours to date: ")
        num_weeks_raw = input("Number of weeks left in semester: ")
        print(" ")
        if re.match("^ *\d+[.+\d+]* *$", allotment_raw) and re.match("^ *\d+[.+\d+]* *$", HTD_raw) and re.match("^ *\d+[.+\d+]* *$", num_weeks_raw):
            allotment = float(allotment_raw)
            HTD = float(HTD_raw)
            num_weeks = int(num_weeks_raw)
            print("Values accepted!")
            break
        else:
            print("Please type in numeric (float or integer) values only!")
    
    # Filler text to make calculator seem cooler :)
    os.system('cls' if os.name == 'nt' else 'clear')
    gen = "\nGenerating report..."
    for char in gen:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nNOTE: The following info is BEFORE TAXES, so the actual pay you've received and will receive may differ.\n")
        
    # Calculations and printing values
    total_pay = round(HTD*rate, 2)
    total_allot = round(allotment-(HTD*rate), 2)
    total_hours = math.floor(((allotment-(HTD*rate))/rate) * 10)/10.0
    rec_weekly_hours = math.floor((total_hours/num_weeks) * 10)/10.0
    print(f"Total pay so far: ${total_pay}")
    print(f"Total allotment left: ${total_allot}")
    print(f"Total # of hours left: {total_hours}")
    print(f"Recommended # of hours per week to get most of allotment: {rec_weekly_hours}")

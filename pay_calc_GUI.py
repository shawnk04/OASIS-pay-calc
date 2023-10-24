"""
OASIS Workstudy Pay Allotment Calculator
GUI Version using Tkinter

by Shawn Khandia, for Spring '23 semester
"""

import re, math
import tkinter as tk

if __name__ == "__main__":
    # Configure window
    window = tk.Tk()
    window.title("OASIS Workstudy Allotment Calculator")
    window.geometry("700x700")


    # Add greeting blurb
    greeting = tk.Label(text = "\nWelcome to the UNC OASIS Workstudy pay allotment calculator!\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nThis calculator prints our relevant information about your pay and current allotment left in a semester, such as total pay so far, how much allotment you have left, and more!\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", wraplength=700, font="helvetica 14", justify="center")
    greeting.pack()


    # Add instructions blurb
    instructions = tk.Label(text = "To get started, please type in the following: \n - Your original allotment amount (can be found on financial aid letter in ConnectCarolina)\n - Total number of hours you have worked so far this semester (see instructions below)\n - The number of weeks left in the semester (minus any breaks/weeks you WON'T be working for MOST of the week, such as Thanksgiving break)\n\n\nTo find the total number of hours you've been paid for, go to ConnectCarolina > Self Service > My Pay and Taxes > View Paycheck. Then view the number of hours from your past paychecks this semester and add them all up.\nNext, to get the number of hours you haven't been paid for yet, go to TIM (unctim.unc.edu) and look at the Previous Pay Period.\nAdd your PAID hours worked AND your YET-TO-BE-PAID hours worked to get the total current hours worked this semester.\n\n", wraplength=660, font="helvetica 14", justify="left")
    instructions.pack()


    # Add entries for user-inputted data
    a = tk.Label(window, text = "Total allotment for the semester:").pack()
    a1 = tk.Entry(window)
    a1.pack()

    b = tk.Label(window, text = "\nTotal number of hours worked so far this semester:").pack()
    b1 = tk.Entry(window)
    b1.pack()

    c = tk.Label(window, text = "\nNumber of weeks left in the semester:").pack()
    c1 = tk.Entry(window)
    c1.pack()


    # Function to calculate variables based on inputs
    def calculate():
        results_window = tk.Toplevel(window)
        results_window.geometry("400x400")
        results_window.title("Results")

        # Retrieving values 
        rate = 13.50
        allotment_raw = a1.get()
        HTD_raw = b1.get()
        num_weeks_raw = c1.get()
        if re.match("^ *\d+[.+\d+]* *$", allotment_raw) and re.match("^ *\d+[.+\d+]* *$", HTD_raw) and re.match("^ *\d+[.+\d+]* *$", num_weeks_raw):
            allotment = float(allotment_raw)
            HTD = float(HTD_raw)
            num_weeks = int(num_weeks_raw)

            # Calculations and displaying values
            total_pay = round(HTD*rate, 2)
            total_allot = round(allotment-(HTD*rate), 2)
            total_hours = math.floor(((allotment-(HTD*rate))/rate) * 10)/10.0
            rec_weekly_hours = math.floor((total_hours/num_weeks) * 10)/10.0
            tk.Label(results_window, text = "\nResults\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n").pack()
            tk.Label(results_window, text = f"Total pay so far: ${total_pay}", justify = "left", wraplength = 360).pack()
            tk.Label(results_window, text = f"Total allotment left: ${total_allot}", justify = "left", wraplength = 360).pack()
            tk.Label(results_window, text = f"Total # of hours left: {total_hours}", justify = "left", wraplength = 360).pack()
            tk.Label(results_window, text = f"Recommended # of hours per week to get most of allotment: {rec_weekly_hours}", justify = "left", wraplength = 360).pack()
        else:
            tk.Label(results_window, text= "Uh oh! We ran into an issue...\n\nPlease type in numeric (float or integer) values only! Exclude any dollar signs", pady=160, justify = "center", wraplength = 395).pack()

    # Add button to submit and calculate 
    button = tk.Button(window, text = "Submit", command = calculate).pack()


    window.mainloop()

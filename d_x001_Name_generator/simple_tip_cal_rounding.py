# Day 2 Tip calculator and
# formatting up to double digit rounding
total_bill = int(input("What is your total bill? "))
tip = int(input("What percent you wanna tip? "))
total_people = int(input("How many people you wanna split the bill? "))

ind_bill = (total_bill + total_bill * tip / 100) / total_people
ind_bill = "{:.2f}".format(ind_bill)

print("Each person should pay: " + ind_bill)

# pcost.py
#
# Exercise 1.27

with open('portfolio.csv','rt') as file:
    headers = next(file)
    total_cost = 0
    for line in file:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])
        
    print('Total cost to purchase the portfolio:', total_cost)

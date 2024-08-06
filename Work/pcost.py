# pcost.py
#
# Exercise 1.27

with open('portfolio.csv','rt') as file:
    headers = next(file)
    total_cost = 0.0
    for line in file:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])
        
    print('Total cost to purchase the portfolio:', total_cost)

# Exercise 1.31

def portfolio_cost(filename):
    '''This function takes a filename as input, 
    reads the portfolio data in that file, 
    and returns the total cost of the portfolio as a float.'''
    with open(filename,'rt') as file:
        headers = next(file)
        total_cost = 0.0
        for line in file:
            row = line.split(',')
            try:
                total_cost = total_cost + int(row[1]) * float(row[2])
            except ValueError:
                print("Oopsie-woopsie, couldn't parsie!", row)
        return(total_cost)

import os
os.chdir('D:\\Dropbox\\Postdoc')
portfolio_cost('py/portfolio.csv')
portfolio_cost('py/missing.csv')

# After rewriting the function in 1.30 above by adding try-except,
# we can now see where something wrong has happened, but continue 
# the program execution after skipping each execption
# NEAT!

# Exercise 1.32

def portfolio_cost_import_csv(filename):
    '''This function takes a filename as input, 
    reads the portfolio data in that file, 
    and returns the total cost of the portfolio as a float.'''
    import csv
    with open(filename) as file:
        rows = csv.reader(file)  # make each row into a list?
        headers = next(rows)
        print('Headers:',headers)
        total_cost = 0.0
        for row in rows:
            try:
                total_cost = total_cost + int(row[1]) * float(row[2])
            except ValueError:
                print("Oopsie-woopsie, couldn't parsie!", row)
        return(total_cost)
    
costs = portfolio_cost_import_csv('py/portfolio.csv')
print('Total cost to purchase the portfolio:', costs)

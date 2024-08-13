# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:24:23 2024

@author: 90036ysh
"""

#############################
#### report.py continued ####
#############################

####
# Exercise 2.18
####

import csv

def read_portfolio(filename):
    '''This function takes a filename as input, 
    reads the portfolio data in that file, 
    and returns the total cost of the portfolio as a float.'''
    portfolio = []
    with open(filename,"rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers,row))
            try:
                holding = {'name':record['name'],
                           'shares':int(record['shares']),
                           'price':float(record['price'])
                }
                portfolio.append(holding)
            except ValueError:
                print("Oopsie-woopsie, couldn't parsie!",row)
    return portfolio
    
def read_prices(filename):
    '''Reads a set of prices into a dictionary where the keys are
    the stock names and the values are the prices'''
    prices = {}
    with open(filename,'r') as file:
        rows = csv.reader(file)
        for row_n,row in enumerate(rows,start=1):
            try:
                # row[0] or row[1] in row
                prices[row[0]] = float(row[1])
                print(row)
            except IndexError:
                print('Oopsie-woopsie, emptie-wemptie in row number',row_n,
                      '... Imma excludo')
    return prices

def make_report(portfolio,prices):
    '''Takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples containing the rows of the table in 2.9'''
    report = []
    header = ('Name','Shares','Prirce','Change')
    for stock in portfolio:
        summary = (
            stock['name'],
            stock['shares'],
            prices[stock['name']],
            prices[stock['name']] - stock['price']
            )
        report.append(summary)
    print('%10s %10s %10s %10s' % header)
    print(('-' * 10 + ' ') * len(header))
    for name,shares,price,change in report:
        print(f'{name:>10s} {shares:>10d} {"$"+str(price):>10s} {change:>10.2f}')
    return report

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices)
report

from collections import Counter
holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']
    # holdings[s['name']] = s['shares'] + holdings[s['name']]
    
holdings
holdings['IBM']
holdings['MSFT']

holdings.most_common(3)

portfolio2 = read_portfolio('Data/portfolio2.csv')
holdings2 = Counter()
for s in portfolio2:
    holdings2[s['name']] += s['shares']

holdings2

holdings
holdings2
combined = holdings + holdings2
combined

####
# Exercise 2.19
####

nums = [1,2,3,4]
squares = [x**2 for x in nums]
twice = [2 * x for x in nums if x > 2]

####
# Exercise 2.20
####

portfolio = read_portfolio('Data/portfolio.csv')
cost = sum([ s['shares'] * s['price'] for s in portfolio ])
cost

value = sum([ s['shares'] * prices[s['name']] for s in portfolio])
value

# these are "map-reduction" operations. 
# The list comprehension is mapping an operation across the list.

[ s['shares'] * s['price'] for s in portfolio ]
sum(_)

####
# Exercise 2.21
####

more100 = [s for s in portfolio if s['shares'] > 100]
more100
msftibm = [s for s in portfolio if s['name'] in {'MSFT','IBM'}] 
msftibm
cost10k = [s for s in portfolio if s['shares'] * s['price'] > 10000]
cost10k

####
# Exercise 2.22
####

name_shares = [ (s['name'],s['shares']) for s in portfolio]
name_shares

# set comprehension takes { } instead of [ ]
names = { s['name'] for s in portfolio}
names

# dictionary comprehension takes { key:value }
holdings = { name:0 for name in names}
holdings
for s in portfolio:
    holdings[s['name']] += s['shares']
holdings

portfolio_prices = { name:prices[name] for name in names }
portfolio_prices

####
# Exercise 2.23
####

import csv
f = open('Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
headers

select = ['name','shares','price']
indices = [ headers.index(colname) for colname in select]
indices
row = next(rows)
record = { colname:row[index] for colname,index in zip(select,indices) }
record

portfolio = [ { colname:row[index] for colname,index in zip(select, indices) } for row in rows ]
portfolio
f.close()

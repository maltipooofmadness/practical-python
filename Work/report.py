# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:00:13 2024

@author: User
"""

#
# Exercise 2.4
#

def read_portfolio(filename):
    '''This function takes a filename as input, 
    reads the portfolio data in that file, 
    and returns the total cost of the portfolio as a float.'''
    portfolio = []
    with open(filename,'rt') as file:
        headers = next(file)
        for line in file:
            row = line.split(',')
            try:
                holding = (row[0],int(row[1]),float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print("Oopsie-woopsie, couldn't parsie!", row)
        return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
total = 0.0
for s in portfolio:
    total += s[1] * s[2]

# OR

for name,shares,price in portfolio:
    total += shares * price
    
print(total)

#
# Exercise 2.5
#

def read_portfolio(filename):
    '''This function takes a filename as input, 
    reads the portfolio data in that file, 
    and returns the total cost of the portfolio as a float.'''
    portfolio = []
    with open(filename,"rt") as file:
        next(file) # skip header without recording it
        for line in file:
            row = line.split(',')
            try:
                holding = {'name':row[0][1:-1], # [1:-1] to get rid of extra ""
                           'shares':int(row[1]),
                           'price':float(row[2])
                    }
                portfolio.append(holding)
            except ValueError:
                print("Oopsie-woopsie, couldn't parsie!",row)
        return portfolio
    
portfolio = read_portfolio('Data/portfolio.csv')
portfolio
portfolio[0]
portfolio[1]
portfolio[1]['shares']
total = 0.0
for s in portfolio:
    total += s['shares'] * s['price']
print(total)

from pprint import pprint
pprint(portfolio)

#
# Exercise 2.6
#

prices = {}
prices['IBM'] = 92.45
prices['MSFT'] = 45.12
prices
prices['IBM']
prices['AAPL']
'AAPL' in prices

import csv
def read_prices(filename):
    '''Reads a set of prices into a dictionary where the keys are
    the stock names and the values are the prices'''
    i = 0
    prices = {}
    with open(filename,'r') as file:
        rows = csv.reader(file)
        for row in rows:
            i += 1
            try:
                # row[0] or row[1] in row
                prices[row[0]] = float(row[1])
                print(row)
            except IndexError:
                print('Oopsie-woopsie, emptie-wemptie in row number',i,
                      '... Imma excludo')
        return prices
    
prices = read_prices('Data/prices.csv')
prices['IBM']
prices['MSFT']

#
# Exercise 2.7
#

import csv

def read_portfolio(filename):
    '''This function takes a filename as input, 
    reads the portfolio data in that file, 
    and returns the total cost of the portfolio as a float.'''
    portfolio = []
    with open(filename,"rt") as file:
        rows = csv.reader(file)
        next(rows) # skip header without recording it
        for row in rows:
            try:
                holding = {'name':row[0],
                           'shares':int(row[1]),
                           'price':float(row[2])
                    }
                portfolio.append(holding)
            except ValueError:
                print("Oopsie-woopsie, couldn't parsie!",row)
        return portfolio
    
def read_prices(filename):
    '''Reads a set of prices into a dictionary where the keys are
    the stock names and the values are the prices'''
    i = 0
    prices = {}
    with open(filename,'r') as file:
        rows = csv.reader(file)
        for row in rows:
            i += 1
            try:
                # row[0] or row[1] in row
                prices[row[0]] = float(row[1])
                print(row)
            except IndexError:
                print('Oopsie-woopsie, emptie-wemptie in row number',i,
                      '... Imma excludo')
        return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
port_initial = 0.0
current_port = 0.0
gainloss = []
for stock in portfolio:
    port_initial += stock['shares'] * stock['price']
    current_port += stock['shares'] * prices[stock['name']]
    gainloss.append({'name':
                     stock['name'],
                     'gain/loss':
                     stock['shares'] * prices[stock['name']] - 
                     stock['shares'] * stock['price']
                     }
                    )
    print(stock['name'], '=', round(gainloss[portfolio.index(stock)]['gain/loss'],2))
    #print(portfolio.index(stock))

net = current_port - port_initial
print('Portfolio net:',round(net,2),'(',current_port,'-',port_initial,')')


#
# Exercise 2.9
#

def make_report(list_of_stocks,dic_of_prices):
    '''Takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples containing the rows of the table in 2.9'''
    report = []
    for stock in list_of_stocks:
        # stock = (
        #     list_of_stocks[list_of_stocks.index(stock)]['name'],
        #     int(list_of_stocks[list_of_stocks.index(stock)]['shares']),
        #     float(list_of_stocks[list_of_stocks.index(stock)]['price']),
        #     float(dic_of_prices[stock['name']] - float(list_of_stocks[list_of_stocks.index(stock)]['price']))
        #     )
        #print(stock)
        stock = (stock['name'],
                 stock['shares'],
                 dic_of_prices[stock['name']],
                 dic_of_prices[stock['name']] - stock['price']
            )
        report.append(stock)
    return report
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices)
report
for r in report:
    print(r)

#
# Exercise 2.10
#

for r in report:
    print('%10s' '%10d' '%10.2f' '%10.2f' % r)
    
for name,shares,price,change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    
def make_report(list_of_stocks,dic_of_prices):
    '''Takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples containing the rows of the table in 2.9'''
    report = []
    for stock in list_of_stocks:
        # stock = (
        #     list_of_stocks[list_of_stocks.index(stock)]['name'],
        #     int(list_of_stocks[list_of_stocks.index(stock)]['shares']),
        #     float(list_of_stocks[list_of_stocks.index(stock)]['price']),
        #     float(dic_of_prices[stock['name']] - float(list_of_stocks[list_of_stocks.index(stock)]['price']))
        #     )
        #print(stock)
        stock = (
            stock['name'],
            stock['shares'],
            dic_of_prices[stock['name']],
            dic_of_prices[stock['name']] - stock['price']
            )
        report.append(stock)
    for name,shares,price,change in report:
        print(f'{name:<10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices)

#
# Exercise 2.11
#

def make_report(portfolio,prices):
    '''Takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples containing the rows of the table in 2.9'''
    report = []
    header = ('Name','Shares','Prirce','Change')
    for stock in portfolio:
        # stock = (
        #     portfolio[portfolio.index(stock)]['name'],
        #     int(portfolio[portfolio.index(stock)]['shares']),
        #     float(portfolio[portfolio.index(stock)]['price']),
        #     float(prices[stock['name']] - float(portfolio[portfolio.index(stock)]['price']))
        #     )
        summary = (
            stock['name'],
            stock['shares'],
            prices[stock['name']],
            prices[stock['name']] - stock['price']
            )
        report.append(summary)
    print('%10s %10s %10s %10s' % header)
    #print(f'{"-":->10} {"-":->10} {"-":->10} {"-":->10}')
    print(('-' * 10 + ' ') * len(header))
    for name,shares,price,change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices)

#
# Exercise 2.12
#

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

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices)

####
# Exercise 2.16
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

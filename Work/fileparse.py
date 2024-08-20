# fileparse.py
#
# Exercise 3.3

####
# Exercise 3.11
####

import csv
import os
os.chdir('C:\\Users\\90036ysh\\Dropbox\\Postdoc\\py')

def parse_csv(filename,
              select=None,
              types=None,
              hasheaders=True,
              delimiter=',',
              silence_errors=False) -> list:
    '''
    Parse a csv file into a list of records (dictionaries)

    '''
    if select and not hasheaders:
        raise RuntimeError('select argument requires column headers')
        
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        
        # Determining whether the file has headers or not
        if hasheaders:
        # Read the file headers
            headers = next(rows)
        else:
            headers = None
        
        # If specific columns have been selected, make indices for filtering
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
            
        records = []
        for row_n,row in enumerate(rows,start=1):
            if not row: # Skip rows with no data
                continue
            
            # If specific columns were selected, pick them out
            if select:
                row = [ row[index] for index in indices ]
             
            # Convert select columns if specific types were selected
            if types:
                try:
                    row = [ funct(val) for funct,val in zip(types,row) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {row_n}: Couldn\'t convert {row}')
                        print(f'Row {row_n}: Reason: {e}')
                    continue
            
            if headers:
            # Make dictionaries
                record = dict(zip(headers,row))
            else:
            # Make tuples
                record = tuple(row)
            
            records.append(record)
    
    return records


# portfolio = parse_csv('Data/missing.csv', types=[str,int,float])

# portfolio

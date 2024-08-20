####
# Exercises 3.11 .. 3.17
####


import csv
import os
#os.chdir('C:\\Users\\90036ysh\\Dropbox\\Postdoc\\py')
os.chdir('D:\\Dropbox\\Postdoc\\py')


def parse_csv(lines,
              select=None,
              types=None,
              hasheaders=True,
              delimiter=',',
              silence_errors=False) -> list:
    '''
    Parse a csv file into a list of records (dictionaries)

    '''
    if type(lines) == str:
        raise RuntimeError('Please, open file first and then call .parse_csv')
    
    if select and not hasheaders:
        raise RuntimeError('select argument requires column headers')
        
    
    rows = csv.reader(lines, delimiter=delimiter)
   
        
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

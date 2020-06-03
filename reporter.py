# reporter.py


import csv

print("SALES REPORT (OCTOBER 2017)")
sum = 0


csv_filepath = "sales-201710.csv"
with open(csv_filepath, "r") as csv_file: 
    reader = csv.DictReader(csv_file)
    for row in reader:
        sum = float(row["sales price"]) + sum




def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("TOTAL SALES:", to_usd(sum))

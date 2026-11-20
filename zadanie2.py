import csv

def parse_csv_line(line):
    return next(csv.reader([line], strict=True))
print(parse_csv_line("a,b,c"))       
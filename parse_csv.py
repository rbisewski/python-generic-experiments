import csv

def read_file(file):
    lines = []
    for line in list(open(file,"r")):
        lines.append(line)

    return lines

def main():
    lines = read_file("data.csv")
    for l in lines:
        reader = csv.reader([l], skipinitialspace=True)
        for r in reader:
            print(r)

#-----
main()
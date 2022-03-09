class etc:
    def noop():
        pass

    def ranger():
        for n in range(1,10,1):
            print(n)

    def read_file(file):
        for line in list(open(file,"r")):
            print(line)

def main():
    # do nothing
    etc.noop()

    # for-loop thru a range
    etc.ranger()

    # reads and prints out the README.md
    etc.read_file("./README.md")

#----------------------------
main()

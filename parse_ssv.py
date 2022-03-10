import csv

def read_file(file):
    lines = []
    for line in list(open(file,"r")):
        lines.append(line)

    return lines

def get_counts(file, column, filtercol, filterby):
    col = 0
    if column == "Stages":
        col = 0
    elif column == "Events":
        col = 1
    elif column == "Errors":
        col = 2

    # lines look like:
    #
    # masters.cloud-snapshot-kops.local DescribeAutoScalingGroups null 2017-06-16T23:54:51Z
    #
    # ...which correspond to the following:
    #
    # Cluster, Event, Error, Time
    #
    lines = read_file(file)

    dictionary = {}
    for l in lines:
        pieces = l.split(" ")

        if filtercol == "":
            pass
        elif filtercol == "Stages":
            stage = pieces[0]
            if stage != filterby:
                continue
        elif filtercol == "Events":
            event = pieces[1]
            if event != filterby:
                continue
        elif filtercol == "Errors":
            error = pieces[2]
            if error != filterby:
                continue

        count = dictionary.get(pieces[col], 0)
        dictionary[pieces[col]] = count + 1

    return dictionary

# GET request
#
# /counts?day=20170617&column=Stages&filtercol=Events&filterby=DescribeRouteTables
#
# params
#   => day (where like 20170617)
#   => column (Stages, Errors, Events)
#   => filtercol (Stages, Errors, Events)
#   => filterby (exact stage, exact error, exact event)
#
def get(day, column, filtercol, filterby):
    filename = "./aws_dataset/data/df" + day + ".ssv"
    dictionary = get_counts(filename, column, filtercol, filterby)
    return dictionary

def main():
    dictionary = get("20170617", "Events", "Stages", "masters.ozzy-inte2-kops.domino.tech")
    print(dictionary)

#-----
main()
#!/usr/bin/env python
import csv


# All Precincts
# File clean
# Strip Headers per Page

def readf(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        lines = list(csvreader)
        return lines

    return None


def write(filename, header, records):
    with open(filename, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               lineterminator='\n', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(header)
        for r in records or []:
            csvwriter.writerow(r)

Parties = {
    "DANIEL WASSMER": "LIB",
    "HEATHER HEIDELBAUGH": "REP",
    "JOSH SHAPIRO": "DEM",
    "RICHARD L WEISS": "GRN",
    "JENNIFER MOORE": "LIB",
    "NINA AHMAD": "DEM",
    "OLIVIA FAISON": "GRN",
    "TIMOTHY DEFOOR": "REP",
    "FRED KELLER": "DEM",
    "LEE GRIFFIN": "REP",
    "PERRY STAMBAUGH": "REP",
    "GEORGE SCOTT": "DEM",
    "JOHN DISANTO": "REP",
    "BIDEN/HARRIS": "DEM",
    "JORGENSEN/COHEN": "LIB",
    "TRUMP/PENCE": "REP",
    "JOE SOLOSKI": "LIB",
    "JOE TORSELLA": "DEM",
    "STACY L GARRITY": "REP",
    "TIMOTHY RUNKLE": "GRN",
    "KAREN BOBACK": "DEM",
    "WI": "Write-Ins",
    "SC": "Scattered"
}

def parse(records):
    newrecords = []
    header = None
    h1 = None
    # precinct, office, district, party, candidate,
    # walk the file
    for r in  records or []:
        if r[0].startswith('Precinct'):
            header = r
            print("New", r)
            h1 = header[4:]

        else:
            v1 = r[4:]
            cancnt = list(zip(h1, v1))
            cancnt = [r for r in cancnt if r[0]]
            print(cancnt)
            for l in cancnt:
                party = Parties.get(l[0], '')
                newrecords.append(['Wyoming', r[0], r[1], r[2], party, l[0], l[1]])



    header = ['county', 'precinct', 'office', 'district', 'party',
              'candidate', 'votes']
    write('20201103__pa__general__whyoming__precinct.csv', header, newrecords)




def main():
    records = readf("imported-20201103__pa__general__wyoming.csv")
    for r in records or []:
        print(r)
    parse(records)


if __name__ == "__main__":
    main()

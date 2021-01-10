#!/usr/bin/env python
import csv

# Choice


# 12TH CONGRESSIONAL WRITE-IN
# 15TH SENATORIAL WRITE-IN
# 86TH LEGISLATIVE WRITE-IN
# ATTORNEY GENERAL WRITE-IN
# AUDITOR GENERAL WRITE-IN
# STATE TREASURER WRITE-IN
# PRESIDENT WRITE-IN
# Attorney General (Vote for 1)
# Auditor General (Vote for 1)
# President (Vote for 1)
# State Treasurer (Vote for 1)
# Congress 12 (Vote for 1)
# PA Rep 86 (Vote for 1)
# PA Senator 15 (Vote for 1)

# 'Congress 12', 'PA Rep 86', 'PA Senator 15'

# Precinct BLAIN BOROUGH
# Precinct BLOOMFIELD BOROUGH
# Precinct BUFFALO TOWNSHIP
# Precinct CARROLL TOWNSHIP
# Precinct CENTRE TOWNSHIP
# Precinct DUNCANNON BOROUGH
# Precinct GREENWOOD TOWNSHIP
# Precinct HOWE TOWNSHIP
# Precinct JACKSON TOWNSHIP
# Precinct JUNIATA TOWNSHIP
# Precinct LANDISBURG BOROUGH
# Precinct LIVERPOOL BOROUGH
# Precinct LIVERPOOL TOWNSHIP
# Precinct MADISON TOWNSHIP
# Precinct MARYSVILLE BOROUGH
# Precinct MILLER TOWNSHIP
# Precinct MILLERSTOWN BOROUGH
# Precinct NEWPORT BOROUGH
# Precinct OLIVER TOWNSHIP
# Precinct PENN TOWNSHIP
# Precinct RYE TOWNSHIP
# Precinct SANDY HILL DISTRICT
# Precinct SAVILLE TOWNSHIP
# Precinct SPRING TOWNSHIP
# Precinct TOBOYNE TOWNSHIP 1ST
# Precinct TOBOYNE TOWNSHIP 2ND
# Precinct TUSCARORA TOWNSHIP
# Precinct TYRONE TOWNSHIP
# Precinct WATTS TOWNSHIP
# Precinct WHEATFIELD TOWNSHIP

# All Precincts
# Total

class ParsePA:

    def __init__(self):
        self.fields = []
        self.Precincts = {}
        self.Races = {}
        self.Header = None

    @staticmethod
    def readf(filename):
        with open(filename) as csvfile:
            csvreader = csv.reader(csvfile)
            lines = list(csvreader)
            # lines = [l for l in lines or [] if not l[0] == 'Choice']
            return lines

        return None



def readf(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        lines = list(csvreader)
        # lines = [l for l in lines or [] if not l[0] == 'Choice']
        return lines

    return None

# File clean
# Strip Headers per Page
#   Choice,Votes,Vote %,ED,MI,PR
#   ['Choice', 'Votes', 'Vote %', 'ED', 'MI', 'PR']
#   ['All Precincts', '', '', '', '', '']

def write(fname, records):
    header = ['county', 'precinct', 'office', 'district', 'party',
              'candidate', 'votes', 'election_day', 'mi', 'pr']
    with open(fname, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(header)
        for r in records or []:
            csvwriter.writerow(r)

def parse(records):
    stateraces = ['Congress 12', 'PA Rep 86', 'PA Senator 15']

    newrecords = []
    curprecinct = None
    currace = None
    district = None
    party = None

    # walk the file
    for r in  records or []:
        if r[0].startswith('Precinct'):
            curprecinct = r[0].replace('Precinct ', '')
            currace = None
        elif r[1:] == ['', '', '', '', '']:
            currace = r[0].split('(')[0].rstrip()
            if currace in stateraces:
                lf = currace.split(' ')
                district = lf.pop(-1)
                currace = ' '.join(lf)
            else:
                district = ''
        elif r[0].startswith('Total'):
            # print(curprecinct, currace, district, r)
            continue
        else:
            r.pop(2)
            if 'WRITE-IN' in r[0]:
                r[0] = "Write-Ins"
            newr = ['Perry', curprecinct, currace, district, party] + r
            newrecords.append(newr)

    write('20201103__pa__general__perry__precinct.csv', newrecords)


def main():
    records = readf("PerryPA.csv")
    header = records.pop(0)
    # print("***",header)
    records = [r for r in records or [] if r != header]

    tot = next((c for c, v in enumerate(records) if v[0] == 'All Precincts'), 0)
    precinct_per = records[:tot]
    if not precinct_per:
        print ("error in file")
    else:
        parse(precinct_per)


if __name__ == "__main__":
    main()

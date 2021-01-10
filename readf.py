#!/usr/bin/env python
import csv

# 12TH CONGRESSIONAL WRITE-IN
# 15TH SENATORIAL WRITE-IN
# 86TH LEGISLATIVE WRITE-IN
# ATTORNEY GENERAL WRITE-IN
# AUDITOR GENERAL WRITE-IN
# All Precincts
# Attorney General (Vote for 1)
# Auditor General (Vote for 1)
# Choice
# Congress 12 (Vote for 1)
# PA Rep 86 (Vote for 1)
# PA Senator 15 (Vote for 1)
# PRESIDENT WRITE-IN
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
# President (Vote for 1)
# STATE TREASURER WRITE-IN
# State Treasurer (Vote for 1)
# Total

class ParsePA:

    def __init__(self):
        self.fields = []
        self.Precincts = {}
        self.Races = {}


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
# ['Choice', 'Votes', 'Vote %', 'ED', 'MI', 'PR']

def
def main():
    records = readf("PerryPA.csv")
    header = records.pop(0)
    # print("***",header)
    records = [r for r in records or [] if r != header]
    for r in records or []:
        print(r)

if __name__ == "__main__":
    main()

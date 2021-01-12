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


# File clean
# Strip Headers per Page
#   Choice,Votes,Vote %,ED,MI,PR
#   ['Choice', 'Votes', 'Vote %', 'ED', 'MI', 'PR']
#   ['All Precincts', '', '', '', '', '']

def readf(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        lines = list(csvreader)

        header = lines.pop(0)
        records = [r for r in lines or [] if r != header]
        # remove the "Total" lines
        records = [r for r in records if not r[0].startswith('Total')]

        # vote % is index 2
        index = 2
        records = [(r[0:index] + r[index+1:]) for r in records]
        return records

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
}

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
        elif r[1:] == ['', '', '', '']:
            currace = r[0].split('(')[0].rstrip()
            if currace in stateraces:
                lf = currace.split(' ')
                district = lf.pop(-1)
                currace = ' '.join(lf)
            else:
                district = ''
        else:
            if 'WRITE-IN' in r[0]:
                r[0] = "Write-Ins"
                party = None
            else:
                party = Parties.get(r[0])
            newr = ['Perry', curprecinct, currace, district, party] + r
            newrecords.append(newr)

    header = ['county', 'precinct', 'office', 'district', 'party',
              'candidate', 'votes', 'election_day', 'mi', 'pr']
    write('20201103__pa__general__perry__precinct.csv', header, newrecords)


def get_totals(summaries):
    stateraces = ['Congress 12', 'PA Rep 86', 'PA Senator 15']
    summaries.pop(0)
    newsum = []
    currace = None
    district = None
    party = None
    for r in summaries or []:
        if r[1:] == ['', '', '', '']:
            currace = r[0].split('(')[0].rstrip()
            if currace in stateraces:
                lf = currace.split(' ')
                district = lf.pop(-1)
                currace = ' '.join(lf)
            else:
                district = ''
        elif r[0].startswith('Total'):
            continue
        else:
            if 'WRITE-IN' in r[0]:
                r[0] = "Write-Ins"
                party = None
            else:
                party = Parties.get(r[0])
                newr = ['Perry', currace, district, party] + r
                newsum.append(newr)

    header = ['county', 'office', 'district', 'party', 'candidate',
         'votes', 'election_day', 'mi', 'pr']
    write('20201103__pa__general__perry__summary.csv', header, newsum)

def main():
    records = readf("imported-20201103__pa__general__perry.csv")

    tot = next((c for c, v in enumerate(records) if v[0] == 'All Precincts'), 0)
    precinct_per = records[:tot]
    if not precinct_per:
        print ("error in file")
    else:
        parse(precinct_per)

        summaries = records[tot:]
        get_totals(summaries)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
'''
This'll show you the low hanging fruit from AD-Recon.ps1.

./fruityad.py Computers.csv
'''

import csv, sys
bad = {}
with open(sys.argv[1]) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 1
      i = 0
      for row in csv_reader:
        if "Server 200" in row[4] or "Server 2012" in row[4]:
          bad[i] = "Name: "+ row[1] + "\nIP: " + row[3] + "\nOS: " + row[4] + "\n"
        line_count += 1
        i+=1
print("Processed, results below \n")
for b in bad:
  print(bad[b])

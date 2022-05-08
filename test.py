import csv
import os

file_name = 'clinic_coords.csv'

cwd = os.getcwd ()
os.chdir (r'C:\Users\Public\Documents')
cwd = os.getcwd ()

fhand = open (file_name, 'w')
csvwriter = csv.writer (fhand)

fields = ['lat', 'long']
lat_long = ['44.45515', '-73.21318']

csvwriter.writerow (fields)
csvwriter.writerow (lat_long)

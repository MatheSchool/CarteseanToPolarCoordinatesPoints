import math
import csv
 
bx = 1.0
by = 4.0

with open('points.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
      print(row[0], row[1])
      px = float(row[0])
      py = float(row[1])
      d = math.sqrt((bx - px)**2 + (by - py)**2)
      a = math.acos((px - bx) / d) 
      print(d, a)


from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client["minute-tracker"]

# Time config
year = 19
month = int(input("Month: "))
day = int(input("Day: "))

while True:
    print("")

    # Get activity
    activity = input("Activity: ")

    # Quit when q is entered
    if activity == 'q':
        break

    # Get starting time
    while True:
        try:
            start = input("Start: ")
            if len(start) == 3:
                start = "0" + start
            start = datetime.strptime(f"{year}-{month}-{day} {start}", "%y-%m-%d %H%M")
            break
        except:
            pass

    # Get ending time
    while True:
        try:
            end = input("End: ")
            if len(end) == 3:
                end = "0" + end
            end = datetime.strptime(f"{year}-{month}-{day} {end}", "%y-%m-%d %H%M")
            break
        except:
            pass

    # Fix day if go to sleep before midnight
    if activity == "Sleep":
        if start.hour > 21:    # Go to sleep after 9PM
            start = start.replace(day=day-1)

    # Create record
    record = {"activity": activity,
              "start": start,
              "end": end}

    # Insert record to MongoDB
    db.Records.insert_one(record)

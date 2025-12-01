import csv
import random
import time

activities = ["walking", "sitting", "standing"]
file_name = "sensor_data.csv"

with open(file_name, "w", newline="") as wcsv:
    writer = csv.writer(wcsv)
    writer.writerow(["timestamp", "ax", "ay", "az", "activity"])

    for i in range(50):
        activity = random.choice(activities)

        if activity == "walking":
            ax = round(random.uniform(0.8, 2.0), 2)
            ay = round(random.uniform(0.8, 2.0), 2)
            az = round(random.uniform(1.0, 2.5), 2)
        elif activity == "sitting":
            ax = round(random.uniform(0.0, 0.3), 2)
            ay = round(random.uniform(0.0, 0.3), 2)
            az = round(random.uniform(0.0, 0.3), 2)
        else:
            ax = round(random.uniform(0.3, 0.7), 2)
            ay = round(random.uniform(0.3, 0.7), 2)
            az = round(random.uniform(0.3, 0.7), 2)

        timestamp = int(time.time())
        writer.writerow([timestamp, ax, ay, az, activity])


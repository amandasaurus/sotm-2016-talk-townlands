from collections import defaultdict
import csv

def mapped_per_user():
    user_mapped = defaultdict(int)
    with open("townlands-no-geom.csv") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            user_mapped[row['OSM_USER']] += 1

    with open("stats_per_user.csv", "w") as fp:
        writer = csv.writer(fp)
        writer.writerow(("name", "num"))
        for name, num in sorted(user_mapped.items(), key=lambda x: x[1], reverse=True):
            writer.writerow((name, num))


mapped_per_user()

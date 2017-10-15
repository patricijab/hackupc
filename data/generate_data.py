import csv
import random
import datetime

def generate_q(i, meal, sweet, wb, cb):
    if i in categories["meal"]:
        r = random.uniform(0, 1)
        q = random.randint(meal[0], meal[1])
        if (r < 0.1):
            q = q - meal[2]
        elif (r > 0.9):
            q = q + meal[2]
    elif i in categories["sweet"]:
        r = random.uniform(0, 1)
        q = random.randint(sweet[0], sweet[1])
        if (r < 0.1):
            q = q - sweet[2]
        elif (r > 0.9):
            q = q + sweet[2]
    elif i in categories["warm beverage"]:
        r = random.uniform(0, 1)
        q = random.randint(wb[0], wb[1])
        if (r < 0.1):
            q = q - wb[2]
        elif (r > 0.9):
            q = q + wb[2]
    else:
        r = random.uniform(0, 1)
        q = random.randint(cb[0], cb[1])
        if (r < 0.1):
            q = q - cb[2]
        elif (r > 0.9):
            q = q + cb[2]
    return q

items = ["croissant", "muffin", "capuccino", "sandwich", "tea", "juice", "toast", "water", "cafe latte", "espresso"]

categories = {"meal": [3, 6],
              "sweet": [0, 1],
              "warm beverage": [2, 4, 8, 9],
              "cold beverage": [5, 7]
              }

rows = []

date = datetime.datetime(2017, 7, 23, 1, 1)  # datum v juliju

for i in range(90):  # primeri za 90 dni

    if (date.weekday() < 5): # med tednom

        for h in range(7, 22): # gremo cez vse ure, ko delajo

            # generate_q(i, meal, sweet, wb, cb)
            ll = [14, 15, 16, 20, 21]  # list of hours of LOW traffic
            if h in ll:
                for i in range(len(items)):  # gremo cez vse hrane
                    q = generate_q(i, [4,6,1], [5,7,1], [12,15,1], [8,10,1])
                    rows.append([h, date.weekday(), date.month, date.year, i, q])

            lm = [7, 8, 13, 17, 19] # list of hours of MIDDLE traffic
            if h in lm:
                for i in range(len(items)):  # gremo cez vse hrane
                    q = generate_q(i, [8,10,1], [6,8,1], [16,20,1], [9,12,1])
                    rows.append([h, date.weekday(), date.month, date.year, i, q])

            lh = [9, 10, 11, 12, 18] # list of hours of HIGH traffic
            if h in lh:
                for i in range(len(items)):  # gremo cez vse hrane
                    q = generate_q(i, [7,11,1], [10,14,1], [20,25,1], [10,12,1])
                    rows.append([h, date.weekday(), date.month, date.year, i, q])

    elif (date.weekday() == 5):

        for h in range(8, 21):  # gremo cez vse ure, ko delajo

            # generate_q(i, meal, sweet, wb, cb)
            ll = [9, 10, 11, 12, 13]  # list of hours of LOW traffic
            if h in ll:
                for i in range(len(items)):  # gremo cez vse hrane
                    q = generate_q(i, [9, 12, 1], [8, 11, 1], [17, 20, 1], [15, 18, 1])
                    rows.append([h, date.weekday(), date.month, date.year, i, q])

            lm = [8, 14, 15, 16, 17, 18, 19, 20]  # list of hours of MIDDLE traffic
            if h in lm:
                for i in range(len(items)):  # gremo cez vse hrane
                    q = generate_q(i, [7, 9, 1], [6, 8, 1], [14, 18, 1], [12, 15, 1])
                    rows.append([h, date.weekday(), date.month, date.year, i, q])

    else:

        for h in range(8, 15):  # gremo cez vse ure, ko delajo

            for i in range(len(items)):  # gremo cez vse hrane
                q = generate_q(i, [8, 10, 1], [9, 11, 1], [13, 15, 1], [8, 10, 1])
                rows.append([h, date.weekday(), date.month, date.year, i, q])

    date = date + datetime.timedelta(days=1)

for r in rows:
    print(r)

print(len(rows))


    # ZA LINEARNO REGRESIJO
    # hour, day, month, year, index izdelka, kolicina izdelka

    # ZA NEVRONSKO MREZO
    # hour - med 7 in 21, ko je odprto
    # day in week, 8 je praznik
    # mesec
    # school year or holiday
    # item name
    # amount
    # in combination with
    # categories


with open('data_03_nn.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    counter = 0
    for r in rows:
        writer.writerow(r)
        if counter > 20:
            break
        counter+=1

import csv
import random
import datetime


items = ["croissant", "muffin", "capuccino", "sandwich", "tea", "juice", "toast", "water", "cafe latte", "espresso"]

categories = {"meal": [3, 6],
              "sweet": [0, 1],
              "warm beverage": [2, 4, 8, 9],
              "cold beverage": [5, 7]
              }

rows = []

for i in range(30):  # primeri za 30 dni

    date = datetime.datetime(2017, 9, i+1, 1, 1)  # datum v septembru

    isweekday = (date.weekday() < 5)

    if (isweekday):

        for h in range(7, 22): # gremo cez vse ure, ko delajo

            ll = [12, 13, 14, 20, 21]  # list of hours of LOW traffic
            if h in ll:
                # stevilo razlicnih hran na uro
                r_q = 6
                q = {}  # seznam hran
                for a in range(r_q):
                    # enaka verjetnost za katerikoli izdelek
                    item = items[random.randint(0, len(items) - 1)]
                    if item not in q:
                        q[item] = random.randint(1, 8)  # kolicina je also random
                # dodamo zdej te hrane v rows
                for qi in q:
                    # hour, day, month, year, index izdelka, kolicina izdelka
                    rows.append([h, date.weekday(), date.month, 2017, items.index(qi), q[qi]])

            lm = [10, 11, 18, 19, 20] # list of hours of MIDDLE traffic
            if h in lm:
                r_q = random.randint(8, 10) # stevilo razlicnih hran na uro
                q = {}  # seznam hran
                for a in range(r_q):
                    # ce je dopoldne je vecja verjetnost za kavo in sweet, ce popoldne za kavo in meal
                    r_p = random.uniform(0, 1)
                    if r_p > 0.3: #izberes kavo in sweet / kavo in meal
                        cofi = items[random.choice(categories["warm beverage"])]
                        if cofi not in q:
                            q[cofi] = random.randint(1, 15)
                        if (h in [10, 11]): # kava in sweet
                            swit = items[random.choice(categories["sweet"])]
                            if swit not in q:
                                q[swit] = random.randint(1, 15)
                        else:
                            meal = items[random.choice(categories["meal"])]
                            if meal not in q:
                                q[meal] = random.randint(1, 15)
                    else: # izberes drugo
                        r_f = items[random.choice(categories["meal"] + categories["sweet"] + categories["cold beverage"])]
                        if r_f not in q:
                            q[r_f] = random.randint(1, 10)

                # dodamo zdej te hrane v rows
                for qi in q:
                    # hour, day, month, year, index izdelka, kolicina izdelka
                    rows.append([h, date.weekday(), date.month, 2017, items.index(qi), q[qi]])

            lh = [7, 8, 9, 15, 16, 17] # list of hours of HIGH traffic
            if h in lh:
                r_q = random.randint(9, 10)  # stevilo razlicnih hran na uro
                q = {}  # seznam hran
                for a in range(r_q):
                    cofi = items[random.choice(categories["warm beverage"])]
                    if cofi not in q:
                        q[cofi] = random.randint(10, 25)
                    if (h in [7, 8, 9]):  # kava in sweet ali meal
                        if (random.uniform(0,1) > 0.4):
                            swit = items[random.choice(categories["sweet"])]
                            if swit not in q:
                                q[swit] = random.randint(5, 20)
                        else:
                            meal = items[random.choice(categories["meal"])]
                            if meal not in q:
                                q[meal] = random.randint(0, 15)

                    else:  # izberes drugo
                        if (random.uniform(0,1) < 0.4):
                            swit = items[random.choice(categories["sweet"])]
                            if swit not in q:
                                q[swit] = random.randint(0, 15)
                        else:
                            meal = items[random.choice(categories["meal"])]
                            if meal not in q:
                                q[meal] = random.randint(5, 20)

                # dodamo zdej te hrane v rows
                for qi in q:
                    # hour, day, month, year, index izdelka, kolicina izdelka
                    rows.append([h, date.weekday(), date.month, 2017, items.index(qi), q[qi]])

    elif (date.weekday() == 5):

        for h in range(8, 21):  # gremo cez vse ure, ko delajo

            r_q = random.randint(6, 9)  # stevilo razlicnih hran na uro
            q = {}  # seznam hran
            for a in range(r_q):
                if (h in [9, 10, 11, 12, 16, 17, 18, 19]):
                    cofi = items[random.choice(categories["warm beverage"])]
                    if cofi not in q:
                        q[cofi] = random.randint(10, 30)
                    rest = items[random.choice(categories["cold beverage"] + categories["meal"] + categories["sweet"])]
                    if rest not in q:
                        q[rest] = random.randint(3, 20)
                else:
                    cofi = items[random.choice(categories["warm beverage"])]
                    if cofi not in q:
                        q[cofi] = random.randint(5, 20)
                    rest = items[random.choice(categories["cold beverage"] + categories["meal"] + categories["sweet"])]
                    if rest not in q:
                        q[rest] = random.randint(1, 13)
            # dodamo zdej te hrane v rows
            for qi in q:
                # hour, day, month, year, index izdelka, kolicina izdelka
                rows.append([h, date.weekday(), date.month, 2017, items.index(qi), q[qi]])

    else:

        for h in range(8, 15):  # gremo cez vse ure, ko delajo

            r_q = random.randint(6, 7)  # stevilo razlicnih hran na uro
            q = {}  # seznam hran
            for a in range(r_q):
                if (h in [9, 10, 11]):
                    cofi = items[random.choice(categories["warm beverage"])]
                    if cofi not in q:
                        q[cofi] = random.randint(5, 20)
                    rest = items[
                        random.choice(categories["cold beverage"] + categories["meal"] + categories["sweet"])]
                    if rest not in q:
                        q[rest] = random.randint(1, 15)
                else:
                    cofi = items[random.choice(categories["warm beverage"])]
                    if cofi not in q:
                        q[cofi] = random.randint(3, 13)
                    rest = items[
                        random.choice(categories["cold beverage"] + categories["meal"] + categories["sweet"])]
                    if rest not in q:
                        q[rest] = random.randint(1, 8)

            # dodamo zdej te hrane v rows
            for qi in q:
                # hour, day, month, year, index izdelka, kolicina izdelka
                rows.append([h, date.weekday(), date.month, 2017, items.index(qi), q[qi]])


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


with open('data_01.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for r in rows:
        writer.writerow(r)

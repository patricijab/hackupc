from sklearn import linear_model, cross_validation
import csv
import numpy as np
import matplotlib.pyplot as plt


def prepare_data(r):
    row = []
    # ure
    for i in range(8, 22):
        if (int(r[0]) == i):
            row.append(1)
        else:
            row.append(0)
    # dan v tednu
    for i in range(7):
        if (int(r[1]) == i):
            row.append(1)
        else:
            row.append(0)
    # vikend
    if (int(r[1]) > 4):
        row.append(1)
    else:
        row.append(0)
    # mesec
    """
    for i in range(12):
        if (r[2] == i):
            row.append(1)
        else:
            row.append(0)
    """
    # item
    for i in range(10):
        if (int(r[4]) == i):
            row.append(1)
        else:
            row.append(0)

    return row

data = []
y = []

with open('data_02.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        row = prepare_data(r)
        data.append(row)
        y.append(int(r[5]))


lm = linear_model.LinearRegression()
model = lm.fit(data,y)

print(lm.predict(prepare_data([9,0,9,2017,0])))
print(lm.predict(prepare_data([21,3,9,2017,0])))

#print(lm.score(data,y))

#mse = np.mean((y - lm.predict(data)) ** 2)
#print(mse)

"""
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(data, y, test_size=0.20)

lm = linear_model.LinearRegression()
lm.fit(X_train, Y_train)
pred_train = lm.predict(X_train)
pred_test = lm.predict(X_test)


mse = np.mean((Y_train - lm.predict(X_train)) ** 2)
print("trein", mse)

mse = np.mean((Y_test - lm.predict(X_test)) ** 2)
print("test", mse)


plt.scatter(lm.predict(X_train), lm.predict(X_train) - Y_train, c='b', s=40, alpha=0.5)
plt.scatter(lm.predict(X_test), lm.predict(X_test) - Y_test, c='g', s=40)
plt.hlines(y=0, xmin=0, xmax=50)
plt.show(block=True)
"""
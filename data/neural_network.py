from sklearn import linear_model, cross_validation
import csv
import numpy as np


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
    # item
    for i in range(10):
        if (int(r[4]) == i):
            row.append(1)
        else:
            row.append(0)

    return row

def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


data = []
target = []

with open('data_03_nn.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        row = prepare_data(r)
        data.append(row)
        target.append([int(r[5])])

"""
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])
print(np.shape(X))

y = np.array([[0],
              [1],
              [1],
              [0]])
print(np.shape(y))
"""

X = np.array(data)
y = np.array(target)

r,c = X.shape

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2 * np.random.random((c, r)) - 1
syn1 = 2 * np.random.random((r, 1)) - 1

for j in range(2):

    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    print(l1)
    l2 = nonlin(np.dot(l1, syn1))
    print(l2)

    # how much did we miss the target value?
    l2_error = y - l2

    #if (j % 10000) == 0:
    print("Error:" + str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error * nonlin(l2, deriv=True)
    print(l2_delta)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)
    print(l1_error)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    print(l1_error[0])
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)


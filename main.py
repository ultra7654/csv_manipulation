import matplotlib.pyplot as mp
import matplotlib as m
import pandas as p


def read_data():
    set = p.read_csv("dataset.csv")
    scores = set['score'].sort_values(ascending=True)
    mp.plot()
    mp.show()


read_data()

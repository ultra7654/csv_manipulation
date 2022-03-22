import pandas as p

def read_data():
    set = p.read_csv("dataset.csv")
    print(len(set.columns))
    print()

read_data()

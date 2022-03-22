import pandas as p

def read_data():
    set = p.read_csv("dataset.csv")
    scores = set['score'].sort_values(ascending=True)
    indexes = set['score'].sort_index(ascending=True)
    print(scores)

read_data()
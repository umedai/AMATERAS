import pickle
import pandas as pd

with open("card.pickle", "rb") as f:
    x = pickle.load(f)

print(x)
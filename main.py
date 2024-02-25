import pandas as pd
import matplotlib.pyplot as plt

student_info = pd.read_csv("data/dataset.csv", index_col=0, parse_dates=True)
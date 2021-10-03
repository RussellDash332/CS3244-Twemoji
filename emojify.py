import pandas as pd

def emojify(idx):
    return pd.read_csv("emoji_map_1791.csv").loc[idx, "ucode"]

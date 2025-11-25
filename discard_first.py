import pandas as pd

def clean_csv():
    df = pd.read_csv('reaction_time_measurements_Florentin.csv') #Just put your name here
    df_clean = df[df['trial'] != 1]
    return df_clean

df_clean = clean_csv()
df_clean.to_csv('clean.csv', index=False)

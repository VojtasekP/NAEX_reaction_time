import pandas as pd
df = pd.read_csv('reaction_time_measurements_Florentin.csv') #Just put your name here
df_clean = df[df['trial'] != 1]
df_clean.to_csv('fichier_nettoye.csv', index=False)
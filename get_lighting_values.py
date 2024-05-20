import pandas as pd
import pprint


def get_construction_values(file_path):
    df = pd.read_csv(file_path)
    # data = []
    return df

# file_path = r'C:\Users\ENIEMEYER\Documents\GitHub\energy_goof_troup\ASHRAE 90.1-2019-9.6.1 LPD Area Type.csv'
file_path = r'C:\Users\ENIEMEYER\Documents\GitHub\energy_goof_troup\ASHRAE 90.1-2019-9.6.1 LPD.csv'
df = get_construction_values(file_path)
print(df)

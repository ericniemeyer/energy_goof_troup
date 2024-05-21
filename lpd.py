#LPDS

import streamlit as st
import pandas as pd
import numpy as np

lpd_path="ASHRAE 90.1-2019-9.6.1 LPD Area Type.csv"

lpd_df = pd.read_csv(lpd_path)
bldg_df = pd.DataFrame()
bldg_type = 2

if bldg_type == 2:
    bldg_df=(lpd_df.iloc[18])
    st.write(bldg_df)


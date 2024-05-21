#Mechanical Systems

import streamlit as st
import pandas as pd
import numpy as np

mech_path = "ASHRAE 90.1-2019 Mech.csv"

mech_df = pd.read_csv(mech_path)
bldg_df = pd.DataFrame()
bldg_type = 2

st.write(mech_df)

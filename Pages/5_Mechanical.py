import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
     page_title='Mechanical',
     layout="wide",
)


st.title("Mechanical")
st.markdown("This section covers the design, installation, and maintenance of mechanical systems to ensure energy-efficient heating, ventilation, air conditioning, and refrigeration (HVAC&R).")

st.subheader("What type of building are you designing?")
bldg_type = st.selectbox(
   "", 
   ("Office", "Bank", "School", "Library"),  
   index=0,
#    placeholder="Office",
)

#Mechanical Systems chart

mech_path = "ASHRAE 90.1-2019 Mech.csv"

mech_df = pd.read_csv(mech_path)
bldg_df = pd.DataFrame()

if bldg_type == "Office":
    st.write("The following systems are recommended based on availability. See they prescriptive performance requirements according to ASHRAE 90.1-2019 below:")
    st.write(mech_df)

st.divider()

st.write('##')
col1,col2,col3,col4 = st.columns(4)

with col1:

    st.image('./images/fault.png', width=200)

    st.write('##')
    st.write('##')
    st.write('##')
    st.write('##')

    st.image('./images/demandcontrol.png', width=200)
    
with col2: 
    st.markdown(
        """
        #### Fault Detection and Diagnostics 
        ##### 6.4.3.1.2

        A fault detection and diagnostics (FDD) system must be included. 

        _FDD is a software that utilizes advanced algorithms and machine learning techniques to analyze data from sensors and equipment within a building._
  
        #### Demand Control Ventilation 
        ##### 6.4.3.8

        Demand control ventilation (DCV) is required for spaces larger than 500 sf. 

        """

    )
with col3:
    st.image('./images/energyrecovery.png', width=200)

with col4:
    """
        #### Energy Recovery for Multifamily  
        ##### 6.5.6

        Energy recovery is required for non-transient dwelling units. _Minimum enthalpy recovery ratio should be 50% at cooling and 60% at heating._
  
        """

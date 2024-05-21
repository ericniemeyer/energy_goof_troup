import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
     page_title='Lighting',
     layout="wide",
)

st.subheader("What type of building are you designing?")
bldg_type = st.selectbox(
   "", 
   ("Office", "Bank", "School", "Library"),  
   index=0,
#    placeholder="Office",
)

#Mechanical Systems chart

lpd_path="ASHRAE 90.1-2019-9.6.1 LPD Area Type.csv"
lpd_df = pd.read_csv(lpd_path)
bldg_df = pd.DataFrame()

if bldg_type == "Office":
    st.write("The following Building Area LPD is recommended based on availability. See the prescriptive performance requirements according to ASHRAE 90.1-2019 below:")
    bldg_df=(lpd_df.iloc[18])
    st.write(bldg_df)



st.divider()



st.title("Lighting")
st.markdown("This section ensures that lighting systems are designed and installed to maximize energy efficiency while providing adequate illumination.")
st.write('##')
col1,col2,col3,col4 = st.columns(4)

with col1:
     st.image('./images/dwellingunit.png', width=150)

     st.image('./images/occupant.png', width=150)

with col2: 
     st.markdown(
          """
          #### Dwelling Unit Lighting  
          ##### 9.4.3

          75% of installed lighting must be highly efficient with a total efficacy of at least 45 luminaire/Watt.  
          """
          )
     st.write("##")
     st.write("##")
     
     st.markdown(
          """
          #### Occupant Sensor Control  
          ##### Table 9.3.1-1

        Most* room types require occupant sensor control. 
        
        _*Offices, corridors, storage rooms, break rooms, restrooms, stairwells, and parking garages_   
        """
     )



with col3:
        st.image('./images/secondary.png', width=250)

        st.write("##")
        st.write("##")
        
        st.image('./images/minimumdaylight.png', width=250)
with col4: 
    st.markdown(
        """
        #### Secondary Side Daylight 
        ##### 9.4.1.1

        Primary and secondary daylight areas must have unique/separate Automatic daylight responsive controls.
  
        """
    )
    st.write("##")
    st.markdown(
          """
          #### Minimum Daylight Control 
          ##### Exception to 9.4.1.1(e)

          Space lighting must be reduced to 20% or less when daylight is available.
  
          """

    )
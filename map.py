import streamlit as st
import numpy as np
import pandas as pd


#Streamlit page config
st.set_page_config(
     page_title='CompEasy',
     layout="wide",
)


##import pd dataframe
data = pd.read_json('ashrae_90_1_2019.construction_properties.json')
df1 = pd.DataFrame(data)



#Random df
chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])



## Select your building type
st.title("What type of building are you designing?")
bldg_type = st.selectbox(
   "", 
   ("Office", "Bank", "School", "Library"),  
   index=None,
   placeholder="Select building...",
)




if bldg_type == "Office":
    st.title("Select the ASHRAE Climate Zone for your project:")      

    ## Select your climate zone
    #CZ1 = st.selectbox(
    #"What the ASHRAE climate zone for your project?", 
    #("CZ0", "CZ1", "CZ2", "CZ3", "CZ4", "CZ5", "CZ6", "CZ7"),  
    #index=None,
    #placeholder="Select contact method...",
    #)

    #CZ = st.select_slider(
    #    "Select the ASHRAE CZ for your project:",
    #    options=["CZ0", "CZ1", "CZ2", "CZ3", "CZ4", "CZ5", "CZ6", "CZ7"]
    #)

    
    CZ = st.selectbox(
   (""),
   ("CZ0", "CZ1", "CZ2", "CZ3", "CZ4", "CZ5", "CZ6", "CZ7"),
   index=None,
   placeholder="Select climate zone...",
    )

    # Results panels for CZ0
    if CZ == "CZ0":
        st.write("Envelope Construction Parameters")
        st.write(df1)
    # Results panels for CZ1
    elif CZ == "CZ1":
        st.write("Yo CZ1")
    # Results panels for CZ1
    elif CZ == "CZ2":
        st.write("Yo CZ2")
        chart_data
    # Results panels for CZ1
    elif CZ == "CZ3":
       st.write("CZ 3 BABEY")
    elif CZ == "CZ4":
        chart_data
    elif CZ == "CZ5":
        chart_data
    elif CZ == "CZ6":
        chart_data
    elif CZ == "CZ7":
        chart_data
    elif CZ == None:   
        ""


#Else statement to 
#else:
#     st.write("Sorry, we haven't produced data for that building type yet. Check back soon!")

import streamlit as st
import numpy as np
import pandas as pd


import pandas as pd
import pprint

import pandas as pd
import pprint


def read_climate_zone_data(df):
    # Initialize dictionary to store data for each climate zone
    climate_data = {}
    climate_zone = None

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        list_of_row_values = row.tolist()

        # Check if the first cell starts with "Table 5.5-"
        if str(row[0]).startswith(f"Table 5.5-"):
            # Get climate zone number from the table header.
            climate_zone = str(row[0]).split()[1].split("-")[1]
            climate_data[climate_zone] = {}
        else:
            if climate_zone is not None:
                envelope_parameter = list_of_row_values[0]
                if envelope_parameter not in climate_data[climate_zone].keys():
                    climate_data[climate_zone][envelope_parameter] = list_of_row_values[1:]
                # else:
                #     climate_data[climate_zone][envelope_parameter + '2'] = list_of_row_values[1:]

    return climate_data


def get_construction_values(file_path, climate_zone):
    df = pd.read_csv(file_path)

    climate_data = read_climate_zone_data(df)
    # pprint.pprint(climate_data[climate_zone])
    return climate_data[climate_zone]


def reformat_construction_values(file_path, climate_zone):
    construction_values = get_construction_values(file_path, climate_zone)

    surface_type_labels = {
        'Roof': {
            'Insulation entirely above deck': 'Ins. Above Roof Deck',
            'Metal buildinga': 'Metal Roof',
            'Attic and other': 'Attic + Other',
        },
        'Wall': {
            'Mass': 'Mass',
            'Metal building': 'Metal',
            'Steel-framed': 'Metal Frame',
            'Wood-framed and other': 'Wood Frame',
            'Below-grade wall': 'Below Grade',
        }
    }

    # data = [['tom', 10], ['nick', 15], ['juli', 14]]
    data = []

    for surface_category, surface_types in surface_type_labels.items():
        for csv_label, display_label in surface_types.items():
            df_label = f"{surface_category} - {display_label}"
            r_value = construction_values[csv_label][1]
            u_value = construction_values[csv_label][0]
            data.append([df_label, r_value, u_value])

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Surface Type', 'R-Value', 'U-Value'])
    #pprint.pprint(df)
    #print(df)

    return df


# file_path = r'C:\Users\ENIEMEYER\Documents\GitHub\energy_goof_troup\ASHRAE 90.1-2019.csv'
# reformat_construction_values(file_path, '2')

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


ashrae_csv = "ASHRAE 90.1-2019.csv"

if bldg_type == "Office":
    st.title("Select the ASHRAE Climate Zone for your project:")      
    
    CZ = st.selectbox(
   (""),
   ("CZ0", "CZ1", "CZ2", "CZ3", "CZ4", "CZ5", "CZ6", "CZ7"),
   index=None,
   placeholder="Select climate zone...",
    )

    # Results panels for CZ0
    if CZ == "CZ0":
        st.write("Envelope Construction Parameters for Climate Zone 0")
        st.write(reformat_construction_values(ashrae_csv, '0'))
    # Results panels for CZ1
    elif CZ == "CZ1":
        st.write("Envelope Construction Parameters for Climate Zone 1")
        st.write(reformat_construction_values(ashrae_csv, '1'))
    # Results panels for CZ1
    elif CZ == "CZ2":
        st.write("Envelope Construction Parameters for Climate Zone 2")
        st.write(reformat_construction_values(ashrae_csv, '2'))
    # Results panels for CZ1
    elif CZ == "CZ3":
        st.write("Envelope Construction Parameters for Climate Zone 3")
        st.write(reformat_construction_values(ashrae_csv, '3'))
    elif CZ == "CZ4":
        st.write("Envelope Construction Parameters for Climate Zone 4")
        st.write(reformat_construction_values(ashrae_csv, '4'))
    elif CZ == "CZ5":
        st.write("Envelope Construction Parameters for Climate Zone 5")
        st.write(reformat_construction_values(ashrae_csv, '5'))
    elif CZ == "CZ6":
        st.write("Envelope Construction Parameters for Climate Zone 6")
        st.write(reformat_construction_values(ashrae_csv, '6'))
    elif CZ == "CZ7":
        st.write("Envelope Construction Parameters for Climate Zone 7")
        st.write(reformat_construction_values(ashrae_csv, '7'))
    elif CZ == None:   
        ""


#Else statement to 
#else:
#        st.write("Sorry, we haven't produced data for that building type yet. Check back soon!")

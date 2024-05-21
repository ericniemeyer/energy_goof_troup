import streamlit as st
import numpy as np
import pandas as pd
import pprint


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

## Select your building type
st.title("Envelope")
st.markdown("The building envelope includes all components that separate the interior of the building from the exterior environment. This section ensures that the building envelope is designed and constructed to minimize energy loss.")
st.write('##')
st.header("Prescriptive Insulation Levels")

st.subheader("What type of building are you designing?")
bldg_type = st.selectbox(
        "", 
        ("Office", "Bank", "School", "Library"),  
        index=0,
)




if bldg_type == "Office":
    st.subheader("Select the ASHRAE Climate Zone for your project:")      

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

ashrae_csv = "ASHRAE 90.1-2019.csv"

if bldg_type == "Office":
    st.title("Select the ASHRAE Climate Zone for your project:")      
    
    CZ = st.selectbox(
        (""),
        ("CZ0", "CZ1", "CZ2", "CZ3", "CZ4", "CZ5", "CZ6", "CZ7"),
        index=0,
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
''' Roof, Wall, Floor '''
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
# Function to add text to an image
def add_text_to_image(image, text, text_color='#C26D41', font_size=24):  # , text_color=(255, 255, 255), position=(100, 100)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate the position to center the text
    text_width, text_height = draw.textsize(text, font=font)
    image_width, image_height = image.size
    position = ((image_width - text_width) // 2, (image_height - text_height) // 2)

    draw.text(position, text, fill=text_color, font=font)
    return image

# Function to convert an image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# Function to display clickable images
def display_clickable_roof(images, popup_image, popup_text_df, popup_size=(200,200)):
    # col1, col2, col3 = st.columns(3)
    cols = st.columns(3)
    
    clicked_image = None

    if cols[0].button('Attic and Other', key=0):
        clicked_image = images[0]
    cols[0].image(images[0], use_column_width=True)

    if cols[1].button('Insulation above deck', key=1):
        clicked_image = images[1]
    cols[1].image(images[1], use_column_width=True)

    if cols[2].button('Metal Roof', key=2):
        clicked_image = images[2]
    cols[2].image(images[2], use_column_width=True)

    popup_placeholder = st.empty()

    # Check if the clicked image matches any of the original images
    if clicked_image is not None:
        # If yes, add text to the pop-up image
        if clicked_image==images[0]:
            popup_text = 'Roof - Attic + Other'
        elif clicked_image==images[1]:
            popup_text = 'Roof - Ins. Above Roof Deck'
        elif clicked_image==images[2]:
                    popup_text = 'Roof - Metal Roof'

        popup_value = popup_text_df.loc[popup_text_df['Surface Type'] == popup_text, 'R-Value'].iloc[0]
        # Size image
        aspect_ratio=popup_image.width / popup_image.height
        new_width=popup_size[0]
        new_height=int(new_width/aspect_ratio)
        popup_image_resized = popup_image.copy().resize((new_width, new_height))  # Resizing the popup image
        popup_image_with_text = add_text_to_image(popup_image_resized, str(popup_value))

        popup_img_base64 = image_to_base64(popup_image_with_text)

        popup_placeholder.markdown(
            f"<div style='text-align: center;'><img src='data:image/png;base64,{popup_img_base64}' alt='popup image'></div>", 
            unsafe_allow_html=True
        )



# Function to display clickable images
def display_clickable_wall(images, popup_image, popup_text_df, popup_size=(200,200)):
    # col1, col2, col3 = st.columns(3)
    cols = st.columns(5)
    
    clicked_image = None

    if cols[0].button('Mass', key=0):
        clicked_image = images[0]
    cols[0].image(images[0], use_column_width=True)

    if cols[1].button('Metal', key=1):
        clicked_image = images[1]
    cols[1].image(images[1], use_column_width=True)

    if cols[2].button('Steel Frame', key=2):
        clicked_image = images[2]
    cols[2].image(images[2], use_column_width=True)

    if cols[3].button('Wood Frame', key=3):
        clicked_image = images[3]
    cols[3].image(images[3], use_column_width=True)

    if cols[4].button('Below Grade', key=4):
        clicked_image = images[4]
    cols[4].image(images[4], use_column_width=True)

    popup_placeholder = st.empty()

    # Check if the clicked image matches any of the original images
    if clicked_image is not None:
        # If yes, add text to the pop-up image
        if clicked_image==images[0]:
            popup_text = 'Wall - Mass'
        elif clicked_image==images[1]:
            popup_text = 'Wall - Metal'
        elif clicked_image==images[2]:
                    popup_text = 'Wall - Metal Frame'
        elif clicked_image==images[3]:
            popup_text = 'Wall - Wood Frame'
        elif clicked_image==images[4]:
                    popup_text = 'Wall - Below Grade'

        popup_value = popup_text_df.loc[popup_text_df['Surface Type'] == popup_text, 'R-Value'].iloc[0]
        # Size image
        aspect_ratio=popup_image.width / popup_image.height
        new_width=popup_size[0]
        new_height=int(new_width/aspect_ratio)
        popup_image_resized = popup_image.copy().resize((new_width, new_height))  # Resizing the popup image
        popup_image_with_text = add_text_to_image(popup_image_resized, str(popup_value))        

        popup_img_base64 = image_to_base64(popup_image_with_text)

        popup_placeholder.markdown(
            f"<div style='text-align: center;'><img src='data:image/png;base64,{popup_img_base64}' alt='popup image'></div>", 
            unsafe_allow_html=True
        )


# Function to display clickable images
def display_clickable_floor(images, popup_image, popup_text_df, popup_size=(200,200)):
    # col1, col2, col3 = st.columns(3)
    cols = st.columns(5)
    
    clicked_image = None

    if cols[0].button('Mass floor', key=0):
        clicked_image = images[0]
    cols[0].image(images[0], use_column_width=True)

    if cols[1].button('Steel Joist', key=1):
        clicked_image = images[1]
    cols[1].image(images[1], use_column_width=True)

    if cols[2].button('Wood Frame', key=2):
        clicked_image = images[2]
    cols[2].image(images[2], use_column_width=True)

    if cols[3].button('Slab-on-Grade Floor - Unheated', key=3):
        clicked_image = images[3]
    cols[3].image(images[3], use_column_width=True)

    if cols[4].button('Slab-onGrade Floor - Heated', key=4):
        clicked_image = images[4]
    cols[4].image(images[4], use_column_width=True)

    popup_placeholder = st.empty()

    # Check if the clicked image matches any of the original images
    if clicked_image is not None:
        # If yes, add text to the pop-up image
        if clicked_image==images[0]:
            popup_text = 'Floor - Mass'
        elif clicked_image==images[1]:
            popup_text = 'Floor - Steel Joist'
        elif clicked_image==images[2]:
                    popup_text = 'Floor - Wood Frame'
        elif clicked_image==images[3]:
            popup_text = 'Slab-on-Grade Floor - Unheated'
        elif clicked_image==images[4]:
                    popup_text = 'Slab-on-Grade Floor - Heated'

        popup_value = popup_text_df.loc[popup_text_df['Surface Type'] == popup_text, 'R-Value'].iloc[0]
        # Size image
        aspect_ratio=popup_image.width / popup_image.height
        new_width=popup_size[0]
        new_height=int(new_width/aspect_ratio)
        popup_image_resized = popup_image.copy().resize((new_width, new_height))  # Resizing the popup image
        popup_image_with_text = add_text_to_image(popup_image_resized, str(popup_value))        

        popup_img_base64 = image_to_base64(popup_image_with_text)

        popup_placeholder.markdown(
            f"<div style='text-align: center;'><img src='data:image/png;base64,{popup_img_base64}' alt='popup image'></div>", 
            unsafe_allow_html=True
        )


def main():
    st.title("Roof type")

    # Define paths to your images
    images_roof = ['images/Attic and Other.png', 'images/Insulation above deck.png', 'images/Metal Roof.png']
    images_wall = ['images/wall_mass.jpg', 'images/wall_metal.jpg', 'images/wall_steal_frame.jpg', 'images/wall_wood_frame.png', 'images/wall_below_grade.jpg']
    images_floor = ['images/floor_mass.png', 'images/floor_steeljoist.png', 'images/floor_woodframe.jpg', 'images/floor_grade_unheated.jpg', 'images/floor_grade_heated.png']

    # Path to the popup image
    popup_image_path = 'images/pop_up.jpg'
    popup_image = Image.open(popup_image_path)

    # Text to display on the popup image
    from get_construction_values import reformat_construction_values
    popup_text_df =  reformat_construction_values('ASHRAE 90.1-2019.csv', '2')

    # Display clickable images and the popup image
    display_clickable_roof(images_roof, popup_image, popup_text_df)

    st.title("Wall type")
    display_clickable_wall(images_wall, popup_image, popup_text_df)

    st.title("Floor type")
    display_clickable_floor(images_floor, popup_image, popup_text_df)

if __name__ == "__main__":
    main()






# st.divider()

st.header("Other Prescriptive Code Requirements")
st.write('##')
col1,col2,col3,col4,col5 = st.columns(5)

with col1:

    st.image('./images/blowerdoor.png', width=200)
    
with col2: 
    st.markdown(
        """
        #### Air Leakage Testing
        ##### 5.4.3.1.1 

        Either whole building air leakage test OR third party design review and field inspection during construction is mandatory.  
        """

    )
with col4:
    st.image('./images/windowall.png', width=175)
with col5: 
    st.markdown(
        """
        #### Window Wall Ratio
        ##### Table 5.5.0-8

        Window to Wall Ratio does not exceed 40%.
        """
    )

st.markdown(
        """
        #### Fenestration Orientation
        ##### 5.5.4.5

        East and West facing windows cannot exceed 25% of the total glazing area unless shaded at 9 a.m. and 3 p.m. on the summer solstice.
        """
        )
st.image('./images/facade2.png', width=1000)

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.markdown( """Equal glazing area on all sides of a square building""")
with col2:
    st.markdown( """More glazing area on the East side than on the South""")
with col3:
    st.markdown( """75% shading at 9 a.m. and 3 p.m. on the summer solstice (June 21)""")
with col4:
    st.markdown( """More glazing area on the East side than on the South""")
with col5:
    st.markdown( """More glazing area on the South side than on the East""")
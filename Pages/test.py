import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO

# Function to add text to an image
def add_text_to_image(image, text, text_color='#C26D41', font_size=30):
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

# Function to display clickable roof images
def display_clickable_roof(images, popup_image, popup_text_df, popup_size=(150, 150)):
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

    if clicked_image is not None:
        if clicked_image == images[0]:
            popup_text = 'Roof - Attic + Other'
        elif clicked_image == images[1]:
            popup_text = 'Roof - Ins. Above Roof Deck'
        elif clicked_image == images[2]:
            popup_text = 'Roof - Metal Roof'

        popup_value = popup_text_df.loc[popup_text_df['Surface Type'] == popup_text, 'R-Value'].iloc[0]
        
        aspect_ratio = popup_image.width / popup_image.height
        new_width = popup_size[0]
        new_height = int(new_width / aspect_ratio)
        popup_image_resized = popup_image.copy().resize((new_width, new_height))
        popup_image_with_text = add_text_to_image(popup_image_resized, str(popup_value))

        popup_img_base64 = image_to_base64(popup_image_with_text)

        popup_placeholder.markdown(
            f"<div style='text-align: center;'><img src='data:image/png;base64,{popup_img_base64}' alt='popup image'></div>", 
            unsafe_allow_html=True
        )

# Function to display clickable wall images
def display_clickable_wall(images, popup_image, popup_text_df, popup_size=(150, 150)):
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

    if clicked_image is not None:
        if clicked_image == images[0]:
            popup_text = 'Wall - Mass'
        elif clicked_image == images[1]:
            popup_text = 'Wall - Metal'
        elif clicked_image == images[2]:
            popup_text = 'Wall - Metal Frame'
        elif clicked_image == images[3]:
            popup_text = 'Wall - Wood Frame'
        elif clicked_image == images[4]:
            popup_text = 'Wall - Below Grade'

        popup_value = popup_text_df.loc[popup_text_df['Surface Type'] == popup_text, 'R-Value'].iloc[0]
        
        aspect_ratio = popup_image.width / popup_image.height
        new_width = popup_size[0]
        new_height = int(new_width / aspect_ratio)
        popup_image_resized = popup_image.copy().resize((new_width, new_height))
        popup_image_with_text = add_text_to_image(popup_image_resized, str(popup_value))

        popup_img_base64 = image_to_base64(popup_image_with_text)

        popup_placeholder.markdown(
            f"<div style='text-align: center;'><img src='data:image/png;base64,{popup_img_base64}' alt='popup image'></div>", 
            unsafe_allow_html=True
        )

def main():
    st.title("Roof type")

    images_roof = ['images/Attic and Other.png', 'images/Insulation above deck.png', 'images/Metal Roof.png']
    images_wall = ['images/wall_mass.jpg', 'images/wall_metal.jpg', 'images/wall_steel_frame.jpg', 'images/wall_wood_frame.png', 'images/wall_below_grade.jpg']

    popup_image_path = 'images/pop_up.jpg'
    popup_image = Image.open(popup_image_path)

    from get_construction_values import reformat_construction_values
    popup_text_df = reformat_construction_values('ASHRAE 90.1-2019.csv', '2')

    display_clickable_roof(images_roof, popup_image, popup_text_df)

    st.title("Wall type")
    display_clickable_wall(images_wall, popup_image, popup_text_df)

if __name__ == "__main__":
    main()

import streamlit as st
from PIL import Image
from pathlib import Path

# Function to process image
def process_image(path):
    img = Image.open(path)
    bw = img.convert('L')  # Convert image to grayscale
    return bw

# Streamlit app
st.title("PhotoWizard: From Color to Classic")
st.write("The app enables users to upload original images and converts them to grayscale, rendering them in black and white.")
st.write("Upload an image to process it.")

# Upload image
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display original image
    st.image(uploaded_image, caption="Original Image", use_column_width=True)

    # Process uploaded image
    processed_image = process_image(uploaded_image)
    
    # Display grayscale image
    col1, col2 = st.columns(2)
    with col1:
        st.image(processed_image, caption="Grayscale Image", use_column_width=True)

    # Save grayscale image
    save_button = st.button("Save Grayscale Image")
    if save_button:
        bw_path = "saved_image.jpg"
        processed_image.save(bw_path)
        st.success(f"Grayscale image saved as {bw_path}")


st.text('')
st.text('')
st.markdown('`Code:` [GitHub](https://github.com/yusufokunlola/image-manipulation)')

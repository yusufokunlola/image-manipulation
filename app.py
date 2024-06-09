import streamlit as st
from PIL import Image
from pathlib import Path
import os

# Create directories to save images if they don't exist
if not os.path.exists("saved_images"):
    os.makedirs("saved_images")

# Function to process image
def process_image(image):
    img = Image.open(image)
    stem = Path(image.name).stem

    # Create paths to save files to
    bw_path = "saved_images/bw_{}.jpg".format(stem)
    rcz_path = "saved_images/rcz_{}.jpg".format(stem)

    # Convert image to grayscale
    bw = img.convert('L')
    bw.save(bw_path)

    # Rotate, crop, and resize grayscale image
    rcz = bw.rotate(45).crop((25, 25, 75, 75)).resize((100, 100))
    rcz.save(rcz_path)

    return bw_path, rcz_path

# Streamlit app
st.title("Image Processing App")
st.write("Upload an image to process it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Process the image
    bw_path, rcz_path = process_image(uploaded_file)

    # Display processed images
    st.write("Processed Images:")
    bw_image = Image.open(bw_path)
    st.image(bw_image, caption='Grayscale Image', use_column_width=True)

    # Provide download link for grayscale image
    with open(bw_path, "rb") as file:
        btn = st.download_button(
            label="Download Grayscale Image",
            data=file,
            file_name=os.path.basename(bw_path),
            mime="image/jpeg"
        )

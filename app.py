# import streamlit as st
# from PIL import Image
# from pathlib import Path
# import os

# # Create directories to save images if they don't exist
# if not os.path.exists("saved_images"):
#     os.makedirs("saved_images")

# # Function to process image
# def process_image(image):
#     img = Image.open(image)
#     stem = Path(image.name).stem

#     # Create paths to save files to
#     bw_path = "saved_images/bw_{}.jpg".format(stem)
#     rcz_path = "saved_images/rcz_{}.jpg".format(stem)

#     # Convert image to grayscale
#     bw = img.convert('L')
#     bw.save(bw_path)

#     # Rotate, crop, and resize grayscale image
#     rcz = bw.rotate(45).crop((25, 25, 75, 75)).resize((100, 100))
#     rcz.save(rcz_path)

#     return bw_path, rcz_path

# # Streamlit app
# st.title("PhotoWizard: From Color to Classic")
# st.write("The app enables users to upload original images and converts them to grayscale, rendering them in black and white.")
# st.write("Upload an image to process it.")

# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Display the uploaded image
#     st.image(uploaded_file, caption='Original Image', use_column_width=True)

#     # Process the image
#     bw_path, rcz_path = process_image(uploaded_file)

#     # Display processed images
#     st.write("Processed Images:")
#     bw_image = Image.open(bw_path)
#     st.image(bw_image, caption='Grayscale Image', use_column_width=True)

#     # Provide download link for grayscale image
#     with open(bw_path, "rb") as file:
#         btn = st.download_button(
#             label="Save Grayscale Image",
#             data=file,
#             file_name=os.path.basename(bw_path),
#             mime="image/jpeg"
#         )
       
# st.text('')
# st.text('')
# st.markdown('`Code:` [GitHub](https://github.com/yusufokunlola/image-manipulation)')

import streamlit as st
from PIL import Image
from pathlib import Path
import os

# Create directories to save images if they don't exist
os.makedirs("saved_images", exist_ok=True)

# Function to process image
def process_image(image):
    img = Image.open(image).convert("RGB")  # force RGB for JPEG compatibility
    stem = Path(image.name).stem

    # Paths
    bw_path = f"saved_images/bw_{stem}.jpeg"
    rcz_path = f"saved_images/rcz_{stem}.jpeg"

    # Convert to grayscale
    bw = img.convert("L")
    bw.save(bw_path, format="JPEG", quality=95)

    # Rotate, crop, resize
    rcz = bw.rotate(45, expand=True).crop((25, 25, 75, 75)).resize((100, 100))
    rcz = rcz.convert("RGB")  # JPEG-safe
    rcz.save(rcz_path, format="JPEG", quality=95)

    return bw_path, rcz_path

# Streamlit app
st.title("PhotoWizard: From Color to Classic")
st.write(
    "Upload an image and watch it transform into a clean, classic black-and-white JPEG."
)

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Original Image", use_column_width=True)

    bw_path, rcz_path = process_image(uploaded_file)

    st.subheader("Processed Images")

    bw_image = Image.open(bw_path)
    st.image(bw_image, caption="Grayscale (JPEG)", use_column_width=True)

    with open(bw_path, "rb") as f:
        st.download_button(
            label="Download Grayscale Image",
            data=f,
            file_name=f"bw_{Path(uploaded_file.name).stem}.jpeg",   # 👈 force .jpeg here
            mime="image/jpeg"
        )

st.markdown('`Code:` [GitHub](https://github.com/yusufokunlola/image-manipulation)')

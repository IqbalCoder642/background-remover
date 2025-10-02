import streamlit as st
import rembg
from rembg import remove
from PIL import Image
import io

st.title("🎨 Image Background Remover")
st.write("Upload an image and remove its background instantly!")

# Add file uploader to allow users to upload photos
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display original image
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)

    with col1:
        st.header("Original")
        st.image(image)

    # Remove background
    with col2:
        st.header("Background Removed")
        # Add spinner while processing
        with st.spinner("Removing background..."):
            # Remove background
            output = remove(image)
            st.image(output)

        # Add download button
        buf = io.BytesIO()
        output.save(buf, format='PNG')
        byte_im = buf.getvalue()
        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="removed_background.png",
            mime="image/png"
        )

st.markdown("""
### How to use:
1. Upload an image using the file uploader
2. Wait for processing
3. Download the result
""")
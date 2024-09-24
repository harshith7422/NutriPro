# NutriPro
import streamlit as st 
import os
import google.generativeai as genai 
from PIL import Image
from dotenv import load_dotenv 

load_dotenv()  # loading the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# function to load Google Gemini Pro model and get response
def get_gemini_response(prompt_text, image_data, prompt_description):
    # Use gemini-1.5-flash instead of gemini-pro-vision
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt_text, image_data[0], prompt_description])
    return response.text

# check if a file has been uploaded
def input_image_setup(uploaded_file):
    if uploaded_file is not None: 
        bytes_data = uploaded_file.getvalue()  # read the file into bytes

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="NutriPro")
st.header('NutriPro with Google Gemini')

# Avoid using 'input' as a variable name to prevent conflict with built-in function
user_input = st.text_input("Input prompt: ", key='user_input')
uploaded_file = st.file_uploader("Choose an image of the food or food table", type=["jpg", 'jpeg', 'png'])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Scan & Analyze")

input_prompt = """You have to identify different types of food in images. 
The system should accurately detect and label various foods displayed in the image, 
providing the name of the food and its location within the image (e.g., bottom left, right corner, etc.). 
Additionally, the system should extract nutritional information and 
categorize the type of food (e.g., fruits, vegetables, grains, etc.) based on the detected items. 
The output should include a comprehensive report or display showing the identified foods, their positions, names,
and corresponding nutritional details."""

if submit:
    try:
        image_data = input_image_setup(uploaded_file)  # Use correct function to get image data
        response = get_gemini_response(user_input, image_data, input_prompt)
        st.subheader("NutriPro Scan Results: ")
        st.write(response)
    except Exception as e:
        st.error(f"Error processing the image: {e}")

st.markdown("<small>© 2024 Harshith YVS. All rights reserved.</small>", unsafe_allow_html=True)

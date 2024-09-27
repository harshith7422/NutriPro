# NutriPro: Nutrition App Using Google Gemini Pro

**NutriPro** is a web application designed to analyze images of food items and provide comprehensive nutritional information. It leverages Google Gemini's generative AI to detect and label different foods, categorize them, and present nutritional facts for a healthier lifestyle.

## Features
- Upload images of food items or meals.
- Automatically identify different food types within the image.
- Display nutritional details such as calorie content and food categories (e.g., fruits, vegetables, grains).
- Generate a detailed report based on the detected items.

## Live Demo
Check out the hosted version of the application here:  
[**NutriPro on Streamlit**](https://nutripro.streamlit.app/)

## Getting Started

### Prerequisites
- Python 3.8+
- Google API Key for accessing Gemini Pro.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/nutripro.git
   cd nutripro
2. **Install Dependencies: Install the required Python packages by running:**
   ```bash
   pip install -r requirements.txt
3. **Set Up Environment Variables: Create a .env file in the project directory and add your Google API key:**
   ```bash
   GOOGLE_API_KEY="your-google-api-key"
4. **Run the App Locally: After setting up the environment and installing dependencies, you can run the app with Streamlit**
   ```bash
   streamlit run app.py
## Usage
- Upload an Image: Upload an image of the food or meal you want to analyze.
- Enter a Prompt: Type a brief prompt (optional) to describe the task.
- Analyze: Click the "Scan & Analyze" button, and NutriPro will process the image using the Gemini API and display the nutritional information.
## Technologies Used
- Streamlit: For building the user interface.
- Google Gemini: AI model for generating food recognition and nutritional data.
- Python: Core programming language.
- PIL (Pillow): For image processing.
- dotenv: To manage environment variables.
## Results
![image](https://github.com/user-attachments/assets/cf80bf0b-9211-4e72-9015-a436307c1417)
![image](https://github.com/user-attachments/assets/e1a827d9-e561-46ed-80f5-6f899b0ed3b9)
![image](https://github.com/user-attachments/assets/48b8956d-f2df-4317-a13d-62fb09c1c3e6)


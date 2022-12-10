from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code !=200:
		return None
	return r.json()

# --USE LOCAL CSS--

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("C:/Users/purva/OneDrive/Desktop/website/style.css")		


# ---LOAD ASSETS---

lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json")
image_project1 = Image.open("C:/Users/purva/OneDrive/Desktop/website/images/images1.png")
image_project2 = Image.open("C:/Users/purva/OneDrive/Desktop/website/images/image2.png")

#---- HEADER SECTION -----

st.subheader("Hi, I am Purva :wave:")
st.title("A Data Enthusiast")
st.write("I am Passionate About Data Science And Machine Learning")
st.write("[here is the link to my Github profile>](https://github.com/purvaa0104)")


# ----WHAT I DO ----
with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("About Me")
		st.write("##")
		st.write(
			"""
			I am driven and curious about solving complex problems.
			I leverage my skills in data science and machine learning daily with also understanding the mathematics involved.
			Additionally, I enjoy reading books and research papers.
			"""
			)

		with right_column:
			st_lottie(lottie_coding, height=500, key ="coding")


# ---PROJECTS---
with st.container():
	st.write("---")
	st.header("My Projects")
	st.subheader("Project1")
	st.write('##')
	image_column, text_column = st.columns((1, 2))
	with image_column:
		st.image(image_project1)

	with text_column:
		st.subheader("Project1 : Book Price prediction")
		st.write(
			"""In this project, we predict the price of books based on given features,
			    using the Book Price dataset from Kaggle.
			   The performance of each model is compared and the best model is selected
			   """
			   ) 
		st.markdown("[here is my project](https://github.com/purvaa0104/Book_price_Prediction)")


# --PROJECT2

with st.container():
	st.write("---")
	st.header("Project2")
	st.write('##')
	image_column, text_column = st.columns((1, 2))
	with image_column:
		st.image(image_project2)

	with text_column:
		st.subheader("Project2 : Customer Segmentation")
		st.write(
			"""Segmentation of customers based on RFM SCORES with the help of RFM analysis. 
			which can give the company a lot of insights on what are the most important customers, 
			Which of your customers are most likely to respond to engagement campaigns, which of your customers can be retained, etc
			   """
			   ) 
		st.markdown("[here is my project](https://github.com/purvaa0104/Customer_segmentation)")


#--CONTACT--
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
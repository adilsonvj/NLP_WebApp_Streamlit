import streamlit as st

st.title("This is a Title")

st.header("This is a Header")

st.subheader("This is a Subheader")

st.text("Lorem Ipsum, Lorem Ipsum, Lorem Ipsum, Lorem Ipsum, Lorem Ipsum, Lorem Ipsum, Lorem Ipsum, ")

st.markdown("## This is a Markdown")

st.success("This is a Success message")

st.info("This is a information message")

st.warning("This is a warning message")

st.error("This is a error message")

st.exception("Is is a EXCEPTION")

st.help(range)

from PIL import Image

img = Image.open("example.JPG")

st.image(img, width = 300, caption = "Simple Image")

vid_file = open("example.mp4", "rb").read()

st.video(vid_file)

if st.checkbox("Show/Hide"):
    st.text("Show something")

status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success("You are active")
else:
    st.warning("Inactive")


occupation = st.selectbox("Your occupation is:", ["Programmer", "DS", "DE"])
st.write("You selected this option", occupation)

location = st.multiselect("where do you work?", ("London", "Paris", "Sao Paulo"))
st.write("You selected", len(location), "locations")

level = st.slider("what is your level", 1, 5)

st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is cool")

# firstname = st.text_input("Enter you firstname", "type here.. ")
# if st.button("Submit"):
#     result = firstname.title()
#     st.success(result)


message = st.text_area("Enter you firstname", "type here.. ")
if st.button("Submit"):
    result = message.title()
    st.success(result)

import datetime
today = st.date_input("Today is", datetime.datetime.now())

the_time = st.time_input("The time is ", datetime.time())

st.text("Display JSON")
st.json({'name' : "Jesse", 'gender':'male'})

st.text("Display Raw Code")
st.code("Import numpy as np")

with st.echo():
    import pandas as pd
    df = pd.DataFrame()

import time
my_bar = st.progress(0)

for p in range(100):
    my_bar.progress(p + 1)

with st.spinner("Waiting.. "):
    time.sleep(5)
st.success("Finished!")

st.balloons()

st.sidebar.header("About")
st.sidebar.text("This is streamlist ")
def run_fxn():
    return range(100)

st.write(run_fxn())

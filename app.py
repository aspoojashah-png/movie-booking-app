import streamlit as st
import pandas as pd
import random

# Background styling
st.markdown("""
<style>
.stApp {
background: linear-gradient(to right,#ff9a9e,#fad0c4,#fbc2eb,#a18cd1);
}

h1{
text-align:center;
color:#2c3e50;
}

.ticket{
background:white;
padding:20px;
border-radius:15px;
border:3px dashed black;
box-shadow:0px 4px 10px gray;
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 Smart Movie Theatre Booking System")

name = st.text_input("Enter Your Name")

df = pd.read_csv("movies.csv")

genre = st.selectbox("🎭 Choose Movie Genre", df["Genre"].unique())

movies = df[df["Genre"]==genre]

st.subheader("🍿 Available Movies")

for i,row in movies.iterrows():

    st.image(row["Image"], width=200)

    st.write("🎬 Movie:",row["Movie"])
    st.write("🏢 Theatre:",row["Theatre"])
    st.write("⏰ Showtime:",row["Showtime"])
    st.write("💰 Price: ₹",row["Price"])

    if st.button("🎟 Book Ticket",key=i):

        ticket_id=random.randint(1000,9999)

        st.markdown('<div class="ticket">',unsafe_allow_html=True)

        st.success("Ticket Booked Successfully!")

        st.write("👤 Name:",name)
        st.write("🎟 Ticket ID:",ticket_id)
        st.write("🎬 Movie:",row["Movie"])
        st.write("🏢 Theatre:",row["Theatre"])
        st.write("⏰ Showtime:",row["Showtime"])
        st.write("💰 Price: ₹",row["Price"])

        st.markdown('</div>',unsafe_allow_html=True)
import streamlit as st

st.title("Movie Ticket Booking System")

customer_name = st.text_input("Customer Name")
movie_title = st.selectbox("Movie Title", ["Avengers", "Kung Fu Panda", "Frozen"])
show_time = st.selectbox("Show Time", ["10:00 AM", "2:00 PM", "8:00 PM"])
seat_type = st.radio("Seat Type", ["Standard", "Premium"])

if st.button("Book Ticket"):
    try:
        if not customer_name or not customer_name.strip():
            st.error("Customer name cannot be empty!")
        else:
            st.success("Ticket booked successfully!")
            ----- Booking Summary -----
            st.write(f"**Customer:** {customer_name}")
            st.write(f"**Movie:** {movie_title}")
            st.write(f"**Show Time:** {show_time}")
            st.write(f"**Seat Type:** {seat_type}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")

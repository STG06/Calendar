
import streamlit as st
from streamlit_calendar import Calendar

st.title("Suleyman's Calendar")

if "events" not in st.session_state:
    st.session_state.events = []

with st.form("Add Event"):
    st.write("Add an event")
    title = st.text_input("Title")
    date = st.text_input("Date")
    time = st.text_input("Time")
    add = st.form_submit_button("Add Event")

    if add:
        new_event = {
            "title": title,
            "start": date.isoformat() + (f"T{time.isoformat()}" if time else ""),
        }
        st.session_state.events.append(new_event)
        st.success(f"Event '{title}' added successfully!")

calendar1 = Calendar(
    initial_view="dayGridMonth",
    events=st.session_state.events,
    default_date="2025-01-01",  # Start the calendar on January 2025
)

selectedEvent = calendar1.show()

if selectedEvent:
    st.write("Event Details")
    st.json(selectedEvent)

st.subheader("All Events")
st.json(st.session_state.events)

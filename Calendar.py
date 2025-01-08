
import streamlit as st
from streamlit_calendar import calendar

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
        if title and date:
            new_event = {
                "title": title,
                "start": date.isoformat() + (f"T{time.isoformat()}" if time else ""),
            }
            st.session_state.events.append(new_event)
            st.success(f"Event '{title}' added successfully!")
        else:
            st.error("Please input a title and date")

calendar_options = {
    "editable": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth,dayGridWeek,dayGridDay",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "dayGridMonth",
}

# Display the calendar with events
calendar_instance = calendar(
    events=st.session_state.events,  # Use the events from session state
    options=calendar_options,
)

# Display the calendar in the Streamlit app
st.write(calendar_instance)

# Display all events in session state
st.subheader("All Events")
st.json(st.session_state.events)

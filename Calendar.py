import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime, time

st.title("Suleyman's Calendar")

# Initialize session state
if "events" not in st.session_state:
    st.session_state.events = []

with st.form("Add Event"):
    st.write("Add an event")
    title = st.text_input("Title")
    date_input = st.text_input("Date (YYYY-MM-DD)")
    time_input = st.text_input("Time (HH:MM) Optional")
    add = st.form_submit_button("Add Event")

    if add:
        if title and date_input:
            try:
                # Parse the date
                parsed_date = datetime.strptime(date_input, "%Y-%m-%d").date()
                
                # Parse the time (if provided)
                if time_input:
                    parsed_time = datetime.strptime(time_input, "%H:%M").time()
                    start = f"{parsed_date}T{parsed_time}"
                else:
                    start = f"{parsed_date}"
                
                # Create the event
                new_event = {
                    "title": title,
                    "start": start,
                }
                st.session_state.events.append(new_event)
                st.success(f"Event '{title}' added successfully!")
            except ValueError:
                st.error("Invalid date or time format. Please follow the format YYYY-MM-DD for the date and HH:MM for the time.")
        else:
            st.error("Please input a title and date.")

# Calendar configuration
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

calendar_instance = calendar(
    events=st.session_state.events,
    options=calendar_options,
)

st.write(calendar_instance)

st.subheader("All Events")
st.json(st.session_state.events)

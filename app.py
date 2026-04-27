import streamlit as st

st.title("✅ Simple To-Do List")

# 1. Initialize the list in session_state if it doesn't exist yet
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
//  this is my fist project
# 2. Input field for a new task
new_task = st.text_input("Add a new task:", placeholder="Type something and press Enter...")

if st.button("Add Task"):
    if new_task:
        # Add task as a dictionary with 'task' name and 'done' status
        st.session_state.tasks.append({"name": new_task, "done": False})
        st.rerun()  # Refresh the page to show the new task immediately
    else:
        st.warning("Please enter a task name.")

# 3. Display the list of tasks
st.write("---")
st.subheader("Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet. Add one above!")

# Iterate through tasks to display them
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    
    # Checkbox for marking as done
    is_done = col1.checkbox(task['name'], value=task['done'], key=f"task_{i}")
    st.session_state.tasks[i]['done'] = is_done
    
    # Delete button for each task
    if col2.button("Delete", key=f"del_{i}"):
        st.session_state.tasks.pop(i)
        st.rerun()

# 4. Clear all button
if st.session_state.tasks:
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.rerun()

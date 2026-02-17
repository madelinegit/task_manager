import streamlit as st
import pandas as pd
import os

st.title("Ai Bot Creation")
DATA_FOLDER = "data"


# ---------- Helper functions ----------
def load_data(file, columns):
    path = os.path.join(DATA_FOLDER, file)
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        return pd.DataFrame(columns=columns)

def save_data(df, file):
    path = os.path.join(DATA_FOLDER, file)
    df.to_csv(path, index=False)


def delete_row(df, index):
    df = df.drop(index).reset_index(drop=True)
    return df


# ---------- Tabs ----------
tab1, tab2, tab3, tab4 = st.tabs([
    "Social Media",
    "Character Bio",
    "LLC Tasks",
    "Coding"
])

# ---------- SOCIAL MEDIA ----------
with tab1:
    st.header("Social Media Planner")

    FILE = "social_media.csv"
    data = load_data(FILE, ["Idea"])

    idea = st.text_input("Post idea or plan")

    if st.button("Add Idea"):
        new_row = pd.DataFrame([[idea]], columns=["Idea"])
        data = pd.concat([data, new_row], ignore_index=True)
        save_data(data, FILE)
        st.success("Saved")

    st.subheader("Ideas")
    for i, row in data.iterrows():
        col1, col2 = st.columns([6,1])
        col1.write(row["Idea"])
        if col2.button("Delete", key=f"social{i}"):
            data = delete_row(data, i)
            save_data(data, FILE)
            st.experimental_rerun()


# ---------- CHARACTER BIO ----------
with tab2:
    st.header("Character Bio")

    FILE = "character_bio.csv"
    data = load_data(FILE, ["Bio"])

    bio = st.text_area("Character details")

    if st.button("Save Bio"):
        new_row = pd.DataFrame([[bio]], columns=["Bio"])
        data = pd.concat([data, new_row], ignore_index=True)
        save_data(data, FILE)
        st.success("Saved")

    st.subheader("Saved Bios")
    for i, row in data.iterrows():
        col1, col2 = st.columns([6,1])
        col1.write(row["Bio"])
        if col2.button("Delete", key=f"bio{i}"):
            data = delete_row(data, i)
            save_data(data, FILE)
            st.experimental_rerun()


# ---------- LLC TASKS ----------
with tab3:
    st.header("LLC To-Do List")

    FILE = "llc_tasks.csv"
    data = load_data(FILE, ["Task"])

    task = st.text_input("Task")

    if st.button("Add Task"):
        new_row = pd.DataFrame([[task]], columns=["Task"])
        data = pd.concat([data, new_row], ignore_index=True)
        save_data(data, FILE)
        st.success("Saved")

    st.subheader("Tasks")
    for i, row in data.iterrows():
        col1, col2 = st.columns([6,1])
        col1.write(row["Task"])
        if col2.button("Delete", key=f"task{i}"):
            data = delete_row(data, i)
            save_data(data, FILE)
            st.experimental_rerun()


# ---------- CLIPBOARD ----------
with tab4:
    st.header("Clipboard")

    FILE = "clipboard.csv"
    data = load_data(FILE, ["Note"])

    note = st.text_area("Quick note")

    if st.button("Save Note"):
        new_row = pd.DataFrame([[note]], columns=["Note"])
        data = pd.concat([data, new_row], ignore_index=True)
        save_data(data, FILE)
        st.success("Saved")

    st.subheader("Saved Notes")
    for i, row in data.iterrows():
        col1, col2 = st.columns([6,1])
        col1.write(row["Note"])
        if col2.button("Delete", key=f"clip{i}"):
            data = delete_row(data, i)
            save_data(data, FILE)
            st.experimental_rerun()

import streamlit as st
from interviewer import ask_interview

st.set_page_config(page_title="AI Interviewer Bot")
st.title("🎤 AI Interviewer Bot")

field = st.selectbox(
    "Choose interview field",
    ["AI/ML", "Web Development", "Data Science", "HR", "Marketing"]
)

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your Answer")

if st.button("Send"):

    if user_input:

        st.session_state.history.append(
            {"role": "user", "content": user_input}
        )

        reply = ask_interview(field, st.session_state.history)

        st.session_state.history.append(
            {"role": "assistant", "content": reply}
        )

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.write("🧑 You:", msg["content"])
    else:
        st.write("🤖 Interviewer:", msg["content"])
import streamlit as st
from api import discuss_ideas

st.title('Idea Discussion')
st.subheader('Discuss your selected Idea with a Senior Mentor')

if "selected_idea" not in st.session_state:
    st.warning('No idea selected')
    st.stop()


idea = st.session_state['selected_idea']
user_info = st.session_state['user_info']

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

st.subheader(idea["title"])
st.write(idea["problem_statement"])

for msg in st.session_state["chat_history"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask about this project...")

if user_input:
    st.session_state["chat_history"].append({
        "role": "user",
        "content": user_input
    })

    payload = {
        "idea": idea,
        "skill_level": user_info["skill_level"],
        "career_goal": user_info["career_goal"],
        "history": st.session_state["chat_history"][-5:],
        "user_message": user_input
    }

    with st.spinner('Thinking...'):
        response = discuss_ideas(payload)
    data = response.json()
    assistant_reply = data["response"]

    st.session_state["chat_history"].append({
        "role": "assistant",
        "content": assistant_reply
    })

    st.rerun()

if st.button('<- Back to Ideas'):
    st.switch_page('./pages/1_Generator.py')
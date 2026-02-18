import streamlit as st
from api import generate_ideas


st.title('Get Awesome Project Ideas',text_alignment='center')
st.subheader('Enter your skill proficiency, interested domain and long term career goal to get the best project ideas..',text_alignment='center')
c1,c2,c3 = st.columns(3)

with c1:
    skill_level = st.selectbox("**Skill Level**",['begineer','intermediate','advanced'],)
with c2:
    domain = st.text_input('**Domain**',help='Comma separated values')
with c3:
    career_goal = st.text_input("**Career Goal**",help='Comma separated values')

if st.button('Generate Ideas',use_container_width=True):
    payload = {
        'skill_level':skill_level,
        'domain':domain,
        'career_goal':career_goal
    }

    with st.spinner("Generating Ideas....",show_time=True,width='stretch'):
        response = generate_ideas(payload)
    data = response.json()
    st.session_state['ideas'] = data['ideas'] ##list of Idea
    st.session_state['user_info'] = payload

if "ideas" in st.session_state:
    st.divider()
    st.header('Viable Ideas',text_alignment='center')
    n_ideas = len(st.session_state['ideas']) ##number of ideas
    all_cols = st.columns(n_ideas)
    for i, idea in enumerate(st.session_state['ideas']):
        with all_cols[i]:
            with st.container():
                st.subheader(idea['title'],text_alignment='center',divider=True)
                st.write(idea['problem_statement'])

                if st.button(f"Discuss Idea",key=f"discuss_{i}"):
                    st.session_state['selected_idea'] = idea
                    st.switch_page('./pages/2_Conversation.py')
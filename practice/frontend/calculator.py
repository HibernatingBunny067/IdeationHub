import streamlit as st

operation2sym = {
    'Addition':'+',
    'Subtraction':'-',
    'Multiplication':'*',
    'Division':'/'
}

def calculate(a:float,b:float,operation:str):
    ans = 0
    match operation:
        case "Addition":
            ans = a+b
        case "Subtraction":
            ans = a-b
        case "Multiplication":
            ans = a*b
        case "Division":
            if b == 0:
                st.warning('Division by Zero')
                return None
            ans = a/b
    return ans


st.title("Basic Calculator")
st.set_page_config(page_title="Calculator", page_icon="🧮")
st.header('Perform Calculations')

if "history" not in st.session_state:
    st.session_state.history = []

col1,col2 = st.columns(2)

with col1:
    a = st.number_input('Input first number')
with col2:
    b = st.number_input('Input second number')
operation = st.radio('Choose operation',["Addition","Subtraction","Multiplication","Division"],horizontal=True)

done = st.button('Calculate')

if done:
    ans = calculate(a,b,operation)
    if ans is not None:
        st.success(f'Answer: {ans:.5f}')
        entry = f"{a} {operation2sym.get(operation)} {b} = {ans:.5f}"
        st.session_state.history.insert(0,entry)
        st.session_state.history = st.session_state.history[:5]
        st.header('History')

if st.session_state.history:
    st.subheader('Last 5 calculations')      
    for h in st.session_state.history:
        st.write(h)


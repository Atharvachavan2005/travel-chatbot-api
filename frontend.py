import streamlit as st
import requests

st.set_page_config(page_title="TravelBot Chat", page_icon="✈️", layout="centered")
st.title("✈️ TravelBot - Travel Agency Assistant")

st.markdown("""
Welcome to TravelBot! Ask any travel-related question and get instant answers based on our knowledge base and AI expertise.
""")

API_URL = "http://localhost:8000/chat"

query = st.text_input("Enter your question:", "")

if st.button("Ask") or (query and st.session_state.get("last_query") != query):
    if query:
        st.session_state["last_query"] = query
        with st.spinner("Getting answer..."):
            try:
                response = requests.post(API_URL, json={"query": query})
                if response.status_code == 200:
                    answer = response.json().get("response", "No answer returned.")
                    st.success(answer)
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Error contacting backend: {e}") 
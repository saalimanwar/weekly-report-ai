import openai
import pandas as pd
import streamlit as st
from openai import OpenAI

# Setup your OpenAI API key here
client = OpenAI(api_key="")

st.set_page_config(page_title="Weekly Status AI Generator", layout="centered")
st.title("AI Weekly Status Report Generator")

uploaded_file = st.file_uploader("Upload your weekly task CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of your tasks")
    st.dataframe(df)

    # Clean and format task input
    task_list = "\n".join([f"- {row['Task']} ({row['Status']})" for idx, row in df.iterrows()])

    # Prompt to OpenAI
    prompt = f"""
    You are an assistant that helps professionals write a weekly status update.
    Given the following list of tasks, generate a professional, concise weekly update.

    Tasks:
    {task_list}

    Summary:
    """

    if st.button("Generate Weekly Summary"):
        with st.spinner("Generating summary..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                temperature=0.5,
                messages=[{"role": "user", "content": prompt}]
            )
            summary = response['choices'][0]['message']['content']
            st.success("Summary generated!")
            st.text_area("Weekly Summary", value=summary, height=300)

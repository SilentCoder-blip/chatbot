import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Set up the Streamlit app
st.title("AI and Computer Science Chatbot")
st.write("Ask any question related to artificial intelligence or computer science!")

# Input for user's question
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question:
        with st.spinner("Thinking..."):
            # Call OpenAI model
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an AI chatbot expert in artificial intelligence and computer science."},
                        {"role": "user", "content": question}
                    ]
                )

                answer = response.choices[0].message['content']
                st.write("Answer:", answer)

            except Exception as e:
                st.error("An error occurred. Please check your API key or try again later.")
    else:
        st.warning("Please enter a question.")

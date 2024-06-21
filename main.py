import streamlit as st
import requests

# Streamlit App title and description
st.title('Text Summarizer App')

# API endpoint
API_URL = 'http://localhost:11434/api/generate'

# HTML template for dynamic textarea resizing
html_template = """
<style>
#user_input {
    height: auto;
    min-height: 200px; /* Set a minimum height */
    resize: vertical; /* Allow vertical resizing */
    overflow-y: scroll; /* Add a scrollbar when needed */
    font-size: 16px; /* Set default font size */
}
</style>
<script>
function resizeTextarea() {
    var textarea = document.getElementById('user_input');
    textarea.style.height = 'auto'; // Reset height to auto
    textarea.style.height = (textarea.scrollHeight) + 'px'; // Set new height based on content
}
</script>
"""

# Inject HTML template into the Streamlit app
st.markdown(html_template, unsafe_allow_html=True)

# Input box for user to enter text
user_input = st.text_area("Enter text to summarize:", height=200, key='user_input')

if st.button("Summarize"):
    if user_input:
        # Display loading indicator
        with st.spinner('Generating summary...'):
            # Prepare payload for API request
            payload = {
                "model": "llama3",
                "prompt": "Summarize the content: " + user_input,
                "stream": False
            }

            # Send POST request to API
            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    # Parse the JSON response
                    json_response = response.json()

                    # Extract the summarized text from the response
                    if 'response' in json_response:
                        summary = json_response['response']
                        st.subheader("Summary:")
                        st.write(summary)
                    else:
                        st.error("Error: Could not find summary in API response.")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching data: {e}")
    else:
        st.warning("Please enter some text to summarize.")

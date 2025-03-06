import streamlit as st
from lamini import Lamini
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch Lamini API key
try:
    api_key = os.getenv("LAMINI_API_KEY")
    if not api_key:
        raise ValueError("LAMINI_API_KEY not found in environment variables.")
    Lamini.api_key = api_key
except Exception as e:
    st.error(f"Error loading Lamini API Key: {e}")
    raise e

# Initialize the fine-tuned Lamini model
try:
    llm = Lamini(model_name="8b11ee2058ec232b293a8fcbf798841c34a2a1efc19698ae1ef3682722046b18")
except Exception as e:
    st.error(f"Error loading fine-tuned model: {e}")
    raise e

# Centralized image path
IMAGE_PATH = "Untitled design (1).png"  # Update this to the correct path


# Define the Streamlit app
def main():
    # Set up page configuration
    st.set_page_config(
        page_title="CysterCare - Your PCOS Support Partner",
        page_icon="🤖",
        layout="wide",
    )

    # Title and subtitle
    st.markdown(
        "<h1 style='color: #070F2B; text-align: center; font-family: Helvetica;'>CysterCare PCOS Help Companion</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h4 style='color: #C14600; text-align: center; font-family: Trebuchet MS;'>Empowering Women with Knowledge and Support for PCOS</h4>",
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Display main image
    st.image(IMAGE_PATH, width=150, use_container_width=True)

    # Sidebar
    with st.sidebar:
        st.markdown(
            "<h3 style='color: #C14600; text-align: center; font-family: Trebuchet MS;'>Welcome to CysterCare</h3>",
            unsafe_allow_html=True,
        )
        st.write("Empowering Women with Knowledge and Support for PCOS")
        mode = st.radio("Select Mode:", ["Latest Updates", "Chat with CysterCare"])
        st.checkbox("Show Basic Interactions", value=True)
        st.markdown(
            """
            <ul style='font-size: 14px; font-family: Arial;'>
            <li><strong>Ask About PCOS:</strong> Type your questions for personalized support.</li>
            <li><strong>Learn About CysterCare:</strong> Stay updated on features and improvements.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # Main content
    st.markdown(
        "<h2 style='color: #070F2B; font-family: Helvetica;'>Hi, I'm Ada, your PCOS Expert!</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='font-size: 16px; font-family: Arial; color: #070F2B;'>"
        "I'm here to guide you in understanding and managing PCOS effectively. "
        "Whether it's about symptoms, treatments, lifestyle changes, or anything else, feel free to ask your questions. "
        "Together, we can navigate the journey to better health and well-being."
        "</p>",
        unsafe_allow_html=True,
    )

    # Input for user queries
    st.markdown("### 💡 Curious about PCOS? Let's chat!")
    user_input = st.text_input("What's on your mind?", placeholder="Type your question here...")

    # Submit button and response display
    if st.button("Submit"):
        user_input = user_input.strip()  # Clean user input
        if user_input:
            response = process_query(user_input)  # Get response
            st.markdown(
                f"<p style='font-size: 16px; font-family: Arial; color: #070F2B;'>"
                f"<strong>Response:</strong> {response}</p>",
                unsafe_allow_html=True,
            )
        else:
            st.warning("Please enter a question before submitting.")


# Function to process user queries
def process_query(user_input):
    try:
        response = llm.generate(user_input)
        return response
    except Exception as e:
        return f"Error generating response: {e}"


# Run the app
if __name__ == "__main__":
    main()

# Display footer image with updated parameters
st.image(
    "pngwing.com (25).png",
    use_container_width=True,
    caption="Know it. Fight it. Manage it."
)

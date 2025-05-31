import streamlit as st
import speech_recognition as sr  # For voice recognition
import re  # For validation
from datetime import datetime

# Set Page Config
st.set_page_config(page_title="Bank Withdraw Form", layout="centered")

# Initialize session state variables
if "manual_input" not in st.session_state:
    st.session_state.manual_input = False
if "voice_input" not in st.session_state:
    st.session_state.voice_input = False
if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""  # Store spoken words

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: white;
            padding: 20px;
            border-radius: 10px;
            background: linear-gradient(90deg, #87CEEB, #4682B4);
            margin-bottom: 20px;
        }
        .stButton>button {
            width: 180px;
            height: 45px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            transition: 0.3s;
            background: #87CEEB;
            color: white;
            border: none;
        }
        .stButton>button:hover {
            background: #4682B4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header (Enlarged)
st.markdown('<p class="title">🏦 Bank Account Withdraw Form</p>', unsafe_allow_html=True)

# Toggle Buttons for Input Method
st.write("### Select Input Method:")
col1, col2 = st.columns(2)

if col1.button("📝 Manual Input"):
    st.session_state.manual_input = True
    st.session_state.voice_input = False

if col2.button("🎤 Use Voice Input"):
    st.session_state.voice_input = True
    st.session_state.manual_input = False
    st.info("🎙 Speak, and your words will be captured in real-time!")

# *Manual Input Section*
if st.session_state.manual_input:
    with st.form("deposit_form"):
        st.subheader("👤 Personal Details")

        col1, col2, col3 = st.columns(3)
        first_name = col1.text_input("First Name*", placeholder="Enter first name")
        middle_name = col2.text_input("Middle Name (Optional)", placeholder="Enter middle name")
        last_name = col3.text_input("Last Name*", placeholder="Enter last name")

        st.subheader("📞 Contact Details")
        contact_col1, contact_col2 = st.columns([1, 3])
        country_code = contact_col1.selectbox("Country Code", ["+91", "+1", "+44", "+61"])
        phone_number = contact_col2.text_input("Phone Number", placeholder="Enter 10-digit phone number")

        st.subheader("🏧 Account Details")
        account_number = st.text_input("🔑 Account Number", placeholder="Enter 12-digit account number")
        deposit_amount = st.text_input("💵 Deposit Amount", placeholder="Enter amount (₹)")

        st.subheader("📅 Date of Deposit")
        deposit_date = st.date_input("Select Date", value=datetime.today())

        notes = st.text_area("📝 Additional Notes (Optional)", placeholder="Any special instructions")

        # Validation
        errors = []
        if not first_name or not last_name:
            errors.append("🔴 Please enter both First and Last names.")
        if phone_number and (not phone_number.isdigit() or len(phone_number) != 10):
            errors.append("🔴 Phone number must be exactly 10 digits.")
        if account_number and (not account_number.isdigit() or len(account_number) != 12):
            errors.append("🔴 Account number must be exactly 12 digits.")
        if deposit_amount and not deposit_amount.isdigit():
            errors.append("🔴 Deposit amount must be a valid number.")

        # Submit button
        submit = st.form_submit_button("✅ Submit Deposit")

        if submit:
            if errors:
                for error in errors:
                    st.error(error)
            else:
                st.success("✅ Deposit request submitted successfully!")
                st.write(f"Account Holder: {first_name} {middle_name} {last_name}")
                st.write(f"Phone: {country_code} {phone_number}")
                st.write(f"Account Number: {account_number}")
                st.write(f"Amount: ₹{deposit_amount}")
                st.write(f"Date: {deposit_date}")

# *Voice Input Section*
elif st.session_state.voice_input:
    st.subheader("🎤 Voice Input")

    # Voice Recognition Function
    def recognize_speech():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎙 Listening... Speak now! (It will stop when you remain silent for 15 seconds)")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for noise

            try:
                # Listen continuously until 15 seconds of silence
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
                text = recognizer.recognize_google(audio)
                st.session_state.voice_text = text  # Store the recognized text
                st.success("✅ Voice captured successfully!")
            except sr.UnknownValueError:
                st.warning("⚠ Sorry, I couldn't understand the audio.")
            except sr.RequestError:
                st.error("🚫 Speech Recognition service is unavailable.")

    # Start Listening Button
    if st.button("🎙 Start Listening"):
        recognize_speech()

    # Display Recognized Voice Text
    voice_text = st.text_area("Voice Data", st.session_state.voice_text, height=100)

    # Process Voice Data Button
    if st.button("Process Voice Data"):
        if voice_text.strip():
            st.success("✅ Extracted Text:")
            st.write(f"🔹 {voice_text}")
        else:
            st.warning("⚠ No voice data captured. Please try again.")
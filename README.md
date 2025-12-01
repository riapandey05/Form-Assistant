🗣️ Voice-Activated Form Assistant

This project is designed to assist users who struggle with manual typing due to physical limitations, age-related issues, accessibility constraints, or simply because they prefer speaking over writing. It provides a hands-free, voice-driven solution for form filling in banking scenarios. The application includes two core form workflows — Deposit and Withdraw, and allows users to provide input in English, Hindi, or Odia, which is then processed and mapped to the correct form fields automatically. The goal is to make digital interaction more human, intuitive, and inclusive.

❗ Challenge Encountered

The biggest difficulty in building this system was extracting the correct entities from raw speech-to-text output — especially distinguishing between:

Amount

Account Number

Phone Number

Name

For example, in the spoken input:

“Deposit 5000 to account 981234567890 and my phone number is 9876543210”

We receive text containing multiple numeric sequences — and the system must correctly map:

5000 → Amount

981234567890 → Account Number

9876543210 → Phone Number

This was solved using Regex-based entity rules, such as:

10-digit pattern → Phone

12–14 digit sequence → Account Number

3–6 digit amount → Amount

Non-numeric text patterns → Name

🚀 Features

🎤 Voice input in Hindi, Odia, or English

🌐 Automatic translation to English

🔍 Reliable entity extraction using Regex + DistilBERT

🧠 Context-based field identification

🖥️ Streamlit interactive UI

♿ Accessibility-friendly

📝 Dedicated forms: Deposit & Withdraw

🔔 Real-time field mapping feedback

🛠️ Tech Stack
Component	Technology Used
Frontend	Streamlit
Speech Input	SpeechRecognition / Web Speech API
Translation	IndicTrans2 / Google Translate API
NLP Models	DistilBERT (fine-tuned), Regex
🧠 How It Works

User speaks in Hindi / Odia / English

Speech is converted to text

If required, text is translated to English

Regex detects structured numeric entities

DistilBERT extracts semantic entities such as name

Correct entities are auto-filled into the Deposit or Withdraw form

✨ Example Voice Inputs
Spoken Input	Extracted Entities
“मेरा नाम रिया पांडे है”	Name = Ria Pandey
“Transfer 1200 to account 551234789632, and my phone number is 9991123344”	Amount = 1200, Account = 551234789632, Phone = 9991123344
“ପିନ୍ କୋଡ୍ ୭୫୦୦୧୪ ଏବଂ ମୋ ଫୋନ୍ ୯୧୨୩୪୫୬୭୮୯ ”	Pincode = 750014, Phone = 9123456789
💻 How to Run
git clone https://github.com/your-username/voice-activated-form-assistant.git
cd voice-activated-form-assistant
pip install -r requirements.txt
streamlit run app.py

🧩 Future Enhancements

Support for Tamil, Bengali, Marathi

Add speaker identity verification

Database integration for form submissions

Text-to-Speech output for confirmation

Adaptive learning to improve entity extraction accuracy over time

👩‍💻 Author

Ria Pandey
B.Tech CSE | Machine Learning & NLP Enthusiast
📬 riapandey0805@gmail.com

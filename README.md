# 🗣️ Voice-Activated Form Assistant

A **multilingual, NLP-powered** voice-controlled application that enables users to fill out forms using speech input in **Hindi, Odia, or English**.

## 🚀 Features

* 🎤 **Voice input** in Hindi, Odia, or English  
* 🌐 **Automatic translation** of Hindi and Odia to English  
* 🤖 **NLP-based field recognition** using:  
  * `DistilBERT` for intent/entity extraction  
  * `Regex` for structured pattern matching  
* 🔁 Smart mapping from speech to form fields  
* 🖥️ **Streamlit-based frontend** for an interactive web UI  
* ♿ Accessibility-friendly design


## 🛠️ Tech Stack

| Component          | Technology Used                                 |
| ------------------ | ----------------------------------------------- |
| Frontend           | [Streamlit](https://streamlit.io/)              |
| Speech Input       | SpeechRecognition / Web Speech API              |
| Translation        | IndicTrans2 / Google Translate API              |
| NLP Models         | `DistilBERT` (fine-tuned), Regex rules          |

---

## 🧠 How It Works

1. **Speech Recognition** captures voice input in Hindi, Odia, or English.
2. **Translation module** converts Hindi and Odia inputs to English.
3. The input is processed using:

   * A **DistilBERT** model to extract field-specific intents and values.
   * **Regex patterns** to catch fixed phrases like emails, phone numbers, etc.
4. Extracted information is used to **auto-populate** form fields on the Streamlit UI.



---

## ✨ Example Voice Commands

| Spoken Input                    | Populated Field      |
| ------------------------------- | -------------------- |
| "मेरा नाम रिया पांडे है"        | Name = "Ria Pandey"  |
| "ପିନ୍ କୋଡ୍ ୭୫୦୦୧୪" (PIN code)   | Pincode = "750014"   |
| "My phone number is 9991123344" | Phone = "9991123344" |

---

## 💻 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/voice-activated-form-assistant.git
   cd voice-activated-form-assistant
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

---

## 📦 Requirements

* `streamlit`
* `transformers`
* `SpeechRecognition`
* `googletrans` or `indic-trans`
* `torch`
* `regex`
* `nltk`, `spacy` *(optional depending on enhancements)*

---

## 🧩 Future Enhancements

* Add more Indic languages (e.g., Tamil, Bengali)
* Bi-directional translation for confirmation
* Store submitted data in database
* Speech feedback using Text-to-Speech

---

## 👩‍💻 Author

**Ria Pandey**
🎓 B.Tech CSE | Machine Learning & NLP Enthusiast
📬(mailto:riapandey0805@gmail.com)

---

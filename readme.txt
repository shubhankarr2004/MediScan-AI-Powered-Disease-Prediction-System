# 🩺 MediScan: AI-Powered Disease Prediction System

> An interactive medical chatbot that predicts diseases from symptoms using **machine learning** and provides **descriptions & precautionary measures**.

---

## 🚀 Features
- ✅ **Symptom-Based Prediction**: Enter your symptoms (comma-separated) and get the most likely disease.  
- ✅ **Disease Information**: Fetch disease descriptions, symptoms, and recommended precautions.  
- ✅ **Dual Interface**:
  - **Command Line (CLI)** via `medbot.py`  
  - **Graphical User Interface (GUI)** via `frontline.py` (Tkinter)  
- ✅ **Machine Learning Models**:
  - Support Vector Machine (SVM)  
  - Naive Bayes (GaussianNB)  
  - Random Forest  
- ✅ **Majority Voting System** for robust predictions.  

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Libraries:**  
  - `numpy`  
  - `pandas`  
  - `scikit-learn`  
  - `tkinter` (built-in for GUI)  

---

## 📂 Project Structure
```
MedicalChatbot/
│── frontline.py              # GUI version with Tkinter
│── medbot.py                 # CLI version
│── Training.csv              # Dataset for training models
│── symptom_precaution.csv    # Precautionary measures
│── symptom_Description.csv   # Disease descriptions
```
---

## ⚡ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MedicalChatbot.git
   cd MedicalChatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or manually:
   ```bash
   pip install numpy pandas scikit-learn
   ```

3. Run the GUI version:
   ```bash
   python frontline.py
   ```

   Or run the CLI version:
   ```bash
   python medbot.py
   ```

---

## 🎯 Usage
### 🩺 Symptom-Based Prediction
- Enter symptoms as a comma-separated list.  
  Example:  
  ```
  itching, skin_rash, nodal_skin_eruptions
  ```

- Output:  
  - Predicted Disease  
  - Description  
  - Recommended Precautions  

### 🦠 Disease Details
- Enter a disease name to get:  
  - Description  
  - Common Symptoms  
  - Precautions  

---

## 📸 Screenshots (GUI)
> *(Add screenshots of your Tkinter windows here after running the app!)*

---

## 🔮 Future Enhancements
- Integration with **real-time medical APIs**.  
- Improved accuracy with **Deep Learning models**.  
- Voice-based symptom entry.  
- Web and mobile versions.  

---

## 👨‍💻 Author
Shubhankar Singh
📌 Connect on [LinkedIn](www.linkedin.com/in/shubhankarr) | 🐙 [GitHub](https://github.com/shubhankarr2004)  

---

⚡ *Disclaimer: This project is for **educational purposes only** and should not be used as a substitute for professional medical advice.*  

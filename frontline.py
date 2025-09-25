import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import statistics

# Load data
data = pd.read_csv("Training.csv").dropna(axis=1)
precaution_data = pd.read_csv("symptom_precaution.csv")
description_data = pd.read_csv("symptom_Description.csv")

# Encode target values
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Split data
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

# Train models
final_svm_model = SVC()
final_nb_model = GaussianNB()
final_rf_model = RandomForestClassifier(random_state=18)

final_svm_model.fit(X, y)
final_nb_model.fit(X, y)
final_rf_model.fit(X, y)

# Symptom index
symptoms = X.columns.values
symptom_index = { " ".join([i.capitalize() for i in value.split("_")]): index for index, value in enumerate(symptoms) }

data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": encoder.classes_
}

# Prediction function
def predictDisease(symptoms):
    symptoms = symptoms.split(", ")
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        symptom = " ".join([i.capitalize() for i in symptom.split("_")])
        if symptom in data_dict["symptom_index"]:
            input_data[data_dict["symptom_index"][symptom]] = 1
        else:
            messagebox.showerror("Error", f"Symptom '{symptom}' not found.")
            return None

    input_data = np.array(input_data).reshape(1, -1)
    input_data_df = pd.DataFrame(input_data, columns=X.columns)

    rf_prediction = final_rf_model.predict(input_data_df)[0]
    nb_prediction = final_nb_model.predict(input_data_df)[0]
    svm_prediction = final_svm_model.predict(input_data_df)[0]

    rf_disease = data_dict["predictions_classes"][rf_prediction]
    nb_disease = data_dict["predictions_classes"][nb_prediction]
    svm_disease = data_dict["predictions_classes"][svm_prediction]

    final_prediction = statistics.mode([rf_disease, nb_disease, svm_disease])

    try:
        precautions = precaution_data[precaution_data["prognosis"] == final_prediction].iloc[0, 1:].dropna().values
        precaution_list = [p for p in precautions]
    except IndexError:
        precaution_list = ["No precautions available."]

    try:
        description = description_data[description_data["prognosis"] == final_prediction]["Description"].values[0]
    except IndexError:
        description = "No description available."

    return {
        "final_prediction": final_prediction,
        "precautions": precaution_list,
        "description": description
    }

# Disease details function
def getDiseaseDetails(disease):
    try:
        description = description_data[description_data["prognosis"] == disease]["Description"].values[0]
        disease_symptoms = []
        for symptom, index in data_dict["symptom_index"].items():
            if data[data["prognosis"] == encoder.transform([disease])[0]].iloc[0, index] == 1:
                disease_symptoms.append(symptom)
        precautions = precaution_data[precaution_data["prognosis"] == disease].iloc[0, 1:].dropna().values
        precaution_list = [p for p in precautions]
    except IndexError:
        description = "No description available."
        disease_symptoms = ["No symptoms found."]
        precaution_list = ["No precautions available."]

    return {
        "description": description,
        "symptoms": disease_symptoms,
        "precautions": precaution_list
    }

# Display results (scrollable)
def display_prediction():
    symptoms = symptom_entry.get()
    result = predictDisease(symptoms)
    if result:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"🩺 Predicted Disease: {result['final_prediction']}\n\n")
        result_text.insert(tk.END, f"📖 Description:\n{result['description']}\n\n")
        result_text.insert(tk.END, f"✅ Precautions:\n- " + "\n- ".join(result['precautions']))

def display_disease_details():
    disease = disease_entry.get()
    result = getDiseaseDetails(disease)
    if result:
        details_text.delete(1.0, tk.END)
        details_text.insert(tk.END, f"🦠 Disease: {disease}\n\n")
        details_text.insert(tk.END, f"📖 Description:\n{result['description']}\n\n")
        details_text.insert(tk.END, f"🔍 Symptoms:\n- " + "\n- ".join(result['symptoms']) + "\n\n")
        details_text.insert(tk.END, f"✅ Precautions:\n- " + "\n- ".join(result['precautions']))

# GUI windows
def open_symptom_prediction_window():
    symptom_window = tk.Toplevel(root)
    symptom_window.title("Symptom-Based Prediction")
    symptom_window.geometry("700x500")

    tk.Label(symptom_window, text="Enter Symptoms (comma-separated):", font=("Arial", 12, "bold")).pack(pady=10)
    global symptom_entry, result_text
    symptom_entry = tk.Entry(symptom_window, width=60, font=("Arial", 11))
    symptom_entry.pack(pady=10)

    submit_button = tk.Button(symptom_window, text="Predict Disease", command=display_prediction, font=("Arial", 11, "bold"), bg="#4CAF50", fg="white")
    submit_button.pack(pady=10)

    result_text = scrolledtext.ScrolledText(symptom_window, wrap=tk.WORD, width=80, height=15, font=("Arial", 11))
    result_text.pack(padx=10, pady=10)

def open_disease_details_window():
    details_window = tk.Toplevel(root)
    details_window.title("Disease Details")
    details_window.geometry("700x500")

    tk.Label(details_window, text="Enter Disease Name:", font=("Arial", 12, "bold")).pack(pady=10)
    global disease_entry, details_text
    disease_entry = tk.Entry(details_window, width=60, font=("Arial", 11))
    disease_entry.pack(pady=10)

    details_button = tk.Button(details_window, text="Get Disease Details", command=display_disease_details, font=("Arial", 11, "bold"), bg="#2196F3", fg="white")
    details_button.pack(pady=10)

    details_text = scrolledtext.ScrolledText(details_window, wrap=tk.WORD, width=80, height=15, font=("Arial", 11))
    details_text.pack(padx=10, pady=10)

# Main menu
def create_main_menu():
    global root
    root = tk.Tk()
    root.title("Disease Prediction System")
    root.geometry("500x400")

    tk.Label(root, text="🤖 Hi! I'm Wall-E, your health assistant!", font=("Arial", 16, "bold")).pack(pady=20)

    symptom_button = tk.Button(root, text="🩺 Symptom-Based Prediction", command=open_symptom_prediction_window, width=35, font=("Arial", 12), bg="#f0ad4e", fg="white")
    symptom_button.pack(pady=10)

    disease_button = tk.Button(root, text="🦠 Disease Details", command=open_disease_details_window, width=35, font=("Arial", 12), bg="#5bc0de", fg="white")
    disease_button.pack(pady=10)

    exit_button = tk.Button(root, text="❌ Exit", command=root.quit, width=35, font=("Arial", 12), bg="#d9534f", fg="white")
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_main_menu()

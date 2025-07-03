from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    symptoms = [s.lower() for s in data.get("symptoms", [])]

    # Combo Symptom Example Logic
    if "fever" in symptoms and "cough" in symptoms and "breathlessness" in symptoms:
        result = "COVID-19"
    elif "fever" in symptoms and "cough" in symptoms:
        result = "Flu"
    elif "fever" in symptoms and "rash" in symptoms and "fatigue" in symptoms:
        result = "Measles"
    elif "runny nose" in symptoms and "sneezing" in symptoms:
        result = "Allergy"
    elif "chest pain" in symptoms and "shortness of breath" in symptoms:
        result = "Heart Disease"
    elif "abdominal pain" in symptoms and "vomiting" in symptoms:
        result = "Food Poisoning"

    # Single Symptom Logic
    elif "fever" in symptoms:
        result = "Viral Infection"
    elif "cough" in symptoms:
        result = "Common Cold"
    elif "headache" in symptoms:
        result = "Migraine"
    elif "sore throat" in symptoms:
        result = "Throat Infection"
    elif "sneezing" in symptoms:
        result = "Allergy"
    elif "runny nose" in symptoms:
        result = "Allergy"
    elif "fatigue" in symptoms:
        result = "Anemia or Viral Infection"
    elif "nausea" in symptoms:
        result = "Food Poisoning"
    elif "vomiting" in symptoms:
        result = "Food Poisoning"
    elif "diarrhea" in symptoms:
        result = "Gastroenteritis"
    elif "abdominal pain" in symptoms:
        result = "Gastritis or Stomach Ulcer"
    elif "chest pain" in symptoms:
        result = "Heart Disease"
    elif "breathlessness" in symptoms:
        result = "Asthma"
    elif "chills" in symptoms:
        result = "Flu"
    elif "joint pain" in symptoms:
        result = "Arthritis"
    elif "rash" in symptoms:
        result = "Allergy or Measles"
    elif "muscle ache" in symptoms:
        result = "Flu"
    elif "dizziness" in symptoms:
        result = "Low Blood Pressure"
    elif "eye pain" in symptoms:
        result = "Conjunctivitis"
    elif "burning sensation" in symptoms:
        result = "Urinary Tract Infection"
    elif "back pain" in symptoms:
        result = "Muscle Strain"
    elif "sweating" in symptoms:
        result = "Fever or Hormonal Imbalance"
    elif "blurred vision" in symptoms:
        result = "Migraine or Eye Problem"
    elif "shortness of breath" in symptoms:
        result = "Asthma"
    elif "swollen glands" in symptoms:
        result = "Infection"
    elif "ear pain" in symptoms:
        result = "Ear Infection"
    else:
        result = "Unknown Illness"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(port=8000, debug=True)

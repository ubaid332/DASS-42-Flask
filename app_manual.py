from flask import Flask, render_template, request
import os
import joblib
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the model file
model_path = os.path.join(current_dir, 'models', 'myanxiety4.model')

# Load the DASS-42 model
#model = joblib.load(model_path)

@app.route('/', methods=['GET'])
def index_page():
 return render_template('index.html', questions=anxiety_questions)

# anxiety survey questions and options
anxiety_questions = [
    "I was aware of dryness of my mouth",
    "I experienced breathing difficulty (eg, excessively rapid breathing, breathlessness in the absence of physical exertion)",
    "I had a feeling of shakiness (eg, legs going to give way)",
    "I found myself in situations that made me so anxious I was most relieved when they ended",
]

@app.route('/anxiety', methods=['GET'])
def anxiety_form():
    return render_template('anxiety.html', questions=anxiety_questions)

@app.route('/anxiety_result', methods=['POST'])
def process_anxiety_form():
    
    responses = []
    for i in range(len(anxiety_questions)):
        response = int(request.form[str(i+1)])
        responses.append(response)

    # Make predictions using the loaded model
    # predicted_scores = model.predict([responses])
    # accuracy = accuracy_score([expected_scores], predicted_scores)

    # return render_template('anxiety_result.html', anxiety_score=predicted_scores[0], accuracy=accuracy)
    
    anxiety_score = sum(responses)*4

    if anxiety_score >= 0 and anxiety_score <= 7 :
        anxiety_severity = "Normal"
    elif anxiety_score >= 8 and anxiety_score <= 9:
        anxiety_severity = "Mild"
    elif anxiety_score >= 10 and anxiety_score <= 14 :
        anxiety_severity = "Moderate";
    elif anxiety_score >= 15 and anxiety_score <= 19 :
        anxiety_severity = "Severe"
    elif anxiety_score > 20:
        anxiety_severity = "Extremely Severe"
    else:
        anxiety_severity = "Invalid anxiety score"

    return render_template('anxiety_result.html', anxiety_score=anxiety_score, anxiety_severity=anxiety_severity)


# Construct the relative path to the model file
model_path = os.path.join(current_dir, 'models', 'mydepression4.model')

# Load the DASS-42 model
#model = joblib.load(model_path)

# depression survey questions and options
depression_questions = [
    "I couldn\'t seem to experience any positive feeling at all",
    "I just couldn\'t seem to get going",
    "I felt that I had nothing to look forward to",
    "I felt sad and depressed",
]

@app.route('/depression', methods=['GET'])
def depression_form():
    return render_template('depression.html', questions=depression_questions)

@app.route('/depression_result', methods=['POST'])
def process_depression_form():
    
    responses = []
    for i in range(len(depression_questions)):
        response = int(request.form[str(i+1)])
        responses.append(response)

    # Make predictions using the loaded model
    # predicted_scores = model.predict([responses])
    # accuracy = accuracy_score([expected_scores], predicted_scores)

    # return render_template('depression_result.html', depression_score=predicted_scores[0], accuracy=accuracy)
    
    depression_score = sum(responses)*4

    if depression_score >= 0 and depression_score <= 9 :
        depression_severity = "Normal"
    elif depression_score >= 10 and depression_score <= 13:
        depression_severity = "Mild"
    elif depression_score >= 14 and depression_score <= 20 :
        depression_severity = "Moderate";
    elif depression_score >= 21 and depression_score <= 27 :
        depression_severity = "Severe"
    elif depression_score > 28:
        depression_severity = "Extremely Severe"
    else:
        depression_severity = "Invalid depression score"

    return render_template('depression_result.html', depression_score=depression_score, depression_severity=depression_severity)


# Construct the relative path to the model file
model_path = os.path.join(current_dir, 'models', 'mystress4.model')

# Load the DASS-42 model
#model = joblib.load(model_path)

#stress survey questions and options
stress_questions = [
    "I found myself getting upset rather easily",
    "I felt that I was using a lot of nervous energy",
    "I found myself getting impatient when I was delayed in any way (eg, elevators, traffic lights, being kept waiting)",
    "I felt that I was rather touchy",
]

@app.route('/stress', methods=['GET'])
def stress_form():
    return render_template('stress.html', questions=stress_questions)

@app.route('/stress_result', methods=['POST'])
def process_stress_form():
    
    responses = []
    for i in range(len(stress_questions)):
        response = int(request.form[str(i+1)])
        responses.append(response)

    # Make predictions using the loaded model
    # predicted_scores = model.predict([responses])
    # accuracy = accuracy_score([expected_scores], predicted_scores)

    # return render_template('stress_result.html', stress_score=predicted_scores[0], accuracy=accuracy)
    
    stress_score = sum(responses)*4

    if stress_score >= 0 and stress_score <= 14 :
        stress_severity = "Normal"
    elif stress_score >= 15 and stress_score <= 18:
        stress_severity = "Mild"
    elif stress_score >= 19 and stress_score <= 25 :
        stress_severity = "Moderate";
    elif stress_score >= 26 and stress_score <= 33 :
        stress_severity = "Severe"
    elif stress_score > 34:
        stress_severity = "Extremely Severe"
    else:
        stress_severity = "Invalid depression score"

    return render_template('stress_result.html', stress_score=stress_score, stress_severity=stress_severity)



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import os
import joblib

app = Flask(__name__)

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the model file
anxiety_model_path = os.path.join(current_dir, 'models', 'anxiety-recommender.joblib')
depression_model_path = os.path.join(current_dir, 'models', 'depression-recommender.joblib')
stress_model_path = os.path.join(current_dir, 'models', 'stress-recommender.joblib')

# Load the DASS-42 model
anxiety_model = joblib.load(anxiety_model_path)
depression_model = joblib.load(depression_model_path)
stress_model = joblib.load(stress_model_path)

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

@app.route('/anxiety', methods=['POST'])
def process_anxiety_form():
    
    responses = []
    for i in range(len(anxiety_questions)):
        response = int(request.form[str(i+1)])
        responses.append(response)

    # Make predictions using the loaded anxiety_model
    predicted_severity = anxiety_model.predict([responses])

    return render_template('anxiety.html', severity=predicted_severity[0], questions=anxiety_questions)





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

@app.route('/depression', methods=['POST'])
def process_depression_form():
    
    responses = []
    for i in range(len(depression_questions)):
        response = int(request.form[str(i+1)])
        responses.append(response)

    # Make predictions using the loaded depression_model
    predicted_severity = depression_model.predict([responses])

    return render_template('depression.html', severity=predicted_severity[0], questions=depression_questions)



# stress survey questions and options
stress_questions = [
    "I found myself getting upset rather easily",
    "I felt that I was using a lot of nervous energy",
    "I found myself getting impatient when I was delayed in any way (eg, elevators, traffic lights, being kept waiting)",
    "I felt that I was rather touchy",
]

@app.route('/stress', methods=['GET'])
def stress_form():
    return render_template('stress.html', questions=stress_questions)

@app.route('/stress', methods=['POST'])
def process_stress_form():
    
    responses = []
    for i in range(len(stress_questions)):
        response = int(request.form[str(i+1)])
        responses.append(response)

    # Make predictions using the loaded stress_model
    predicted_severity = stress_model.predict([responses])

    return render_template('stress.html', severity=predicted_severity[0], questions=stress_questions)


@app.route('/dass12', methods=['GET'])
def dass_12_form():
    return render_template('dass12.html', anxiety_questions = anxiety_questions, depression_questions = depression_questions, stress_questions=stress_questions)

@app.route('/dass12', methods=['POST'])
def process_dass_12_form():
    
    #Predict Anxiety

    anxiety_responses = []
    for i in range(len(anxiety_questions)):
        anxiety_response = int(request.form['a'+str(i+1)])
        anxiety_responses.append(anxiety_response)

    # Make predictions using the loaded stress_model
    predicted_anxiety_severity = anxiety_model.predict([anxiety_responses])



    #Predict Depression
    
    depression_responses = []
    for i in range(len(depression_questions)):
        depression_response = int(request.form['d'+str(i+1)])
        depression_responses.append(depression_response)

    # Make predictions using the loaded depression_model
    predicted_depression_severity = depression_model.predict([depression_responses])


    #Predict Stress
    
    stress_responses = []
    for i in range(len(stress_questions)):
        stress_response = int(request.form['s'+str(i+1)])
        stress_responses.append(stress_response)

    # Make predictions using the loaded stress_model
    predicted_stress_severity = stress_model.predict([stress_responses])

    return render_template('dass12.html',anxiety_severity=predicted_anxiety_severity[0], depression_severity=predicted_depression_severity[0],stress_severity=predicted_stress_severity[0], anxiety_questions = anxiety_questions, depression_questions = depression_questions, stress_questions=stress_questions)

if __name__ == '__main__':
    app.run(debug=True)

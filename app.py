import pickle
from flask import Flask, render_template, request
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    # an array to store the user's input
    input = []
    scaler = MinMaxScaler()

    # age of the user
    age = int(request.form.get('age'))
    age = [[age]]
    age = scaler.fit_transform(age)
    age = age[0, 0]
    input.append(age)

    # gender of the user
    gender = int(request.form.get('gender'))
    input.append(gender)

    # user's family_history
    family_history = int(request.form.get('family-history'))
    input.append(family_history)

    # benefits for the user
    benefits = int(request.form.get('benefits'))
    input.append(benefits)

    # care_options for the user
    care_options = int(request.form.get('care-options'))
    input.append(care_options)

    # anonymity of the user
    anonymity = int(request.form.get('anonymity'))
    input.append(anonymity)

    # leave policy at user's workplace
    leave = int(request.form.get('leave'))
    input.append(leave)

    # work_interfere at user's workplace
    work_interfere = int(request.form.get('work-interfere'))
    input.append(work_interfere)

    print(model.predict([input]))
    prediction = model.predict_proba([input])
    output='{:.0f}'.format(prediction[0][1] * 100)

    if output >= str(50):
        return render_template('output.html', lineOne='YOU REQUIRE A TREATMENT PLAN.', lineTwo='PERCENTAGE OF MENTAL ILLNESS IS {}%.'.format(output))
    else:
        return render_template('output.html', lineOne='NO TREATMENT PLAN IS REQUIRED.', lineTwo='PERCENTAGE OF MENTAL ILLNESS IS {}%.'.format(output))

if __name__ == '__main__':
    app.run(debug=True)

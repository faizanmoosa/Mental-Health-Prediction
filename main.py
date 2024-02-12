import pickle
from flask import Flask, render_template, request
import numpy as np
from datetime import datetime

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
new_model = pickle.load(open('new_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    # an array to store the user's input
    input = []

    # age of the user
    age = int(request.form.get('age'))
    input.append(age)

    # gender of the user
    gender = int(request.form.get('gender'))
    input.append(gender)

    # user is self_employed or not
    self_employed = int(request.form.get('self-employed'))
    input.append(self_employed)

    # user's family_history
    family_history = int(request.form.get('family-history'))
    input.append(family_history)

    # work_interfere at user's workplace
    work_interfere = int(request.form.get('work-interfere'))
    input.append(work_interfere)

    # no_of_employees at user's workplace
    no_of_employees = int(request.form.get('no-of-employees'))
    input.append(no_of_employees)
    
    # remote_work by the user
    remote_work = int(request.form.get('remote-work'))
    input.append(remote_work)

    # is user's workplace a tech_company ?
    tech_company = int(request.form.get('tech-company'))
    input.append(tech_company)

    # leave policy at user's workplace
    leave = int(request.form.get('leave'))
    input.append(leave)

    # obs_consequence for the user
    obs_consequence = int(request.form.get('obs-consequence'))
    input.append(obs_consequence)

    # date_time of the user's input
    date_time = request.form.get('time-stamp')
    time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
    year = time.year
    input.append(year)
    month = time.month
    input.append(month)
    day = time.day
    input.append(day)
    hour = time.hour
    input.append(hour)
    minute = time.minute
    input.append(minute)

    # country of the user
    countries = np.zeros(46)
    country = int(request.form.get('country'))
    countries[country] = 1
    input.extend(countries)

    # american state of the user
    states = np.zeros(45)
    state = int(request.form.get('state'))
    if(state != -1):
        states[state] = 1
    input.extend(states)

    # benefits for the user
    benefits = np.zeros(3)
    benefit = int(request.form.get('benefits'))
    benefits[benefit] = 1
    input.extend(benefits)

    # care_options for the user
    care_options = np.zeros(3)
    care_option = int(request.form.get('care-options'))
    care_options[care_option] = 1
    input.extend(care_options)

    # wellness_program for the user
    wellness_programs = np.zeros(3)
    wellness_program = int(request.form.get('wellness-program'))
    wellness_programs[wellness_program] = 1
    input.extend(wellness_programs)

    # seek_help by the user
    seeks_help = np.zeros(3)
    seek_help = int(request.form.get('seek-help'))
    seeks_help[seek_help] = 1
    input.extend(seeks_help)

    # anonymity of the user
    anonymitys = np.zeros(3)
    anonymity = int(request.form.get('anonymity'))
    anonymitys[anonymity] = 1
    input.extend(anonymitys)

    # mental_health_consequence of the user
    mental_health_consequences = np.zeros(3)
    mental_health_consequence = int(request.form.get('mental-health-consequence'))
    mental_health_consequences[mental_health_consequence] = 1
    input.extend(mental_health_consequences)

    # phys_health_consequence of the user
    phys_health_consequences = np.zeros(3)
    phys_health_consequence = int(request.form.get('phys-health-consequence'))
    phys_health_consequences[phys_health_consequence] = 1
    input.extend(phys_health_consequences)

    # coworkers of the user
    coworkers_arr = np.zeros(3)
    coworkers = int(request.form.get('coworkers'))
    coworkers_arr[coworkers] = 1
    input.extend(coworkers_arr)

    # supervisor of the user
    supervisors = np.zeros(3)
    supervisor = int(request.form.get('supervisor'))
    supervisors[supervisor] = 1
    input.extend(supervisors)

    # mental_health_interview of the user
    mental_health_interviews = np.zeros(3)
    mental_health_interview = int(request.form.get('mental-health-interview'))
    mental_health_interviews[mental_health_interview] = 1
    input.extend(mental_health_interviews)

    # phys_health_interview of the user
    phys_health_interviews = np.zeros(3)
    phys_health_interview = int(request.form.get('phys-health-interview'))
    phys_health_interviews[phys_health_interview] = 1
    input.extend(phys_health_interviews)

    # mental_vs_physical of the user
    mental_vs_physical_vs = np.zeros(3)
    mental_vs_physical = int(request.form.get('mental-vs-physical'))
    mental_vs_physical_vs[mental_vs_physical] = 1
    input.extend(mental_vs_physical_vs)

    # let's predict
    # prediction = model.predict([input])
    # new_prediction = new_model.predict([input])
    # if(prediction[0] == 0 or new_prediction[0] == 0):
    #     return render_template('best.html')
    # else:
    #     return render_template('worst.html')

    prediction=model.predict_proba([input])
    output = '{:.0f}'.format(prediction[0][1] * 100)

    if output>str(50):
        return render_template('output.html', pred='YOU REQUIRE A TREATMENT PLAN AND THE PERCENTAGE OF MENTAL ILLNESS IS {}%.'.format(output))
    else:
        return render_template('output.html', pred='NO TREATMENT PLAN IS REQUIRED AND THE PERCENTAGE OF MENTAL ILLNESS IS {}%.'.format(output))

if __name__ == '__main__':
    app.run(debug=True)

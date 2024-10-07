from flask import Flask, render_template, request
import test_model
import numpy as np

app = Flask(__name__)

lst = ['itching', 'skin_rash', 'nodal_skin_eruptions',
       'sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze']

@app.route("/")
def disease():
    return render_template('disease.html', lst=lst, pred='', precaution='', desp='', test='', med='', dosage='')

@app.route("/form", methods=['POST'])
def form():
    Sym1 = request.form['Sym1']
    Sym2 = request.form['Sym2']
    Sym3 = request.form['Sym3']
    Sym4 = request.form['Sym4']
    Sym5 = request.form['Sym5']
    Sym6 = request.form['Sym6']

    
    
    if Sym1 == "Select Symptom 1":
        return render_template('disease.html', lst=lst , pred="Please select at least one valid symptom", precaution="None", desp="Not Available",confidence=0)

    lst2 = np.zeros((1, len(lst)))
    for i in range(len(lst)):
        if Sym1 == lst[i] or Sym2 == lst[i] or Sym3 == lst[i] or Sym4 == lst[i] or Sym5 == lst[i] or Sym6 == lst[i]:
            lst2[0][i] = 1.

    lst3 = [Sym1, Sym2, Sym3, Sym4, Sym5, Sym6]
    
    pred, confidence = test_model.pred(lst2)


    
    precaution = test_model.precaution(pred)
    desp = test_model.description(pred)
    
    print(lst3)
    lst3 = [sym for sym in lst3 if sym != "Open this select menu"]

    return render_template('disease.html', lst=lst, pred=pred, precaution=precaution, desp=desp, lst3=lst3, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True, port=8080)




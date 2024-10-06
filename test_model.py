import numpy as np
import pandas as pd
import tensorflow as tf

def pred(X):
    model = tf.keras.models.load_model("model.h5")
    
    # Preprocess input data X as needed (e.g., scaling, reshaping)
    # X_processed = preprocess_input(X)
    
    # Make predictions using the loaded model
    prediction = model.predict(X)
    
    disease_classes = {
        0: 'Fungal infection', 1: 'Allergy', 2: 'GERD', 3: 'Chronic cholestasis', 4: 'Drug Reaction',
        5: 'Peptic ulcer disease', 6: 'AIDS', 7: 'Diabetes', 8: 'Gastroenteritis', 9: 'Bronchial Asthma',
        10: 'Hypertension', 11: 'Migraine', 12: 'Cervical spondylosis', 13: 'Paralysis (brain hemorrhage)',
        14: 'Jaundice', 15: 'Malaria', 16: 'Chicken pox', 17: 'Dengue', 18: 'Typhoid', 19: 'hepatitis A',
        20: 'Hepatitis B', 21: 'Hepatitis C', 22: 'Hepatitis D', 23: 'Hepatitis E', 24: 'Alcoholic hepatitis',
        25: 'Tuberculosis', 26: 'Common Cold', 27: 'Pneumonia', 28: 'Dimorphic hemorrhoids (piles)',
        29: 'Heart attack', 30: 'Varicose veins', 31: 'Hypothyroidism', 32: 'Hyperthyroidism', 33: 'Hypoglycemia',
        34: 'Osteoarthritis', 35: 'Arthritis', 36: '(vertigo) Paroxysmal Positional Vertigo',
        37: 'Acne', 38: 'Urinary tract infection', 39: 'Psoriasis', 40: 'Impetigo'
    }
    
    # Get the predicted class index
    predicted_index = np.argmax(prediction)
    
    if predicted_index in disease_classes:
        predicted_disease = disease_classes[predicted_index]
        return predicted_disease, prediction[0][predicted_index]  # Return disease and confidence
    else:
        return 'could not predict', 0  # Unknown prediction


def precaution(X):
    main_df2 = pd.read_csv("symptom_precaution.csv")
    for i in range(len(list(main_df2['Disease']))):
        if main_df2['Disease'][i] == X:
            Y = (main_df2['Precaution_1'][i], main_df2['Precaution_2']
                 [i], main_df2['Precaution_3'][i])
    return Y


def description(X):
    main_df3 = pd.read_csv("symptom_Description.csv")
    for i in range(len(list(main_df3['Disease']))):
        if main_df3['Disease'][i] == X:
            Y = main_df3['Description'][i]
    return Y


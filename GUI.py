import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import plotly.graph_objects as go
import pickle
import pandas as pd

# Create the main window
window = tk.Tk()
window.title("Health Preduction Model ")
window.geometry("400x500")

# Set the background image
background_image = Image.open("download.jpg")
background_image = background_image.resize((400, 500), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the content
content_frame = ttk.Frame(window, width=350, height=450, style="Background.TFrame")
content_frame.place(x=25, y=25)

# Function to handle the button click event
def predict():
    # Retrieve values from the input fields
    bmi = bmi_entry.get()
    smoking = smoking_var.get()
    alcohol_drinking = alcohol_var.get()
    stroke = stroke_var.get()
    physical_health = physical_health_entry.get()
    mental_health = mental_health_entry.get()
    difficulty_walking = walking_var.get()
    sex = sex_var.get()
    age_category = age_var.get()
    race = race_var.get()
    diabetic = diabetic_var.get()
    physical_activity = activity_var.get()
    general_health = gen_health_var.get()
    sleep_time = sleep_entry.get()
    asthma = asthma_var.get()
    kidney_disease = kidney_var.get()
    skin_cancer = skin_cancer_var.get()


    pipe=pickle.load(open('pipe.pkl','rb'))
    preduct_value=pipe.predict(pd.DataFrame([[bmi,smoking,alcohol_drinking,stroke,physical_health,mental_health,difficulty_walking
    ,sex,age_category,race,diabetic,physical_activity,general_health,sleep_time,asthma,kidney_disease,skin_cancer]],columns=['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth',
       'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic',
       'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease',
       'SkinCancer']))
    
    # l_click=ttk.Label(text=preduct_value,font="Times 15 bold")
    # l_click.grid(row=17, column=0, padx=5, pady=5, sticky="w")

    # l_click = ttk.Label(text=preduct_value)
    # l_click.grid(row=17, column=0, padx=5, pady=5, sticky="e")
    # l_click_entry = ttk.Entry(preduct_value)
    # l_click_entry.grid(row=17, column=1, padx=5, pady=5, sticky="w")

    




    
# # Preducted_value

# preduct_label = ttk.Label(input_frame, text="Preducted Values:")
# preduct_label.grid(row=17, column=0, padx=5, pady=5, sticky="e")
# preduct_entry = ttk.Entry(input_frame)
# preduct_entry.grid(row=17, column=1, padx=5, pady=5, sticky="w")


    # Perform prediction based on the input values
      # Replace with your prediction logic

    def values(x):
        if x=="Yes":
            return 1
        else:
            return 0
    
    
    value_2 =values(preduct_value)
    print(value_2)
    # Set the color based on the prediction value
    if value_2 == 1:
        color = 'red'
    else:
        color = 'green'

    # Create the gauge figure
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value_2,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Prediction"},
        gauge={'bar': {'color': color}}
    ))

    # Display the gauge figure
    fig.show()

# Create a label frame for the input fields
input_frame = ttk.LabelFrame(content_frame, text="Input")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Configure grid weights to make the input frame expandable
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_rowconfigure(0, weight=1)
input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)

# BMI
bmi_label = ttk.Label(input_frame, text="BMI:")
bmi_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
bmi_entry = ttk.Entry(input_frame)
bmi_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Smoking
smoking_label = ttk.Label(input_frame, text="Smoking:")
smoking_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
smoking_var = tk.StringVar()
smoking_combobox = ttk.Combobox(input_frame, textvariable=smoking_var, values=["Yes", "No"])
smoking_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Alcohol Drinking
alcohol_label = ttk.Label(input_frame, text="Alcohol Drinking:")
alcohol_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
alcohol_var = tk.StringVar()
alcohol_combobox = ttk.Combobox(input_frame, textvariable=alcohol_var, values=["Yes", "No"])
alcohol_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Stroke
stroke_label = ttk.Label(input_frame, text="Stroke:")
stroke_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
stroke_var = tk.StringVar()
stroke_combobox = ttk.Combobox(input_frame, textvariable=stroke_var, values=["Yes", "No"])
stroke_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Physical Health
physical_health_label = ttk.Label(input_frame, text="Physical Health:")
physical_health_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
physical_health_entry = ttk.Entry(input_frame)
physical_health_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Mental Health
mental_health_label = ttk.Label(input_frame, text="Mental Health:")
mental_health_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
mental_health_entry = ttk.Entry(input_frame)
mental_health_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

# Difficulty Walking
walking_label = ttk.Label(input_frame, text="Difficulty Walking:")
walking_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
walking_var = tk.StringVar()
walking_combobox = ttk.Combobox(input_frame, textvariable=walking_var, values=["Yes", "No"])
walking_combobox.grid(row=6, column=1, padx=5, pady=5, sticky="w")

# Sex
sex_label = ttk.Label(input_frame, text="Sex:")
sex_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
sex_var = tk.StringVar()
sex_combobox = ttk.Combobox(input_frame, textvariable=sex_var, values=["Male", "Female"])
sex_combobox.grid(row=7, column=1, padx=5, pady=5, sticky="w")

# Age Category
age_label = ttk.Label(input_frame, text="Age Category:")
age_label.grid(row=8, column=0, padx=5, pady=5, sticky="e")
age_var = tk.StringVar()
age_combobox = ttk.Combobox(input_frame, textvariable=age_var, values=['70-74', '35-39', '40-44', '25-29', '50-54', '65-69', '18-24', '60-64', '45-49', '55-59', '80+', '75-79', '30-34'])
age_combobox.grid(row=8, column=1, padx=5, pady=5, sticky="w")

# Race
race_label = ttk.Label(input_frame, text="Race:")
race_label.grid(row=9, column=0, padx=5, pady=5, sticky="e")
race_var = tk.StringVar()
race_combobox = ttk.Combobox(input_frame, textvariable=race_var, values=['White', 'Other', 'Hispanic', 'Black', 'Asian', 'American Indian/Alaskan Native'])
race_combobox.grid(row=9, column=1, padx=5, pady=5, sticky="w")

# Diabetic
diabetic_label = ttk.Label(input_frame, text="Diabetic:")
diabetic_label.grid(row=10, column=0, padx=5, pady=5, sticky="e")
diabetic_var = tk.StringVar()
diabetic_combobox = ttk.Combobox(input_frame, textvariable=diabetic_var, values=["Yes", "No"])
diabetic_combobox.grid(row=10, column=1, padx=5, pady=5, sticky="w")

# Physical Activity
activity_label = ttk.Label(input_frame, text="Physical Activity:")
activity_label.grid(row=11, column=0, padx=5, pady=5, sticky="e")
activity_var = tk.StringVar()
activity_combobox = ttk.Combobox(input_frame, textvariable=activity_var, values=["Yes", "No"])
activity_combobox.grid(row=11, column=1, padx=5, pady=5, sticky="w")

# General Health
gen_health_label = ttk.Label(input_frame, text="General Health:")
gen_health_label.grid(row=12, column=0, padx=5, pady=5, sticky="e")
gen_health_var = tk.StringVar()
gen_health_combobox = ttk.Combobox(input_frame, textvariable=gen_health_var, values=["Very good", "Poor", "Excellent", "Good", "Fair"])
gen_health_combobox.grid(row=12, column=1, padx=5, pady=5, sticky="w")

# Sleep Time
sleep_label = ttk.Label(input_frame, text="Sleep Time:")
sleep_label.grid(row=13, column=0, padx=5, pady=5, sticky="e")
sleep_entry = ttk.Entry(input_frame)
sleep_entry.grid(row=13, column=1, padx=5, pady=5, sticky="w")

# Asthma
asthma_label = ttk.Label(input_frame, text="Asthma:")
asthma_label.grid(row=14, column=0, padx=5, pady=5, sticky="e")
asthma_var = tk.StringVar()
asthma_combobox = ttk.Combobox(input_frame, textvariable=asthma_var, values=["Yes", "No"])
asthma_combobox.grid(row=14, column=1, padx=5, pady=5, sticky="w")

# Kidney Disease
kidney_label = ttk.Label(input_frame, text="Kidney Disease:")
kidney_label.grid(row=15, column=0, padx=5, pady=5, sticky="e")
kidney_var = tk.StringVar()
kidney_combobox = ttk.Combobox(input_frame, textvariable=kidney_var, values=["Yes", "No"])
kidney_combobox.grid(row=15, column=1, padx=5, pady=5, sticky="w")

# Skin Cancer
skin_cancer_label = ttk.Label(input_frame, text="Skin Cancer:")
skin_cancer_label.grid(row=16, column=0, padx=5, pady=5, sticky="e")
skin_cancer_var = tk.StringVar()
skin_cancer_combobox = ttk.Combobox(input_frame, textvariable=skin_cancer_var, values=["Yes", "No"])
skin_cancer_combobox.grid(row=16, column=1, padx=5, pady=5, sticky="w")




# Predict button
predict_button = ttk.Button(content_frame, text="Predict", command=predict)
predict_button.grid(row=1, column=0, padx=10, pady=10)





# Start the main event loop
window.mainloop()

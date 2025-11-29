import PySimpleGUI as sg
import multipleChoice as mc
import pandas as pd
import diabetes

l1 = [mc.multipleChoice(0,'no') , mc.multipleChoice(1,'yes')]

l6 = [mc.multipleChoice(1,'Never attended school or only kindergarten') , mc.multipleChoice(2,'Grades 1 through 8 (Elementary)') ,
      mc.multipleChoice(3,'Grades 9 through 11 (Some high school)') , mc.multipleChoice(4,'Grade 12 or GED (High school graduate)') ,
      mc.multipleChoice(5,'College 1 year to 3 years (Some college or technical school)') ,
      mc.multipleChoice(6,'College 4 years or more (College graduate)') ]

l8 = [mc.multipleChoice(1,'less than $10,000') , mc.multipleChoice(2,'$10,000 - 20,000') ,mc.multipleChoice(3,'$20,000 - 25,000') ,
      mc.multipleChoice(4,'$25,000 - 30,000') , mc.multipleChoice(5,'$30,000 - 35,000 ') , mc.multipleChoice(6,'$35,000 - 55,000 ') ,
      mc.multipleChoice(7, '$55,000 - 75,000') , mc.multipleChoice(8,'more than $75,000')]

l13 = [mc.multipleChoice(1,'18-24') , mc.multipleChoice(2,'25-29') ,mc.multipleChoice(3,'30-34') ,
       mc.multipleChoice(4,'35-39') , mc.multipleChoice(5,'40-44') , mc.multipleChoice(6,'45-49') ,
       mc.multipleChoice(7, '50-54') , mc.multipleChoice(8,'55-59'), mc.multipleChoice(9,'60-64') ,mc.multipleChoice(10,'65-69') ,
       mc.multipleChoice(11,'70-74') , mc.multipleChoice(12,'75-79') , mc.multipleChoice(13,'80 or older')]

l30 = []
for i in range(1,31):
    l30.append(mc.multipleChoice(i,f"{i}"))

layout = [ [sg.Text ("Is your blood presure high?")] ,  [sg.Combo (l1)] ,
           [sg.Text ("Is your cholesterol  high?")] ,  [sg.Combo (l1)] , # 0 no 1 yes
           [sg.Text ("Have you done a cholesterol check in the last five years?")] ,  [sg.Combo (l1)] ,
           [sg.Text("What is your BMI?")], [sg.InputText()] ,   #its only in integers so do i need to tell the user or should i do a functionn that rount it?! ##
           [sg.Text("Have you smoked at least 100 cigarettes in your entire life? (Note: 5 packs = 100 cigarettes)?")], [sg.Combo (l1)],
           [sg.Text("Did you have a stroke?")], [sg.Combo (l1)] ,
           [sg.Text("Do you have coronary heart disease or myocardial infarction (MI)?")], [sg.Combo (l1)] ,
           [sg.Text("Have you done physical activity in past 30 days - not including job?")], [sg.Combo (l1)],
           [sg.Text("Do you Consume Fruit 1 or more times per day?")], [sg.Combo (l1)],
           [sg.Text("Do you Consume Vegetables 1 or more times per day?")], [sg.Combo (l1)],
           [sg.Text("Do you have heavy drinks regulary (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)?")], [sg.Combo (l1)],
           [sg.Text("Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc?")], [sg.Combo (l1)],
           [sg.Text("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?")], [sg.Combo (l1)],
           [sg.Text("Would you say that in general your health?")], [sg.Combo([mc.multipleChoice(1,'excellent') , mc.multipleChoice(2,'very good') , mc.multipleChoice(3,'good') , mc.multipleChoice(4,'fair') , mc.multipleChoice(5,'poor') ])],
           [sg.Text("Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? scale 1-30 days")],[sg.Combo(l30)],
           [sg.Text("Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? scale 1-30 days")], [sg.Combo(l30)],
           [sg.Text("Do you have serious difficulty walking or climbing stairs?")], [sg.Combo (l1)],
           [sg.Text("What is your sex?")], [sg.Combo ([mc.multipleChoice(0,'female') , mc.multipleChoice(1,'male')])],
           [sg.Text("What is your age?")], [sg.Combo (l13)],
           [sg.Text("What is your Education level?")], [sg.Combo(l6)],
           [sg.Text("What is Income scale scale 1-8 1 = less than $10,000 5 = less than $35,000 8 = $75,000 or more?")], [sg.Combo (l8)],
           [sg.Button('Ok'), sg.Button('Cancel')]  ]

window = sg.Window('Do you have diebetes?', layout)

while True:
    event, values = window.read()

    if event == 'Ok':
        # create series of names
        bmi = int(float(values[3]))
        values[3] = mc.multipleChoice(0, '')

        userInput = pd.Series([values[i].value for i in range(21)])
        userInput[3] = bmi

        print(userInput)

        score = diabetes.diabetesScore(userInput, 10)
        print(score)

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


window.close()


#create series of the user input (using a loop if your not the bmi. for the bmi enter it in its place and make it an integer)
#create a combination of the two
#import the main and use the function with th user row.
#add the statistics






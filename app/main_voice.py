import speech_recognition as sr

from gtts import gTTS
from time import sleep

import os

language = 'en'

# Setup
yes_no = ['y', 'n']

r = sr.Recognizer()
mic = sr.Microphone()


def prompt(str):
    print(str)
    myobj = gTTS(text=str, lang=language, slow=False)
    myobj.save("next_prompt.mp3")
    os.system("next_prompt.mp3")
    sleep(3)


def M1():
    prompt('\nSounds like you are feeling ok.\n')
    quit()


def M2():
    prompt('\nCall 911 – You may be having a medical emergency.\n')
    quit()


def M3():
    prompt('\nSorry, this Coronavirus Self-Checker is for people who are at least 2 years old.\n')
    quit()


def M4():
    prompt('\nUrgent medical attention may be needed. Please go to the Emergency Department.\n')
    quit()


def M5():
    prompt('\nSorry you’re feeling sick. Call medical provider within 24 hours.\n')
    quit()


def M6():
    prompt('\nContact the occupational health provider at your workplace immediately.\n')
    quit()


def M7():
    prompt('Contact a healthcare provider in the long-term care facility where you live.\n')
    quit()


def M8():
    prompt('\nStay at home and take care of yourself. Call your provider if you get worse.\n')
    quit()


def M9():
    prompt('\nStay home and take care of yourself in home isolation. Call a medical provider within 24 hours.\n')
    quit()


def M10():
    prompt('\nSorry you’re feeling ill. Stay at home and monitor your symptoms. Call your provider if you get worse.\n')
    prompt('* Non-COVID *\n')
    quit()


def Q1():
    prompt('\nAre you ill, or caring for someone who is ill?\n')
    return input('[y\\n]: ')


def Q2():
    prompt('\nAre you answering for yourself or someone else?\n')
    return input('[1: myself, 2: someone else]: ')


def Q3():
    prompt('\nWhat is your age?\n')
    return input('[age in years]: ')


def Q4():
    prompt('\nAre they experiencing any of the following life-threatening symptoms?')
    prompt('   - Extremely fast or shallow breathing')
    prompt('   - Blue-colored lips or face')
    prompt('   - Not waking up or not interacting when awake')
    prompt('   - So irritable that the child does not want to be held')
    prompt('   - Seizures\n')
    return input('[y\\n]: ')


def Q5():
    prompt('\nAre you experiencing any of the following life-threatening symptoms?')
    prompt('   - Gasping for air or cannot talk without catching your breath (extremely difficult breathing)')
    prompt('   - Blue-colored lips or face')
    prompt('   - Severe and constant pain or pressure in the chest')
    prompt('   - Severe and constant dizziness or lightheadedness')
    prompt('   - Acting confused (new or worsening)')
    prompt('   - Unconscious or very difficult to wake up')
    prompt('   - Slurred speech (new or worsening)')
    prompt('   - New seizure or seizures that won’t stop\n')
    return input('[y\\n]: ')


def Q6():
    prompt('\nDo you have any of the following?')
    prompt('   - Moderate to severe difficulty breathing (unable to speak full sentences)')
    prompt('   - Coughing up blood (more than about 1 teaspoon)')
    prompt('   - Signs of low blood pressure (feeling cold, pale, clammy skin, light-headed, too weak to stand)')
    prompt('   - Ribs are pulling in with each breath (retractions)')
    prompt('   - Dehydration\n')
    return input('[y\\n]: ')


def Q7():
    prompt('\nDo you have any of the following?')
    prompt('   - Moderate to severe difficulty breathing (unable to speak full sentences)')
    prompt('   - Coughing up blood (more than about 1 teaspoon)')
    prompt('   - Signs of low blood pressure (feeling cold, pale, clammy skin, light-headed, too weak to stand)\n')
    return input('[y\\n]: ')


def Q8():
    prompt('\nIn the two weeks before you felt sick, did you:')
    prompt('    - Have contact with someone diagnosed with COVID-19')
    prompt('    - Live in or visit a place where COVID-19 is spreading\n')
    return input('[y\\n]: ')


def Q9():
    prompt('\nDo you have any of the following?')
    prompt('    - Fever or feeling feverish (chills, sweating)')
    prompt('    - Shortness of breath (not severe)')
    prompt('    - Cough')
    prompt('    - Other\n')
    return input('[1: ≥1 COVID-19 symptom, 2: Only Other]: ')


def Q10():
    prompt('\nDo you have any of the following?')
    prompt('    - Runny or stuffy nose')
    prompt('    - Sore throat')
    prompt('    - Muscle aches, body aches, or headache')
    prompt('    - Tiredness or fatigue')
    prompt('    - Nausea, vomiting, or diarrhea\n')
    return input('[y\\n]: ')


def Q11():
    prompt('\nDo you live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q12():
    prompt('\nIn the last two weeks have you worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q13():
    prompt('\nDo you have any of the following conditions')
    prompt('    - Chronic lung disease, moderate to severe asthma, or smoking')
    prompt('    - Serious heart conditions')
    prompt('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    prompt('    - Pregnancy')
    prompt('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    prompt('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    return input('[y\\n]: ')


def Q14():
    prompt('\nDo you have any of the following?')
    prompt('    - Fever or feeling feverish (chills, sweating)')
    prompt('    - Shortness of breath (not severe)')
    prompt('    - Cough')
    prompt('    - Other\n')
    return input('[1: 1 COVID-19 symptom, 2: ≥2 COVID-19 symptoms, 3: Only Other]: ')


def Q15():
    prompt('\nDo you have any of the following?')
    prompt('    - Runny or stuffy nose')
    prompt('    - Sore throat')
    prompt('    - Muscle aches, body aches, or headache')
    prompt('    - Tiredness or fatigue')
    prompt('    - Nausea, vomiting, or diarrhea')
    prompt('    - Other\n')
    return input('[y\\n]: ')


def Q16():
    prompt('\nDo you live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q17():
    prompt('\nIn the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q18():
    prompt('\nDo you have any of the following conditions?')
    prompt('    - Chronic lung disease, moderate to severe asthma, or smoking')
    prompt('    - Serious heart conditions')
    prompt('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    prompt('    - Pregnancy')
    prompt('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    prompt('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    return input('[y\\n]: ')


def Q19():
    prompt('\nDo you live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q20():
    prompt('\nIn the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q21():
    prompt('\nDo you have any of the following conditions?')
    prompt('    - Chronic lung disease, moderate to severe asthma, or smoking')
    prompt('    - Serious heart conditions')
    prompt('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    prompt('    - Pregnancy')
    prompt('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    prompt('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    return input('[y\\n]: ')


def Q22():
    prompt('\nIn the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q23():
    prompt('\nIn the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q25():
    prompt('\nDo you live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q26():
    prompt('\nIn the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q27():
    prompt('\nDo you have any of the following conditions?')
    prompt('    - Chronic lung disease, moderate to severe asthma, or smoking')
    prompt('    - Serious heart conditions')
    prompt('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    prompt('    - Pregnancy')
    prompt('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    prompt('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    return input('[y\\n]: ')


def Q28():
    prompt('\nWhat is your gender?\n')
    return input('[1: Female, 2: Male]: ')


def Q29():
    prompt('\nDo you have any of the following conditions?')
    prompt('    - Chronic lung disease, moderate to severe asthma, or smoking')
    prompt('    - Serious heart conditions')
    prompt('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    prompt('    - Pregnancy')
    prompt('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    prompt('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    return input('[y\\n]: ')


def phase1():
    a1 = Q1()
    if a1 == 'y':
        a2 = Q2()
        a3 = Q3()
        if int(a3) < 2:
            a4 = Q4()
            if a4 == 'y':
                M2()
            else:
                M3()
        else:
            a28 = Q28()
            a5 = Q5()
            if (a5 == 'n' and int(a3) < 5):
                a6 = Q6()
                if a6 == 'y':
                    M4()
                else:
                    phase2(a3)
            elif (a5 == 'n' and int(a3) >= 5):
                a7 = Q7()
                if a7 == 'y':
                    M4()
                else:
                    phase2(a3)
            else:
                M2()
    else:
        M1()


def phase2(a3):
    a8 = Q8()
    if a8 == 'y':
        a9 = Q9()
        if a9 == 1:
            a11 = Q11()
            if a11 == 'y':
                M7()
            elif (a11 == 'n' and int(a3) >= 19):
                a12 = Q12()
                if a12 == 'y':
                    M9()
                else:
                    a13 = Q13()
                    if a13 == 'y':
                        M5()
                    else:
                        M8()
            elif (a11 == 'n' and int(a3) < 19):
                a13 = Q13()
                if a13 == 'y':
                    M5()
                else:
                    M8()
        else:
            a10 = Q10()
            a25 = Q25()
            if a25 == 'y':
                M7()
            elif (a25 == 'n' and int(a3) >= 19):
                a26 = Q26()
                if a26 == 'y':
                    M10()
                else:
                    a27 = Q27()
                    M10()
            elif (a25 == 'n' and int(a3) < 19):
                a27 = Q27()
                M10()
    else:
        a14 = Q14()
        if a14 == '1':
            a16 = Q16()
            if a16 == 'n':
                if int(a3) < 19:
                    Q18()
                    M8()
                else:
                    a17 = Q17
                    if a17 == 'n':
                        Q18()
                        M8()
                    else:
                        M8()
            else:
                M7()
        elif a14 == '2':
            a19 = Q19()
            if a19 == 'y':
                M7()
            else:
                if int(a3) < 65:
                    a21 = Q21()
                    if a21 == '1':
                        if int(a3) < 19:
                            M5()
                        else:
                            a22 = Q22()
                            if a22 == 'n':
                                M5()
                            else:
                                M5()
                                M6()
                    else:
                        if int(a3) < 19:
                            M8()
                        else:
                            a23 = Q23()
                            if a23 == 'n':
                                M8()
                            else:
                                M8()
                                M6()
                else:
                    a29 = Q29()
                    a20 = Q20()
                    if a29 == 'n':
                        if a20 == 'n':
                            M9()
                        else:
                            M9()
                            M6()
                    else:
                        if a20 == 'n':
                            M5()
                        else:
                            M5()
                            M6()
        elif a14 == '3':
            Q15()
            M10()


phase1()

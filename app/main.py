# Setup
yes_no = ['y', 'n']


def M1():
    print('\nMSG1: Sounds like you are feeling ok.\n')
    quit()


def M2():
    print('\nMSG2: Call 911 – You may be having a medical emergency.\n')
    quit()


def M3():
    print('\nMSG3: Sorry, this Coronavirus Self-Checker is for people who are at least 2 years old.\n')
    quit()


def M4():
    print('\nMSG4: Urgent medical attention may be needed. Please go to the Emergency Department.\n')
    quit()


def M5(quitAfter=True):
    print('\nMSG5: Sorry you’re feeling sick. Call a medical provider within 24 hours.\n')
    if (quitAfter):
        quit()
    else:
        return


def M6():
    print('\nMSG6: Contact the occupational health provider at your workplace immediately.\n')
    quit()


def M7():
    print('\nMSG7: Contact a healthcare provider in the long-term care facility where you live.\n')
    quit()


def M8(quitAfter=True):
    print('\nMSG8: Stay at home and take care of yourself. Call your provider if you get worse.\n')
    if (quitAfter):
        quit()
    else:
        return


def M9(quitAfter=True):
    print('\nMSG9: Stay home and take care of yourself in home isolation. Call a medical provider within 24 hours.\n')
    if (quitAfter):
        quit()
    else:
        return


def M10():
    print('\nMSG10: Sorry you’re feeling ill. Stay at home and monitor your symptoms. Call your provider if you get worse.\n')
    print('* Non-COVID *\n')
    quit()


def Q1():
    print('\nQ1: Are you ill, or caring for someone who is ill?\n')
    return input('[y\\n]: ')


def Q2():
    print('\nQ2: Are you answering for yourself or someone else?\n')
    return input('[1: myself, 2: someone else]: ')


def Q3():
    print('\nQ3: What is your (their) age?\n')
    return input('[age in years]: ')


def Q4():
    print('\nQ4: Are they experiencing any of the following life-threatening symptoms?')
    # print('   - Not experiencing any life-threatening symptoms')
    print('   - Extremely fast or shallow breathing')
    print('   - Blue-colored lips or face')
    print('   - Not waking up or not interacting when awake')
    print('   - So irritable that the child does not want to be held')
    print('   - Seizures\n')
    return input('[y\\n]: ')


def Q5():
    print('\nQ5: Are you (they) experiencing any of the following life-threatening symptoms?')
    # print('   - Not experiencing any life-threatening symptoms')
    print('   - Gasping for air or cannot talk without catching your breath (extremely difficult breathing)')
    print('   - Blue-colored lips or face')
    print('   - Severe and constant pain or pressure in the chest')
    print('   - Severe and constant dizziness or lightheadedness')
    print('   - Acting confused (new or worsening)')
    print('   - Unconscious or very difficult to wake up')
    print('   - Slurred speech (new or worsening)')
    print('   - New seizure or seizures that won’t stop\n')
    return input('[y\\n]: ')


def Q6():
    print('\nQ6: Do you (they) have any of the following?')
    print('   - Moderate to severe difficulty breathing (unable to speak full sentences)')
    print('   - Coughing up blood (more than about 1 teaspoon)')
    print('   - Signs of low blood pressure (feeling cold, pale, clammy skin, light-headed, too weak to stand)')
    print('   - Ribs are pulling in with each breath (retractions)')
    print('   - Dehydration\n')
    # print('   - None of the above')
    return input('[y\\n]: ')


def Q7():
    print('\nQ7: Do you (they) have any of the following?')
    print('   - Moderate to severe difficulty breathing (unable to speak full sentences)')
    print('   - Coughing up blood (more than about 1 teaspoon)')
    print('   - Signs of low blood pressure (feeling cold, pale, clammy skin, light-headed, too weak to stand)\n')
    # print('   - None of the above')
    return input('[y\\n]: ')


def Q8():
    print('\nQ8: In the two weeks before you (they) felt sick, did you (they):')
    print('    - Have contact with someone diagnosed with COVID-19')
    print('    - Live in or visit a place where COVID-19 is spreading\n')
    return input('[y\\n]: ')


def Q9():
    print('\nQ9: Do you (they) have any of the following?')
    print('    - Fever or feeling feverish (chills, sweating)')
    print('    - Shortness of breath (not severe)')
    print('    - Cough')
    print('    - Other\n')
    return input('[1: ≥1 COVID-19 symptom, 2: Only Other]: ')


def Q10():
    print('\nQ10: Do you (they) have any of the following?')
    print('    - Runny or stuffy nose')
    print('    - Sore throat')
    print('    - Muscle aches, body aches, or headache')
    print('    - Tiredness or fatigue')
    print('    - Nausea, vomiting, or diarrhea\n')
    return input('[y\\n]: ')


def Q11():
    print('\nQ11: Do you (they) live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q12():
    print('\nQ12: In the last two weeks have you (they) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q13():
    print('\nQ13: Do you have any of the following conditions?')
    print('    - Chronic lung disease, moderate to severe asthma, or smoking')
    print('    - Serious heart conditions')
    print('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    print('    - Pregnancy')
    print('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    print('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    # print('    - None of the above')
    return input('[y\\n]: ')


def Q14():
    print('\nQ14: Do you (they) have any of the following?')
    print('    - Fever or feeling feverish (chills, sweating)')
    print('    - Shortness of breath (not severe)')
    print('    - Cough')
    print('    - Other\n')
    return input('[1: 1 COVID-19 symptom, 2: ≥2 COVID-19 symptoms, 3: Only Other]: ')


def Q15():
    print('\nQ15: Do you (they) have any of the following?')
    print('    - Runny or stuffy nose')
    print('    - Sore throat')
    print('    - Muscle aches, body aches, or headache')
    print('    - Tiredness or fatigue')
    print('    - Nausea, vomiting, or diarrhea')
    print('    - Other\n')
    return input('[y\\n]: ')


def Q16():
    print('\nQ16: Do you (they) live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q17():
    print('\nQ17: In the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q18():
    print('\nQ18: Do you have any of the following conditions?')
    print('    - Chronic lung disease, moderate to severe asthma, or smoking')
    print('    - Serious heart conditions')
    print('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    print('    - Pregnancy')
    print('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    print('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    # print('    - None of the above')
    return input('[y\\n]: ')


def Q19():
    print('\nQ19: Do you (they) live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q20():
    print('\nQ20: In the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q21():
    print('\nQ21: Do you have any of the following conditions?')
    print('    - Chronic lung disease, moderate to severe asthma, or smoking')
    print('    - Serious heart conditions')
    print('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    print('    - Pregnancy')
    print('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    print('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    # print('    - None of the above')
    return input('[y\\n]: ')


def Q22():
    print('\nQ22: In the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q23():
    print('\nQ23: In the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


# def Q24():
#    print('noop')


def Q25():
    print('\nQ25: Do you (they) live in a long-term care facility or nursing home?\n')
    return input('[y\\n]: ')


def Q26():
    print('\nQ26: In the last two weeks have you (sick person) worked or volunteered in a hospital, emergency room, clinic, medical office, long-term care facility or nursing home, ambulance service, first responder services, or any health care setting or taken care of patients as a student or part of your work?\n')
    return input('[y\\n]: ')


def Q27():
    print('\nQ27: Do you have any of the following conditions?')
    print('    - Chronic lung disease, moderate to severe asthma, or smoking')
    print('    - Serious heart conditions')
    print('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    print('    - Pregnancy')
    print('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    print('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
    return input('[y\\n]: ')


def Q28():
    print('\nQ28: What is your (their) gender?\n')
    return input('[1: Female, 2: Male]: ')


def Q29():
    print('\nQ29: Do you have any of the following conditions?')
    print('    - Chronic lung disease, moderate to severe asthma, or smoking')
    print('    - Serious heart conditions')
    print('    - Weakened immune system (cancer treatment, prolonged use of steroids, transplant or HIV/AIDS)')
    print('    - Pregnancy')
    print('    - Severe obesity (Body Mass Index [BMI] ≥ 40)')
    print('    - Underlying conditions (diabetes, renal failure, or liver disease)\n')
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
        if a9 == '1':
            a11 = Q11()
            if a11 == 'y':
                M7()
            elif (a11 == 'n' and int(a3) >= 19):
                a12 = Q12()
                if a12 == 'y':
                    M9(quitAfter=False)
                    M6()
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
                    a17 = Q17()
                    if a17 == 'n':
                        Q18()
                        M8()
                    else:
                        M8(quitAfter=False)
                        M6()
            else:
                M7()
        elif a14 == '2':
            a19 = Q19()
            if a19 == 'y':
                M7()
            else:
                if int(a3) < 65:
                    a21 = Q21()
                    if a21 == 'y':
                        if int(a3) < 19:
                            M5()
                        else:
                            a22 = Q22()
                            if a22 == 'n':
                                M5()
                            else:
                                M5(quitAfter=False)
                                M6()
                    else:
                        if int(a3) < 19:
                            M8()
                        else:
                            a23 = Q23()
                            if a23 == 'n':
                                M8()
                            else:
                                M8(quitAfter=False)
                                M6()
                else:
                    a29 = Q29()
                    a20 = Q20()
                    if a29 == 'n':
                        if a20 == 'n':
                            M9()
                        else:
                            M9(quitAfter=False)
                            M6()
                    else:
                        if a20 == 'n':
                            M5()
                        else:
                            M5(quitAfter=False)
                            M6()
        elif a14 == '3':
            Q15()
            M10()


phase1()

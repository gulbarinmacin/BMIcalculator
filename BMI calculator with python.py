mass= float(input("Enter mass in kg: "))

if 0<mass<500:
    height=int(input("Enter height in cm: "))
    print(" ")
    if 0<height<300:
        bmi=mass/(((height/100))**2)
        if bmi<18.5:
            if bmi >= 16:
                print("BMI: ", bmi, "- You are underweight")
            elif 15<=bmi<16:
                 print("BMI: ", bmi, "- You are underweight")
                 print("Please note that you are SEVERELY underweight")
            elif bmi <15:
                 print("BMI: ", bmi, "- You are underweight")
                 print("Please note that you are VERY SEVERELY underweight")
        elif 18.5<= bmi <25:
            print("BMI: ", bmi, "- You are normal weight")
        elif 25<= bmi <30:
             print("BMI: ", bmi, "- You are  overweight")
        elif bmi >= 30:
            if 30<= bmi <35:
                 print("BMI: ", bmi, "- You are obese")
                 print("Please note that you are MODERATELY obese")
            elif 35 <= bmi < 40:
                 print("BMI: ", bmi, "- You are obese")
                 print("Please note that you are SEVERELY obese")
            elif bmi >= 40:
                 print("BMI: ", bmi, "- You are obese")
                 print("Please note that you are VERY SEVERELY obese")
    elif height < 0:
        print("Height must be greater than 0")
    elif height > 300:
        print("Mass must be less than 300")
elif mass<0:
    print("Mass must be greater than 0")
elif mass>500:
     print("Mass must be less than 500")

print("Goodbye")
    
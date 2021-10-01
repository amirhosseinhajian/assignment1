weight = float(input("Enter the height in kg: "))
height = float(input("Enter the height in meter: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Your body mass index is under weight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your body mass index is normal.")
if bmi >= 25 and bmi <= 29.9:
    print("Your body mass index is over weight.")
if bmi >=30 and bmi <= 34.9 :
    print("Your body mass index is obese.")
if bmi >= 35:
    print("Your body mass index is extermely obese.")
Weight = float(input("Please write your weight (in kilograms)"))
Height = float(input("Please write your height (in meters)"))
BIM = Weight/((Height)**2)
print("Your BIM is", BIM)
if BIM < 18.5:
    print("You are Underweight")
elif BIM < 25:
    print("You are Normal Weight")
elif BIM < 30:
    print("You are Overweight")
elif BIM > 30:
    print("You are Obese")
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

# print(type(height))
# print(type(weight))

height_in_metres=float(height/100)

BMI = round(weight/ (height_in_metres **2),2)

# print(f"Your BMI is: {BMI}")

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")

elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")

elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")

else:
  print(f"Your BMI is {BMI}, you are clinically obese.")







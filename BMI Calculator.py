from unittest import result

def bmi(weight, height):
    return weight / (height ** 2 )

print("BMI calculator")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: ")) / 100 # convert cm into meters
print(f"Your BMI is: {bmi(weight, height):.2f}")                                                                                                                            
result = bmi(weight, height)
print(f"Your BMI is: {result:.2f}")
 # show bmi category 
if result < 18.5:
    print("You are underweight.")
elif result < 25:
    print("You have a normal weight.")
elif result < 30:
   print("You are overweight.")
else:
  print("You are obese.")
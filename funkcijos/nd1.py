# Create a function to calculate and display the Body Mass Index (BMI) from user-provided height in meters and weight in kilograms. The formula is BMI = <weight in kg> / <height in m>2. The output should be rounded to 2 digits after the decimal point.

def my_bmi (hight, weight):
    calc1 = weight / (hight*2)
    return calc1

w=float(input("Weight: "))
h=float(input("Height:"))

bmiresult=my_bmi(w,h)
# print(bmiresult)
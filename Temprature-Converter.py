celsius = float(input("Please enter temperature in celsius..."))

fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)

if (fahrenheit >= 90):
    print("It is Hot!!")
elif (fahrenheit <= 45):
    print("It is Cold!")
else:
    print("The weather is Perfect! Go out and play!")

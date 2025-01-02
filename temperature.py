'''
You will write a function called "celsiusToFahrenheit" to convert temperature in Celsius to Fahrenheit. These two values are related by the formula: celsius * 1.8 = fahrenheit – 32

As an input to the program, you will have to prompt the user to enter a value in Celsius. For prompting
and accepting the user for an input, use input(msg) in your code. It presents a prompt to the user (you
will have to replace ‘msg’ with a prompt message in quotes), gets input from the user and stores the
input entered by the user in a string. You will have to write code for displaying the equivalent Fahrenheit
value on screen.
Test your function with known inputs to verify if your output is correct or not.
'''

def celsiusToFahrenheit(temperature):
    pass
    # write your code here (and delete the pass statement above)


# write a couple tests for this program. They should call the function celsiusToFahrenheit and check that the returned value is correct

def celsiustofahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

celsius = float(input("Enter the Temeperature in Celsius Scale"))
fahrenheit = celsiustofahrenheit(celsius)
print("The value of the temperature in Fahrenheit:", fahrenheit)

#Thank You So MUCH NAks BOsss

#OUTPUT:
#Enter the Temeperature in Celsius Scale37.5
#The value of the temperature in Fahrenheit: 99.5

#Enter the Temeperature in Celsius Scale44
#The value of the temperature in Fahrenheit: 111.2
#S C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-1>

#Enter the Temeperature in Celsius Scale0
#The value of the temperature in Fahrenheit: 32.0
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-1>

#Enter the Temeperature in Celsius Scale100
#The value of the temperature in Fahrenheit: 212.0
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-1>

#Enter the Temeperature in Celsius Scale69
#The value of the temperature in Fahrenheit: 156.2
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-1>

#Enter the Temeperature in Celsius Scale273
#The value of the temperature in Fahrenheit: 523.4000000000001
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-1>
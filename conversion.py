# Python Program - Convert Fahrenheit to Celsius

while True:
  print("Enter 'x' for exit.")
fah = input("Enter Temperature in Fahrenheit: ")
if fah == 'x':
break
else:
fahrenheit = float(fah)
celsius = (fahrenheit-32)/1.8
print("Temperature in Celsius =",celsius,"\n")

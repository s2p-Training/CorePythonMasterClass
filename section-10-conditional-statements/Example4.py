temp = int(input("Enter room temperature : "))

if temp > 40:
    print("Turn On AC")
elif temp > 35:
    print("Turn On Cooler")
elif temp > 25:
    print("Turn On Fan")
elif temp > 10:
    print("Open Windows")
else:
    print("It's Time To Use Heater!")

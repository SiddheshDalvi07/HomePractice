richter_magnitude = float(input("Enter the Richter magnitude value: "))

if richter_magnitude < 1.0:
    print("Below the threshold of perceptibility")
elif 1.0 <= richter_magnitude < 2.0:
    print("Microearthquakes not felt or rarely felt")
elif 2.0 <= richter_magnitude < 4.0:
    print("Very rarely causes damage")
elif 4.0 <= richter_magnitude < 5.0:
    print("Damage done to weak buildings")
elif 5.0 <= richter_magnitude < 6.0:
    print("Cause damage to the poorly constructed building")
elif 6.0 <= richter_magnitude < 7.0:
    print("Causes damage to well-built structures")
elif 7.0 <= richter_magnitude < 8.0:
    print("Causes damage to most buildings")
elif 8.0 <= richter_magnitude < 9.0:
    print("Causes major destruction")
elif richter_magnitude >= 9.0:
    print("Causes unbelievable damage")
else:
    print("Invalid Richter magnitude value entered")

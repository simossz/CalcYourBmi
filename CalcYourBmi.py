peso = int(input("Peso in kg "))
altezza_cm = int(input("Altezza in cm "))
altezza_m = altezza_cm / 100
bmi = peso / (altezza_m * altezza_m)
print("Il tuo BMI è circa", int(bmi))
if bmi < 18:
    print("Sottopeso")
elif bmi < 26:
    print("Normopeso")
else:
    print("Sovrappeso")

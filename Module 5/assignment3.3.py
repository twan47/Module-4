score = input("Enter Score: ")
try:
    fh = float(score)
except:
    print("Error, please enter number equal to 1 or below.")

if fh >= 0.9 :
    print("A")
elif fh >= 0.8 :
    print("B")
elif fh >= 0.7 :
    print("C")
elif fh >= 0.6 :
    print("D")
elif fh < 0.6 :
    print("F")
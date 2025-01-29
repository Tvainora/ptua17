s=float(input("Skaicius: "))
sm=input("Simbolis: ")
ass=float(input("Antras skaicius: "))
suma=None
if sm == "+":
    suma=s+ass
elif sm =="-":
    suma=s-ass
elif sm == "/":
    suma=s/ass
elif sm == "*":
    suma=s*ass
print(f"{s} {sm} {ass} {suma}")
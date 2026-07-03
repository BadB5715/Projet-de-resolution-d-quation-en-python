import math
print("Bienvenue")
print("Je suis là pour résoudre vos équations de 1 et 2 dégrés en R et en C")
dégré=int(input("Si vous voulez résoudre les équations du premier dégré appuyez sur 1 sinon si c'est les équations de dégré 2 appuyez sur 2:"))
if dégré ==1:
    print("Les equations du 1 dégré sont sous forme ax+b=0")
    a=float(input("Veuillez entrer a :"))
    b=float(input("Veuillez entrer b :"))
    c=-b/a
    print("La solution dans R est ",c)
elif dégré ==2 :
    print("les équations du 2 dégrés sont sous forme de ax²+bx+c=0")
    a=float(input("Veuillez entrer a :"))
    b=float(input("Veuillez entrer b :"))
    c=float(input("Veuillez entrer c :"))
    d= (b*b) -(4*a*c)
    print("Le discriminant est ",d)
    if d>0 :
        r=math.sqrt(d)
        n=(-b-r)/(2*a)
        m=(-b+r)/(2*a)
        print("Les solutions de l'équation dans R sont ",n ,"et",m)
    elif d==0 :
        s=(-b)/(2*a)
        print ("la solution de l'équation est",s)
    else:
        print("L'éqution n'est pas résolvable en R , Vouliez vous le résoudre en C ??")
        passa=int(input("Si oui appuyez 1 ,si non appuyez 0:"))
        if passa ==1 :
            o=(-1)*d
            r=math.sqrt(o)
            e=2*a
            t=(-b)/e
            h=(r)/e
            print("Les solutions complexes de l'équation sont ",t,"-",h,"i","et",t,"+",h,"i","avec i le nombre complexe")
        else:
            print("merci")

print("Bye")
    
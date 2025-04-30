student_name=input("Dose to ononma tou mathiti: ")
mark1=int(input("Dose vathmo1: "))
mark2=int(input("Dose vathmo2: "))
mark3=int(input("Dose vathmo3: "))
mesos_oros=0
mesos_oros=mark1+mark2+mark3
mark4=mesos_oros
mark4=mark4/3
if mark4 >= 10 and mark4 <=20:
    print(f"{student_name} exei meso oro: {mark4}")
    print("Apotelesma: Perase")
elif mark4 < 10:
    print(f"{student_name} exei meso oro: {mark4}")
    print("Apotelesma: Apetuxe")
else:
    print("Lathos Vathmos")
    
print("Telos vathmologias")
print("Vlepeis eno perpatas sto dasos duo monopatia pou mporeis na pas")
print("1: Odhgei pros ena vouno")
print("2: Odhgei pros ena potami")

choice=input("Ti dialegeis:")
if choice=="1":
    print("Pernas pros to vouno kai tha prepei na skarfaloseis pshla oste na to diaperaseis\n")
elif choice=="2":
    print("Pernas pros to potami kai tha prepei na peraseis apenanti apo auto oste na sunexiseis\n")
else:
    print("Tha prepei na pas anagkastika se ena apo ta duo monopatia allios tha pethaneis ekei")
while choice=="1":
    print("Exeis ftasei sto pshlo vouno ti antikeimeno tha epilekseis gia na to diaperases apo pano tou\n")
    choice2=input("1:Eksoplismo oreivaseias me skoini\n2:Ena autokinhti ikano gia na anevei epano pshla:")
    if choice2=="1":
        print("Molis parelaves oloklhro eksoplismo oreivasias me makrosteno skoini ksekina thn poreia sou")
        break
    elif choice2=="2":
        print("Molis parelaves ena ikano autokinhto oste na diaperasei olo to vouno me tis rodes pou antexoun arketa tis anhfores")
        break 
while choice=="2":
    print("Exeis ftasei sto potami kai prepei kapos na peraseis apenanti\n")
    choice3=input("1:Mia ksilinh varka oste na ftaseis apenanti\n2:Na pas pros thn deksia meria tou potamou pou sou exei akoma duo epiloges gia na kopseis dromo:")
    if choice3=="1":
        print("Oraia apokthses mia ksilinh varka gia na peraseis sthn allh meria")
        break
    elif choice3=="2":
        choice4=input("Exeis akoma duo dromous (den paizei rolo pou tha pas):\n 1:deksia\n2:aristera:")
    if choice4=="1":
        print("Dialekses deksia exeis 2 ores dromo akomh")
        break
    elif choice4=="2":
        print("Dialekses aristera exeis 1.5 ora dromo akomh")
        break
        
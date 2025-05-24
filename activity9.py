print ("Ypologise mia mathimatikh praksi\n")
while True:
    praksi=input("Grapse mia praksi oste na thn upologiseis: \n")
    if praksi.lower()== "telos":
        print("Eksodos apo to programma\n")
        break
    try:
        apot=eval(praksi)
        print("Apotelesma: ",apot)
    except:
        print("Mh egkurh praksi\n")
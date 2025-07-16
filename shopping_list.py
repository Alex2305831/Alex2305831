shopping_list=[]

def show_menu():
    print("1.Prosthiki proiontos")
    print("2.Emfanisi listas")
    print("3.Diagrafh proiontos")
    print("4.Adeiasma listas")
    print("5.Exodos\n")

def add_item():
    item=input("Grapse proion pros prosthiki: \n")
    shopping_list.append(item)
    print(f"To {item} prostethike sth lista\n")
    
def show_list():
    if not shopping_list:
        print("H lista einai adeia\n")
    else:
        print("\n Proionta sth lista")
        for i,item in enumerate(shopping_list,1):
            print(f"{i}.{item}\n")
def delete_item():
    show_list()
    try:
        index=int(input("Dose ton arithmo tou proiontos gia diagrafh: \n"))
        if 1<=index<=len(shopping_list):
            removed=shopping_list.pop(index-1)
            print(f"To {removed} diagrafthke\n")
        else:
            print("Mh egkuros arithoms\n")
    except ValueError:
        print("Prepei na doseis arithmo\n")
        
def clear_list():
    shopping_list.clear()
    print("H lista adeiase\n")
    
while True:
    show_menu()
    choice=input("Epelekse enan arithmo metaksi 1-5: \n")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        show_list()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        print("Eksodos apo to programma")
        break
    else:
        print("Mh egkurh epilogh\n")
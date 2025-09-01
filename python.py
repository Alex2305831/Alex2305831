import tkinter
my_info={
"phone_pin":2426}
attempts=2
window=tkinter.Tk()
label=tkinter.Label(window, text=("Type your pin to success the code and to see a triangle with stars"),font=("Consolas",20))
label.grid(row=0,column=0)
window.title("Password through the code")
window.mainloop()
guess=int(input("Type your pin to sucess the code:"))
while guess!=my_info["phone_pin"]:
    guess=int(input("Type again its wrong:"))
    attempts-=1
    if attempts==0:
        print("Too bad the code cant be sucess")
        break
if guess==my_info["phone_pin"]:
    print("You succesflully in the code")
    rows=7
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print()
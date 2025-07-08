import tkinter as tk 
from time import strftime, time 

class ClockApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Psifiako roloi me xronometro")

        self.clock_label=tk.Label(root,font=("Helvetica",32), fg="blue")
        self.clock_label.pack(pady=10)
        
        self.timer_label=tk.Label(root,font=("Helvetica",24),fg="green",text="Xronometro: 0 deuterolepta")
        self.timer_label.pack(pady=10)
        
        self.start_button=tk.Button(root,text="Enarksi Xronometrou",command=self.start_timer)
        self.start_button.pack(pady=5)
        
        self.stop_button=tk.Button(root,text="Stamathse",command=self.stop_timer)
        self.stop_button.pack(pady=5)
        
        self.timer_running=False
        self.start_time=0
        
        self.update_clock()
    def update_clock(self):
        current_time=strftime("%H:%M:%S")
        self.clock_label.config(text="Ora: "+current_time)
        
        if self.timer_running:
            elapsed=int(time() - self.start_time)
            self.timer_label.config(text=f"Xronometro: {elapsed} deuterolepta")
            
        self.root.after(1000, self.update_clock)
            
    def start_timer(self):
        self.start_time=time()
        self.timer_running=True
        
    def stop_timer(self):
        self.timer_running=False
root=tk.Tk()
app=ClockApp(root)
root.mainloop()
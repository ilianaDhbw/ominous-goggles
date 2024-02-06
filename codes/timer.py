import tkinter as tk

class TimerApp:
    def __init__(self, root):
        
        self.root = root

        self.label = tk.Label(root, text="Timer: ", font=("Arial", 15))
        self.label.pack(pady=50,padx=50)

        # Timer direkt beim Start ausführen
        self.start_timer()

    def start_timer(self):
        self.seconds = 0
        self.update_timer()

    def update_timer(self): 
        self.seconds += 1
        self.label.config(text=f"Timer: {self.seconds} seconds")
        self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

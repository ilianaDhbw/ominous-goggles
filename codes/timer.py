import tkinter as tk

class TimerApp:
    def __init__(self, root):
        
        self.root = root
        self.root.configure(bg="pink")  # Hintergrund auf Rosa setzen

        self.label = tk.Label(root, text="Timer: ",bg="pink", font=("Arial", 15))
        self.label.pack(pady=50, padx=50)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        self.timer_running = False
        self.seconds = 0

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self): 
        if self.timer_running:
            self.seconds += 1
            self.label.config(text=f"Timer: {self.seconds} seconds")
            self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

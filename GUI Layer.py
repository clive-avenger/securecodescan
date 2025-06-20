import tkinter as tk
from tkinter import filedialog, messagebox

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("SecureCodeScan")
        self.text = tk.Text(master, height=20, width=80)
        self.text.pack()
        tk.Button(master, text="Upload Code", command=self.upload_code).pack()
        tk.Button(master, text="Scan", command=self.scan_code).pack()

    def upload_code(self):
        file = filedialog.askopenfilename()
        with open(file, 'r') as f:
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, f.read())

    def scan_code(self):
        code = self.text.get("1.0", tk.END)
        # Pass to RuleEngine and show results
        # Example placeholder
        messagebox.showinfo("Scan Result", "No vulnerabilities found!")

root = tk.Tk()
app = App(root)
root.mainloop()

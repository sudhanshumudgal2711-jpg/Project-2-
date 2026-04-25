import tkinter as tk
from tkinter import messagebox, Toplevel
import math

# Global history list
history = []

# Evaluate the expression safely
def evaluate_expression(event=None):
    try:
        expression = entry.get()
        expression = expression.replace("^", "**")

        # Safe math functions with degrees for trig
        safe_dict = math.__dict__.copy()
        safe_dict.update({
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x))
        })

        result = eval(expression, {"__builtins__": None}, safe_dict)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        history.append(f"{expression} = {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception:
        messagebox.showerror("Error", "Invalid input. Please enter a valid expression.")

# Append text to entry
def append_to_entry(value):
    entry.insert(tk.END, value)

# Clear entry
def clear_entry():
    entry.delete(0, tk.END)

# Delete last character
def delete_last_char(event=None):
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)

# Show history in popup
def show_history():
    if not history:
        messagebox.showinfo("History", "No calculations yet.")
        return
    history_window = Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("300x300")
    history_window.resizable(False, False)
    history_window.configure(bg="white")
    tk.Label(history_window, text="History", font=("Arial", 14, "bold"), bg="white", fg="#2F4F4F").pack(pady=5)
    text_area = tk.Text(history_window, wrap="word", font=("Arial", 12), bg="white", fg="#2F4F4F")
    text_area.pack(expand=True, fill="both", padx=5, pady=5)
    text_area.insert(tk.END, "\n".join(history))
    text_area.config(state="disabled")

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.resizable(False, False)
root.configure(bg="white")  # All white background

# Entry widget (white screen)
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=2, relief="solid", justify="right", bg="white", fg="#2F4F4F")
entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

# Bind keyboard keys
root.bind("<Return>", evaluate_expression)  # Enter key
root.bind("<BackSpace>", delete_last_char)  # Backspace key

# Button layout with Backspace button
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt(', 1, 4), ('^', 1, 5),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sin(', 2, 4), ('cos(', 2, 5),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan(', 3, 4), ('log(', 3, 5),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('(', 4, 3), (')', 4, 4), ('pi', 4, 5),
    ('e', 5, 0), ('C', 5, 1), ('=', 5, 2), ('History', 5, 3), ('⌫', 5, 4)
]

# Create buttons dynamically with white theme
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14, "bold"),
                        command=evaluate_expression, bg="white", fg="#2F4F4F", activebackground="#E0E0E0")
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14, "bold"),
                        command=clear_entry, bg="white", fg="#2F4F4F", activebackground="#E0E0E0")
    elif text == "History":
        btn = tk.Button(root, text=text, width=8, height=2, font=("Arial", 14, "bold"),
                        command=show_history, bg="white", fg="#2F4F4F", activebackground="#E0E0E0")
    elif text == "⌫":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14, "bold"),
                        command=delete_last_char, bg="white", fg="#2F4F4F", activebackground="#E0E0E0")
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14, "bold"),
                        command=lambda t=text: append_to_entry(t), bg="white", fg="#2F4F4F", activebackground="#E0E0E0")
    btn.grid(row=row, column=col, padx=2, pady=2)

# Run the application
root.mainloop()

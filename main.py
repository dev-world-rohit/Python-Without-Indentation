import tkinter as tk
from tkinter import filedialog, messagebox


class TextEditor:
    def __init__(self, root):
        self.content = ""
        self.root = root
        self.root.title("Pytho Without Indentation Execution")
        self.root.config(bg="#222222")

        self.text_widget = tk.Text(root, wrap="word", font=("Courier New", 12), fg="black")
        self.text_widget.pack(expand="yes", fill="both", padx=2, pady=2)

        open_button = tk.Button(root, text="Open", font=(
            'Arial', 10, "bold"), command=self.open_file)
        open_button.pack(side="left")

        execute_button = tk.Button(root, text="Execute", font=(
            'Arial', 10, "bold"), command=self.execute_code)
        execute_button.pack(side="right")

        save_button = tk.Button(root, text="Save", font=('Arial', 10, "bold"), command=self.save_file)
        save_button.pack(side="left")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, self.content)

    def execute_code(self):
        if self.content != '':
            try:
                c_code = self.content
                # statement_seprator = ';'
                # indentation_identifier_open = '{'
                # indentation_identifier_close = '}'
                code_without_newline = """"""
                code_list_without_newline = c_code.split("\n")

                for line in code_list_without_newline:
                    if line != '':
                        line = ' '.join(line.split(' ')).strip()
                        code_without_newline += line

                PYTHON_CODE = """"""
                INDENTATION_NUMBER = 0
                previous_character = None
                new_character = None
                future_character = None

                for i in range(0, len(code_without_newline)):
                    if code_without_newline[i] == ';':
                        new_character = "\n" + "    " * INDENTATION_NUMBER
                    elif code_without_newline[i] == '{':
                        if code_without_newline[i - 1] in ['=', '"', 'f'] or code_without_newline[i - 2] in ['=', '"', 'f']:
                            new_character = code_without_newline[i]
                        else:
                            INDENTATION_NUMBER += 1
                            new_character = ":\n" + "    " * INDENTATION_NUMBER
                    elif code_without_newline[i] == '}':
                        INDENTATION_NUMBER -= 1
                        new_character = "\n" + "    " * INDENTATION_NUMBER
                    else:
                        new_character = code_without_newline[i]
                    PYTHON_CODE += new_character

                exec(PYTHON_CODE)
            except Exception as e:
                print(e)
                messagebox.showerror('Warning', "An error occured while executing the code.\nCheck your code again.")
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                self.content = self.text_widget.get(1.0, tk.END)
                file.write(self.content)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

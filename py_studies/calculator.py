import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        # Display Layout
        self.text_input = tk.StringVar()
        entry_view = tk.Entry(root, textvariable=self.text_input, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        entry_view.grid(row=0, column=0, columnspan=4)

        # Button Layout
        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
        ]

        for (text, line, column) in buttons:
            self._create_button(text, line, column)

    def _create_button(self, text, line, column):
        button_use = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18),
                          command=lambda: self._click(text))
        button_use.grid(row=line, column=column, sticky="nsew")

    def _click(self, item):
        if item == 'C':
            self.expression = ""
        elif item == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(item)
        self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

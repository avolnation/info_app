import customtkinter
import paho.mqtt.client as mqtt

LABEL_EMPLOYEE_INITIAL_TEXT = "Приложите чип или ID карту"
LABEL_ENTRY_TIME_TEXT = "к считывателю"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("Информационная система")
        self.geometry("500x200")


        self.label_employee_initials = customtkinter.CTkLabel(self, text="Привет!")
        self.label_employee_initials.configure(font=("Bahnschrift SemiLight Condensed", 40, "bold"))
        self.label_employee_initials.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.grid_columnconfigure(0, weight=1)




app = App()
app.mainloop()
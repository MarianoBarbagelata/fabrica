import customtkinter
from tkinter        import ttk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('App Fábrica')
        self.geometry(f"{1000}x{650}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # Title
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="App Fábrica", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Create table
        self.create_table = customtkinter.CTkButton(self.sidebar_frame, text="Opción 1")
        self.create_table.grid(row=2, column=0, padx=20, pady=10)

        # Select table
        self.select_table = customtkinter.CTkButton(self.sidebar_frame, text="Opción 2")
        self.select_table.grid(row=3, column=0, padx=20, pady=10)

        # Delete table
        self.delete_table = customtkinter.CTkButton(self.sidebar_frame, text="Opción 3")
        self.delete_table.grid(row=4, column=0, padx=20, pady=10)

        # Dark mode
        self.dark_mode = customtkinter.CTkSwitch(self.sidebar_frame, text=f'Dark Mode', command=self.change_appearance_mode_event)
        self.dark_mode.grid(row=6, column=0, padx=10)

        # Exit
        self.exit = customtkinter.CTkButton(self.sidebar_frame, text="Salir", command=self.destroy)
        self.exit.grid(row=7, column=0, padx=20, pady=20)

    
    def change_appearance_mode_event(self):
        if self.dark_mode.get():
            self.change_appearance("Dark")
        else:
            self.change_appearance("Light")


if __name__ == "__main__":
    app = App()
    app.mainloop()
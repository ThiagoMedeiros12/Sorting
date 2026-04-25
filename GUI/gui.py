import customtkinter as ctk


ctk.set_appearance_mode("dark")


class MainApp():
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1280x720")
        self.app.title("Sorting Algorithm Visualizer")

        self.visualizer = Visualizer(self.app)
        self.visualizer.pack()

        self.app.mainloop()


class Visualizer(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.canvas = ctk.CTkCanvas(self, width=1280, height=550, bg="black")
        self.canvas.pack(side="top", anchor="n")

        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(side="bottom", anchor="s")

        self.sort_button = ctk.CTkButton(self.control_frame, text="Sort", command=self.sort)
        self.sort_button.pack()

    def sort(self, algorithm: str):
        pass

    def start_visualizer(self, algorithm: str):
        pass

    def visualize_sort(self, algorithm: str):
        pass

    def stop_visualizer(self):
        pass


    def reset_visualizer(self):
        pass

    def pause_visualizer(self):
        pass

    def resume_visualizer(self):
        pass

    def step_visualizer(self):
        pass

    def get_algorithm(self, algorithm: str):
        pass

    def get_speed(self, speed: str):
        pass

    def get_array_size(self, array_size: str):
        pass

    def get_array(self, array: list):
        pass

    def get_sorted_array(self, sorted_array: list):
        pass



if __name__ == "__main__":
    main_app = MainApp()
    main_app.app.mainloop()
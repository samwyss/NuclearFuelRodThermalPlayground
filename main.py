from os import mkdir, path
from shutil import rmtree

from PIL import Image, ImageTk  # Add this import for handling image conversion
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import csv
import cv2
import os
import tkinter as tk
import PIL
from src.Config import Config
from src.Model import Model
from tkinter import *


# GUI starts, initializes inputs, and calls Model when "Run" is pressed -------------------------------------------------------------
def main():
    """main driver function for ThermalPlayground"""

    # creating basic frame, background, and layout
    root = Tk()
    root.geometry("1000x600")

    # creates the frame's title and centers it
    title = Label(root, text="Pseudo 3D Heat Generation Simulation for Nuclear Fuel", bg="white",
                  fg="#7e57c2", font=('Helvetica', 18))
    reminder = Label(root, text="Please ensure that each input has an associated value. Do not leave any blank boxes. No negative values are allowed.",
                     bg="white", fg="red", font=('Helvetica', 10))
    title.grid(row=0, column=0)
    reminder.grid(row=1, column=0)

    # creates labels for each input
    label_1 = Label(root, text="Fuel Thickness [m] (Example input: 0.005)", bg="white", fg="#7e57c2", font=('Helvetica', 15))
    label_4 = Label(root, text="Initial Cladding Temperature [K] (Example input: 561)", bg="white", fg="#7e57c2",
                    font=('Helvetica', 15))
    label_5 = Label(root, text="Fuel Volumetric Heat Generation [W/m\u00b3] (Example input: 428e6)", bg="white", fg="#7e57c2",
                    font=('Helvetica', 15))
    label_6 = Label(root, text="Number of Saved Time Steps (Example input: 100)", bg="white", fg="#7e57c2", font=('Helvetica', 15))
    label_7 = Label(root, text="Total Simulation Time [s] (Example input: 3600)", bg="white", fg="#7e57c2", font=('Helvetica', 15))

    # defines a string variable for each input, used later to convert from string to text to float
    fuel_thick = StringVar()
    mat_bul = StringVar()
    fuel_vol = StringVar()
    saved = StringVar()
    end_tim = StringVar()

    # creates an entry widget for each input and sets the input equal to a text variable
    entry_1 = Entry(root, textvariable=fuel_thick)
    entry_4 = Entry(root, textvariable=mat_bul)
    entry_5 = Entry(root, textvariable=fuel_vol)
    entry_6 = Entry(root, textvariable=saved)
    entry_7 = Entry(root, textvariable=end_tim)

    # places each input label
    label_1.grid(row=6, sticky=E)
    label_4.grid(row=8, sticky=E)
    label_5.grid(row=10, sticky=E)
    label_6.grid(row=12, sticky=E)
    label_7.grid(row=14, sticky=E)

    # places each input text box
    entry_1.grid(row=6, column=2)
    entry_4.grid(row=8, column=2)
    entry_5.grid(row=10, column=2)
    entry_6.grid(row=12, column=2)
    entry_7.grid(row=14, column=2)

    # creating the function that closes the window
    def exit_window():
        print("\nWindow is being closed.")
        root.destroy()
        return

    # function gets each input and converts into a floats and an int for simulation purposes
    def start_sim():
        print("\nsimulation is running")
        fuel_thickness = float(fuel_thick.get()); """[m] thickness of fuel"""
        bulk_material_temp = float(mat_bul.get()); """[K] initial cladding temperature"""
        core_heat_generation = float(fuel_vol.get()); """[W/m^3] volumetric heat generation rate of core"""
        num_saved_time_steps = int(saved.get()); """[] number of saved time steps"""
        end_time = float(end_tim.get()); """[s] end time of simulation"""

        # remove old files
        if path.exists("./out"):
            print("\nremoving old output files\n")
            rmtree("./out")

        # make new folder for output files
        mkdir("./out")

        config = Config(
            fuel_thickness,
            bulk_material_temp,
            core_heat_generation,
            num_saved_time_steps,
            end_time,
        )

        # construct model
        model: Model = Model(config)

        # run model here
        model.run()
        return

    # creates our buttons, binds functions to them, and places them in the window
    button_1 = Button(root, text="Process Data", command=exit_window, activebackground='#dfc5fe')
    button_2 = Button(root, text="Run", command=start_sim, activebackground='#dfc5fe')
    button_1.grid(row=20, column=1)
    button_2.grid(row=20, column=2)

    root.mainloop()

    # ------------------------------------------------------------------------------------------------------------------

    # when post-processing button is clicked run this code -------------------------------------------------------------
    # Process Final Temp Distribution
    file3 = open("./out/time.csv", "r")
    timesteps = list(csv.reader(file3, delimiter=","))

    file2 = open("./out/temperature.csv", "r")
    temperatures = list(csv.reader(file2, delimiter=","))

    # Process the length of the fuel rod
    file = open("./out/position.csv", "r")
    position = list(csv.reader(file, delimiter=","))

    def postprocessing():
        # Function to generate the plot and save it as an image
        def generate_temperature_gradient(temps, min_temp, max_temp, timestep, position):
            # Normalize the temperature values between 0 and 1
            norm = plt.Normalize(min_temp, max_temp)

            # Create a color map from blue (cold) to red (hot) using the updated method
            cmap = plt.colormaps['coolwarm']  # Updated from get_cmap()

            # Normalize temperatures to the range [0, 1] and map to colors
            colors = cmap(norm(temps))

            # Plot the row of colors for the given timestep
            fig, ax = plt.subplots(figsize=(len(temps), 2))

            # Create a horizontal line of color blocks
            ax.imshow([colors], aspect='auto',
                      extent=(1.0, float(len(temps)), 0.0, 1.0))  # Convert list to tuple of floats

            # Set labels
            ax.set_xticks(np.arange(1, len(position) + 1))
            ax.set_xticklabels([f"{pos:.4f}" for pos in position])
            ax.set_yticks([])
            ax.set_xlabel('Location index')
            ax.set_title(f'Temperature Gradient at Timestep {timestep}')

            # Show color bar for reference
            cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
            cbar.set_label('Temperature')

            # Save the figure
            plt.savefig(f'./out/temperature_gradient_timestep_{timestep}.png', bbox_inches='tight')
            plt.show()

        maxPosition = float(max(position[0]))
        minPosition = float(min(position[0]))
        maxTemperature = float(max(temperatures[-1]))
        minTemperature = float(min(temperatures[0]))
        j = 0
        rounded_positions = np.linspace(minPosition, maxPosition, len(position[0]))
        for i in timesteps:
            rounded_timestep = round(float(i[0]))  # Round the timestep to the nearest integer
            tempTemps = list(map(float, temperatures[j]))  # Convert temperature values to floats
            generate_temperature_gradient(tempTemps, minTemperature, maxTemperature, rounded_timestep, rounded_positions)
            j += 1

        def create_video_from_images(image_folder, video_name, fps=1):
            # Get a list of image filenames in the specified folder
            images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

            # Sort images by timestep, assuming filename is 'temperature_gradient_timestep_{timestep}.png'
            images.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

            # Read the first image to get the frame size (height, width)
            frame = cv2.imread(os.path.join(image_folder, images[0]))
            height, width, layers = frame.shape

            # Define the codec and create a VideoWriter object to save the video
            video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

            # Iterate through the sorted images and write each one to the video
            for image in images:
                img_path = os.path.join(image_folder, image)
                frame = cv2.imread(img_path)
                video.write(frame)  # Add frame to video

            # Release the VideoWriter object
            video.release()
            print(f"Video saved as {video_name}")

        # Example usage
        image_folder = './out'  # Folder where images are saved
        video_name = './out/temperature_gradient_video.mp4'  # Name of the output video
        fps = 4  # Frames per second (change as needed)

        create_video_from_images(image_folder, video_name, fps)

        def play_video_in_new_window(video_path, root, fps=4, scale_factor=0.5):
            # Create a new window for the video
            video_window = tk.Toplevel(root)
            video_window.title("Temperature Gradient Video")

            # Capture the video using OpenCV
            cap = cv2.VideoCapture(video_path)

            def update_frame():
                nonlocal cap
                # Read a frame from the video
                ret, frame = cap.read()
                if not ret:  # If the video ends, restart it
                    cap.release()
                    cap = cv2.VideoCapture(video_path)
                    ret, frame = cap.read()

                if ret:
                    # Get the original dimensions of the frame
                    height, width, _ = frame.shape

                    # Calculate the new height to maintain aspect ratio
                    new_width = int(width * scale_factor)
                    new_height = int(height * scale_factor)

                    # Resize the frame to the new dimensions
                    resized_frame = cv2.resize(frame, (new_width, new_height))

                    # Convert the frame from BGR (OpenCV format) to RGB
                    resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

                    # Convert the frame to a PIL Image
                    img = PIL.Image.fromarray(resized_frame)

                    # Convert the PIL Image to an ImageTk format for Tkinter
                    imgtk = ImageTk.PhotoImage(image=img)

                    # Update the Label widget with the new frame
                    video_label.imgtk = imgtk
                    video_label.configure(image=imgtk)

                    # Schedule the next frame update (FPS)
                    video_label.after(1000 // fps, update_frame)
                else:
                    cap.release()  # Release the video when done

            # Create a Label to display the video in the new window
            video_label = tk.Label(video_window)
            video_label.pack()  # Pack it to fill the new window

            # Start the video playback
            update_frame()

            # Set the new window size based on the video size (optional)
            video_window.geometry(f"{int(800 * scale_factor)}x{int(600 * scale_factor)}")  # Adjust as needed

        def generate_chart():

            # Example data: temperature distribution
            distance = np.linspace(minPosition, maxPosition, len(position[0]))
            temperature = list(map(float, temperatures[-1]))

            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(distance, temperature)
            ax.set_xlabel('Distance (m)')
            ax.set_ylabel('Temperature (K)')
            ax.set_title('Temperature Distribution')

            return fig

        # Function to update the displayed values
        def update_values(center_temp, bulk_fuel_temp, bulk_clad_temp, avg_coolant_temp):
            center_line_temp.set(f"{center_temp:.2f} K")
            bulk_fuel_temp_var.set(f"{bulk_fuel_temp:.2f} K")
            bulk_clad_temp_var.set(f"{bulk_clad_temp:.2f} K")
            avg_coolant_temp_var.set(f"{avg_coolant_temp:.2f} K")

        # Create the main window
        root = tk.Tk()
        root.title("Final Solution")

        # Create a frame for the input values on the left
        input_frame = tk.Frame(root)
        input_frame.pack(side=tk.LEFT, padx=20, pady=20)

        # Add header label
        header_label = Label(root, text="Final Temperature Distribution Highlights", font=("Arial", 16))
        header_label.pack(pady=10)

        # Create StringVars to hold the values for display
        center_line_temp = StringVar()
        bulk_fuel_temp_var = StringVar()
        bulk_clad_temp_var = StringVar()
        avg_coolant_temp_var = StringVar()

        # Add labels and value fields for the four data points
        Label(input_frame, text="Center Line Temp (K):", font=("Arial", 12)).pack(anchor="w", pady=5)
        Label(input_frame, textvariable=center_line_temp, font=("Arial", 12)).pack(anchor="w", pady=5)

        Label(input_frame, text="Bulk Fuel Temp (K):", font=("Arial", 12)).pack(anchor="w", pady=5)
        Label(input_frame, textvariable=bulk_fuel_temp_var, font=("Arial", 12)).pack(anchor="w", pady=5)

        Label(input_frame, text="Bulk Clad Temp (K):", font=("Arial", 12)).pack(anchor="w", pady=5)
        Label(input_frame, textvariable=bulk_clad_temp_var, font=("Arial", 12)).pack(anchor="w", pady=5)

        #Label(input_frame, text="Average Coolant Temp dr from Clad (k):", font=("Arial", 12)).pack(anchor="w", pady=5)
        #Label(input_frame, textvariable=avg_coolant_temp_var, font=("Arial", 12)).pack(anchor="w", pady=5)

        # Generate the temperature distribution chart
        fig = generate_chart()

        # Create a canvas to embed the chart into tkinter
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, padx=20, pady=20)

        averageBulkFuelTemp = sum(list(map(float, temperatures[-1]))) / len(temperatures[-1])
        # Example of how to update the values dynamically
        intmatbul = int(mat_bul.get())
        # These values would come from your data source
        update_values(max(list(map(float, temperatures[-1]))), averageBulkFuelTemp, intmatbul, 50)

        # Call the function with a scale factor of 0.5 to reduce the video size to 50%
        play_video_in_new_window('./out/temperature_gradient_video.mp4', root, fps=4, scale_factor=0.5)

        # Start the Tkinter main loop
        root.mainloop()

    postprocessing()


    # ------------------------------------------------------------------------------------------------------------------


# runs main
if __name__ == "__main__":
    main()

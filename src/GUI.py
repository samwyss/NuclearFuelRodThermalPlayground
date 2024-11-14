from tkinter import *

#creating basic frame, background, and layout
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
label_1 = Label(root, text="Fuel Thickness [m]", bg="white", fg="#7e57c2", font=('Helvetica', 15))
label_4 = Label(root, text="Initial Cladding Temperature [K]", bg="white", fg="#7e57c2",
                    font=('Helvetica', 15))
label_5 = Label(root, text="Fuel Volumetric Heat Generation [W/m\u00b3]", bg="white", fg="#7e57c2",
                    font=('Helvetica', 15))
label_6 = Label(root, text="Number of Saved Time Steps", bg="white", fg="#7e57c2", font=('Helvetica', 15))
label_7 = Label(root, text="Total Simulation Time [s]", bg="white", fg="#7e57c2", font=('Helvetica', 15))

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

# function gets each input and converts into a float for simulation purposes, ONLY REQUIREMENT: there must be an input for each variable
def start_sim():
    print("\nSimulation is running.")
    fuel_thickness = float(fuel_thick.get()); """[m] thickness of fuel"""
    bulk_material_temp = float(mat_bul.get()); """[K] initial cladding temperature"""
    core_heat_generation = float(fuel_vol.get()); """[W/m^3] volumetric heat generation rate of core"""
    num_saved_time_steps = int(saved.get()); """[] number of saved time steps"""
    end_time = float(end_tim.get()); """[s] end time of simulation"""
    print("\nAll saved entries are as follows: ", fuel_thickness, bulk_material_temp, core_heat_generation, num_saved_time_steps, end_time)
    return

#creates our buttons, binds functions to them, and places them in the window
button_1 = Button(root, text = "Exit", command = exit_window, activebackground = '#dfc5fe')
button_2 = Button(root, text = "Run", command = start_sim, activebackground = '#dfc5fe')
button_1.grid(row = 20, column = 1)
button_2.grid(row = 20, column = 2)

root.mainloop()

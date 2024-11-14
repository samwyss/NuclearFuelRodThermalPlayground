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

#creating the function that closes the window
def exitwindow():
    print("\nWindow is being closed.")
    root.destroy()
    return

#function gets each input and converts into a float for simulation purposes, ONLY REQUIREMENT: there must be an input for each variable
def startsim():
    print("\nSimulation is running.")
    fuel_thickness = float(fuelthick.get())
    cladding_thickness = float(cladthick.get())
    coolant_temp = float(cooltemp.get())
    bulk_material_temp = float(matbul.get())
    core_heat_generation = float(fuelvol.get())
    num_saved_time_steps = float(saved.get())
    end_time = float(endtim.get())
    if fuel_thickness or cladding_thickness or coolant_temp or bulk_material_temp or core_heat_generation or num_saved_time_steps or end_time < 0:
        print("\nMake sure all input values are postive.")
    else:
        print("\nAll saved entries are as follows: ", fuel_thickness, cladding_thickness,coolant_temp, bulk_material_temp,core_heat_generation, num_saved_time_steps, end_time)
    return

#creates our buttons, binds functions to them, and places them in the window
button_1 = Button(root, text = "Exit", command = exitwindow, activebackground = '#dfc5fe')
button_2 = Button(root, text = "Run", command = startsim, activebackground = '#dfc5fe')
button_1.grid(row = 20, column = 1)
button_2.grid(row = 20, column = 2)

root.mainloop()

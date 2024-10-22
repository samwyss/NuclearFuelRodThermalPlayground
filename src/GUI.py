from tkinter import *

#creating basic frame, background, and layout
root = Tk()
root.geometry("900x700")

title = Label(root, text = "Pseudo 3D Heat Generation Simulation Between Nuclear Fuel and Cladding", bg = "white", fg = "blue", font = 20)
title.grid(row = 0, column = 0)

label_1 = Label(root, text = "Fuel Thickness [m]", bg = "white", fg = "blue", font = 15)
label_2 = Label(root, text = "Cladding Thickness [m]", bg = "white", fg = "blue", font = 15)
label_3 = Label(root, text = "Coolant Temperature [K]", bg = "white", fg = "blue", font = 15)
label_4 = Label(root, text = "Initial Material Bulk Temperature [K]", bg = "white", fg = "blue", font = 15)
label_5 = Label(root, text = "Fuel Volumetric Heat Generation [W/m\u00b3]", bg = "white", fg = "blue", font = 15)
label_6 = Label(root, text = "Number of Saved Time Steps", bg = "white", fg = "blue", font = 15)
label_7 = Label(root, text = "End Time [s]", bg = "white", fg = "blue", font = 15)

entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_4 = Entry(root)
entry_5 = Entry(root)
entry_6 = Entry(root)
entry_7 = Entry(root)

label_1.grid(row = 4, sticky = E)
label_2.grid(row = 6, sticky = E)
label_3.grid(row = 8, sticky = E)
label_4.grid(row = 10, sticky = E)
label_5.grid(row = 12, sticky = E)
label_6.grid(row = 14, sticky = E)
label_7.grid(row = 16, sticky = E)

entry_1.grid(row = 4, column = 3)
entry_2.grid(row = 6, column = 3)
entry_3.grid(row = 8, column = 3)
entry_4.grid(row = 10, column = 3)
entry_5.grid(row = 12, column = 3)
entry_6.grid(row = 14, column = 3)
entry_7.grid(row = 16,column = 3)

def exitwindow():
    print("\nWindow is being closed.")
    root.destroy()
    return

def startsim():
    print("\nSimulation is running.")
    fuel_thickness = float(entry_1.get())
    cladding_thickness = float(entry_2.get())
    coolant_temp = float(entry_3.get())
    bulk_material_temp = float(entry_4.get())
    core_heat_generation = float(entry_5.get())
    num_saved_time_steps = float(entry_6.get())
    end_time = float(entry_7.get())
    print("All saved entries are as follows: ", fuel_thickness, cladding_thickness,coolant_temp, bulk_material_temp,core_heat_generation, num_saved_time_steps, end_time)
    print("Let's add fuel thickness and cladding thickness: ", (fuel_thickness + cladding_thickness)) #checking that numbers are being returned as floats
    return

button_1 = Button(root, text = "Exit", command = exitwindow)
button_2 = Button(root, text = "Run", command = startsim)
button_1.grid(row = 20, column = 1)
button_2.grid(row = 20, column = 2)



root.mainloop()

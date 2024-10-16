from tkinter import *

#creating basic frame, background, and layout
root = Tk()
root.geometry("900x700")

title = Label(root, text = "Pseudo 3D Heat Generation Simulation Between Nuclear Fuel and Cladding", bg = "white", fg = "blue", font = 20)
title.grid(row = 0, column = 0)

label_1 = Label(root, text = "Fuel Thickness [cm]", bg = "white", fg = "blue", font = 15)
label_2 = Label(root, text = "Cladding Thickness [cm]", bg = "white", fg = "blue", font = 15)
label_3 = Label(root, text = "Water Temperature [°C]", bg = "white", fg = "blue", font = 15)
label_4 = Label(root, text = "Initial Material Bulk Temperature [°C]", bg = "white", fg = "blue", font = 15)
label_5 = Label(root, text = "Heat Sink Temperature [°C]", bg = "white", fg = "blue", font = 15)
label_6 = Label(root, text = "Fuel Volumetric Heat Generation [W/m\u00b3]", bg = "white", fg = "blue", font = 15)
label_7 = Label(root, text = "Number of Saved Time Steps", bg = "white", fg = "blue", font = 15)

entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_4 = Entry(root)
entry_5 = Entry(root)
entry_6 = Entry(root)
entry_7 = Entry(root)

label_1.grid(row = 4, sticky = E)
label_2.grid(row = 5, sticky = E)
label_3.grid(row = 6, sticky = E)
label_4.grid(row = 7, sticky = E)
label_5.grid(row = 8, sticky = E)
label_6.grid(row = 9, sticky = E)
label_7.grid(row = 10, sticky = E)

entry_1.grid(row = 4, column = 1)
entry_2.grid(row = 5, column = 1)
entry_3.grid(row = 6, column = 1)
entry_4.grid(row = 7, column = 1)
entry_5.grid(row = 8, column = 1)
entry_6.grid(row = 9, column = 1)
entry_7.grid(row = 10,column = 1)


root.mainloop()

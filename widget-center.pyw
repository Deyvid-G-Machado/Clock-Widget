from tkinter import *
import json
from time import strftime
import os

left_distance_entry = None
top_distance_entry = None
config_filename = "config.json"
root = None

def start_clock():
    global left_distance_entry, top_distance_entry, config_filename  
    x = left_distance_entry.get()
    y = top_distance_entry.get()
    update_clock_position(config_filename, x, y)
    create_clock_widget(x, y)

def close_widget():
    root.destroy()
    os.system('taskkill /im pythonw.exe')

# Read clock positions
def read_clock_position(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get("clock_position", {})
    except FileNotFoundError:
        return {}

# Save and update clock positions
def update_clock_position(filename, new_x, new_y):
    data = {"clock_position": {"x": new_x, "y": new_y}}
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Create and show the clock
def create_clock_widget(x, y):
    window = Tk()
    rel = Label(window, font='Helvetica 50 bold', fg='white', bg='black')
    rel.pack()
    window.overrideredirect(True)
    window.attributes("-transparentcolor", "black")
    window.geometry('+{}+{}'.format(x, y))

    def tic():
        rel['text'] = strftime('%H:%M:%S')
    
    def tac():
        tic()
        rel.after(1000, tac)
    
    tac()
    window.mainloop()

def main():
    global left_distance_entry, top_distance_entry, config_filename, root

    root = Tk()
    root.title("Clock Widget")

    # Widgets
    instruction_label = Label(root, text="Set the widget's position:")
    left_distance_label = Label(root, text="Left distance: ")
    top_distance_label = Label(root, text="Top distance: ")

    left_distance_entry = Entry(root)
    top_distance_entry = Entry(root)

    confirm_button = Button(root, text="Confirm", command=start_clock)
    close_button = Button(root, text="Close Widget", command=close_widget)

    # Widgets positioning
    instruction_label.grid(row=0, columnspan=2, pady=10)
    left_distance_label.grid(row=1, column=0, sticky=W)
    left_distance_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    top_distance_label.grid(row=2, column=0, sticky=W)
    top_distance_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    confirm_button.grid(row=3, column=0, padx=5, pady=10)
    close_button.grid(row=3, column=1, padx=5, pady=10)

    config_filename = "config.json"
    clock_positions = read_clock_position(config_filename)
    left_distance_entry.insert(0, str(clock_positions.get("x", "")))
    top_distance_entry.insert(0, str(clock_positions.get("y", "")))

    root.mainloop()

main()

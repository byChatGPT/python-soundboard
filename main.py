import os
import json
from tkinter import filedialog, simpledialog, Tk, Button
import pygame

pygame.mixer.init()

# Load the list of buttons from buttons.json if it exists
basedir = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(basedir, 'buttons.json')

if os.path.isfile(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        buttons = data['buttons']
else:
    with open(json_file, 'w') as f:
        json.dump({'buttons': []}, f)
        buttons = []

# Function to play an audio clip
def play_audio(audio_path):
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

# Function to add a new button
def add_button():
    # Open a file dialog to allow the user to select an audio clip
    file_path = filedialog.askopenfilename()

    # Get the filename without the path
    audio_name = os.path.basename(file_path)

    # Prompt the user to enter a name for the button
    name = simpledialog.askstring("Button Name", "Enter a name for the button:")

    if name is not None and name.strip() != "":
        # Add the new button to the list
        buttons.append({'name': name, 'audio_name': audio_name})

        # Create a new button in the GUI for the new audio clip
        Button(root, text=name, command=lambda: play_audio(os.path.join('audio', audio_name))).pack()

        # Save the updated list of buttons to buttons.json
        with open(json_file, 'w') as f:
            json.dump({'buttons': buttons}, f)

# Create the main window
root = Tk()

# Add a button to add a new audio clip
add_button_button = Button(root, text="Add Button", command=add_button)
add_button_button.pack()

# Add a button for each audio clip
for button in buttons:
    audio_path = os.path.join('audio', button['audio_name'])
    button_name = button['name']
    Button(root, text=button_name, command=lambda audio_path=audio_path: play_audio(audio_path)).pack()

# Start the main loop
root.mainloop()

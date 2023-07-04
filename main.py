import pyautogui as p
import tkinter as tk
import time
import subprocess
import os
import string
import string
import random
import openai


openai.api_key = 'put API key here'





def runWebBuilder():




    description = p.prompt("Please enter a description of your website", "Dickens Web Builder")




    def generate_html_code(description):
        # Define the prompt with system and user instructions
        prompt = "You are a helpful assistant that generates HTML code for websites.\nUser: {}\nAssistant:".format(description)

        # Generate HTML code using ChatGPT
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=1000,
            temperature=0.6
        )

        # Extract the assistant's reply containing the HTML code
        assistant_reply = response.choices[0].text.strip()

        # Assemble the complete HTML document
        html_code = """
        <html>
        <head>
            <title>Generated Website</title>
        </head>
        <body>
            {}
        </body>
        </html>
        """.format(assistant_reply)

        return html_code


    # Generate HTML code based on the description
    generated_html_code = generate_html_code(description)

    # Print the generated HTML code
    #print("Generated HTML code:")
    #print(generated_html_code)

    #variable setup

    def generate_random_string(length):
        # Define the set of characters to choose from
        characters = string.ascii_letters + string.digits

        # Generate a random string of the specified length
        random_string = ''.join(random.choice(characters) for _ in range(length))

        return random_string
    def close_process(process_name):
        os.system(f"taskkill /f /im {process_name}.exe")

    folderName = generate_random_string(5)
    screen_width, screen_height = p.size()
    username = os.getenv("USERNAME")
    subprocess.call("explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}", shell=True)

    search_bar_x_ratio = 0.4 
    search_bar_y_ratio = 0.98  
    search_bar_x = int(screen_width * search_bar_x_ratio)
    search_bar_y = int(screen_height * search_bar_y_ratio)

    os.startfile("cmd.exe")
    time.sleep(3)
    p.write(fr"mkdir C:\Users\{username}\Desktop\websiteBuilder{folderName}")
    time.sleep(3) #C:\Users\alxdi\Desktop\websiteBuilder
    p.press("Enter")
    time.sleep(3)
    close_process("cmd")
    time.sleep(3)

    p.moveTo(search_bar_x, search_bar_y)
    p.leftClick()
    time.sleep(0.5)
    p.write("Visual Studio Code", interval=0.25)
    p.press("Enter")
    time.sleep(2)
    p.hotkey("win", "up")

    p.hotkey("ctrl", "k")
    p.hotkey("ctrl", "o")
    time.sleep(0.5)
    p.hotkey("alt","d")
    p.press("back")
    p.write(fr"C:\Users\{username}\Desktop")
    time.sleep(2)
    p.press("Enter")
    time.sleep(2)
    p.hotkey("ctrl", "e")
    p.write(f"websiteBuilder{folderName}")

    time.sleep(3)
    p.press("down")
    time.sleep(0.5)

    p.press("down")
    time.sleep(0.5)

    p.press("tab")
    time.sleep(0.5)

    p.press("tab")
    time.sleep(0.5)

    p.press("Enter")
    time.sleep(2)

    p.hotkey("ctrl", "n")
    time.sleep(2)

    p.hotkey("ctrl", "k")
    p.press("m")
    time.sleep(2)

    p.write("html")
    time.sleep(3)
    p.press("Enter")
    time.sleep(0.5)
    p.hotkey("ctrl", "s")
    p.press("tab")
    time.sleep(0.5)
    p.press("tab")
    p.press("Enter")
    time.sleep(1)
    p.write(generated_html_code)


root = tk.Tk()

root.title = "Alex Dickens Website builder"

header = tk.Label(root, text="Website Builder AI")
header.pack()

button = tk.Button(root, text="start", command=runWebBuilder)
button.pack()

while(True):
    root.update()







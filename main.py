from tkinter import *
import requests
import translators as ts

def get_quote():
    data = requests.get("https://api.kanye.rest")
    quote = data.json()["quote"]
    translated_quote = ts.google(quote, from_language="en", to_language="tr")
    canvas.itemconfig(quote_text, text=quote)
    canvas.itemconfig(translated_text, text=translated_quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(150, 120, text="", width=250, font=("Arial", 15, "bold"), fill="black")
translated_text = canvas.create_text(150, 250, text="", width=250, font=("Arial", 15, "bold"), fill="red")


canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
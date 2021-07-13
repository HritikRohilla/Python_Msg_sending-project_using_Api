from base64 import b64encode
import eel

import json
import requests
from tkinter import *
from PIL import ImageTk,Image

def wt(city):
    # Required Details
    root = Tk()
    root.geometry("320x320")
    root.title("Weather App")
    root.configure(bg='white')

    # for images

    img = ImageTk.PhotoImage(Image.open('um.png'))
    panel = Label(root, image=img)
    panel.place(x=112, y=3)

    lable_0 = Label(root, text="Weather App", width=20, bg='white', font=("bold", 20), fg='brown')
    lable_0.place(x=0, y=93)

    lable_2 = Label(root, text="Temprature : ", width=20, bg='white', font=("bold", 10), fg='blue')
    lable_2.place(x=62, y=220)

    lable_3 = Label(root, text="Pressure : ", width=20, bg='white', font=("bold", 10), fg='blue')

    lable_3.place(x=62, y=240)

    lable_5 = Label(root, text="Description : ", width=20, bg='white', font=("bold", 10), fg='blue')
    lable_5.place(x=62, y=260)

    lable_temp = Label(root, text="...", width=5, bg='white', font=("bold", 10), fg='blue')
    lable_temp.place(x=192, y=220)

    lable_pres = Label(root, text="...", width=5, bg='white', font=("bold", 10), fg='blue')
    lable_pres.place(x=192, y=240)

    lable_desc = Label(root, text="...", width=5, bg='white', font=("bold", 10), fg='blue')
    lable_desc.place(x=192, y=260)

    # api config
    api_key = "e25bd8527b33c5eca8d02a2c60f7cd58"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # module response get

    response = requests.get(complete_url)
    x = response.json()

    if ["cod"] != '404':
        y = x["main"]
        current_temprature = y["temp"]
        current_pressure = y["pressure"]

        z = x["weather"]
        weather_description = z[0]["description"]

        lable_pres.configure(text=current_pressure)
        lable_temp.configure(text=current_temprature)
        lable_desc.configure(text=weather_description)
    else:
        lable_pres.configure(text="Err")
        lable_temp.configure(text="Err")
        lable_desc.configure(text="Err")


    lable_unit = Label(root, text="Temprature in Kelvin And Pressure in mb", width=35, bg='white', font=("bold", 10),
                       fg='brown')
    lable_unit.place(x=22, y=290)

    mainloop()


eel.init('web')

@eel.expose
def generate_qr(data):
    city=data
    print(city)
    wt(city)
    return city

eel.start('index2.html', size=(1000, 600))


from tkinter import *
from pyowm import OWM
from pyowm.utils.config import get_default_config

root = Tk()
root['bg'] = '#fafafa'
root.title('Погодное приложение')
root.geometry('700x550')
root.resizable(width=False, height=False)

frame = Frame(root, bg='#ffb700', bd=5)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Введите название города:', bg='gray', font=40)
title.pack()

config_dict = get_default_config()
config_dict['language'] = 'ru'

city_entry = Entry(frame, bg='white', font=30)
city_entry.pack()

def get_weather():
    place = city_entry.get()
    if place:
        owm = OWM('cf563df0de261ce5af9be6ec502a4fa8', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        status = w.detailed_status
        temp = w.temperature('celsius')['temp']
        humidity = w.humidity
        wind_speed = w.wind()['speed']
        result_label.config(text="Погода в городе {}:\nСтатус: {}\nТемпература: {} градусов по Цельсию\nВлажность: {}%\nСкорость ветра: {} м/с".format(
            place, status, round(temp), humidity, wind_speed))
    else:
        result_label.config(text="Вы не ввели название города")

get_weather_btn = Button(frame, text='Получить погоду', bg='pink', command=get_weather)
get_weather_btn.pack()

result_label = Label(frame, bg='white', font=30)
result_label.pack(fill=BOTH, expand=True)

root.mainloop()
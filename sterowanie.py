import Tkinter as tk
import RPi.GPIO as gpio
import os


#Powiązanie pinów z kierunkiem obrotów silników
PrawyPrzod  = 31
PrawyTyl = 35
LewyPrzod = 40
LewyTyl  = 37


def init():
    #setup GPIO using board numbering
    gpio.setmode(gpio.BOARD)


    gpio.setup(PrawyPrzod, gpio.OUT)
    gpio.setup(PrawyTyl, gpio.OUT)
    gpio.setup(LewyPrzod, gpio.OUT)
    gpio.setup(LewyTyl, gpio.OUT)


def przod():
    gpio.output(LewyPrzod, gpio.HIGH)
    gpio.output(PrawyPrzod, gpio.HIGH)


def tyl():
    gpio.output(LewyTyl, gpio.HIGH)
    gpio.output(PrawyTyl, gpio.HIGH)


def lewo():
    gpio.output(LewyTyl, gpio.HIGH)
    gpio.output(PrawyPrzod, gpio.HIGH)


def prawo():
    gpio.output(LewyPrzod, gpio.HIGH)
    gpio.output(PrawyTyl, gpio.HIGH)


def stop():
    gpio.output(LewyPrzod, gpio.LOW)
    gpio.output(LewyTyl, gpio.LOW)
    gpio.output(PrawyPrzod, gpio.LOW)
    gpio.output(PrawyTyl, gpio.LOW)


# Wywołuje sie po kazdym wcisnieciu przycisku
def key_input(event):
    init()
    # Wchodzienie z programu
    if ord(event.char) == 27:
        gpio.cleanup()
        quit()
   	 
    print 'Przycisk:', event.char
    key_press = event.char.lower()


    if key_press == 'w':
        przod()
    elif key_press == 's':
        tyl()
    elif key_press == 'a':
        lewo()
    elif key_press == 'd':
        prawo()
	elif key_press ==  'p':
		os.system("sudo shutdown -h now")
    else:
        print 'Zły klawisz! Użyj W,A,S,D do poruszania się.'


# Wywołuje się gdy puścisz klawisz
def key_release(event):
    stop()


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.bind('<KeyRelease>', key_release)
command.mainloop()
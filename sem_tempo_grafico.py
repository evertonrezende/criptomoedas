from tkinter import *
import tkinter.messagebox
import json
import requests

class TempGraf():
    
    def sem_tg():
        header= {'Content-Type':'application/json; charset=utf-8'}
        tkinter.messagebox.showinfo('Erro', 'Sem tempo grafico!!')
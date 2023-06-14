
import customtkinter as tk
import random as rndm

tk.set_appearance_mode("dark")#ciemny motyw dla aplikacji
tk.set_default_color_theme("dark-blue")#ciemno niebieski jako kolor pomocny

def script():
    try:
        value1 = num1.get()
        value2 = num2.get()
        value1 = int(value1)
        value2 =int(value2)
        randomNumber = rndm.randint(value1, value2)
        answer.configure(text = randomNumber, fg_color = "#212121")
    except:
        answer.configure(text = "ERR", fg_color = "#FF0000")
    

#ustawienia okna
root = tk.CTk()
root.geometry("800x600")
root.iconbitmap(True, "icon.ico")
root.title("Random Number Generator")

#obramowanie
frame = tk.CTkFrame(master = root)
frame.pack(pady = 20, padx = 40, fill = "both", expand = True) #trzeba w packu określić bo python jest retarted

#nagłówek
header = tk.CTkLabel(master = frame, text="Random Number Generator", font=("comic Sans MS", 37, "bold"), padx = 20, pady = 20)
header.pack()

#obramowanie dla inputów
numberFrame = tk.CTkFrame(master=frame)
numberFrame.pack()

#range of random numbers
num1 = tk.CTkEntry(master = numberFrame, placeholder_text = "min. value that can be generated", width = 200)
num1.pack(pady = 10, padx = 10, side = "left")

dash = tk.CTkLabel(master = numberFrame, text="-", font=("arial", 20))
dash.pack(side = "left")

num2 = tk.CTkEntry(master = numberFrame, placeholder_text = "max. value that can be generated", width = 200)
num2.pack(pady = 10, padx = 10, side = "left")

#button activating generator
button = tk.CTkButton(master = frame, text = "Generate", command = script)
button.pack(pady = 20, padx = 20)

#frame with answer
answerFrame = tk.CTkFrame(master = frame, width=100)
answerFrame.pack(pady = 10, padx = 10)

#label with answer
answer = tk.CTkLabel(master = answerFrame, text = "", font=("arial", 30), fg_color="#212121", wraplength = 700)
answer.pack()

root.mainloop()


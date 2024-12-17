import tkinter as tk
from tkinter import ttk
import random
#Nimi1 = input("sisesta oma nimi")


#elusolendid-------------------------------------------------------------------------
player1 = 100
karu = 150
lind = 10
hiir = 15
haavatu = 0

#kohad-------------------------------------------------------------------------------
maja = ["kook", "õun","hiir", "tool"]
surnuaed = ["haud", "kont", "kont", "puu"]
tiik = ["kala", "kala", "kala", "pilliroog"]
mets = ["seen", "puu", "puu", "seen", "kivi", "puu"]
aas = ["lill", "lill", "lill", "seen"]
põld = ["nisu", "lind", "karu", "nisu", "nisu", "seen"]

#taskud--------------------------------------
tasku = []
liiga_suur_ese = ["karu", "puu", "lind", "hiir", "haud", "kivi"]

#oluline kraam mis ei sobi kuskile---------------------------------------------------
koht = aas
kohad = [maja, surnuaed, tiik, aas, põld]
suva = 0
damage = 0


# Käsud-------------------------------------------._.----------------
#while True: #kõige süda. (:
    #try:
    #def käsud(sisend):
#sisend = input(": ")    #Püha algus ksureale

def game_brain(sisend):
    sisend = sisend.lower()
    sisend = sisend.split()

    
    if sisend[0] == "go":
        if sisend[1] == "maja":
            return "Saabusid majja"
            koht = maja
        if sisend[1] == "surnuaed":
            return "Saabusid surnuaeda"
            koht = surnuaed
        if sisend[1] == "tiik":
            return "Saabusid tiigi äärde"
            koht = tiik
        if sisend[1] == "aas":
            return "Saabusid aasale"
            koht = aas
        if sisend[1] == "põld":
            return "Saabusid põllule"
            koht = põld
        if sisend[1] == "mets":
            return "Saabusid metsa"
            koht = mets

    #scan ----------------------------------------------------    

    elif sisend[0] == "scan":
        for paik in koht:
            koht2 = ( str(koht) + "," + str(koht[paik]))
        return koht

    #shoot-----------------------------------------------        

    elif sisend[0] == "shoot":
        suva = random.randint(1, 6)
        if sisend[1] in koht:
            if not suva == 4:
                damage = 20
            else:
                damage = 100
            
            if sisend[1] == "karu":
                karu -= damage
                haavatu = karu
            if sisend[1] == "hiir":
                hiir -= damage
                haavatu = hiir
            if sisend[1] == "lind":
                lind -= damage
                haavatu = lind
            if haavatu <= 0:
                return(sisend[1] + " on surnud.")
                koht += [(str(sisend[1]) + "liha")]
                koht += [sisend[1] + "korjus"]
                koht.remove(sisend[1])
        

            


    #Korjesüsteem----------------------------------------------        

    elif sisend[0] == "pick":
        if len(tasku) == 10:
            return "Taskud on täis."
        elif sisend[1] in liiga_suur_ese:
            return "Ese on liiga raske."
        else:
            if sisend[1] in koht:
                tasku += [sisend[1]]
                koht.remove(sisend[1])
            
            elif "liha" in sisend[1]:
                for sõna in koht:
                    if sõna == sisend[1]:
                        tasku += [sisend[1]]
                        koht.remove(sisend[1])
                    
                        
                      

    #maha viskamis süsteem--------------------------------------
                            
    elif sisend[0] == "drop":
        
        if sisend[1] == "nisu" or sisend[1] == "õun" or sisend[1] == "kont" or sisend[1] == "kook" or sisend[1] == "lill": 
            koht += [sisend[1]]
            tasku.remove(sisend[1])
        elif "liha" in sisend[1]:
            koht += [sisend[1]]
            tasku.remove(sisend[1])
                    
    #Tasku vaatamine -------------------------------------------
                    
                    
    elif sisend[0] == "inv":
        if len(tasku) == 0:
            return "Tasku on tühi."
        else:
            return("Taskus on " + str(tasku) + ".")
                    
    #püha söömine-------------------------------------------------
    elif sisend[0] == "eat" or sisend[0] == "heal":
        if sisend[1] == "õun":
            suva = random.randint(5, 30)
            player1 += suva
        if sisend[1] == "kook":
            suva = random.randint(10, 25)
        if sisend[1] == "seen":
            suva = random.randint(-30, 10)
                
        if "liha" in sisend[1]:
            suva = random.randint(20, 50)
        player1 += suva
        if suva < 0:
            return "Oush"
                
                
    #elu kontrollimine--------------------------------------------
    elif sisend[0] == "healt" or sisend[0] == "elud":
        return("elud: " + str(player1))

    #Vaatamine

    elif sisend[0] == "look" or sisend[0] == see:
        if koht == "mets":
            return"Näha on aas ja põld"
            mindavad_kohad = ["pold", "aas"]
                    
    else:
        return "käsku ei leitud."
    #errori tapja------------------------------------------------
        #except Exception as e:
            #print(f"Sisestasit midagi valesti: {e}")
        


def send_message():
    sisend = input_var.get().strip()
    if sisend:
        # Display user message in chat area
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f"User: {sisend}\n", "user_tag")
        chat_area.config(state='disabled')
        
        # Clear input field
        input_var.set("")

        # Get reply from the game_brain function
        reply = game_brain(sisend)

        # Display reply in chat area
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f"Action: {reply}\n", "bot_tag")
        chat_area.config(state='disabled')
        
def on_enter_key(event):
    send_message()

# GUI---------------------------------------------------

root = tk.Tk()
root.title("Rule-Based Chat IDE")

# Configure grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)

# Frame for chat area and input
chat_frame = ttk.Frame(root, padding="10")
chat_frame.grid(row=0, column=0, sticky="nsew")

# Frame for hints/keywords
hint_frame = ttk.Frame(root, padding="10", relief="groove")
hint_frame.grid(row=0, column=1, sticky="ns")

# Chat area (scrollable)
chat_text_frame = ttk.Frame(chat_frame)
chat_text_frame.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(chat_text_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

chat_area = tk.Text(chat_text_frame, wrap="word", yscrollcommand=scrollbar.set, state="disabled")
chat_area.pack(side="left", fill="both", expand=True)
scrollbar.config(command=chat_area.yview)

# Tags for formatting
chat_area.tag_config("user_tag", foreground="blue")
chat_area.tag_config("bot_tag", foreground="green")

# Input field and send button
input_frame = ttk.Frame(chat_frame)
input_frame.pack(fill="x", pady=5)

input_var = tk.StringVar()
input_entry = ttk.Entry(input_frame, textvariable=input_var)
input_entry.pack(side="left", fill="x", expand=True, padx=(0,5))
input_entry.bind("<Return>", on_enter_key)

send_button = ttk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side="right")

# Hint panel
hint_label = ttk.Label(hint_frame, text="Keywords / Commands:", font=("Arial", 12, "bold"))
hint_label.pack(pady=(0,10))

# Example keywords
keywords = ["hello", "bye", "help", "info"]

for kw in keywords:
    kw_label = ttk.Label(hint_frame, text=kw, font=("Arial", 10))
    kw_label.pack(anchor="w")

# Sample rules display (just informational)
rules_frame = ttk.LabelFrame(hint_frame, text="Sample Rules", padding="5")
rules_frame.pack(fill="x", pady=10)

rule1_label = ttk.Label(rules_frame, text='Rule 1: If user says "hello" → respond with greeting.')
rule1_label.pack(anchor="w")
rule2_label = ttk.Label(rules_frame, text='Rule 2: If user says "bye" → respond with farewell.')
rule2_label.pack(anchor="w")

# Set up the main event loop
root.mainloop()



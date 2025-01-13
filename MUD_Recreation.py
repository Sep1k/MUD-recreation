import tkinter as tk                
from tkinter import ttk

import random
#Nimi1 = input("sisesta oma nimi")


#elusolendid-------------------------------------------------------------------------
player1 = 100
karu = 150
lind = 10
liblikas = 1
hiir = 15
haavatu = 0


#world gen pahn

ax = 0 
aas = [] 
ese = "" 
eluka_lisamine = 1

lisatav = "" 

#kohad-------------------------------------------------------------------------------

maja = []
surnuaed = []
tiik = []
aas = []
põld = []
kirik = []
kelder = []
pööning = []
mets = []
kohad = [maja, surnuaed, tiik, aas, põld, kirik, kelder, pööning, mets]

mindavad_kohad = ["maja", "surnuaed", "tiik", "aas", "põld", "mets", "kirik", "kelder", "pööning"]
#taskud--------------------------------------
tasku = []
liiga_suur_ese = ["karu", "puu", "haud", "kivi", "laud", "luukere"]
lastavad = ["karu", "hiir", "lind", "lamp", "liblikas", "kala"]

#oluline kraam mis ei sobi kuskile--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------
koht = aas
koht2 = []
suva = 0
damage = 0
poise = 0
poises = 0
poiseh = 0
weapon = "käed"
weapons = ["kalasnikov", "puhkpüss", "nuii", "piits" ]
kordaja = 1
kord = 0
relvad = ["kalasnikov", "puhkpüss", "nuii", "piits" ]
poise_damage = 0
poise_kordaja = 0

aas_esemed = ["lill", "lill", "lill", "seen", "liblikas", "puu"] 
põld_esemed = ["nisu", "lind", "karu", "nisu","nisu","kivi", "kivi", "nisu", "nisu", "seen"]
mets_esemed = ["puu", "puu","kivi", "puu", "kivi", "seen", "seen"]
maja_esemed = ["kook", "õun","hiir", "tool", "tool", "laud"]
surnuaed_esemed = ["haud", "kont", "kont", "puu"]
tiik_esemed = ["kala", "kala", "kala", "pilliroog", "puhkpüss"]
kelder_esemed = ["luukere", "kett", "kett", "piits", "pealuu", "kont"]
pööning_esemed = ["hallitusseen", "lamp", "kalasnikov","kuulid_x20"]
kirik_esemed = ["piibel", "küünal", "küünal"]

esemed_list = [maja_esemed, surnuaed_esemed, tiik_esemed, aas_esemed, põld_esemed, kirik_esemed, kelder_esemed, pööning_esemed, mets_esemed]

for i in range(len(kohad)):
    randomhulk = random.randint(3, 10)
    ax = 0
    while ax != randomhulk:
        random_value = random.randint(0, len(esemed_list[i])-1)
        ese = esemed_list[i][random_value]
        
        if ese in ["liblikas", "karu", "lind", "hiir"] and eluka_lisamine > 0:
            eluka_lisamine -= 1
            esemed_list[i].remove(ese)
        
        kohad[i].append(ese)
        ax += 1
    eluka_lisamine = 1

for item in kohad:
    print(item)
for i in kohad:
    for itam in i:
        if itam == "kalasnikov" or itam == "puhkpüss":
            i.append("kuulid_x25")
            break
        elif itam == "puhkpüss":
            i.append("nooled_x10")
            break

# Käsud-------------------------------------------._.-------------------------------------------------------------------------------------------------------------------------------------------- --------
#while True: #kõige süda. (:
    #try:
    #def käsud(sisend):
#sisend = input(": ")    #Püha algus ksureale

def game_brain(sisend):
    global player1, karu, lind, hiir, liblikas, haavatu, koht, kord, kordaja
    global tasku, mindavad_kohad, poise, kordaja, poises, poiseh, damage, weapon, poise_damage, poise_kordaja
    global maja, surnuaed, tiik, mets, aas, põld, kirik, kelder, pööning
    
    sisend = sisend.lower()
    sisend = sisend.split()
    
    if not poiseh == 0:
        poise += poises
        poiseh -= 1
    if poiseh == 0:
        poises = 0
    
    if "hiir" in tasku:
        poise += 10
    if "lind" in tasku:
        poise += 10
    if not poise == 0:
        player1 -= random.randint((poise - 5), (poise + 1))
        if player1 <= 0:
            surma_teated = ["Sa oled kutu", "Sinu teekond on lõppenud", "Surm võttis sind oma embusse", "Game Over"]
            return random.choice(surma_teated)
        
    poise -= poises
    poise = 0
#random message----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
    
    arv = random.randint(1,3)

    
#ränndamine----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------    
    if sisend[0] == "go":
        if sisend[1] == "maja":
            if sisend[1] in mindavad_kohad:
                koht = maja
                mindavad_kohad = ["aas", "pööning"]
                maja_teated = ["Saabusid majja", "Jõudsid kodusesse majja", "Astusid üle maja läve", "Leidsid tee majja"]
                return random.choice(maja_teated)
        if sisend[1] == "surnuaed":
            if sisend[1] in mindavad_kohad:
                koht = surnuaed
                mindavad_kohad = ["mets", "kirik"]
                surnuaia_teated = ["Saabusid surnuaeda", "Jõudsid hauaplatside vahele", "Leidsid end surnuaiast", "Sammud viisid sind surnuaeda"]
                return random.choice(surnuaia_teated)
        if sisend[1] == "tiik":
            if sisend[1] in mindavad_kohad:
                koht = tiik
                mindavad_kohad = ["tiik", "mets"]
                tiigi_teated = ["Saabusid tiigi äärde", "Jõudsid veekogu kaldale", "Leidsid end tiigi kaldalt", "Seisad nüüd tiigi ääres"]
                return random.choice(tiigi_teated)
        if sisend[1] == "aas":
            if sisend[1] in mindavad_kohad:    
                koht = aas
                mindavad_kohad = ["tiik", "maja", "mets", "põld"]
                aasa_teated = ["Saabusid aasale", "Jõudsid õitsvale aasale", "Leidsid end lilleliselt aasalt", "Sammud viisid sind aasale"]
                return random.choice(aasa_teated)
        if sisend[1] == "põld":
            if sisend[1] in mindavad_kohad:    
                koht = põld
                mindavad_kohad = ["aas", "mets", "tiik"]
                põllu_teated = ["Saabusid põllule", "Jõudsid viljapõllule", "Leidsid end põllult", "Seisad nüüd põllul"]
                return random.choice(põllu_teated)
        if sisend[1] == "mets":
            if sisend[1] in mindavad_kohad: 
                koht = mets
                mindavad_kohad = ["surnuaed", "põld", "aas", "tiik"]
                metsa_teated = ["Saabusid metsa", "Jõudsid metsasalusse", "Leidsid end metsast", "Puude vahel on nüüd sinu kodu"]
                return random.choice(metsa_teated)
        if sisend[1] == "kirik":
            if sisend[1] in mindavad_kohad:
                koht = kirik
                mindavad_kohad = ["surnuaed", "kelder"]
                kiriku_teated = ["Saabusid kirikusse", "Jõudsid püha paika", "Leidsid end kirikust", "Astusid kiriku uksest sisse"]
                return random.choice(kiriku_teated)
        if sisend[1] == "kelder":
            if sisend[1] in mindavad_kohad:
                koht = kelder
                mindavad_kohad = ["kirik"]
                keldri_teated = ["Sünge peidetud trepp viis teid keldrisse", "Laskusid mööda treppi keldrisse", "Leidsid end pimedast keldrist", "Oled nüüd keldris"]
                return random.choice(keldri_teated)
        if sisend[1] == "pööning":
            if sisend[1] in mindavad_kohad:
                koht = pööning
                mindavad_kohad = ["maja"]
                pööningu_teated = ["Jõudsid redeli kaudu pööningule", "Ronisid üles pööningule", "Leidsid end tolmuselt pööningult", "Oled nüüd pööningul"]
                return random.choice(pööningu_teated)
        eksimise_teated = ["Sa ei leidnud teed kuhugile!", "Eksinud! Proovi teist teed.", "See tee on suletud.", "Sinna ei saa praegu minna."]
        return random.choice(eksimise_teated)

    #scan -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

    elif sisend[0] == "scan":
        koht2.clear()  
        for item in koht:  
            koht2.append(str(item))
        skannimise_teated = [",".join(koht2), "Näed järgmisi asju: " + ",".join(koht2), "Siin on: " + ",".join(koht2), "Ümberringi on: " + ",".join(koht2)]
        return random.choice(skannimise_teated)

    #shoot-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

    elif sisend[0] == "atc" or sisend[0] == "attack" or sisend[0] == "shoot":
        arvk = 0
        if weapon == "käed":
            damage = 1000
            kordaja = 2


        elif weapon == "kalasnikov":
            damage = 20000
            kordaja = 1
            
            for i, item in enumerate(tasku):
                if item[:8] == "kuulid_x":
                    tasku[i] = "kuulid_x" + str(int(item[8:]) - 1)
                    arvk = 1  
                    break
                
            if "kuulid_x0" in tasku:
                tasku.remove("kuulid_x0")
            if arvk == 0:
                kuulitu_teated = ["Pole kuule, mida lasta", "Kuulid puuduvad, mida lasta", "Relv ei tööta"]
                return random.choice(kuulitu_teated)
                
        elif weapon == "puhkpüss" or weapon == "poise":
            damage = 5000
            poise_damage = 15
            poise_kordaja = 5
            kordaja = 1
            for i, item in enumerate(tasku):
                if item[:8] == "nooled_x":
                    tasku[i] = "nooled_x" + str(int(item[8:]) - 1)
                    arvk = 1  
                    break
                
            if "nooled_x0" in tasku:
                tasku.remove("nooled_x0")
            if arvk == 0:
                kuulitu_teated = ["Pole nooli, mida lasta", "nooled puuduvad, mida lasta", "Relv ei tööta"]
                return random.choice(kuulitu_teated)
        elif weapon == "nuii":
            damage = 1500
            kordaja = 5
        elif weapon == "piits":
            damage = 10000
            kordaja = 3


        if sisend[1] in koht:
            if sisend[1] == "kala" or sisend[1] == "liblikas":
                
                    koht.append(str(sisend[1]) + "liha")
                    koht.append(sisend[1] + "korjus") 
                    koht.remove(sisend[1])
                    surma_teated = [sisend[1] + " on surnud.", sisend[1] + " langes surnult maha.", "Tabamus oli surmav " + sisend[1] + "-le", sisend[1] + " ei elanud seda üle"]
                    return random.choice(surma_teated)
                
            if sisend[1] in lastavad:
                if kord == 1:
                    
                    
                    suva = random.randint(1, 9)                                                                  #shoot______________________________
                    if suva == 8:
                        damage = damage * 2
                    
                    if sisend[1] == "karu":
                        karu -= damage
                        haavatu = karu
                            
                    if sisend[1] == "hiir":
                        hiir -= damage
                        haavatu = hiir
                    if sisend[1] == "lind":
                        lind -= damage
                        haavatu = lind
                        
                    kord = kordaja  

                    if haavatu <= 0:
                        koht.append(str(sisend[1]) + "liha")
                        koht.append(sisend[1] + "korjus") 
                        koht.remove(sisend[1])
                        surma_teated = [sisend[1] + " on surnud.", sisend[1] + " langes surnult maha.", "Tabamus oli surmav " + sisend[1] + "-le", sisend[1] + " ei elanud seda üle"]
                        return random.choice(surma_teated)
                    else:
                        haavatud_teated = [str(sisend[1]) + sisend[1] +": müöö", str(sisend[1]) + " karjatas valust", str(sisend[1]) + " sai pihta", str(sisend[1]) + " on haavatud"]
                        return random.choice(haavatud_teated) 
                        
                elif kord > 1:
                    kord -= 1
                else:
                    kord = kordaja
        if sisend[1] in koht:  
            elutute_esemete_teated = [sisend[1]+ " on nüüd auk sees", sisend[1] + " on nüüd katki"]
            return random.choice(elutute_esemete_teated)
        else:
            mööda_teated = ["kuul lendas mööda", "käis lihtsalt pauk", "Peale ehmatust avastasid, et käis lihtsalt pauk"]
            return random.choice(mööda_teated)
    #Korjesüsteem---------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------        

    elif sisend[0] == "pick":
        if sisend[0] in relvad:
            relv_taskus = ["Peate vanast relvast loobuma", "Relv on juba olemas", "Peate Relva enne maha viskama"]
            return random.choice(relv_taskus)
        elif len(tasku) == 10:
            täis_teated = ["Taskud on täis.", "Ei mahu enam midagi taskusse.", "Sul pole ruumi.", "Tasku ajab üle."]
            return random.choice(täis_teated)
        elif sisend[1] in weapons:
            weapon = sisend[1]
            koht.remove(sisend[1])
            relva_teated = ["Omades nüüd Vägevat relva, täitub su keha raevuga", "Oled nüüd relvastatud", "Oled nüüd võitmatu, Äkki", ""]
            return random.choice(relva_teated)
        elif sisend[1] in liiga_suur_ese:
            raske_teated = ["Ese on liiga raske.", "Ei jõua seda tõsta.", "See on liiga suur.", "Ei suuda seda kaasa võtta."]
            return random.choice(raske_teated)
        else:
            if sisend[1] == "hiir" or sisend[1] == "lind":
                elusolendi_teated = ["loodetavasti " + str(sisend[1]) + " ei vigasta mind", str(sisend[1]) + " sibab taskus ringi", "Püüdsid " + str(sisend[1]) + " kinni", str(sisend[1]) + " on nüüd sinu taskus"]
                return random.choice(elusolendi_teated)
            elif sisend[1] in koht:
                tasku += [sisend[1]]
                koht.remove(sisend[1])
                korjamise_teated = ["Taskus on nüüd " + sisend[1], "Võtsid " + sisend[1] + " kaasa", "Korjasid " + sisend[1] + " üles", sisend[1] + " on nüüd sinu oma"]
                return random.choice(korjamise_teated)
            elif "liha" in sisend[1]:
                for sõna in koht:
                    if sõna == sisend[1]:
                        tasku += [sisend[1]]
                        koht.remove(sisend[1])
                        liha_teated = ["Taskus on nüüd " + sisend[1], "Korjasid " + sisend[1] + " üles", "Võtsid " + sisend[1] + " kaasa", sisend[1] + " on nüüd sinu oma"]
                        return random.choice(liha_teated)
            elif "kuulid" in sisend[1]:
                kordus = -1
                kuuli_teated = ["Oled nüüd valmis laskma", "lõpuks saad oma relva kasutusele panna", "Sull on nüüd laskemoona "]
                
                for itam in koht:
                    
                    
                    if "kuulid" in itam:
                        tasku += [koht[int(kordus + 1)]]
                        koht.remove(koht[kordus + 1])
                        
                        return random.choice(kuuli_teated)
                    kordus += 1

                        
    #maha viskamis süsteem-------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------
                            
    elif sisend[0] == "drop":
        
        if sisend[1] in weapons:
            koht += [sisend[1]]
            weapon = "käead"
            kord = kordaja
            relva_viskamise_teated = ["Pole seda relva enam vaja", "Viskasid " + sisend[1] + " minema", sisend[1] + " on nüüd maas", "Loobusid esemest " + sisend[1]]
            return random.choice(relva_viskamise_teated)
        elif sisend[1] == "nisu" or sisend[1] == "õun" or sisend[1] == "kont" or sisend[1] == "kook" or sisend[1] == "lill": 
            koht += [sisend[1]]
            tasku.remove(sisend[1])
            viskamise_teated = [sisend[1] + " kukkus maha", "Viskasid " + sisend[1] + " minema", sisend[1] + " on nüüd maas", "Loobusid esemest " + sisend[1]]
            return random.choice(viskamise_teated)
        elif "liha" in sisend[1]:
            koht += [sisend[1]]
            tasku.remove(sisend[1])
            liha_teated = ["Viskasid " + sisend[1] + " maha", sisend[1] + " kukkus taskust", "Loobusid toidust", sisend[1] + " on nüüd maas"]
            return random.choice(liha_teated)
        elif sisend[1] == hiir or sisend[1] == lind:
            koht += [sisend[1]]
            tasku.remove(sisend[1])
            looma_teated = [str(sisend[1]) + " sai taskust välja", str(sisend[1]) + " põgenes taskust", str(sisend[1]) + " hüppas vabaks", str(sisend[1]) + " on nüüd vaba"]
            return random.choice(looma_teated)
                    
    #Tasku vaatamine ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------
                    
                    
    elif sisend[0] == "inv":
        if len(tasku) == 0:
            tühi_teated = ["Tasku on tühi.", "Sul pole midagi kaasas.", "Taskud on tühjad.", "Ei leia taskust midagi."]
            return random.choice(tühi_teated)
        
        else:
            tasku_teated = ["Taskus on " + str(tasku) + ".", "Kaasas on " + str(tasku) + ".", "Leidsid taskust: " + str(tasku), "Sul on kaasas: " + str(tasku)]
            return random.choice(tasku_teated)
                    
    #püha söömine------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------
    elif sisend[0] == "eat" or sisend[0] == "heal":
        
        suva = 0
        if sisend[1] == "õun":
            suva = random.randint(5, 30)
            player1 += suva
            tasku.remove(sisend[1])
            söömise_teated = ["nom nom", "Maitsev!", "See oli hea!", "Kõht sai täis"]

        if sisend[1] == "kook":
            suva = random.randint(10, 25)
            player1 += suva
            tasku.remove(sisend[1])
            söömise_teated = ["nom nom", "Maitsev!", "See oli hea!", "Kõht sai täis"]

        if sisend[1] == "seen":
            poises += random.randint(10, 20)
            poiseh += 5
            tasku.remove(sisend[1])
            söömise_teated = ["nom nom", "Maitsev!", "See oli hea!", "Kõht sai täis"]

        if "liha" in sisend[1]:
            suva = random.randint(20, 50)
            tasku.remove(sisend[1])
            söömise_teated = ["nom nom", "Maitsev!", "See oli hea!", "Kõht sai täis"]
        else:
            söömise_teated = ["See ei kõlba küll süüa", "see ei ole eriti maitsev", "öäk", "See on söömiseks liiga räpane"]
        player1 += suva
        return random.choice(söömise_teated)
        
        
        
                
                
    #elu kontrollimine------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------
    elif sisend[0] == "health" or sisend[0] == "elud" or sisend[0] == "hp":
        elu_teated = ["elud: " + str(player1), "Sul on " + str(player1) + " elu", "Tervis: " + str(player1), "Elupunkte: " + str(player1)]
        return random.choice(elu_teated)

    #Vaatamine------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------

    elif sisend[0] == "look":   
        if koht == mets:
            metsa_teated = ["Puude vahelt on näha tiik, aas, surnuaed ja põld", "Läbi metsa paistab tiik, surnuaed aas ja põld", "Näed kauguses tiiki, surnuaeda, aasa ja põldu", "Puude vahelt avanevad vaated tiigile, surnuaiale, aasale ja põllule"]
            return random.choice(metsa_teated)
        elif koht == maja:
            maja_teated = ["Näha on aas ja pööning", "Aknast paistab aas, trepist pääseb pööningule", "Vaade aasale, üleval on pööning", "Maja aknast näed aasa, trepid viivad pööningule"]
            return random.choice(maja_teated)
        elif koht == surnuaed:
            surnuaia_teated = ["Näha on mets ja kirik", "Hauaplatside vahelt paistab mets ja kirik", "Vaade avaneb metsale ja kirikule", "Surnuaiast näed metsa ja kirikut"]
            return random.choice(surnuaia_teated)
        elif koht == tiik:
            tiigi_teated = ["Üle vee on näha aas, põld ja mets", "Tiigi kaldalt paistavad aas, põld ja mets", "Veekogu ümbruses näed aasa, põldu ja metsa", "Tiigi äärest avanevad vaated aasale, põllule ja metsale"]
            return random.choice(tiigi_teated)
        elif koht == aas:
            aasa_teated = ["Näha on maja, tiik, põld ja mets", "Aasalt paistavad maja, tiik, põld ja mets", "Ümberringi näed maja, tiiki, põldu ja metsa", "Aasalt avanevad vaated majale, tiigile, põllule ja metsale"]
            return random.choice(aasa_teated)
        elif koht == põld:
            põllu_teated = ["Näha on tiik, aas ja mets", "Põllult paistavad tiik, aas ja mets", "Vaade avaneb tiigile, aasale ja metsale", "Põllult näed tiiki, aasa ja metsa"]
            return random.choice(põllu_teated)
        elif koht == kirik:
            kiriku_teated = ["Akendest välja vaadates on näha surnuaeda, sammuti on näha ka sünge trepp sildiga kelder", "Kirikust näed surnuaeda ja treppi keldrisse", "Vaade avaneb surnuaiale, all on kelder", "Kirikust paistavad surnuaed ja tume trepikäik keldrisse"]
            return random.choice(kiriku_teated)
        elif koht == kelder:
            keldri_teated = ["Näha on trepid mis viivad kiriku", "Trepid suunduvad üles kiriku", "Keldrist viivad trepid kiriku", "Pimedast keldrist näed treppe, mis viivad kiriku"]
            return random.choice(keldri_teated)
        elif koht == pööning:
            pööningu_teated = ["Näha on trepid mis viivad majja", "Pööningult viivad trepid majja", "Tolmune trepp suundub majja", "Pööningult näed treppe, mis viivad majja"]
            return random.choice(pööningu_teated)
        else:
            eksimise_teated = ["Sa oled eksinud!", "Ei tea, kus oled!", "See koht on võõras.", "Oled ära eksinud!"]
            return random.choice(eksimise_teated)
    
    #relva vaatamine------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------
    
    elif sisend[0] == "weapon":
        relva_teated = [("Seljal on " + weapon), ("Oled relvastatud" + weapon + "iga")]
        return random.choice(relva_teated)
    
    #abikäsk------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------
    
    elif sisend[0] == "help":
        return "Ole viimane mängi elus!!"
    
    #tere------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------

    elif sisend[0] == "hi" or sisend[0] == "hello" or sisend[0] == "tere":
        teretus_teated = ["Tere", "Tere Tere", "Tere tulemast", "Tere tulemast mängu", "HI"]
        return random.choice(teretus_teated)             
    
    #nägemist------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------
    
    elif sisend[0] == "bye" or sisend[0] == "goodbye":
        saatmis_teated = ["Nägemist!", "Head aega!", "Nägemist, mängija!", "Head aega mängimast!"]
        return random.choice(saatmis_teated)
    
    #käsu eksimine------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------
    
    else:
        vea_teated = ["käsku ei leitud.", "Tundmatu käsk.", "Ei saa aru käsust.", "Proovi teist käsku."]
        return random.choice(vea_teated)
    #errori tapja----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------
        #except Exception as e:
            #print(f"Sisestasit midagi valesti: {e}")
        



















def send_message():
    sisend = input_var.get().strip()
    if sisend:
        # Display user message in chat area
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f" {sisend}\n", "user_tag")
        chat_area.config(state='disabled')
        
        # Clear input field
        input_var.set("")

        # Get reply from the game_brain function
        reply = game_brain(sisend)

        # Display reply in chat area
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f" {reply}\n", "bot_tag")
        chat_area.config(state='disabled')
        scroll_to_bottom()
        
def on_enter_key(event):
    send_message()

# GUI------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------





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
keywords = ["scan", "inv", "pick <item>", "drop <item>", "look", "go <place>", "eat <item>", "health or hp", "atc <target> or attack <target>", "weapon" ]

for kw in keywords:
    kw_label = ttk.Label(hint_frame, text=kw, font=("Arial", 10))
    kw_label.pack(anchor="w")

# Sample rules display (just informational)
#rules_frame = ttk.LabelFrame(hint_frame, text="Map", padding="5")
#rules_frame.pack(fill="x", pady=10)

#rule1_label = ttk.Label(rules_frame, text='Rule 1: If user says "hello" → respond with greeting.')
#rule1_label.pack(anchor="w")
#rule2_label = ttk.Label(rules_frame, text='Rule 2: If user says "bye" → respond with farewell.')
#rule2_label.pack(anchor="w")

# Auto-scroll chat area to bottom when new content is added
def scroll_to_bottom():
    chat_area.see("end")
    chat_area.update_idletasks()

# Set up the main event loop
root.mainloop()


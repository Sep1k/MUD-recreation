import random 
ax = 0 
aas = [] 
ese = "" 
eluka_lisamine = 1
randomhulk = random.randint(3, 10)
lisatav = "" 

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
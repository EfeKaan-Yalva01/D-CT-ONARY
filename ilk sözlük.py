
meme_dict = {
            "AGGRO": "  agresifleşmek/sinirlenmek",
            "CREEPY ": "korkunç",
            "ROFL" :   "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
             "LOL":   "komik bir şeye verilen cevap",
            }
kelime= input("Anlamadığınız bir kelime yazın")

if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print("malesef bu kelime bizde yok")

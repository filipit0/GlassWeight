# funkcja do pobierania wartosci, zwraca wartosc w postaci float
# z obsluga bledow
# w przypadku wykrycia slowa kluczowego "exit_text" zwraca wartosc None

def input_float(text, exit_text):
        while True:
            inp = input(text)
            try:
                float_inp = float(inp)
                break
            except:
                if inp == exit_text:
                    float_inp = None
                    break                   
                else:
                    print("Nieprawidlowa Wartosc")
        return float_inp


print("""   ***********************************************************************
   * Program do obliczania ciezaru szyby na podstawie podanych wymiarow. *
   * Grubosc calkowita nie odnosi sie do pakietu szyby zespolonej lecz   *
   * tylko i wylacznie do calkowitej grubosci pojedynczych szyb:         *
   * np.: dla szyby typu 4-12Ar-4 podajemy grubosc 8 bo(4+4)             *
   ***********************************************************************
""")

# petla wlasciwa programu:
while True:
        width = input_float("szerokosc [mm] = ", "exit")
        if width == None: break
        height = input_float("wysokosc [mm] = ", "exit")
        if height == None: break
        thickness = input_float("grubosc calkowita [mm] = ", "exit")
        if thickness == None: break

        area = width*height/1000000
        weight = area*thickness*2.5
        print("pole powierzchni = ",round(area,2), " [m2]")
        print("ciezar to        = ", round(weight,2)," [kg]")
        print("****************************************************** \n")

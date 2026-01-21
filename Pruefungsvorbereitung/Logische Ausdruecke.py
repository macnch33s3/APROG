def pruefe_rabatt(alter, aktiv, guthaben):
    retval = alter >= 18 and alter < 65
    retval = retval and aktiv==True
    retval = retval and guthaben >= 0
    return retval

testfaelle = [
    (20, True, 50), #True
    (17, True, 30), #False
    (70, True, 100), #False
    
]

def main():
    print("Pruefe Rabatt:\n")
    for alter, aktiv, guthaben in testfaelle:
        resultat = pruefe_rabatt(alter, aktiv, guthaben)
        print(f"Alter={alter}, Aktiv={aktiv}, Guthaben={guthaben} -> Rabatt:{resultat}")

if __name__ == "__main__":
    main()
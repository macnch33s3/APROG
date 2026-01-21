def funktion_a():
    print("Funktion a")
    
def funktion_b():
    print("Funktion b")

def funktion_c(a):
    funktion_b()
    print(a)
    funktion_a()

def funktion_d(a):
    funktion_c(a)
    print("Ende!")
    
print(funktion_d(b))
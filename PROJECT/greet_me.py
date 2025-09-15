def greet(name):
    """
    Greets the user with their name.
    Args:
        name (str): The name of the user to greet.
    Returns:
        None
    """
    print(f"Hello, {name}!")


# Hauptprogramm: Macht dasselbe wie das Jupyter Notebook
# Es ruft die Funktion greet mit dem Namen "Peter" auf.
def main():
    greet("Marc")

# 
if __name__ == "__main__":
    main()

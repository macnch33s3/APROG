# text input
# choose rendering style
# convert to ASCII
# Output to console

## choose rendering style and convert to ASCII
from pyfiglet import Figlet

## text input
user_text = input("Enter your text: ")
user_font = input("Enter font: ")

# print(user_text)

# chose font
f = Figlet(font=user_font)

# output to console
print(f.renderText(user_text))
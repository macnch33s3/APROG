import numpy as np
import matplotlib.pyplot as plt

# Wertebereich definieren
x = np.linspace(0, 2 * np.pi, 1000)  # Von 0 bis 2π, 1000 Punkte
y = np.sin(x)  # Sinusfunktion

# Plot erstellen
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Plot der Sinusfunktion')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()
plt.show()
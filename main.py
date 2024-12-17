
import numpy as np
import matplotlib.pyplot as plt

# X değerlerini oluşturma
x = np.linspace(0, 10, 100)

# Sinüs ve kosinüs değerlerini hesaplama
y_sin = np.sin(x)
y_cos = np.cos(x)

# Şekli ve eksenleri oluşturma
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='--')
plt.scatter(x[::10], y_sin[::10], color='blue', marker='o', label='Sinüs Noktaları')
plt.scatter(x[::10], y_cos[::10], color='red', marker='x', label='Kosinüs Noktaları')
plt.title('Sinüs ve Kosinüs Fonksiyonları')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


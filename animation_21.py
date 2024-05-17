import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Создание сетки значений x и y
x = np.linspace(0, 10, 100)
y = np.linspace(0, 5, 100)

# Создание сетки значений x и y
X, Y = np.meshgrid(x, y)

# Задание значения времени t
T = np.linspace(0, 0.01, 100)  # Массив значений времени от 0 до 10

# Функция, возвращающая значения функции u(x, y, t) в зависимости от t
def update(t):
    u = np.sin(np.pi * X) * np.cos(2 * np.pi * Y) * np.exp(-20 * np.pi**2 * t)
    ax.clear()
    ax.set_zlim(-0.5, 0.5)
    surf = ax.plot_surface(X, Y, u, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('u')
    ax.set_title(f'График функции u(x, y, t={t:.2f})')
# Создание трехмерного графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Создание анимации
ani = FuncAnimation(fig, update, frames=T, interval=100)

plt.show()

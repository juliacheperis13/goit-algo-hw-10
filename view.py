import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 40

y_min = -5
y_max = 128_000

def func(x):
    return 2 * x ** 3 + 13


if __name__ == "__main__":
    x = np.linspace(-10, 40, 100)
    y = func(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.axhline(y=y_min, color='g', linestyle="--")
    ax.axhline(y=y_max, color='g', linestyle="--")
    ax.axvline(x=a, color='g', linestyle="--")
    ax.axvline(x=b, color='g', linestyle="--")

    fill_x = np.linspace(a, b, 100)
    fill_y = func(fill_x)
    ax.fill_between(fill_x, fill_y, color='pink', alpha=0.5)

    plt.grid(True)
    plt.show()

import matplotlib.pyplot as plt
import numpy as np


def plot_complexity_comparison(max_n=20):
    """
    Пример визуализации асимптотической сложности: n, n², n³, 2ⁿ
    с логарифмической шкалой только по оси Y
    """

    n_values = np.arange(1, max_n + 1)

    functions = {
        "O(n)": n_values,
        "O(n²)": n_values**2,
        "O(n³)": n_values**3,
        "O(2ⁿ)": 2**n_values,
    }

    plt.figure(figsize=(10, 6))

    function_colors = ["blue", "green", "orange", "red"]

    for (function_name, function_values), color in zip(
        functions.items(), function_colors
    ):
        plt.semilogy(
            n_values,
            function_values,
            label=function_name,
            linewidth=2,
            color=color,
            marker="o",
            markersize=2,
        )

    plt.title(
        "Сравнение асимптотической сложности\n(логарифмическая шкала по оси Y)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("n (размер входных данных)")
    plt.ylabel("Относительное время выполнения (логарифмическая шкала)")
    plt.legend()
    plt.grid(True, alpha=0.3, which="both")

    plt.tight_layout()
    plt.show()


def plot_complexity(n_values, x_values, title="Асимптотическая сложность"):
    """
    Визуализация асимптотической сложности для заданных значений

    Args:
        n_values: список значений n (размер входных данных)
        x_values: список значений времени/операций x(n)
        title: заголовок графика
    """
    plt.figure(figsize=(10, 6))
    plt.semilogy(
        n_values, x_values, linewidth=2, marker="o", markersize=2, color="blue"
    )
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("n (размер входных данных)")
    plt.ylabel("Время/Операции (логарифмическая шкала)")
    plt.grid(True, alpha=0.3, which="both")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_complexity_comparison(max_n=50)

    n_values = np.arange(1, 1000)
    x_values = n_values**2
    plot_complexity(n_values, x_values)

"""
Symulacja Monte Carlo prawdopodobieństwa bankructwa portfela ubezpieczeń na życie.

Model analizuje jak na prawdopobieństwo bankructwa wpływa:
    - wielkość portfela
    - forma narzutu finansowego
    - wielkość narzutu finansowego

Autor: Konrad Barszczewski
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xscale


def plot_paths(paths,show = True,save_path = None):
    """
    Wykres przebiegów stanu portfela, 5. oraz 95. centyla i mediany z wyników
    Oś X: kolejne lata trwania umowy
    Oś Y: Stan portfela w danym roku
    Parametry:
    ----------
    paths : list
        Tablica przebiegów stanu portfela z symulacji Monte Carlo
    show : bool
        Czy wykres ma być pokazany?
    save_path: str
        Ścieżka zapisu pliku
    """
    plt.style.use("seaborn-v0_8")
    paths = np.array(paths)
    for path in paths:
        plt.plot(path, color = "blue", alpha = 0.1)

    p5 = np.percentile(paths, 5,axis=0)
    p50 = np.percentile(paths, 50 , axis=0)
    p95 = np.percentile(paths, 95, axis=0)
    plt.plot(p50, color="black", linewidth=3, label="Mediana")

    plt.plot(p5, color="orange", linestyle="--", label="5%")
    plt.plot(p95, color="orange", linestyle="--", label="95%")
    plt.axhline(y = 0, color = "red", linestyle = "--", label = "Bankructwo")

    plt.xlabel("Rok")
    plt.ylabel("Kapitał")
    plt.title("Symulacja kapitału")

    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path,dpi = 300)
    if show:
        plt.show()

def plot_histogram(finals,show = True,save_path = None):
        """
    Histogram stanów końcowych portfela
    Oś X: Stan końcowy portfela
    Oś Y: Ilość symulacji
    Parametry:
    ----------
    finals : list
        Lista stanów końcowych portfela z symulacji Monte Carlo
    show : bool
        Czy wykres ma być pokazany?
    save_path: str
        Ścieżka zapisu pliku
    """
    plt.hist(finals, bins = 30 )

    plt.xlabel("Kapitał końcowy")
    plt.ylabel("Liczba symulacji")
    plt.title("Rozkład wyników końcowych")

    plt.grid(True)
    if save_path:
        plt.savefig(save_path,dpi = 300)
    if show:
        plt.show()


def plot_bank_prob(propabilities,arguments,aplha_or_n,show = True,save_path = None):
    """
    Wykres szansy oszacowanej szansy bankructwa danego portfela z symulacji Monte Carlo w zależności od liczby klientów lub współczynnika narzutu alpha
    Oś X: Liczba klientów (w skali logarytmicznej) lub parametr alpha
    Oś Y: Prawdopodobieństwo bankructwa

    Parametry:
    -----------
    propabilities : list
        Lista oszacowanych prawdopodobieństw bankructwa
    arguments : list
        Lista ilości klientów n lub parametrów alpha
    alpha_or_n : str
        Parametr względem którego badaliśmy prawdopodobieństwo
    show : bool
        Czy wykres ma być pokazany?
    save_path: str
        Ścieżka zapisu pliku
        
    """
    plt.style.use("seaborn-v0_8")
    if aplha_or_n == "aplha":
        pass
    elif aplha_or_n == "n":
        plt.xscale("log")
    plt.plot(arguments,propabilities, color = "black")
    plt.title("Prawdopodobieństwo bankructwa w zależności od " + aplha_or_n)
    plt.xlabel(aplha_or_n)
    plt.ylabel("Prawdopodobieństwo bankrutctwa")
    plt.grid(True)

    if save_path:
        plt.savefig(save_path,dpi = 300)
    if show:
        plt.show()

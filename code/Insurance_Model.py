"""
Symulacja Monte Carlo prawdopodobieństwa bankructwa portfela ubezpieczeń na życie.

Model analizuje jak na prawdopobieństwo bankructwa wpływa:
    - wielkość portfela
    - forma narzutu finansowego
    - wielkość narzutu finansowego

Autor: Konrad Barszczewski
"""
import numpy as np
import pandas as pd
import openpyxl
class InsurancePortfolio:
    """
    Reprezentacja portfela ubezpieczeń na życie używanego w symulacji Monte Carlo.

    Parametry:
    ----------
    n_clients : int
        Liczba ubezpieczonych klientów w portfelu
    Sum_assured : float
        Wartość wypłacana po śmierci klienta
    Interest_rate : float
        Techniczna stopa procentowa
    Clients_Age : int
        Wiek klienta w momencie zawarcia umowy
    filepath : str
        Ścieżka do pliku excela zawierającego tablice trwania życia
    sheet_name : str
        Nazwa arkusza zawierającego prawdopodobieństwa zgonu
    """
    def __init__(
            self,
            n_clients,
            Sum_assured,
            Interest_rate,
            Clients_Age,
            filepath,
            sheet_name
            ):
        self.n_clients = n_clients
        self.Sum_assured = Sum_assured
        self.Interest_rate = Interest_rate
        self.Clients_Age = Clients_Age
        self.qx = self.import_qx(filepath,sheet_name)
    def import_qx(self, filepath, sheet_name):
        """
        Importuje tablicę trwania życia
        
        Zwraca
        -------
        Lista
            prawdopodobieństwo zgonu w kolejnych latach życia klienta
        """
        df = pd.read_excel(filepath, sheet_name=sheet_name, header = 3)
        qx = df["qx"].iloc[self.Clients_Age:101].reset_index(drop = True)
        qx.iloc[-1] = 1.0
        return qx
    def Expected_Value(self):
        """
        Oblicza oczekiwaną obecną wartość wypłacanego świadczenia

        Zwraca
        -------
        float
            Oczekiwana obecna wartość świadczenia
        """
        total = 0
        Discount_Factor = 1 / (1+self.Interest_rate)
        Survival_Prob = 1
        for i,q in enumerate(self.qx):
            total += Survival_Prob * q * (Discount_Factor ** (i+1))
            Survival_Prob *= (1-q)
        return total * self.Sum_assured
    def Variance(self):
        """
        Oblicza wariancje z obecnej wartości wypłacanego świadczenia

        Zwraca
        -------
        float
            Wariancja obecnej wartości świadczenia
        """
        total = 0
        Discount_Factor = 1 / (1 + self.Interest_rate) ** 2
        Survival_Prob = 1
        for i, q in enumerate(self.qx):
            total += Survival_Prob * q * (Discount_Factor ** (i + 1))
            Survival_Prob *= (1 - q)
        return self.Sum_assured ** 2 * total - self.Expected_Value()**2
    def Calculate_claims(self,num,qx):
        """
        Losuje ilość śmierci wśród klientów w danym roku z rozkładu dwumianowego i wylicza sumę świadczeń do wypłaty

        Parametry
        ---------
        num : int
            Ilość żywych klientów na początku danego roku
        qx : float
            Prawdopodobieństwo śmierci w danym roku życia

        Zwraca
        -------
        float
            Suma świadczeń do wypłaty na koniec danego roku
        """
        n_deaths = np.random.binomial(n = num, p = qx)
        return n_deaths * self.Sum_assured
    def Simulate(self,Initial_Capital):
        """
        Symuluje stan portfela ubezpieczeń.

        Każdego roku:
        - losuje ilość zmarłych klientów w danym roku
        - aktualizuje ilość żywych klientów
        - wylicza sumę świadczeń do wypłaty
        - kapitalizuje środki portfela o stopę procentową 
        - odejmuje od środków sumę wypłat
        - zapisuje stan porfela do listy

        Gdy wszyscy klienci umrą:
        - zapisuje do histori stan portfela z poprzedniego roku
        Gdy stan portfela spadnie poniżej 0(bankructwo):
        - zapisuje do histori stan portfela jako 0

        Parametry:
        ---------
        Initial_Capital : float
            Kwota którą inwestuje ubezpieczyciel przy zawarciu umowy

        Zwraca:
        --------
        history : list
            Lista z corocznym stanem portfela przez cały czas trwania umowy
        """

        history = [Initial_Capital]
        capital = Initial_Capital
        clients_alive = self.n_clients
        for i,q in enumerate(self.qx):
            n_deaths = np.random.binomial(n = clients_alive, p = q)
            capital = capital * (1 + self.Interest_rate) - n_deaths * self.Sum_assured
            clients_alive = clients_alive - n_deaths
            if clients_alive == 0:
                history.append(history[-1])
            elif capital <= 0:
                history.append(0)
            else:
                history.append(capital)
        return history

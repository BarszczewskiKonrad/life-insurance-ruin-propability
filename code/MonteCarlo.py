"""
Symulacja Monte Carlo prawdopodobieństwa bankructwa portfela ubezpieczeń na życie.

Model analizuje jak na prawdopobieństwo bankructwa wpływa:
    - wielkość portfela
    - forma narzutu finansowego
    - wielkość narzutu finansowego

Autor: Konrad Barszczewski
"""

from Insurance_Model import InsurancePortfolio
def MonteCarlo(n_simulations,portfolio,inicial_capital):
    """
    Wielokrotnie wykonuje symulacje przebiegu stanu porfela ubezpieczeń na życie

    Parametry:
    ---------
    n_simulations : int
        Ilość symulacji do wykonania
    portfolio: InsurancePortfolio
        Portfel ubezpieczeń na życie
    inicial_capital: float
        Początkowy kapitał danego portfela

    Zwraca:
    -------
    histories : list
        tablica z przebiegami stanu portfela w czasie
    final_capitals : list
        lista końcowych kapitałów w portfelu
    prob_bankruptcy: float
        Oszacowane prawdopodobieństwo bankructwa danego portfela przy ustalonym kapitale początkowym
    """
    final_capitals = []
    histories = []
    bankrupt = 0
    for i in range(n_simulations):
        history = portfolio.Simulate(inicial_capital)
        final_capital = history[-1]
        histories.append(history)
        final_capitals.append(final_capital)
        if final_capital <= 0:
            bankrupt += 1
        else:
            pass
    return {
        "histories": histories,
        "final_capitals": final_capitals,
        "prob_bankruptcy": bankrupt / n_simulations,
    }
def Bankruptcy_Prob(
        n,
        alpha,
        n_simulations,
        interest_rate,
        clients_age,
        sum_assured,
        filepath,
        sheet_name,
        loading_type,

):
    """
    Wykonuje symulacje Monte Carlo dla określonych parametrów porfela, formy narzutu, oraz współczynnika narzutu

    Parametry:
    ----------
    n : int
        Ilość klientów w danym portfelu
    alpha : float
        Współczynnik narzutu
    n_simulations : int
        Ilość symulacji Monte Carlo
    interest_rate : float
        Techniczna stopa procentowa
    clients_age: int
        Wiek klientów w momencie zawarcia umowy
    sum_assured : float
        Wysokość świadczenia wypłacanego na koniec roku śmierci
    filepath : str
        Ścieżka do pliku excela z tablicami trwania życia
    sheet_name : str
        Nazwa arkusza z TTŻ
    loading_type : str
        Forma narzutu finansowego:
        - Jeżeli "proportional" to Expected Value * alpha
        - Jeżeli sigma to pierwiastek z Variance * alpha

    Zwraca:
    --------
    results : float
        Oszacowane prawdopodobieństwo bankructwa danego portfela przy danej formie narzutu i parametrze alpha
        
    """
    portfolio = InsurancePortfolio(
        n,
        sum_assured,
        interest_rate,
        clients_age,
        filepath,
        sheet_name)
    ev = portfolio.Expected_Value()
    std = portfolio.Variance() ** 0.5
    if loading_type == "sigma":
        premium_per_client = ev + alpha * std
    elif loading_type == "proportional":
        premium_per_client = (1 + alpha) * ev
    else:
        raise ValueError("loading_type must be either 'sigma' or 'proportional'")

    initial_capital = n * premium_per_client
    results =  MonteCarlo(n_simulations,portfolio,initial_capital)
    return results["prob_bankruptcy"]

def bankruptcy_vs_n(
        n_values,
        alpha_values,
        n_simulations,
        interest_rate,
        clients_age,
        sum_assured,
        filepath,
        sheet_name,
        loading_type,
        alpha_or_n
):
    """
    Wyznacza prawdopodobieństwa bankructwa portfela dla różnych n lub alpha 

    Parametry:
    ----------
    n_values : int / list
        Ilość klientów w danym portfelu
    alpha_values : float / list
        Współczynnik narzutu
    n_simulations : int
        Ilość symulacji Monte Carlo
    interest_rate : float
        Techniczna stopa procentowa
    clients_age: int
        Wiek klientów w momencie zawarcia umowy
    sum_assured : float
        Wysokość świadczenia wypłacanego na koniec roku śmierci
    filepath : str
        Ścieżka do pliku excela z tablicami trwania życia
    sheet_name : str
        Nazwa arkusza z TTŻ
    loading_type : str
        Forma narzutu finansowego:
        - Jeżeli "proportional" to Expected Value * alpha
        - Jeżeli sigma to pierwiastek z Variance * alpha
    alpha_or_n : str
        Wartość po której zmianie badamy prawdopodobieństwo bankructwa
    Zwraca:
    --------
    propabilities : list
           Lista oszacowanych prawdopodobieństw bankructwa danego portfela przy danej formie narzutu i parametrze alpha
        
    """
    propabilities = []
    if alpha_or_n == "n":
        for n in n_values:
            p = Bankruptcy_Prob(
                n,
                alpha_values,
                n_simulations,
                interest_rate,
                clients_age,
                sum_assured,
                filepath,
                sheet_name,
                loading_type,
            )
            propabilities.append(p)
    elif alpha_or_n == "alpha":
        for alpha in alpha_values:
            p = Bankruptcy_Prob(
                n_values,
                alpha,
                n_simulations,
                interest_rate,
                clients_age,
                sum_assured,
                filepath,
                sheet_name,
                loading_type,
            )
            propabilities.append(p)
    return propabilities

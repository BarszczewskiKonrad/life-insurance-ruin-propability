from Insurance_Model import InsurancePortfolio
def MonteCarlo(n_simulations,portfolio,inicial_capital):
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

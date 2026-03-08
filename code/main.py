from plots import plot_paths, plot_histogram, plot_bank_prob
from MonteCarlo import MonteCarlo,Bankruptcy_Prob,bankruptcy_vs_n
from Insurance_Model import InsurancePortfolio


def main():
    sum_assured=1000
    interest_rate=0.05
    filepath = "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/tablice_trwania_zycia_w_latach_1990-2023.xlsx"
    sheet = "2022"
    clients_age = 30
    Portfolio1 = InsurancePortfolio(
        n_clients = 10,
        Sum_assured = sum_assured,
        Interest_rate = interest_rate,
        Clients_Age = clients_age,
        filepath = filepath,
        sheet_name = sheet
    )
    Portfolio2 = InsurancePortfolio(
        n_clients = 1000,
        Sum_assured=sum_assured,
        Interest_rate=interest_rate,
        Clients_Age=clients_age,
        filepath=filepath,
        sheet_name=sheet
    )
    Portfolio3 = InsurancePortfolio(
        n_clients = 100000,
        Sum_assured=sum_assured,
        Interest_rate=interest_rate,
        Clients_Age=clients_age,
        filepath=filepath,
        sheet_name=sheet
    )
    Premium1 = Portfolio1.Expected_Value()
    Premium2 = Portfolio1.Expected_Value() * 1.1
    Premium3= Portfolio2.Expected_Value() + (Portfolio2.Variance() ** 0.5)  * 0.15
    n_list = []
    for i in range(100):
        n_list.append(100 + i * 100)
    alpha_list = []
    for i in range(40):
        alpha_list.append(i * 0.01)
    n_sim = 5000
    result1_1 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio1,
        inicial_capital =  Premium1 * Portfolio1.n_clients)
    plot_paths(result1_1["histories"],1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n10_alpha0_paths.png")
    plot_histogram(result1_1["final_capitals"],1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n10_alpha0_hist.png")
    result1_2 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio1,
        inicial_capital =  Premium2 * Portfolio1.n_clients)
    plot_paths(result1_2["histories"],1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n10_alphaprop01_paths.png")
    plot_histogram(result1_2["final_capitals"],1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n10_alpha_prop01_hist.png")
    result1_3 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio1,
        inicial_capital =  Premium3 * Portfolio1.n_clients)
    plot_paths(result1_3["histories"],1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n10_alphasigma015_paths.png")
    plot_histogram(result1_3["final_capitals"],1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n10_alphasigma015_hist.png")
    result2_1 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio2,
        inicial_capital =  Premium1 * Portfolio2.n_clients)
    plot_paths(result2_1["histories"], 1, "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n1000_alpha0_paths.png")
    plot_histogram(result2_1["final_capitals"], 1,
                   "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n1000_alpha0_hist.png")
    result2_2 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio2,
        inicial_capital =  Premium2 * Portfolio2.n_clients)
    plot_paths(result2_2["histories"], 1, "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n1000_alphaprop01_paths.png")
    plot_histogram(result2_2["final_capitals"], 1,
                   "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n1000_alphaprop01_hist.png")
    result2_3 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio2,
        inicial_capital =  Premium3 * Portfolio2.n_clients)
    plot_paths(result2_3["histories"], 1, "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n1000_alphasigma015_paths.png")
    plot_histogram(result2_3["final_capitals"], 1,
                   "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n1000_alphasigma015_hist.png")
    result3_1 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio3,
        inicial_capital =  Premium1 * Portfolio3.n_clients)
    plot_paths(result3_1["histories"], 1, "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n100000_alpha0_paths.png")
    plot_histogram(result3_1["final_capitals"], 1,
                   "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n100000_alpha0_hist.png")
    result3_2 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio3,
        inicial_capital =  Premium2 * Portfolio3.n_clients)
    plot_paths(result3_2["histories"], 1, "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n100000_alphaprop01_paths.png")
    plot_histogram(result3_2["final_capitals"], 1,
                   "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n100000_alphaprop01_hist.png")
    result3_3 = MonteCarlo(
        n_simulations = n_sim,
        portfolio = Portfolio3,
        inicial_capital =  Premium3 * Portfolio3.n_clients)
    plot_paths(result3_3["histories"], 1, "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n100000_alphasigma015_paths.png")
    plot_histogram(result3_3["final_capitals"], 1,
                   "C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/n100000_alphasigma015_hist.png")

    results4_1 = bankruptcy_vs_n(
        n_values = n_list,
        alpha_values = 0.15,
        n_simulations = n_sim,
        interest_rate = interest_rate,
        clients_age = clients_age,
        sum_assured = sum_assured,
        filepath = filepath,
        sheet_name = sheet,
        loading_type = "sigma",
        alpha_or_n = "n"
    )
    plot_bank_prob(results4_1,n_list,"n",1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/bankrupcy_vs_n_alphaprop015.png")

    results4_2 = bankruptcy_vs_n(
        n_values = n_list,
        alpha_values = 0.1,
        n_simulations = n_sim,
        interest_rate = interest_rate,
        clients_age = clients_age,
        sum_assured = sum_assured,
        filepath = filepath,
        sheet_name = sheet,
        loading_type = "proportional",
        alpha_or_n = "n"
    )
    plot_bank_prob(results4_2,n_list,"n",1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/bankrupcy_vs_n_alphasigma01.png")

    results5_1 = bankruptcy_vs_n(
        n_values = 100,
        alpha_values = alpha_list,
        n_simulations = n_sim,
        interest_rate = interest_rate,
        clients_age = clients_age,
        sum_assured = sum_assured,
        filepath = filepath,
        sheet_name = sheet,
        loading_type = "sigma",
        alpha_or_n = "alpha"
    )
    plot_bank_prob(results5_1, alpha_list, "alpha",1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/bankrupcy_vs_alphasigma_n100.png")
    results5_2 = bankruptcy_vs_n(
        n_values = 100,
        alpha_values = alpha_list,
        n_simulations = n_sim,
        interest_rate = interest_rate,
        clients_age = clients_age,
        sum_assured = sum_assured,
        filepath = filepath,
        sheet_name = sheet,
        loading_type = "proportional",
        alpha_or_n = "alpha"
    )
    plot_bank_prob(results5_2, alpha_list, "alpha",1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/bankrupcy_vs_alphaprop_n100.png")
    results5_3 = bankruptcy_vs_n(
        n_values = 1000,
        alpha_values = alpha_list,
        n_simulations = n_sim,
        interest_rate = interest_rate,
        clients_age = clients_age,
        sum_assured = sum_assured,
        filepath = filepath,
        sheet_name = sheet,
        loading_type = "proportional",
        alpha_or_n = "alpha"
    )
    plot_bank_prob(results5_3, alpha_list, "alpha",1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/bankrupcy_vs_alphaprop_n1000.png")
    results5_4 = bankruptcy_vs_n(
        n_values = 1000,
        alpha_values = alpha_list,
        n_simulations = n_sim,
        interest_rate = interest_rate,
        clients_age = clients_age,
        sum_assured = sum_assured,
        filepath = filepath,
        sheet_name = sheet,
        loading_type = "sigma",
        alpha_or_n = "alpha"
    )
    plot_bank_prob(results5_4, alpha_list, "alpha",1,"C:/Users/konra/OneDrive/Pulpit/MUZ_PR/Wykresy/bankrupcy_vs_alphasigma_n1000.png")
if __name__ == "__main__":
    main()

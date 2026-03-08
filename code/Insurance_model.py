import numpy as np
import pandas as pd
import openpyxl
class InsurancePortfolio:
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
        df = pd.read_excel(filepath, sheet_name=sheet_name, header = 3)
        qx = df["qx"].iloc[self.Clients_Age:101].reset_index(drop = True)
        qx.iloc[-1] = 1.0
        return qx
    def Expected_Value(self):
        total = 0
        Discount_Factor = 1 / (1+self.Interest_rate)
        Survival_Prob = 1
        for i,q in enumerate(self.qx):
            total += Survival_Prob * q * (Discount_Factor ** (i+1))
            Survival_Prob *= (1-q)
        return total * self.Sum_assured
    def Variance(self):
        total = 0
        Discount_Factor = 1 / (1 + self.Interest_rate) ** 2
        Survival_Prob = 1
        for i, q in enumerate(self.qx):
            total += Survival_Prob * q * (Discount_Factor ** (i + 1))
            Survival_Prob *= (1 - q)
        return self.Sum_assured ** 2 * total - self.Expected_Value()**2
    def Calculate_claims(self,num,qx):
        n_deaths = np.random.binomial(n = num, p = qx)
        return n_deaths * self.Sum_assured
    def Simulate(self,Initial_Capital):
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

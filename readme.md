# Symulacja Monte Carlo prawdopodobieństwa bankructwa portfela ubezpieczeń na życie
Projekt analizuje prawdopodobieństwo bankructwa portfela ubezpieczeń na życie w zależności od:
- Wielkości portfela
- Formy narzutu finansowego
- Współczynnika narzutu finansowego

Model jest oparty na tablicach trwania życia oraz symulacjach Monte Carlo

---
## Założenia modelu
Przedmiotem analizy są portfele ubezpieczeń na życie z następującymi założeniami:
- Świadczenie jest wypłacane na koniec roku śmierci beneficjenta 
- Klientami są grupy 30 - letnich mężczyzn
- Wysokość świadczenia : 1000 zł
- Stała techniczna stopa procentowa $i = 5\$%
- Polskie tablice trwania życia (GUS 2022)
- maksymalny czas trwania życia : 100 lat
- Ubezpieczyciel otrzymuje **jednorazową płatność w momencie zawarcia umowy**

---
## Płatności
Rozważamy trzy sposoby wyceny świadczenia:
1. **Jednorazowa składka netto (JSN)**
2. **Zasada narzutu proporcjonalnego**

$$
Cena = JSN * (1 + \alpha)
$$

3.	**Zasada odchylenia standardowego**

$$
Cena = JSN + \alpha\sigma
$$

---
## Metoda symulacji
Kapitał ubezpieczyciela zmienia się corocznie według wzoru:

$$
C_n = C_{n-1} * (1+i) - D_n *S
$$ 

gdzie:
- $D_n$ - ilość klientów zmarłych w n - tym roku trwania umowy
- $S$ - Kwota wypłacana przy śmierci

Ilość śmierci jest symulowana przy użyciu **rozkładu dwumianowego** bazującego na prawdopodobieństwie śmierci z TTŻ

Każdy przebieg symulujemy **5000 razy** przy użyciu metody Monte Carlo

## Przykładowe symulacje 
- Przebieg stanu portfela dla n = 10 i JSN
![Przebieg stanu portfela dla n = 10 i JSN](figures/paths/n10_alpha0_paths.png)
- Przebieg stanu portfela dla n = 1000 i zasadzie odchylenia standardowego $\alpha = 0.15 $
![Przebieg stanu portfela dla n = 1000 i zasadzie odchylenia standardowego $\alpha = 0.15 $](figures/paths/n1000_alphasigma015_paths.png)

---
## Wyniki
Symulacje pokazują jak prawdopodobieństwo bankructwa zależy od:
- Skali portfela
- Formy narzutu
- Wielkości stosowanego narzutu

Pozostałe wykresy są dostępne w repozytorium 

## Wykorzystane narzędzia
- Python
- Numpy
- Pandas
- Matplotlib
## Autor
Konrad Barszczewski

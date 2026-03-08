# Prawdopodobieństwo bankructwa ubezpieczyciela ze względu na skalę działalności oraz formę i wielkość narzutu finansowego

## Cel projektu
 Zbadanie wpływu ilości klientów w portfelu ubezpieczeń na życie na ryzyko bankructwa tego portfela.

---
## Założenia
Przedmiotem badania będą portfele ubezpieczeń na życie płatnych na koniec roku śmierci.

Dla uproszczenia modelu zakładamy:
1. Stałą techniczną stopę procentową $i = 5$%
2. Brak kosztów operacyjnych 
3. Ubezpieczyciel otrzymuje jednorazową płatność w momencie zawarcia umowy tj. jednorazową składkę netto i opcjonalnie narzut
4. Bierzemy pod uwagę portfele ubezpieczeń dla 30-letnich mężczyzn, ze zobowiązaniem wypłaty kwoty 1000 zł na koniec roku śmierci
5. Podczas trwania umowy do ubezpieczyciela nie spływają dodatkowe środki
6. Korzystamy z tablic trwania życia mężczyzn z roku 2022, ze strony GUS'u
7. Zakładamy maksymalny czas trwania życia jako 100 lat tj. prawdopodobieństwo że 100 latek umrze w przeciągu następnego roku jest równe 100%
## Wycena świadczenia 
 Rozważymy trzy różne formy wyceny świadczenia:
1. Brak narzutu - bierzemy od klienta jedynie jednorazową składkę netto w formie:
   
$$
Cena=JSN = S *\sum_{n=1}^{100-k} (\frac{1}{1+i})^{n} *({}_{n}q_{k} - {}_{n-1}q_{k})
$$
   
2. **Zasada narzutu proporcjonalnego:**
   
$$
Cena = JSN * (1 + \alpha)
$$

3. **Zasada odchylenia standardowego**

$$
Price = JSN + \alpha   \sigma
$$

Gdzie:
- $S$ - wysokość wypłacanego świadczenia
- $i$ - techniczna stopa procentowa
- $k$ - wiek klienta w momencie zawarcia umowy}
- $\_{n}q_{k}$ - prawdopodobieństwo że $k$ - latek umrze w przeciągu $n$ - lat
- $\alpha$ - współczynnik narzutu finansowego
-
$$
\sigma = \sqrt{S^2 *\sum_{n=1}^{100-k} (\frac{1}{1+i})^{2n} *({}_{n}q_{k} - {}_{n-1}q_{k})}
$$

## Metodologia symulacji
Dla każdego portfela ustalamy kapitał początkowy postaci: 

$$
C_0 = \text{Ilość klientów} * \text{Cena}
$$ 

Każdego roku kapitalizujemy tą kwotę o stopę procentową $i$, następnie losujemy z rozkładu dwumianowego ilość $D_n$ śmierci wśród klientów w poprzednim roku. Odejmujemy od naszego kapitału sumę świadczeń do wypłaty w postaci: 

$$
D_n * S
$$

Finalny wzór rekurencyjny na kapitał ubezpieczyciela w danym roku trwania umowy prezentuje się następująco 

$$ C_n = C_{n-1} *(1 + i) - D_{n-1} * S
$$

Daną procedurę powtarzamy aż do momentu kiedy kapitał ubezpieczyciela nie spadnie poniżej zera bądź wszyscy klienci umrą. Przedstawioną wyżej symulacje powtarzamy **5000 razy**.
Na podstawie przeprowadzonych symulacji estymowano szansę na bankructwo każdego z badanych portfelów oraz zbadano zależność między tym prawdopodobieństwem, a ilością klientów  oraz współczynnikiem narzutu $\alpha$.

## Wyniki
Rozpatrzmy najpierw sytuacje w której ubezpieczyciel pobiera od klienta jedynie składkę netto:

- Przebieg portfela 10 klientów

![](figures/paths/n10_alpha0_paths.png)

- Przebieg portfela 1000 klientów
  
![](figures/paths/n1000_alpha0_paths.png)

- Przebieg portfela 100000 klientów
  
![](figures/paths/n100000_alpha0_paths.png)

Pierwszym co może się rzucać w oczy jest delikatna przewaga portfela o niskiej liczbie klientów, co przeczyłoby pewnej matematycznej intuicji. Dla porównania spójrzmy jeszcze na rozkład wyników końcowych portfeli 10 i 1000 klientów

- Wyniki końcowe portfela 10 klientów

![](figures/histograms/n10_alpha0_hist.png)

- Wyniki końcowe portfela 1000 klientów

![](figures/histograms/n1000_alpha0_hist.png)

Jak widać portfel 10 klientów zbankrutował w około **40% przeprowadzonych symulacji**, z kolei portfel 1000 klientów zbankrutował już w lekko ponad **50% przypadków**. Wobec tego jaka może być przyczyna takich wyników? - Otóż przy pobieraniu od klientów jednorazowej składki netto tj. de facto oczekiwanej obecnej wartości wypłacanego świadczenia, końcowy kapitał ubezpieczyciela naturalnie powinien zbiegać do 0. Z definicji jednorazowa składka netto to kwota która powinna pokryć jedynie wartość świadczenia nie uwzględniając żadnego zysku dla samego ubezpieczyciela. W związku z tym na mocy prawa wielkich liczb, wraz ze zwiększaniem liczby klientów końcowy poziom kapitału zbiega do 0. Natomiast portfele o niskiej skali są bardziej podatne na odchylenia. Część wyników końcowych będzie stosunkowo bardzo dobra i cześć z nich będzie tragiczna. Wobec tego mamy zarówno duże szanse na świetny zarobek jak i równie duże szanse na spektakularne bankructwo w pierwszych latach portfela. Warto jednak jeszcze zauważyć że portfele o dużej skali bankrutują stosunkowo późno względem tych o mniejszej skali. Na wykresach możemy zobaczyć, iż w tych przypadkach do bankructwa dochodzi pod koniec trwania umowy, natomiast przy mniejszej skali do bankructw dochodziło na całym okresie trwania umowy. Mimo wszystko model JSN jest bardziej teoretyczny. Nie ma logicznych podstaw aby ubezpieczyciel oferował świadczenia bez pewnej wizji zysku, nie mówiąc już nawet o nieuwzględnionych w naszym modelu kosztach prowadzenia takiej działalności

Rozważmy teraz jak na ten przebieg wpłynie dodanie do ceny 10% JSN, czyli zastosujmy zasadę narzutu proporcjonalnego ze współczynnikiem $\alpha = 0.1$

- Przebieg portfela 10 klientów

![](figures/paths/n10_alphaprop01_paths.png)

- Przebieg portfela 1000 klientów
  
![](figures/paths/n1000_alphaprop01_paths.png)

- Przebieg portfela 100000 klientów
  
![](figures/paths/n100000_alphaprop01_paths.png)

Jak widać przy dodaniu narzutu portfele radzą sobie tym lepiej im więcej klientów obejmują. Portfel 100000 klientów podczas 5000 symulacji nie zbankrutował ani razu, portfel 1000 klientów bankrutował bardzo sporadycznie. Natomiast porfel 10 klientów wyraźnie w tych wynikach odstaje nadal mając duży odsetek bankructw. Natomiast patrząc na 5 centyl naszych wyników możemy zauważyć pewną poprawę względem modelu bez jakiegokolwiek narzutu. Spójrzmy jeszcze na rozkład wyników końcowych tego portfela:

- Wyniki końcowe portfela 10 klientów

![](figures/histograms/n10_alpha_prop01_hist.png)

Jak widać na 5000 symulacji portfel ten zbankrutował w około 1600 przypadkach - co daje nam prawdopodobieństwo bankructwa w okolicach 32%, czyli dość sporo.

Przyjrzyjmy się jeszcze wynikom uzyskanym stosując zasadę odchylenia standardowego ze współczynnikiem $\alpha = 0.15$:
- Przebieg portfela 10 klientów

![](figures/paths/n10_alphasigma015_paths.png)

- Przebieg portfela 1000 klientów
  
![](figures/paths/n1000_alphasigma015_paths.png)

Jak widać otrzymane wyniki są w znacznej mierze podobne do tych przy zasadzie narzutu proporcjonalnego.

Spróbujmy teraz zbadać prawdopodobieństwo bankructwa dla obu sposobów wyceny, przy zmiennej ilości klientów. Zastosujmy te same współczynniki narzutu co przy poprzednich przykładach i zobaczymy jak szansa bankructwa zmienia się wraz ze wzrostem n w obu przypadkach.

- Zasada narzutu proporcjonalnego:

![](figures/bankrupcy_vs/bankrupcy_vs_n_alphaprop015.png)

- Zasada odchylenia standardowego:

![](figures/bankrupcy_vs/bankrupcy_vs_n_alphasigma01.png)

W obu przypadkach potwierdza się fakt, że przy stałym współczynniku narzutu szansa na bankructwo maleje wraz ze wzrostem ilości klientów. Natomiast przy podobnym współczynniku narzutu wyłania się lekka przewaga zasady narzutu proporcjonalnego. Dlaczego tak jest? Otóż wartość oczekiwana obecnej wartości wypłaty jest większa od odchylenia standardowego z tej samej wartości. Wobec tego zwyczajnie z zasady narzutu proporcjonalnego wychodzi przy tym samym współczynniku wyższa cena - a to w oczywisty sposób zmniejsza ryzyko bankructwa.

Na koniec porównajmy jeszcze portfele 100 i 1000 klientów. Przy zasadzie odchylenia standardowego spróbujmy oszacować jaki współczynnik narzutu zapewni mniejszemu portfelowi podobne ryzyko bankructwa do portfela większego.

- Portfel 100 klientów:

![](figures/bankrupcy_vs/bankrupcy_vs_alphasigma_n100.png)

- Portfel 1000 klientów:

![](figures/bankrupcy_vs/bankrupcy_vs_alphasigma_n1000.png)

Jak widać na powyższych wykresach - prawdopodobieństwo bankructwa portfela 1000 klientów zbliża się do 0 już w okolicach $\alpha = 0.1$, natomiast dla mniejszego portfela osiągniecie tej samej wartości wymaga już współczynnika $\alpha = 0.3$

## Wnioski
- Z przeprowadzonej analizy wynika, iż portfele o wyższej liczbie klientów cechuje niższe ryzyko bankructwa. Jedyna sytuacja w której pojawia się niewielka przewaga na rzecz portfeli mniejszych to sytuacja braku narzutu finansowego - czego nie uświadczymy rzecz jasna w praktyce. 
- Obie formy narzutu prowadzą do zadowalających rezultatów, przy czym narzut proporcjonalny przy tym samym współczynniku prowadzi do lepszych wyników.
- Nawet różnica jednego rzędu wielkości w liczbie klientów prowadzi do zauważalnie wyższych cen świadczenia - jeżeli chcemy zagwarantować to samo ryzyko. Stąd bycie ubezpieczycielem o niskiej skali działalności zmusza nas do niskiej konkurencyjności względem innych firm. Przy zapewnieniu podobnych cen mały ubezpieczyciel naraża się na wyższe ryzyko, co w dłuższej perspektywie może doprowadzić do spadku zaufania wobec niego.

## Bibliografia:
1. Błaszczyszyn B., Rolski T.,  
   *Podstawy matematyki ubezpieczeń na życie*,  
   Wydawnictwo Naukowe PWN, Warszawa, 2018. :contentReference[oaicite:0]{index=0}

2. Główny Urząd Statystyczny (GUS),  
   *Tablice trwania życia ludności Polski 2022*,  
   Warszawa, 2023.  
   Dostęp online: https://stat.gov.pl/en/topics/population/life-expectancy/life-expectancy-tables-of-poland-2022/

# WB-XIC: Projekt

**TL;DR**: W projekcie staramy się podejść do wyzwania z dziedziny wyjaśnialnego uczenia maszynowego zdefiniowanego w artykule: 
> H. Müller & A. Holzinger. **Kandinsky Patterns**. *Artificial Intelligence*, 300, 103546. 2021. URL: https://doi.org/10.1016/j.artint.2021.103546.

## Opis

| ![Kandinsky Patterns introduce a set of challenges focusing on developing **human-understandable** explanations of machine learning predictive models. Each challenge is associated with a corresponding dataset generated from the **ground-truth** human explanation of a given abstract phenomenon. An exemplary challenge is “Objects and Shapes”, where the ground-truth defines strict relations between the patterns’ shapes and colors, while the **contradictory** and **random** patterns need to be carefuly distinguished and explained.](graphical_abstract.png) |
|:--:| 
| Kandinsky Patterns wprowadzają zbiór wyzwań skupiających się na rozwijaniu **zrozumiałych przez człowieka** wyjaśnień modeli predykcyjnych uczenia maszynowego. Każde wyzwanie związane jest z odpowiadającym jemu zbiorem danych wygenerowanym z pewnej **definicji** wyjaśnienia; ludzkiego wyjaśnienia danego abstrakcyjnego zjawiska. Przykładowym wyzwaniem są “Obiekty i Kształty”, gdzie definicja ta opisuje ścisłe reguły powstawania wzorców z odpowiednimi kształtami i kolorami na obrazie, podczas gdy **sprzeczne** i **losowe** wzory powinny być odróżnione i wyjaśnione. |

Podstawowy plan projektu zakłada wytrenowanie modeli klasyfikacyjnych na wybranym wyzwaniu (danych), a następnie wyjaśnienie ich przy pomocy ogólnodostępnych metod. Częścią rozszerzającą projekt powinna być próba zaadresowania szczególnego zjawiska/problemu; na przykład:
- wyjaśnienie związane z kolorem,
- wyjaśnienie związane z kształtem,
- wyjaśnienia tekstowe,
- klasyfikacja i wyjaśnienie wielu wyzwań jednocześnie,
- analiza wektora/przestrzeni reprezentacji,
- analiza wyjaśnień klas sprzecznych i losowych,
- generowanie nowych wyzwań i danych,
- animacja i wizualizacja wyjaśnień.

## Harmonogram i szczegóły

1. Na **04-21**: raport z **KM1** w postaci jupyter notebook
- Wybranie i poprawne zdefiniowanie problemu do rozwiązania (1pkt)
- Wstępne podejście do modelowania danych związanych z artykułem (2pkt)
- 3x [TL;DR wybranego artykułu z dziedziny + dobra i słaba strona artykułu + zaleta/wada metody, danych etc. (łącznie 4-5 zdań)] (3pkt)
- Jakość raportu oraz wyniki ponad powyższy program (2pkt)
2. Na **05-05**: raport z **KM2** w postaci jupyter notebook
- Działające modele do klasyfikacji (1pkt)
- Wstępne podejście do wyjaśnień związanych z postawionym problemem (2pkt)
- 3x [TL;DR wybranego artykułu z dziedziny + dobra i słaba strona artykułu + zaleta/wada metody, danych etc. (łącznie 4-5 zdań)] (3pkt)
- Jakość raportu oraz wyniki ponad powyższy program (2pkt)
3. Na **05-19**: raport z **KM3** w postaci jupyter notebook
- Wyjaśnienie klasyfikatora metodami z labolatoriów (1pkt)
- Dopracowane podejście do wyjaśnień związanych z postawionym problemem (2pkt)
- 3x [TL;DR wybranego artykułu z dziedziny + dobra i słaba strona artykułu + zaleta/wada metody, danych etc. (łącznie 4-5 zdań)] (3pkt)
- Jakość raportu (1pkt)
- Szablon sekcji raportu <ins>końcowego</ins> (1pkt)
4. Na **06-03**: raport końcowy w PDF (co najmniej pierwsza wersja)
- Abstrakt, wstęp, motywacja [0-5 punktów]
- Literatura i jakość bibliografii [0-4 punktów]
- Główne wyniki pracy [0-14 punktów]
- Wnioski [0-5 punktów]
- Jakość wykresów / wizualizacji / diagramów, umiejętne korzystanie z LaTeXa [0-4 punktów]

## Zgłaszanie postępów

Postępy, raporty zgłaszamy poprzez PR o tytule `[KM{#N}] Nazwisko1 Nazwisko2 Nazwisko3` do folderu `projects/nazwisko1_nazwisko2_nazwisko3/km{#N}`, gdzie w miejsce `{#N}` wstawiamy 1, 2, lub 3. Omawiane są w powyższych dniach na indywidualnych konsultacjach z zespołem.

## Przydatne linki
- Dane (wyzwania) https://github.com/human-centered-ai-lab/dat-kandinsky-patterns
- Generator https://github.com/human-centered-ai-lab/app-kandinsky-pattern-generator
- Artykuł https://doi.org/10.1016/j.artint.2021.103546
- Wyjaśnienia oparte na konceptach https://christophm.github.io/interpretable-ml-book/detecting-concepts.html; https://arxiv.org/abs/1711.11279; https://arxiv.org/abs/1902.03129
- Holzinger et al. **KANDINSKY Patterns as IQ-Test for Machine Learning**. CD-MAKE, 2019. https://link.springer.com/chapter/10.1007/978-3-030-29726-8_1
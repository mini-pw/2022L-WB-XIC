# Praca Domowa 2

Indywidualnie, zaimplementować model konwolucyjnej sieci neuronowej (CNN) do klasyfikacji w `torch` i przetestować go na **wybranym zbiorze danych**. Powstały raport w formatach `.ipynb` oraz `.html` powinien zawierać wnioski z przeprowadzonej analizy.
1. 1 punkt uzyskuje się za pracę z zbiorem danych [CIFAR10](https://pytorch.org/vision/main/generated/torchvision.datasets.CIFAR10.html)  (60k [take a subset: 1/3-1/2], 10 classes, 32x32 images)
2. 2 punkty uzyskuje się za pracę z zbiorem danych [OxfordIIITPet](https://pytorch.org/vision/main/generated/torchvision.datasets.OxfordIIITPet.html)  (7.4k, 37 classes, varied sizes of images)
3. 3 punkty uzyskuje się za pracę z zbiorem danych [StanfordCars](https://pytorch.org/vision/main/generated/torchvision.datasets.StanfordCars.html) (17k [if too large, take a subset], 196 classes, 360×240 images)

- do 2 punktów uzyskuje się za wytrenowanie skutecznego modelu ResNet (porównać dwie wielkości, np. 18 i 34, na zbiorze treningowym i testowym)
- 1 punkt uzyskuje się za zaprezentowanie zwalczania zjawiska przeuczenia wykorzystując Dropout (lub inny sposób regularyzacji)
- 1 punkt uzyskuje się za zwizualizowanie macierzy konfuzji ORAZ pokazanie ozasadnionych/ciekawych przykłady obrazów, na których model się mylił 
- 1 punkt uzyskuje się za zwizualizowanie wektora reprezentacji obrazów w podziale na klasy (kolor), wykorzystując PCA/TSNE (lub inny algorytm redukcji wymiaru)
- do 2 punktów uzyskuje sie za jakość raportu (opisu, wizualizacji, kodu), a w szczególności *agregację wyników* w postaci tabel lub/i wykresów.

**Uwaga!** (1) Zabronione jest importowanie modeli z bibliotek; można korzystać z repozytoriów takich jak https://github.com/kuangliu/pytorch-cifar. (2) Warto zacząć od uczenia sieci na podzbiorze, np. 10%, danych treningowych (i ewaluowania na podzbiorze danych testowych) dla zaoszczędzenia czasu. 

Praca domowa jest na 8 punktów (można uzyskać max 10 punktów).

Deadline: 30 marca 23:59. Na zajęciach 31 marca 5 wybranch osób krótko zaprezentuje swoje wyniki.

Pracę zgłaszamy poprzez PR o tytule `[PD2] Imię Nazwisko` do folderu `homeworks/pd2/imię_nazwisko`.

# Wizualizacja wektora reprezentacji obrazów

Przykład: https://medium.com/@pslinge144/representation-learning-cifar-10-23b0d9833c40

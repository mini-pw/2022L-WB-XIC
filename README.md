# WB-XIC: Explaining Image Classification

Semestr Wiosenny 2021/22 [@hbaniecki](https://github.com/hbaniecki)

## Tematyka zajęć

Kontekst: [Knowing What and Why? — Explaining Image Classifier Predictions](https://towardsdatascience.com/knowing-what-and-why-explaining-image-classifier-predictions-680a15043bad)

Projekty:
1. Klasyfikacja obrazu i kreatywne wyjaśnianie zagadnień opisanych w pracy [Kandinsky Patterns](https://www.sciencedirect.com/science/article/pii/S0004370221000977)
2. Zostanie podany na zajęciach

Materiały:
1. [Neural networks by 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi), [Neural Network Playground](https://playground.tensorflow.org)
2. [An Introduction to Statistical Learning, **Chapter 10**](https://www.statlearning.com/)
3. [Interpretable Machine Learning. A Guide for Making Black Box Models Explainable, **Chapter 10**](https://christophm.github.io/interpretable-ml-book/)
4. [Dive into Deep Learning, **Chapters 1-7**](https://d2l.ai/index.html)
5. [Explanatory Model Analysis. Explore, Explain and Examine Predictive Models](https://pbiecek.github.io/ema/)

Technologie:
- [torch](https://pytorch.org/)
- [captum](https://captum.ai/) - Model Interpretability for PyTorch
- [shap](https://github.com/slundberg/shap) - SHapley Additive exPlanations

Dane:
- Fashion-MNIST: [[GitHub](https://github.com/zalandoresearch/fashion-mnist)] [[PyTorch](https://pytorch.org/vision/stable/datasets.html#fashion-mnist)]
- .

Literatura:
- M. T. Ribeiro et al. **"Why Should I Trust You?": Explaining the Predictions of Any Classifier.** KDD, 2016. https://doi.org/10.1145/2939672.2939778
- S. M. Lundberg & S. Lee. **A Unified Approach to Interpreting Model Predictions.** NeurIPS, 2017. https://dl.acm.org/doi/10.5555/3295222.3295230
- M. Sundararajan et al. **Axiomatic attribution for deep networks.** ICML, 2017. https://dl.acm.org/doi/10.5555/3305890.3306024
- J. Adebayo et al. **Sanity Checks for Saliency Maps.** NeurIPS, 2018. https://dl.acm.org/doi/10.5555/3327546.3327621
 

## Terminy zajęć 

<table>
<thead>
  <tr>
    <th></th>
    <th>data</th>
    <th>temat</th>
    <th>zadanie</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>02-24</td>
    <td>Opis zajęć i przedstawienie tematyki projektu.</td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>03-03</td>
    <td>Wstęp do sieci neuronowych i PyTorch.</td>
    <td>PD-1 start</td>
  </tr>
  <tr>
    <td>3</td>
    <td>03-10</td>
    <td>Sieci neuronowe w praktyce.</td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>03-17</td>
    <td>Wstęp do konwolucyjnych sieci neuronowych (ResNet, DenseNet).</td>
	  <td>PD-1 oddanie,<br>PD-2 start</td>
  </tr>
  <tr>
    <td>5</td>
    <td>03-24</td>
    <td>Konwolucyjne sieci neuronowe w praktyce.</td>
    <td></td>
  </tr>
  <tr>
    <td>6</td>
    <td>03-31</td>
    <td>Wstęp do wyjaśnień konwolucyjnych sieci neuronowych (SHAP, IG etc.).</td>
	  <td>PD-2 oddanie,<br>PD-3 start</td>
  </tr>
  <tr>
    <td>7</td>
    <td>04-07</td>
    <td>Wyjaśnienia konwolucyjnych sieci neuronowych w praktyce.</td>
    <td>KM-1 start</td>
  </tr>
	<tr><td colspan="4"></td></tr>
  <tr>
    <td>8</td>
    <td>04-14</td>
    <td>Przegląd danych związanych z projektem.</td>
    <td>PD-3 oddanie</td>
  </tr>
  <tr>
    <td>9</td>
    <td>04-21</td>
    <td>Przedstawienie postępów projektów, konsultacje.</td>
    <td>KM-1 oddanie,<br>KM-2 start</td>
  </tr>
  <tr>
    <td>10</td>
    <td>04-28</td>
    <td>Przegląd modeli związanych z projektem.</td>
    <td></td>
  </tr>
  <tr>
    <td>11</td>
    <td>05-05</td>
    <td>Przedstawienie postępów projektów, konsultacje.</td>
    <td>KM-2 oddanie,<br>KM-3 start</td>
  </tr>
  <tr>
    <td>12</td>
    <td>05-19</td>
    <td>Przegląd wyjaśnień związanych z projektem.</td>
    <td>
  </tr>
  <tr>
    <td>13</td>
    <td>05-26</td>
    <td>Przedstawienie postępów projektów, konsultacje.</td>
    <td>KM-3 oddanie,<br>Prezentacja</td>
  </tr>
  <tr>
    <td>14</td>
    <td>06-02</td>
    <td>*Manipulowanie wyjaśnieniami sieci neuronowych.</td>
    <td>Raport</td>
  </tr>
  <tr>
    <td>15</td>
    <td>06-09</td>
    <td>Podsumowanie projektu.</td>
    <td></td>
  </tr>
</tbody>
</table>

## Zasady oceniania (100 pkt)

Warszataty Badawcze składają się z wykładu, zajęć laboratoryjnych i projektowych:

-   praca podczas projektu -- 6 x 8 pkt = 48 pkt.
-   prezentacja końcowa na wykładzie -- 16 pkt. (deadline: 29 maja)
-   raport końcowy -- 32 pkt. (deadline: 3 czerwca)
-   stosowanie dobrych praktyk wykorzystania GitHub -- 4 pkt.

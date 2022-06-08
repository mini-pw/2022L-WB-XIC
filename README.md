# WB-XIC: Explaining Image Classification

Semestr Wiosenny 2021/22 [@hbaniecki](https://hbaniecki.com)

## Tematyka zajęć

Kontekst: [Knowing What and Why? — Explaining Image Classifier Predictions](https://towardsdatascience.com/knowing-what-and-why-explaining-image-classifier-predictions-680a15043bad)

Projekt: Klasyfikacja obrazu i kreatywne wyjaśnianie zagadnień opisanych w pracy [Kandinsky Patterns](https://www.sciencedirect.com/science/article/pii/S0004370221000977).

Materiały:
1. [Neural networks by 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi); [Neural Network Playground](https://playground.tensorflow.org)
2. [An Introduction to Statistical Learning, **Chapter 10**](https://www.statlearning.com/)
3. [Interpretable Machine Learning. A Guide for Making Black Box Models Explainable, **Chapter 10**](https://christophm.github.io/interpretable-ml-book/neural-networks)
4. [Dive into Deep Learning, **Chapters 1-7**](https://d2l.ai/index.html); [CNN Explainer](https://poloclub.github.io/cnn-explainer)
5. [Explanatory Model Analysis. Explore, Explain and Examine Predictive Models](https://pbiecek.github.io/ema/)

Technologie:
- [torch](https://pytorch.org/), [torchvision](https://pytorch.org/vision)
- [captum](https://captum.ai/) - Model Interpretability for PyTorch
- [shap](https://github.com/slundberg/shap) - SHapley Additive exPlanations

Dane:
- Fashion-MNIST: [[GitHub](https://github.com/zalandoresearch/fashion-mnist)] [[PyTorch](https://pytorch.org/vision/stable/datasets.html#fashion-mnist)]
- CIFAR10: [[PyTorch](https://pytorch.org/vision/main/generated/torchvision.datasets.CIFAR10.html)]; CIFAR100: [[PyTorch](https://pytorch.org/vision/main/generated/torchvision.datasets.CIFAR100.html)]
- ImageNet: [[.org](https://image-net.org/)]
- Kandinsky Patterns: [[GitHub](https://github.com/human-centered-ai-lab/dat-kandinsky-patterns)]

Literatura:
- Y. LeCun et al. **Backpropagation Applied to Handwritten Zip Code Recognition.** *Neural Computation*, 1989. https://www.doi.org/10.1162/neco.1989.1.4.541; http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf
- A. Krizhevsky et al. **ImageNet Classification with Deep Convolutional Neural Networks.** *NeurIPS*, 2012. https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- S. Ioffe & C. Szegedy. **Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift.** *ICML*, 2015. https://dl.acm.org/doi/10.5555/3045118.3045167; https://arxiv.org/abs/1502.03167
- K. He et al. **Deep Residual Learning for Image Recognition.** *CVPR*, 2016. https://www.doi.org/10.1109/CVPR.2016.90; https://arxiv.org/abs/1512.03385
- M. T. Ribeiro et al. **"Why Should I Trust You?": Explaining the Predictions of Any Classifier.** *KDD*, 2016. https://www.doi.org/10.1145/2939672.2939778; https://arxiv.org/abs/1602.04938
- G. Huang et al. **Densely Connected Convolutional Networks.** *CVPR*, 2017. https://www.doi.org/10.1109/CVPR.2017.243; https://arxiv.org/abs/1608.06993
- M. Sundararajan et al. **Axiomatic attribution for deep networks.** *ICML*, 2017. https://dl.acm.org/doi/10.5555/3305890.3306024; https://arxiv.org/abs/1703.01365
- S. M. Lundberg & S. Lee. **A Unified Approach to Interpreting Model Predictions.** *NeurIPS*, 2017. https://dl.acm.org/doi/10.5555/3295222.3295230; https://arxiv.org/abs/1705.07874
- J. Adebayo et al. **Sanity Checks for Saliency Maps.** *NeurIPS*, 2018. https://dl.acm.org/doi/10.5555/3327546.3327621; https://arxiv.org/abs/1810.03292
- H. Müller & A. Holzinger **Kandinsky Patterns.** *Artificial Intelligence*, 2021. https://doi.org/10.1016/j.artint.2021.103546

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
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/labs/lab2" target="_blank">Wstęp do sieci neuronowych i PyTorch.</a></td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/homeworks/pd1" target="_blank">PD-1 start</a></td>
  </tr>
  <tr>
    <td>3</td>
    <td>03-10</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/labs/lab3" target="_blank">Sieci neuronowe w praktyce.</a></td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>03-17</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/labs/lab4" target="_blank">Wstęp do konwolucyjnych sieci neuronowych.</a></td>
	  <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/homeworks/pd1" target="_blank">PD-1 oddanie</a>,
		  <br><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/homeworks/pd2" target="_blank">PD-2 start</a></td>
  </tr>
  <tr>
    <td>5</td>
    <td>03-24</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/labs/lab5" target="_blank">Konwolucyjne sieci neuronowe w praktyce (ResNet, DenseNet).</a></td>
    <td></td>
  </tr>
  <tr>
    <td>6</td>
    <td>03-31</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/labs/lab6" target="_blank">Wstęp do wyjaśnień konwolucyjnych sieci neuronowych (LIME, IG etc.).</a></td>
	  <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/homeworks/pd2" target="_blank">PD-2 oddanie</a>,
		  <br><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/homeworks/pd3" target="_blank">PD-3 start</a></td>
  </tr>
  <tr>
    <td>7</td>
    <td>04-07</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/labs/lab7" target="_blank">Wyjaśnienia konwolucyjnych sieci neuronowych c.d. (SHAP, TCAV etc.).</a></td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/projects" target="_blank">KM-1 start</a></td>
  </tr>
	<tr><td colspan="4"></td></tr>
  <tr>
    <td>8</td>
    <td>04-14</td>
    <td>Przegląd danych i modeli związanych z projektem.</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/homeworks/pd3" target="_blank">PD-3 oddanie</a></td>
  </tr>
  <tr>
    <td>9</td>
    <td>04-21</td>
    <td>Przedstawienie postępów projektów, konsultacje.</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/projects" target="_blank">KM-1 oddanie</a>,<br><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/projects" target="_blank">KM-2 start</a></td>
  </tr>
  <tr>
    <td>10</td>
    <td>04-28</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/labs/lab10" target="_blank">Przegląd postępów w projekcie i struktury raportu.</a></td>
    <td></td>
  </tr>
  <tr>
    <td>11</td>
    <td>05-<b>05</b></td>
    <td>Przedstawienie postępów projektów, konsultacje.</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/projects" target="_blank">KM-2 oddanie</a>,<br><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/projects" target="_blank">KM-3 start</a></td>
  </tr>
  <tr>
    <td>12</td>
    <td>05-<b>19</b></td>
    <td>Przedstawienie postępów projektów, konsultacje.</td>
    <td><a href="https://github.com/MI2-Education/2022L-WB-XIC/tree/main/projects" target="_blank">KM-3 oddanie</a></td>
  </tr>
  <tr>
    <td>13</td>
    <td>05-26</td>
    <td>Przedstawienie i dyskusja wyników projektu na zajęciach.</td>
    <td>Prezentacja</td>
  </tr>
  <tr>
    <td>14</td>
    <td>06-02</td>
    <td>*Prezentacja: <a href="https://github.com/hbaniecki/talks/blob/main/2021/mlinpl_manipulating.pdf" target="_blank">Manipulowanie wyjaśnieniami sieci neuronowych.</a></td>
    <td>Raport v0.1</td>
  </tr>
  <tr>
    <td>15</td>
    <td>06-09</td>
    <td>Podsumowanie zajęć laboratoryjnych i projektowych.</td>
    <td>Raport v1.0</td>
  </tr>
</tbody>
</table>

## Zasady oceniania (100 pkt)

Warszataty Badawcze składają się z wykładu, zajęć laboratoryjnych i projektowych:

-   praca podczas laboratoriów i projektu -- 6 x 8 pkt = 48 pkt.
-   prezentacja końcowa na wykładzie -- 16 pkt. (deadline: 29 maja)
-   raport końcowy -- 32 pkt. (deadline: 9 czerwca)
-   stosowanie dobrych praktyk wykorzystania GitHub -- 4 pkt.

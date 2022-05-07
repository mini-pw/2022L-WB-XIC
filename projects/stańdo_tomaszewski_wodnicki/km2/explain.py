from captum.attr import Lime, IntegratedGradients, KernelShap
from skimage import segmentation
import matplotlib.pyplot as plt
import torch


def lime_explain(m, img, target):
    explainer = Lime(m.cpu())

    mask = segmentation.quickshift(
        img.permute(1, 2, 0).double(), 
        kernel_size=14, 
        max_dist=7, 
        ratio=0.5
    )

    attr = explainer.attribute(
        img.unsqueeze(0), 
        target=target, 
        n_samples=200, 
        feature_mask=torch.as_tensor(mask),
        show_progress=False
    )


    def show_image_mask_explanation(image, mask, explanation):
        plt.axis("off")
        plt.imshow(explanation, cmap="bwr")
        plt.colorbar()

    show_image_mask_explanation(img, mask, attr[0].mean(axis=0))
 
    
def IG_explain(m, img, target):
    explainer = IntegratedGradients(m.cpu())

    attr = explainer.attribute(img.unsqueeze(0), target=target)
    plt.axis("off")
    plt.imshow(attr[0].mean(axis=0), cmap="bwr")
    plt.colorbar()

    
def SHAP_explain(m, img, target):
    explainer = KernelShap(m.cpu())

    mask = segmentation.quickshift(
        img.permute(1, 2, 0).double(), 
        kernel_size=14, 
        max_dist=7, 
        ratio=0.5
    )

    attr = explainer.attribute(
        img.unsqueeze(0), 
        target=target, 
        n_samples=200, 
        feature_mask=torch.as_tensor(mask),
        show_progress=False
    )

    plt.axis("off")
    plt.imshow(attr[0].mean(axis=0), cmap="bwr")
    plt.colorbar()
   
    
def explain_image(m, single_test_loader, idx, mapping):
    i = 0
    img = None
    for batch in single_test_loader:  
        if i == idx:
            img = batch[0][0]
            label = batch[1]
            break
        i = i + 1

    _, predicted = m(img.unsqueeze(0)).max(1)
    predicted = predicted.item()


    plt.figure(figsize = (20, 5))
    plt.suptitle(f'Classification explanation, predicted class: {mapping[predicted]}, true class: {mapping[label.item()]}')

    plt.subplot(1, 4, 1)
    plt.axis("off")
    plt.title('Original image')
    plt.imshow(img.permute(1, 2, 0))

    plt.subplot(1, 4, 2)
    lime_explain(m, img, label.item())
    plt.title("Lime explanation")

    plt.subplot(1, 4, 3)
    IG_explain(m, img, label.item())
    plt.title("Integrated Gradients explanation")

    plt.subplot(1, 4, 4)
    SHAP_explain(m, img, label.item())
    plt.title("SHAP explanation")

    plt.show()
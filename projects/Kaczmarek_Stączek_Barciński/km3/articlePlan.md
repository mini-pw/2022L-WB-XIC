# The plan of the article

## Title
Explaining CNN models trained on Kandinsky Patterns 

## Abstract  
A few words about our main work - training models on one of the Kandisnky Patterns datasets and explaining them.

## Introduction
Importance of this topic. Related work.

## Methods

### Data decription
Used code available online to generate more data and to not be limited to 3k images linked to this article.

### Used models
First, a complex, pretrained ResNet18, then a simple CNN + architecture were used. Accuracy scores. Probabilities (the model is rather confident about it's decisions).

## Results

### Image representations 
Show PCA of image representations by a model at the last layer - explain clusters. Do not include this paragraph if no explanations were made.

### Local Explanations
Include a few SHAP/LIME/IG images next to each other, overwhelm the reader and summarize stating that local explanations are not the solution for finding the rules differentiating the classes.

### Global Explanations
A mention of the attempt to add a few SHAP explanation images together with poor results (image). Possibly add an early attempt of accumulating data in tabular form (shape and color of a few most important small figures as selected by SHAP).

## Conclusion
Summarize what's above.
Future work for continuing this work and ideas for different approaches.

## References
Possibly reuse a few articles read for the previous milestones.

# Machine Learning Engineer Nanodegree
## Capstone Proposal

# Malaria Cells Detection

Daniel Valcarce

May 14th, 2019

## Domain Background

According to the <em>World malaria report</em><sup>1</sup>, in 2017, an estimated 219 million cases of malaria occurred worldwide (95% confidence interval [CI]: 203–262 million), compared with 239 million cases in 2010 (95% CI: 219–285 million) and 217 million cases in 2016 (95% CI: 200–259 million).

In 2017, there were an estimated 435 000 deaths from malaria globally, compared with 451000 estimated deaths in 2016, and 607000 in 2010. Nearly 80% of global malaria deaths in 2017 were concentrated in 17 countries in the WHO African Region and India; 7 of these countries accounted for 53% of all global malaria deaths.

Effective surveillance of malaria cases and deaths is essential for identifying the areas or population groups that are most affected by malaria, and for targeting resources for maximum impact. A strong surveillance system requires high levels of access to care and case detection, and complete reporting of health information by all sectors, whether public or private. 

## Problem Statement

In order to reduce the burden for microscopists in resource-constrained regions and improve diagnostic accuracy, the <em>National Library of Medicine</em><sup>2</sup> provide us with a dataset<sup>3</sup> with which we will create a model to detect malaria parasite in thin blood smear images.

## Datasets and Inputs

A detailed description about how the images had been obtained and labeled can be found in the dataset page<sup>4</sup>.

The dataset contains a total of 27560 images separated in two folders, Parasitized folder and Uninfected folder with 13780 images each.

The images size varies between 49x58 and 349x241.

## Solution Statement

The solution proposed is to create a CNN image classifier to know when an image of a cell is parasitized or uninfected, applying the progressive resizing technique<sup>5</sup>, consisting in a progressive, sequential resizing of all images while training, from smaller to bigger sizes.

The Accuracy is a good metric to evaluate the model due to the dataset is well balanced for both classes, having the same amount of images for each, parasitized and uninfected, but other metrics like F1-score or Specificity could be interesting to use as well.

## Benchmark Model

In the research article "Pre-trained convolutional neural networks as feature extractors toward improved malaria parasite detection in thin blood smear images"<sup>6</sup>, Dr Rajaraman S and his team shown a table<sup>7</sup> with the performance metrics results obtained during their experiments, comparing their custom model against other well-known models like AlexNet, VGG-16, ResNet-50, Xception and DenseNet-121. 

In our project we will use the same metrics and we will to compare the results against the values of their custom model.

## Evaluation Metrics

In the article cited before the metrics used are: 
- Accuracy
- AUC
- Sensitivity
- Specificity
- F1-score
- MCC

We will use the same evaluation metrics in order to compare if our model performs better or worst than theirs.

## Project Design

- No clean data
- Split data into Training / Validation / Test
- Design the network with default values
- Train the model and evaluate
- Tuning - Re-train
- Test the model against Test data
- Show the results obtained

## References

1. https://www.who.int/malaria/media/world-malaria-report-2018/en/
2. https://www.nlm.nih.gov/
3. https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip (zip file ~345 MB)
4. https://ceb.nlm.nih.gov/repositories/malaria-datasets/
5. https://towardsdatascience.com/boost-your-cnn-image-classifier-performance-with-progressive-resizing-in-keras-a7d96da06e20
6. https://peerj.com/articles/4568/
7. https://peerj.com/articles/4568/#table-2
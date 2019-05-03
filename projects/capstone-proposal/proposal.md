# Machine Learning Engineer Nanodegree
## Capstone Proposal

# State Farm Distracted Driver Detection

Daniel Valcarce

May 3rd, 2019


## Domain Background

According to the [CDC][1] motor vehicle safety division, one in five car accidents is caused by a distracted driver. Each day in the United States, approximately 9 people are killed and more than 1,000 injured in crashes that are reported to involve a distracted driver<sup>1</sup>, this translates to 425,000 people injured and 3,000 people killed by distracted driving every year.

Distracted driving is driving while doing another activity that takes your attention away from driving. Distracted driving can increase the chance of a motor vehicle crash

## Problem Statement

In the [Kaggle competition][1], [State Farm][2] hopes to improve these alarming statistics, and better insure their customers, by testing whether dashboard cameras can automatically detect drivers engaging in distracted behaviors. Given a dataset of 2D dashboard camera images, State Farm is challenging Kagglers to classify each driver's behavior. Are they driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat?


## Datasets and Inputs

The dataset consist in 102150 images of drivers, each taken in a car with a driver doing something in the car (texting, eating, talking on the phone, makeup, reaching behind, etc).

The train set is divided in 10 categories, one per class to be classified and contains ~2300 images each.

The test set contains ~79000 images.

All images has been resized to a resolution of 640x480

## Solution Statement

## Benchmark Model

## Evaluation Metrics

The metric to evaluate the performance of the model will be the multi-class logarithmic loss.

![multi-class logarithmic loss formula](./logloss_formula.svg)

Where <em>N</em> is the number of images in the test set, <em>M</em> is the number of image class labels, <em>log</em> is the natural logarithm, <em>y<sub>ij</sub></em> <em>y<sub>ij</sub></em>is 1 if observation <em>i</em>
belongs to class <em>j</em> and 0 otherwise, and <em>p<sub>ij</sub></em> is the predicted probability that observation <em>i</em> belongs to class <em>j</em>

## Project Design

## References

1. National Highway Traffic Safety Administration. Traffic Safety Facts Research Notes 2016: Distracted Driving.S. Department of Transportation, Washington, DC: NHTSA; 2015 [https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812517](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812517)

[1]: https://www.cdc.gov/motorvehiclesafety/distracted_driving/
[2]: https://www.kaggle.com/c/state-farm-distracted-driver-detection/data
[3]: https://www.statefarm.com/
---
layout: page
title: "Image Recognition with CNNs"
subheadline: "Using Bayesian Deep Learning to Improve CNN Image Recognition Accuracy"
teaser: "Image Recognition Project Highlights and Details"
permalink: "/imagerecognitionproject/"
header:
    image_fullwidth: "IMG_20171229_065330815(1).jpg"
---

## Highlights

* The goal of this project was to use a novel Bayesian deep learning network (a deep convolutional gaussian process, or DCGP) to improve the performance of an image classification convolutional neural network  (CNN) without requiring more training data. 
* DCGPs tend to be less accurate than CNNs for image recognition tasks, but are frequently more confident about their predictions than most CNNs. Using this property, we can combine the answers of the CNN and the DCGP to get better classification results. 
* We used both a 3-layer CNN and a 2-layer DCGP to classify 10,000 images from the commonly-used CIFAR-10 dataset. These results, as well as the confidence values each network gave their classifications, were then passed into another CNN to produce final answers. The resulting classification accuracy was superior to either of the networks on their own. 
* This project improved the accuracy of our CNN on CIFAR-10 by 6%, from 72% to 78%, without an increase in training data. This technique could, therefore, be useful in domains with limited training data. 

## Technologies Used

* Python
* Jupyter
* Numpy
* Pytorch, Tensorflow, Keras, and GPFlow (Library for gaussian processes in Python)
* Convolutional neural networks and deep convolutional gaussian processes

## Project Introduction & Details

### Introduction

Bayesian deep learning offers a number of advantages over typical deep learning methods. Bayesian neural nets, unlike regular neural nets, incorporate uncertainty into their decision-making processes. In practice, this trait of bayesian networks is useful because it enables types of statistical analysis that are impossible with other kinds of neural nets. In particular, it is possible to measure how confident the network is about each prediction it makes. These confidence values can then be used to make decisions about how much to trust / distrust the output of the model. In addition, confidence values from Bayesian neural networks are, when compared with those from more traditional deep learnig methods, much higher (see the Difference in Confidence of Prediction figure below). However, despite these advantages, DCGPs tend to have lower accuracy than traditional image classification networks. For this reason, the goal of this project was not to replace the standard image recognition methodology, but to improve its accuracy with the help of a DCGP. 

By taking advantage of the DCGP's relatively high confidence values we can improve a convolutional neural network's (CNN) classification accuracy by replacing low-confidence classifications from the CNN with high-confidence classifications from the DCGP. These replacements aren't 100% beneficial, but testing shows a signficant net gain in accuracy. This methodology is desirable because it results in higher classification accuracy witout requiring more training data. 

### Images

#### Sample of CIFAR-10 Images

This is a sample of pictures contained in the CIFAR-10 dataset. The dataset contains 10 different classes of image. 

![Sample CIFAR-10 Images](/assets/img/CIFAR10images.jpeg)

#### Difference in Confidence of Predictions 

This is a graph showing the different average confidence levels per classification of our DCGP and CNN. 

![CNN / DCGP Confidence Values](/assets/img/CNN_DCGP_Conf.jpg)

#### Project Results

This is a bar graph showing the final classification results of each of our networks. DCGP is the deep convolutional gaussian process, ICNN is our initial CNN result, and ECNN is the improved result obtained by combining the other two networks' outputs. 

![CNN Project Results](/assets/img/CNNProjectresults.jpg)


## References

The DCGP was originally proposed in this paper:

Blomqvist, Kenneth, Samuel Kaski, and Markus Heinonen. "Deep convolutional Gaussian processes." Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2019, Würzburg, Germany, September 16–20, 2019, Proceedings, Part II. Springer International Publishing, 2020.

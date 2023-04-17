---
layout: page
title: "Image Recognition with CNNs"
subheadline: "Using Bayesian Deep Learning to Improve CNN Image Recognition Accuracy"
teaser: "Image Recognition Project highlights and details"
permalink: "/imagerecognitionproject/"
header:
    image_fullwidth: "header_drop.jpg"
---

## Highlights

* The goal of this project was to use a novel Bayesian deep learning network (a deep convolutional gaussian process or DCGP) to improve the performance of an image classification convolutional neural network. 
* DCGPs tend to be less accurate than CNNs for image recognition tasks, but are frequently more confident about their predictions than most CNNs. Using this property, we can combine the answers of the CNN and the DCGP to get better classification results. 
* We used both a 4-layer CNN and a 3-layer DCGP to classify images from the commonly-used CIFAR-10 dataset. These results, as well as the confidence values each network gave their classifications, were then passed into another CNN to produce final answers. The resulting classification accuracy was superior to either of the networks on their own. 
* This project improved the accuracy of our CNN on CIFAR-10 by 6%, from 72% to 78%, without an increase in training data. This technique could, therefore, be useful in domains with limited training data. 

## Technologies Used

* Python
* Jupyter
* Numpy
* Tensorflow, Keras, and GPFlow (Library for gaussian processes in Python)
* Convolutional neural networks and deep convolutional gaussian processes

## Summary

![CNN Project Results](/assets/img/CNNProjectresults.jpg)


## References

The DCGP was originally proposed in this paper:

Blomqvist, Kenneth, Samuel Kaski, and Markus Heinonen. "Deep convolutional Gaussian processes." Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2019, Würzburg, Germany, September 16–20, 2019, Proceedings, Part II. Springer International Publishing, 2020.

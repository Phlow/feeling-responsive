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

* The goal of this project was to use a novel Bayesian deep learning network (a deep convolutional gaussian process or DCGP) to improve the performance of an image classification convolutional neural network without requiring more training data. 
* DCGPs tend to be less accurate than CNNs for image recognition tasks, but are frequently more confident about their predictions than most CNNs. Using this property, we can combine the answers of the CNN and the DCGP to get better classification results. 
* We used both a 3-layer CNN and a 2-layer DCGP to classify 10,000 images from the commonly-used CIFAR-10 dataset. These results, as well as the confidence values each network gave their classifications, were then passed into another CNN to produce final answers. The resulting classification accuracy was superior to either of the networks on their own. 
* This project improved the accuracy of our CNN on CIFAR-10 by 6%, from 72% to 78%, without an increase in training data. This technique could, therefore, be useful in domains with limited training data. 

## Technologies Used

* Python
* Jupyter
* Numpy
* Tensorflow, Keras, and GPFlow (Library for gaussian processes in Python)
* Convolutional neural networks and deep convolutional gaussian processes

## Summary

### Images

#### Sample of CIFAR-10 Images

This is a sample of pictures contained in the CIFAR-10 dataset. The dataset contains 10 different classes of image. 

![Sample CIFAR-10 Images](/assets/img/CIFAR10images.jpeg)

#### Project Results

This is a bar graph showing the final classification results of each of our networks. DCGP is the deep convolutional gaussian process, ICNN is our initial CNN result, and ECNN is the improved result obtained by combining the other two networks' outputs. 

![CNN Project Results](/assets/img/CNNProjectresults.jpg)


## References

The DCGP was originally proposed in this paper:

Blomqvist, Kenneth, Samuel Kaski, and Markus Heinonen. "Deep convolutional Gaussian processes." Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2019, Würzburg, Germany, September 16–20, 2019, Proceedings, Part II. Springer International Publishing, 2020.

---
layout: page
title: "Timeseries Data Projects"
subheadline: "Working with Timeseries Datasets"
teaser: "Some of my Major Projects Involving Timseries Data"
permalink: "/timeseriesproject/"
header:
    image_fullwidth: "nanzan.jpg"
---

# Timeseries Data Exploration Project

## Highlights

* Project focused on a timeseries data exploration web app that was used to find similar subsections within a timeseries dataset. The application was designed to use clustering to reduce the computational requirements of the task. 
* Benchmarked the app by using Docker and AWS Batch to run experiments on AWS hardware. 
* Created a UI for using the app, including a query entry system as well as a viewer for the timeseries and the results. 

## Technologies Used
* Python
* Multiprocessing
* Cloud computing tools including: AWS Lambda, AWS API Gateway, and AWS Batch
* Django and React
* Docker



# Automated Machine Learning on Neural Data

## Highlights

* The goal of this project was to create an application that would allow un-trained users to run classification models on inputted neural data. This application was meant for researchers doing work in brain computer interfaces who don't have machine learning experience. 
* The application used sktime, a timeseries data classification library, to give users a number of options for classification models to run. 

## Technologies Used\
* Python
* Numpy and Scipy
* sklearn
* sktime

## Project Introduction
The goal of this project was to implement a system to automate the running of timeseries machine learning algorithms on neural data. This system levereges a timeseries machine learning library called sktime. Using sktime we can create an application that will allow users, even those without advanced training, to run complex machine learning algorithms consistently. These ML algorithms were used to extract information from fNIRS (functional near-infrared spectroscopy) datasets. Modern neuroimaging techniques like fNIRS or EEG (Electroencephalography) produce long multidimensional timeseries datasets that generally require advanced statistical analysis techniques to analyze. As a result, analysis of this data often becomes a bottleneck that requires time investments from people who have advanced training in machine learning. It is for this reason that I created an application to allow users without advanced training access to state-of-the-art algorithms for analyzing this data. This allowed more researchers of different backgrounds to effectively analyze brain data.

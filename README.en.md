[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/jmontejr/tecnicas-preditivas-para-auxilio-no-diagnostico-de-melanomas-via-images/blob/main/README.md)

# Predictive Techniques for Assisting in the Diagnosis of Melanomas via Images

This repository contains the source code of the implementations of the experiments used for the project presented in the thesis submitted to the Bachelor's Degree in Information Systems at the Federal Rural University of Pernambuco, as a partial requirement for obtaining the degree of Bachelor in Information Systems.

## Table of Contents

- [Project Details](#project-details)
- [Abstract](#abstract)
  - [Keywords](#keywords)
- [Dataset](#dataset)
  - [How to find and use the data to reproduce this work](#how-to-find-and-use-the-data-to-reproduce-this-work)

## Project Details

**Author:** José Carlos Monte Silva Júnior  
**Advisor:** Prof. Dr. Rodrigo Gabriel Ferreira Soares  
**Institution:** Federal Rural University of Pernambuco - UFRPE  
**Department:** Department of Statistics and Computer Science - DEINFO  
**Course:** Bachelor's Degree in Information Systems  
**Location and Date of Publication:** Recife, 2024  
**Defended and Approved on:** October 02, 2024  
**URI**: [https://repository.ufrpe.br/handle/123456789/6372](https://repository.ufrpe.br/handle/123456789/6372)

## Abstract

Skin cancer is the most common type of cancer worldwide, divided into two main types: melanoma and non-melanoma. Although rarer, melanoma is the most lethal due to its potential to cause metastasis. Non-invasive methods, such as dermoscopy and the ABCDE rule, have been used to avoid unnecessary surgical procedures and have helped in the identification of lesions, contributing to faster diagnoses. With advances in technology, Artificial Intelligence (AI) has gained prominence, proving to be a promising solution for medical data analysis, especially with the use of Convolutional Neural Networks (CNNs), which can recognize patterns in dermoscopic images and help classify lesions as melanoma or non-melanoma in an automated manner. This project proposes an ensemble of classifiers based on Convolutional Neural Networks to classify dermoscopic images as melanoma or non-melanoma, comparing its performance with validated architectures, such as AlexNet and VGG-16, using Transfer Learning techniques. The analyses of Precision, Recall, and F1 Score showed that the ensemble of Convolutional Neural Networks outperformed the models using Transfer Learning techniques, with AlexNet showing better performance than VGG-16. The ensemble of Convolutional Neural Networks demonstrated a greater generalization capability, proving to be promising in capturing relevant features from the images, revealing potential for medical applications, although it still needs refinement to meet clinical standards.

### Keywords

Skin Cancer, Machine Learning, Ensemble Techniques, Convolutional Neural Networks, Transfer Learning.

Sure! Here’s the translated content:

## Dataset

For the experiment, images from the [ISIC Challenge](https://challenge.isic-archive.com/) archive were chosen. A total of 25,331 images from the training set of the [ISIC Challenge 2019](https://challenge.isic-archive.com/data/#2019) were used, as they include the Ground Truth, which is essential for ensuring the accuracy and reliability of the data.

### How to find and use the data to reproduce this work?

Due to the size of the dataset, the files containing images of dermatoscopic lesions were not included in this repository. However, these files can be found on the official challenge page: [ISIC Challenge 2019 - Training Data](https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_Input.zip). The training Ground Truth file is available at `src/data/ISIC_2019_Training_GroundTruth.csv` and can also be accessed on the official challenge page, along with the images.

When downloading the files, the images should be placed in the `src/data/images` folder for the experiments to be reproduced.

# Pypdac - Classification of tissue types on H&E scans and Data Cleaning via Communicators
Based on the Paper:  Communicator-driven Data Preprocessing Improves Deep Transfer Learning of Histopathological Prediction of Pancreatic Ductal Adenocarcinoma.<br>
Data are not avaible. <br>
Implemented in Python using the PyTorch Framework<br>
We provide the code to be able to analyse H&E tissue slides scans automatically and quickly.<br>
We provide a fast solution here. 
<br>
# Installation Guide
See https://github.com/MolecularMedicine2/PyQoVi

# Usage
<br>
The script always expects the following folder structure: train, test, val  and then the classes.
See patches_A_resnet as example.
<br>
train_public_hpc.py - Script for Training a CNN form the list.
<br>
color_public_hpc.py - Use a trained CNN to classify & color the image patches.
<br>
automatic_cleaning.py - Clean two CNNs per Tissue type (HLN, HP, PDAC) and additional well labeled data.
<br>
clean_public_hpc.py - Use the Nets six nets from automatic_cleaning.py to clean up the whole dataset
<br>

# Error Handling:
Error -2 tempfile.tif: Cannot read TIFF header. conda install libtiff=4.1.0=h885aae3_4 -c conda-forge or  conda install -c anaconda libtiff<br>

# TBC / Todo
- Open Code for Hyperparametertuning

# Latest features (03/2022)
- train, coloring, automatic_cleaning, clean,

# Support 
If you **really** like this repository and find it useful, please consider (★) **starring** it, so that it can reach a broader audience of like-minded people. It would be highly appreciated !

# Contributing to Pypdac
If you find a bug, create a GitHub issue, or even better, submit a pull request. Similarly, if you have questions, simply post them as GitHub issues. 

# License , citation and acknowledgements
Please advice the **LICENSE.md** file. For usage of third party libraries and repositories please advise the respective distributed terms. Please cite our paper, when using this code:

```
@Article{c1506795,
AUTHOR = {Raphael M. Kronberg, Melanie Pfaus, Lena Haeberle, Haifeng C. Xu, Karina S. Krings, Martin Schlensog,
Tilman Rau, Aleksandra A. Pandyra, Karl S. Lang, Irene Esposito and Philipp A. Lang},
TITLE = {Communicator-driven Data Preprocessing Improves Deep Transfer Learning of Histopathological Prediction of Pancreatic Ductal Adenocarcinoma.},
JOURNAL = {Submitted},
ABSTRACT = {Pancreatic cancer is a fatal malignancy with poor prognosis and limited treatment options.
Early detection in primary and secondary locations is critical, but fraught with challenges.
While digital pathology can assist with the classification of histopathological images, the training
of such networks always relies on a ground truth, which is frequently compromised as tissue sections
contain several types of tissue entities. Here we show that pancreatic cancer can be detected on
hematoxylin and eosin (H&E) sections by convolutional neural networks using deep transfer learning.
To improve the ground truth, we describe a preprocessing data cleanup process using two communicators
that were generated through existing and new datasets. Specifically, the communicators moved image
tiles containing adipose tissue and background to a new data class. Hence, the original dataset
exhibited an improved labelling and consequently a higher ground truth accuracy.
Deep transfer learning of a ResNet18 network resulted in a four-class accuracy of about 94% on test
data images. The network was validated on independent tissue sections composed of healthy pancreatic
tissue, pancreatic ductal adenocarcinoma, and pancreatic cancer lymph node metastases.
Screening of different models and hyperparameter fine tuning was performed to optimize the 
performance on the independent tissue sections. Taken together, we introduce a data preprocessing
via communicators step as a means of improving the ground truth during deep transfer learning and
hyperparameter tuning to identify pancreatic ductal adenocarcinoma primary tumors and metastases
in histological tissue sections.},
}

```
## Acknowledgements
Based on the implementation of the previous paper:  https://doi.org/10.3390/v13040610 .<br>
normalizeStaining.py - A method for normalizing histology slides for quantitative analysis. M. Macenko et al., ISBI 2009: https://ieeexplore.ieee.org/document/5193250 <br>

# Disclaimer
This progam/code can not be used as diagnostic tool.


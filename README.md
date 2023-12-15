# Molecular docking enhancement with machine learning 
Molecular docking is a critical component of drug discovery and virtual screening, where potential drug candidates are evaluated for their binding affinity to a target biomolecule (Morris et al., 2008). In general, molecular docking is a time-consuming process, particularly in the face of the escalating size of chemical libraries, now consisting of billions of molecules (Warr et at., 2022). Considering this, conducting molecular docking without an initial reduction in library size has become impractical. This reduction is paramount to streamline the time and computational resources required for docking, but it must be executed with precision to avoid the loss of potentially valuable drug candidates (Aittokallio, 2022). However, it is essential to preserve potential drug candidates within these libraries. The objective of this research project is to develop a mechanism that not only reduces the initial library size but also effectively filters out unsuitable or less suitable molecules. The ultimate goal is to establish an efficient pre-docking filtration system, resulting in a selection of the most promising candidates for docking.![image]

![image](https://github.com/emanskaia/CPSC545_final_project/assets/139388597/296486a9-4cde-4116-91a5-ddfe881b20c1)


## Methods

For this experiment, the workflow was designed to train a neural network on known values of binding affinity for various molecules. For the neural network, a model called DeepPurpose was selected. DeepPurpose is a Deep Learning Based Molecular Modeling and Prediction Toolkit on Drug-Target Interaction Prediction, that is designed to work with such prediction values as ki, kd, IC50 values. More importantly, while DeepPurpose works with several types of drug and target encodings, it also works directly with SMILES for drugs and CNN (amino acids sequence) for proteins, which are the lightest and least resource-consuming types of encodings.

A trained model then was applied to predict affinity between molecules for one target protein. For consensus, the model was trained on two distinct datasets with publicly available data on molecular affinity. Datasets PDBBind (Su et al., 2019) and BindingDB (Gilson et al., 2015) were used for model training. Training of those models with further affinity prediction is described below as Experiments 1 and 2. In this scientific research endeavor, I implemented two distinct methodologies. The initial approach involved employing the BindingDB dataset in conjunction with a pre-existing model derived from the DeepPurpose repository. In the subsequent endeavor, an entirely new model was constructed from the ground up using the PDBBind dataset. In preparation for the training process, the dataset underwent appropriate preprocessing.

The target protein: ESTROGEN RECEPTOR
SKKNSLALSLTADQMVSALLDAEPPILYSEYDPTRPFSEASMMGLLTNLADRELVHMINWAKRVPGFVDLTLHDQVHLLECAWLEILMIGLVWRSMEHPGKLLFAPNLLLDRNQGKCVEGMVEIFDMLLATSSRFRMMNLQGEEFVCLKSIILLNSGVYTFLSSTLKSLEEKDHIHRVLDKITDTLIHLMAKAGLTLQQQHQRLAQLLLILSHIRHMSNKGMEHLYSMKCKNVVPLYDLLLEMLDAHRLHAPT

Dataset for prediction: 986,970 small molecules randomly sampled from Zinc15 database

## Set up

``` 
conda create -n DeepPurpose python=3.6
conda activate DeepPurpose
conda install -c conda-forge notebook
pip install git+https://github.com/bp-kelley/descriptastorus 
pip install DeepPurpose
```

### Experiment 1. BindingDB dataset
In the first experiment, I harnessed a pre-trained model sourced from the DeepPurpose repository to evaluate its performance against a vast collection of one million distinct molecular compounds in conjunction with a specified target protein. The molecular compounds, numbering in the millions, were systematically acquired from the Zinc15 database and selected through a random sampling process conducted in a prior phase of the study. This compiled dataset was denominated as "molecules_dataset."
The acquisition and processing scripts for the BindingDB dataset can be found here 
, while the script for executing the pre-trained model can be accessed here

### Experiment 2. A model trained on PDB-Bind dataset

In the second experiment, we procured the training dataset from the open-source PDB Data - A core Dataset. Subsequently, the model was painstakingly trained until optimal performance was achieved. Detailed information concerning the training configuration and the number of training iterations are comprehensively delineated below.

![image](https://github.com/emanskaia/CPSC545_final_project/assets/139388597/aefee69b-4d94-4da9-bf8f-6f7752e74c85)

### Docking of the same dataset

-----

### Statistical analysis docking results and results obtained using DeepPurpose

Very low linear positive correlation between model predictions and docking scores (ranking of molecules in terms of binding probability).

## Conclusion

This project aims to address the challenges posed by the increasing size of chemical libraries in molecular docking. The project will contribute to the optimization of drug discovery processes and provide valuable insights into the intersection of machine learning and molecular docking.


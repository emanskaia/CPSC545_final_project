# Molecular docking enhancement with machine learning 
Molecular docking is a critical component of drug discovery and virtual screening, where potential drug candidates are evaluated for their binding affinity to a target biomolecule (Morris et al., 2008). In general, molecular docking is a time-consuming process, particularly in the face of the escalating size of chemical libraries, now consisting of billions of molecules (Warr et at., 2022). Considering this, conducting molecular docking without an initial reduction in library size has become impractical. This reduction is paramount to streamline the time and computational resources required for docking, but it must be executed with precision to avoid the loss of potentially valuable drug candidates (Aittokallio, 2022). However, it is essential to preserve potential drug candidates within these libraries. The objective of this research project is to develop a mechanism that not only reduces the initial library size but also effectively filters out unsuitable or less suitable molecules. The ultimate goal is to establish an efficient pre-docking filtration system, resulting in a selection of the most promising candidates for docking.![image]

## Experiment 1
In the first experiment, we harnessed a pre-trained model sourced from the DeepPurpose repository to evaluate its performance against a vast collection of one million distinct molecular compounds in conjunction with a specified target protein. The molecular compounds, numbering in the millions, were systematically acquired from the Zinc15 database and selected through a random sampling process conducted in a prior phase of the study. This compiled dataset was denominated as "molecules_dataset."
The acquisition and processing scripts for the BindingDB dataset can be found here 
, while the script for executing the pre-trained model can be accessed here

## Experiment 2
In the second experiment, we procured the training dataset from the open-source PDB Data - A core Dataset. Subsequently, the model was painstakingly trained until optimal performance was achieved. Detailed information concerning the training configuration and the number of training iterations are comprehensively delineated below.


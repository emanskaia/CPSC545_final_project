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

### pip
``` 
conda create -n DeepPurpose python=3.6
conda activate DeepPurpose
conda install -c conda-forge notebook
pip install git+https://github.com/bp-kelley/descriptastorus 
pip install DeepPurpose
```

### Build from source

``` 
git clone https://github.com/kexinhuang12345/DeepPurpose.git ## Download code repository
cd DeepPurpose ## Change directory to DeepPurpose
conda env create -f environment.yml  ## Build virtual environment with all packages installed using conda
conda activate DeepPurpose ## Activate conda environment (use "source activate DeepPurpose" for anaconda 4.4 or earlier) 
jupyter notebook ## open the jupyter notebook with the conda env
conda deactivate ## when done, exit conda environment 
```

### Experiment 1. BindingDB dataset
In the first experiment, I harnessed a pre-trained model sourced from the DeepPurpose repository to evaluate its performance against a vast collection of one million distinct molecular compounds in conjunction with a specified target protein. The molecular compounds, numbering in the millions, were systematically acquired from the Zinc15 database and selected through a random sampling process conducted in a prior phase of the study. This compiled dataset was denominated as "molecules_dataset."
The acquisition and processing scripts for the BindingDB dataset can be found here 
, while the script for executing the pre-trained model can be accessed here

### Experiment 2. A model trained on PDB-Bind dataset

In the second experiment, we procured the training dataset from the open-source PDB Data - A core Dataset. Subsequently, the model was painstakingly trained until optimal performance was achieved. Detailed information concerning the training configuration and the number of training iterations are comprehensively delineated below.

![image](https://github.com/emanskaia/CPSC545_final_project/assets/139388597/aefee69b-4d94-4da9-bf8f-6f7752e74c85)

### Docking of the same dataset

As a supplementary aspect of our investigation, I conducted molecular docking simulations employing the GLIDE docking software. This approach aimed to complement the neural network predictions and provide an alternative perspective on the affinity between molecules and a specific target protein. The dataset utilized for neural network training was concurrently subjected to docking simulations to facilitate a comprehensive comparison of outcomes.

### Statistical analysis docking results and results obtained using DeepPurpose

Following the completion of the docking simulations, the generated outcomes underwent thorough statistical assessment. The evaluation encompassed the calculation of Pearson and Spearman correlation coefficients. These coefficients were instrumental in quantifying the correlation between the predicted affinities from the neural network models and the results derived from the docking simulations. The script can be found here (statistical_analysis.py)

## References

Aittokallio, T. (2022). What are the current challenges for machine learning in drug discovery and repurposing? Expert Opinion on Drug Discovery, 17(5), 423-425. https://doi.org/10.1080/17460441.2022.2050694.

Gilson, M. K., Liu, T., Baitaluk, M., Nicola, G., Hwang, L., & Chong, J. (2015). BindingDB in 2015: A public database for medicinal chemistry, computational chemistry, and systems pharmacology. Nucleic Acids Research, 44, D1045-D1053.

Huang, K., Fu, T., Glass, L. M., Zitnik, M., Xiao, C., & Sun, J. (2020). DeepPurpose: A deep learning library for drug–target interaction prediction. Bioinformatics, 36(22-23), 5545-5547. https://doi.org/10.1093/bioinformatics/btaa1005.

Morris, G.M., & Lim-Wilby, M. (2008). Molecular Docking. In A. Kukol (Ed.), Molecular Modeling of Proteins (Methods Molecular Biology™, Vol. 443). Humana Press. https://doi.org/10.1007/978-1-59745-177-2_19.

Su, M., Yang, Q., Du, Y., Feng, G., Liu, Z., Li, Y., & Wang, R. (2019). Comparative Assessment of Scoring Functions: The CASF-2016 Update. Journal of Chemical Information and Modeling, 59, 895-913.

Warr, W. A., Nicklaus, M. C., Nicolaou, C. A., & Rarey, M. (2022). Journal of Chemical Information and Modeling, 62(9), 2021-2034. https://doi.org/10.1021/acs.jcim.2c00224.

@article{huang2020deeppurpose,
  title={DeepPurpose: A Deep Learning Library for Drug-Target Interaction Prediction},
  author={Huang, Kexin and Fu, Tianfan and Glass, Lucas M and Zitnik, Marinka and Xiao, Cao and Sun, Jimeng},
  journal={Bioinformatics},
  year={2020}
}



from DeepPurpose import DTI as models
from DeepPurpose.utils import *
import dataset
from dataset import *

#Use pretrained model for a chosen target and a chosen dataset
net = models.model_pretrained(model = 'CNN_CNN_BindingDB')
drug_ID, X_repurpose = dataset.read_file_repurposing_library('/home/user/dataset_DD_original/1ERR/iteration_1/text_output.csv')

target, target_name = dataset.read_file_target_sequence('/home/user/dataset_DD_original/1ERR/Protein_1ERR_target_seq.txt')

print('The target is: ' + target)
#The target is: SKKNSLALSLTADQMVSALLDAEPPILYSEYDPTRPFSEASMMGLLTNLADRELVHMINWAKRVPGFVDLTLHDQVHLLECAWLEILMIGLVWRSMEHPGKLLFAPNLLLDRNQGKCVEGMVEIFDMLLATSSRFRMMNLQGEEFVCLKSIILLNSGVYTFLSSTLKSLEEKDHIHRVLDKITDTLIHLMAKAGLTLQQQHQRLAQLLLILSHIRHMSNKGMEHLYSMKCKNVVPLYDLLLEMLDAHRLHAPT‘’’

print('The target name is: ' + target_name)
#The target name is: 1ERR’’’

_ = models.repurpose(X_repurpose, target, net, drug_ID, target_name)

#‘’’repurposing...
#Drug Target Interaction Prediction Mode...
#in total: 986889 drug-target pairs
#encoding drug...
#unique drugs: 986889
#encoding protein...
#unique target sequence: 1
#Done.
#predicting...
#---------------
#Drug Repurposing Result for 1ERR‘’’


#/home/user/descriptastorus/result/repurposing.txt

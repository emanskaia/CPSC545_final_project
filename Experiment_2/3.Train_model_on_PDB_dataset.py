from DeepPurpose import DTI as models
from DeepPurpose.utils import *
import dataset
from dataset import *

def read_file_training_dataset_drug_target_pairs_PDB_kd(path = '/home/emanskaia/Desktop/data_PBD/PDB_Refined_processed_pkd.csv'):
    try:
        file = open(path, "r")
    except:
        print('path not found')
    X_drug = []
    X_target = []
    y = []
    for aline in file:
        values = aline.split()
        X_drug.append(values[2])
        X_target.append(values[0])
        y.append(float(values[1]))
    file.close()
    return np.array(X_drug), np.array(X_target), np.array(y)

X_drug, X_target, y = read_file_training_dataset_drug_target_pairs_PDB_kd('/home/emanskaia/Desktop/data_PBD/PDB_Refined_processed_pkd.csv')
drug_encoding, target_encoding = 'CNN', 'CNN'
train, val, test = data_process(X_drug, X_target, y,
                                drug_encoding, target_encoding,
                                split_method='cold_protein',
                                frac=[0.7,0.1,0.2])

#Drug Target Interaction Prediction Mode...
#in total: 2221 drug-target pairs
#encoding drug...
#unique drugs: 1675
#encoding protein...
#unique target sequence: 1197
#splitting dataset...
#Done.

config = generate_config(drug_encoding, target_encoding,
    cls_hidden_dims = [512],
    train_epoch = 20,
    LR = 0.001,
    batch_size = 128,
)

net = models.model_initialize(**config)
net.train(train, val, test)

#Training at Epoch 20 iteration 0 with loss 0.25727. Total time 0.04611 hours
#Validation at Epoch 20 with loss:2.42420, MSE: 2.33329 , Pearson Correlation: 0.52233 with p-value: 2.54E-19 , Concordance Index: 0.67645
#--- Go for Testing ---
#Testing MSE: 1.8871456969397908 , Pearson Correlation: 0.5922994212265742 with p-value: 8.01E-43 , Concordance Index: 0.6878786610440842


#ROUND 2 - changed 1
#config = generate_config(drug_encoding, target_encoding,
#    cls_hidden_dims = [1024,1024,512],
#    train_epoch = 20,
#    LR = 0.001,
#    batch_size = 128,
#)

#net = models.model_initialize(**config)
#net.train(train, val, test)

#Training at Epoch 20 iteration 0 with loss 0.36508. Total time 0.04583 hours
#Validation at Epoch 20 with loss:2.37844, MSE: 2.52373 , Pearson Correlation: 0.45980 with p-value: 8.51E-15 , Concordance Index: 0.65109
#--- Go for Testing ---
#Testing MSE: 1.8489849866257897 , Pearson Correlation: 0.6127529378400469 with p-value: 1.68E-46 , Concordance Index: 0.7124373476199943
#--- Training Finished —

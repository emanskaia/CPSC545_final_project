from DeepPurpose import DTI as models
from DeepPurpose.utils import *
import dataset
from dataset import *

#downloading the dataset for trainibg the model
def download_BindingDB_New(path = './data_new'):
    print('downloading')
    if not os.path.exists(path):
        os.makedirs(path)
    url = "https://www.bindingdb.org/bind/downloads/BindingDB_All_202305.tsv.zip"
    saved_path = wget.download(url, path)
    print('Beginning to extract zip file...')
    with ZipFile(saved_path, 'r') as zip:
        zip.extractall(path = path)
        print('Done!')
    path = path + '/BindingDB_All.tsv'
    return path

#download_BindingDB_New()
#downloading
#100% [....................................................] 458386830 / 458386830Beginning to extract zip file...
#Done!
#'./data_new/BindingDB_All.tsv'


X_drug, X_target, y  = process_BindingDB('/home/emanskaia/Desktop/data_BD/BindingDB_All.tsv',
    y = 'Kd',
    binary = False,
    convert_to_log = True)
drug_encoding, target_encoding = 'CNN', 'CNN'
train, val, test = data_process(X_drug, X_target, y,
	drug_encoding, target_encoding,
	split_method='cold_protein',
	frac=[0.7,0.1,0.2])
#Drug Target Interaction Prediction Mode...
#in total: 89179 drug-target pairs
#encoding drug...
#unique drugs: 89177
#encoding protein...
#unique target sequence: 1750
#splitting dataset...
#Done.””

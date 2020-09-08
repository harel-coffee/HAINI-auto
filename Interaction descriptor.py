
import csv
import numpy as np
import pandas as pd
from PyBioMed.PyInteraction import PyInteraction
from PyBioMed.PyMolecule import moe
from rdkit import Chem
smis = pd.read_csv('training_dataset.csv',header=None)
smis.index1 = smis[1]
smis.index2 = smis[3]

features = []
for i in range(i):  
    m = Chem.MolFromSmiles(smis.index1[i])
    n = Chem.MolFromSmiles(smis.index2[i])
    mol_des1 = moe.GetMOE(m)
    mol_des2 = moe.GetMOE(n)
    mol_mol_interaction2 = PyInteraction.CalculateInteraction2(mol_des1,mol_des2)
    print mol_mol_interaction2
    features.append(mol_mol_interaction2.values())


file_name = 'output.csv'
with open(file_name, 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for row in features:
        writer.writerow(row)
  
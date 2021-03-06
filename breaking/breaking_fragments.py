import numpy as np 
import pandas as pd 
import ast
import warnings
from Bio.PDB import *

warnings.simplefilter(action='ignore', category='PDBConstructionWarning')
DOWNLOAD_PATH = '../download_pdb/'

# id_list = open("id_list.txt", "r") 
# list_of_ids = ast.literal_eval(id_list.read())

list_of_ids = ['104L', '103M', '102L', '4ZPY', '4MBS', '3K3J', '2GFS', '1HQ3']

df_all = []

for file_name in list_of_ids:
    file_type = '.pdb'
    print(file_name)
    
    for fragment_start in range(3, 42):
        parser = PDBParser()
        
        try:
            structure = parser.get_structure(file_name, DOWNLOAD_PATH + file_name + file_type)
            
        except Exception:
            continue
        
        chains = structure.get_chains()
    
        for chain in chains:
            
            seq_list = []
            start_list = []
            end_list = []
            df = pd.DataFrame()
        
            count = 0
            seq = ''

            residues = chain.get_residues()
            
            rem_size = 0
            
            start = 0
            for residue in residues:
                
                start = residue.get_id()[1]
              
                if residue.get_resname() == 'HOH':
                    break
                
                seq += residue.get_resname().replace(" ", "")
                count += 1
                
                if count > fragment_start:
                    seq = seq[3:]
                else:
                    start_list.append(residue.get_id()[1])
                
                if len(seq.strip()) == (3 * fragment_start) and seq.isalpha():
                    seq_list.append(seq)
                    start_list.append(residue.get_id()[1])
                    end_list.append(residue.get_id()[1])
                
            rem_size = len(start_list) - len(end_list)
            start_list = start_list[:-rem_size]
                
            df['Fragments'] = seq_list
            df['Name'] = file_name + '_' + chain.id
            df['Start'] = start_list
            df['End'] = end_list
            df_all.append(df)

    
    
        
        
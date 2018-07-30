import numpy as np 
import pandas as pd 
import ast
import Bio.PDB
from Bio.PDB import *

DONWLOAD_PATH = '../download_pdb/'

id_list = open("id_list.txt", "r") 
list_of_ids = ast.literal_eval(id_list.read())

file_name = '1hq3'
file_type = '.pdb'
fragment_start = 3
fragment_end = 42

parser = PDBParser()
structure = parser.get_structure(file_name, DONWLOAD_PATH + file_name + file_type)

chains = structure.get_chains()
df_chains = []

for chain in chains:
    
    seq_list = []
    start_list = []
    end_list = []
    df = pd.DataFrame()

    count = 0
    seq = ''
    print(chain)
    residues = chain.get_residues()
    
    rem_size = 0
    
    start = 0
    for residue in residues:
        print(residue.get_resname(), residue.get_id()[1])
        
        start = residue.get_id()[1]
      
        if residue.get_resname() == 'HOH':
            break
        
        seq += residue.get_resname().replace(" ", "")
        count += 1
        
        if count > fragment_start:
            seq = seq[fragment_start:]
        else:
            start_list.append(residue.get_id()[1])
            
        print(seq)
        
        if len(seq.strip()) == (fragment_start * fragment_start) and seq.isalpha():
            seq_list.append(seq)
            start_list.append(residue.get_id()[1])
            end_list.append(residue.get_id()[1])
        
    rem_size = len(start_list) - len(end_list)
    start_list = start_list[:-rem_size]
        
    df['Fragments'] = seq_list
    df['Name'] = file_name + '_' + chain.id
    df['Start'] = start_list
    df['End'] = end_list
    df_chains.append(df)
        
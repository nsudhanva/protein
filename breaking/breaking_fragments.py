import numpy as np 
import pandas as pd 
import Bio.PDB
from Bio.PDB import *

DONWLOAD_PATH = '../download_pdb/'

file_name = '1hq3'
file_type = '.pdb'
fragment_start = 3
fragment_end = 42

parser = PDBParser()
structure = parser.get_structure(file_name, DONWLOAD_PATH + file_name + file_type)

# for model in structure:
#     for chain in model:
#         for residue in chain:
#             for atom in residue:
#                 print(atom)

# Iterate over all atoms in a structure
# for atom in structure.get_atoms():
#     print(atom)

# # Iterate over all residues in a model
# for residue in structure.get_residues():
#     print(residue)


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
            
            
        print(seq)
        
        if len(seq.strip()) == (fragment_start * fragment_start):
            seq_list.append(seq)
            
    df['Fragments'] = seq_list
    df['Name'] = file_name + '_' + chain.id
    
    df_chains.append(df)
        
        
        
        

# sup = Superimposer()
# sup.set_atoms(fixed, moving)
# print(sup.rotran)
# print(sup.rms)
import numpy as np 
import pandas as pd 
from Bio.PDB import *

DONWLOAD_PATH = '../download_pdb/'

file_name = '1hq3'
file_type = '.pdb'
start = 3
end = 42

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

for chain in chains:
    print(chain)
    residues = chain.get_residues()
    for residue in residues:
        print(residue.get_resname(), residue.get_id()[1])
        break
        
        
---
title: PIGNet
prev1_title: Drug-Target Interaction
prev2_title: Pharmacology
prev3_title: Biology
date: 2021-04-03
description: A physics-informed deep learning model toward generalized drug-target interaction predictions
_previous: https://ailever.github.io/education/2021/04/03/_BIO-pc-en-drug-target-interaction/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Biology.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Help:Displaying_a_formula'">Mathematical Formula</button>
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->

## Summary
### Challenging problem in the practice of in-silico drug discovery
- Generalization of DTI Models
- Accurate prediction for the key steps in the earlystage in-silico drug discovery
- The reasonable binding poses and binding affinities of protein-ligand complexes

### DNN-based DTI Model Issues
- Overfitting by the deficiency in 3D structural data of the protein-ligand complexes
- The insufficient experimental data on protein-ligand binding structures
- Lack of interpretability in deep learning models

### Two key strategies to enhance the generalization ability of DTI models
- Novel physics-informed graph neural network
- Data augmentation strategy for a wider range of binding poses

### Results
- Improvement in docking success rate, screening enhancement factor, and screening success rate
- Devising uncertainty estimator of our model’s prediction
- Assessment of the contribution of each ligand substructure in total binding free energy

<br><br><br>
## Related Works
### Summary of previous works: 3D CNN and GNN
### Physics-informed neural networks


<br><br><br>
## Overview of our model
### Model Architecture
![image](https://user-images.githubusercontent.com/52376448/113819672-9682e400-97b4-11eb-9533-d6368eae7782.png)
- **Gated graph attention network (gated GAT)** for covalent bonds & **interaction network** for intermolecular interactions 

### Physics-informed parameterized function
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$E^{total}= \frac{E^{vdw}+E^{hbond}+E^{metal}+E^{hydrophobic}}{T^{rotor}}$$
$$\begin{align*}
  E^{vdw} &= \sum_{i,j} {c_{i,j}\left [(\frac{d^{\prime}_{i,j}}{d_{i,j}})^{12} - 2(\frac{d^{\prime}_{i,j}}{d_{i,j}})^6 \right ]}\\
  E^{hbond},\ E^{metal},\ E^{hydrophobic} &= \sum_{i,j} e_{ij}\\
  T^{rotor} &= 1 + C_{rotor} \times N_{rotor}\\
\end{align*}$$
  
$$  e_{ij} = 
    \begin{cases}
      \omega, & \text{if }d_{ij}-d^{\prime}_{ij} < c_{1} \\
      \omega \left (  \frac{d_{ij}-d^{\prime}_{ij}-c_{2}}{c_{1}-c_{2}} \right ), & \text{if }c_{1}< d_{ij}-d^{\prime}_{ij} < c_{2} \\
      0, & \text{if }d_{ij}-d^{\prime}_{ij} > c_{2}
    \end{cases}
$$
  
<br><br></div>
### Loss functions
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">

$$\begin{align*}
  L_{total} &= {\color{violet}{L_{energy}}} \\
  \quad &{\color{red}{+c_{derivative}L_{derivative}}} \\  
  \quad &{\color{green}{+c_{docking}L_{docking}}} \\
  \quad &{\color{blue}{+c_{random\ screening}L_{random\ screening}}} \\
  \quad &{\color{orange}{+c_{cross\ screening}L_{cross\ screening}}} \\
\end{align*}$$  

$$\begin{align*}
  {\color{violet}{L_{energy}}} &= \frac{1}{N_{train}} \sum_{i} {(y_{pred,i}-y_{true,i})^2} \\
  {\color{red}{L_{derivative}}} &= \sum_{i} {((\frac{\partial E^{total}}{\partial q_{i}})^2 - \min(\frac{\partial^2 E^{total}}{\partial q_{i}^{2}},C_{der2}))} \\
  {\color{green}{L_{docking}}} &= \sum_{i} {\max(y_{exp,i}-y_{decoy,i}, 0)}\\
  {\color{blue}{L_{random\ screening}}} &= \sum_{i} {\max(-y_{random,i}-6.8,0)}\\
  {\color{orange}{L_{cross\ screening}}} &= \sum_{i} {\max(-y_{cross,i}-6.8,0)}\\
\end{align*}$$

<br><br></div>


### Dataset
[ART|<a href="#ART">2</a>]
- CASF-2016
- CSAR_NRC_HiQ_Set
- CSAR1
- CSAR2
- pdbbind_v2019_cross_screening
- pdbbind_v2019_docking_nowater
- pdbbind_v2019_random_screening
  - https://chembl.gitbook.io/chembl-interface-documentation/
  - https://www.ibscreen.com/
- pdbbind_v2019_refined
- rcsb_pdb

### Benchmark method

<br><br><br>
## Results and Discussions
### Assessment of the model performance and generalization ability
### Ablation study on the generalization ability of the model 
### Interpretation of the physically modeled outputs
### Uncertainty quantification of PIGNet

<br><br><br>
## Conclusion

<br><br><br>
## Supplimentary: Electronic Supplementary Information
### 1. Model construction
#### (a) Neural model architecture
#### (b) Physics-informed parameterized function
### 2. Benchmark methods
#### CASF2016 benchmark metrics6
### 3. Interpretation of the physically modeled outputs
#### Distribution plot of atom-atom pairwise interaction in each energy component
### 4. Uncertainty quantification method
### 5. Implementation
[REF|<a href="#REF">2</a>, 
<a href="https://github.com/jaechanglim/DTI_PDBbind/blob/master/README.md" style="font-size:xx-small;">Installation</a>,
<a href="https://github.com/jaechanglim/DTI_PDBbind/blob/master/data/README.md" style="font-size:xx-small;">Dataset</a>]<br>
<code class="code-title">Full Directory</code>
<pre class="code-path">
├── README.md
├── arguments.py
├── benchmarks
│   ├── csar1
│   │   └── csar1_test.sh
│   ├── csar2
│   │   └── csar2_test.sh
│   ├── docking
│   │   └── docking_test.sh
│   ├── scoring
│   │   └── scoring_test.sh
│   ├── screening
│   │   └── screening_test.sh
│   └── test.sh
├── casf2016_benchmark
│   ├── docking_power.py
│   ├── index.txt
│   ├── ranking_power.py
│   ├── scoring_power.py
│   └── screening_power.py
├── data
│   ├── CASF-2016
│   │   ├── docking
│   │   ├── mol2_decoy_docking
│   │   ├── mol2_decoy_screening
│   │   ├── scoring
│   │   └── screening
│   ├── CSAR_NRC_HiQ_Set
│   │   └── binding.pkl
│   ├── README.md
│   ├── csar1
│   │   ├── csar1.txt
│   │   ├── data
│   │   ├── keys
│   │   ├── pdb_to_affinity.py
│   │   └── split_receptor_ligand.py
│   ├── csar2
│   │   ├── csar2.txt
│   │   ├── data
│   │   ├── keys
│   │   ├── pdb_to_affinity.py
│   │   └── split_receptor_ligand.py
│   ├── pdbbind_v2019_cross_screening
│   │   ├── cal_docking.py
│   │   ├── data
│   │   ├── keys
│   │   ├── pdb_to_affinity.py
│   │   ├── pdb_to_affinity.txt
│   │   ├── pdbqt_to_pdb.py
│   │   ├── test.txt
│   │   ├── total.txt
│   │   └── train.txt
│   ├── pdbbind_v2019_docking_nowater
│   │   ├── cal_docking.py
│   │   ├── data
│   │   ├── keys
│   │   ├── pdb_to_affinity.py
│   │   ├── pdb_to_affinity.txt
│   │   ├── pdbqt_to_pdb.py
│   │   └── total.txt
│   ├── pdbbind_v2019_random_screening
│   │   ├── cal_docking.py
│   │   ├── chembl_27_chemreps.txt
│   │   ├── data
│   │   ├── id_smiles.txt
│   │   ├── keys
│   │   ├── pdb_to_affinity.py
│   │   ├── pdb_to_affinity.txt
│   │   ├── pdbqt_to_pdb.py
│   │   ├── test.txt
│   │   ├── total.txt
│   │   └── train.txt
│   ├── pdbbind_v2019_refined
│   │   ├── keys
│   │   ├── ligand_to_complex.txt
│   │   ├── pdb_to_affinity.py
│   │   ├── pdb_to_affinity.txt
│   │   ├── pp_test
│   │   ├── pp_train
│   │   └── test.txt
│   └── rcsb_pdb
│       ├── INDEX_refined_data.2019
│       ├── download_ligand.py
│       ├── ligand_crawling.py
│       ├── ligand_to_complex0.txt
│       ├── ligand_to_complex2.txt
│       ├── ligand_to_complex3.txt
│       ├── refined_data
│       ├── rename.py
│       ├── test_keys.pkl
│       └── train_keys.pkl
├── dataset.py
├── dependencies
├── layers.py
├── model.py < layers, dataset, utils
├── predict.py < arguments, dataset, model, utils
├── save
│   └── save_1000.pt
├── submit.py
├── test.py < arguments, dataset, model, utils
├── train.py < arguments, model, utils
├── train.sh
└── utils.py < dataset
</pre>
<code class="code-title">Python Files</code>
<pre class="code-path">
./casf2016_benchmark/docking_power.py
./casf2016_benchmark/ranking_power.py
./casf2016_benchmark/scoring_power.py
./casf2016_benchmark/screening_power.py
./data/CASF-2016/docking/data/preprocess.py
./data/CASF-2016/docking/keys/generate_keys.py
./data/CASF-2016/docking/pdb_to_affinity.py
./data/CASF-2016/mol2_decoy_docking/run_split.py
./data/CASF-2016/mol2_decoy_screening/run_split.py
./data/CASF-2016/scoring/data/preprocess.py
./data/CASF-2016/scoring/keys/generate_keys.py
./data/CASF-2016/scoring/pdb_to_affinity.py
./data/CASF-2016/screening/data/preprocess.py
./data/CASF-2016/screening/keys/generate_keys.py
./data/CASF-2016/screening/pdb_to_affinity.py
./data/csar1/data/preprocess.py
./data/csar1/keys/generate_keys.py
./data/csar1/pdb_to_affinity.py
./data/csar1/split_receptor_ligand.py
./data/csar2/data/preprocess.py
./data/csar2/keys/generate_keys.py
./data/csar2/pdb_to_affinity.py
./data/csar2/split_receptor_ligand.py
./data/pdbbind_v2019_cross_screening/cal_docking.py
./data/pdbbind_v2019_cross_screening/data/preprocess.py
./data/pdbbind_v2019_cross_screening/data/remove_noatom_protein.py
./data/pdbbind_v2019_cross_screening/data/submit.py
./data/pdbbind_v2019_cross_screening/keys/generate_keys.py
./data/pdbbind_v2019_cross_screening/pdbqt_to_pdb.py
./data/pdbbind_v2019_cross_screening/pdb_to_affinity.py
./data/pdbbind_v2019_docking_nowater/cal_docking.py
./data/pdbbind_v2019_docking_nowater/data/preprocess.py
./data/pdbbind_v2019_docking_nowater/keys/generate_keys.py
./data/pdbbind_v2019_docking_nowater/pdbqt_to_pdb.py
./data/pdbbind_v2019_docking_nowater/pdb_to_affinity.py
./data/pdbbind_v2019_random_screening/cal_docking.py
./data/pdbbind_v2019_random_screening/data/preprocess.py
./data/pdbbind_v2019_random_screening/keys/generate_keys.py
./data/pdbbind_v2019_random_screening/pdbqt_to_pdb.py
./data/pdbbind_v2019_random_screening/pdb_to_affinity.py
./data/pdbbind_v2019_refined/keys/generate_keys.py
./data/pdbbind_v2019_refined/pdb_to_affinity.py
./data/pdbbind_v2019_refined/pp_test/preprocess.py
./data/pdbbind_v2019_refined/pp_train/preprocess.py
./data/rcsb_pdb/download_ligand.py
./data/rcsb_pdb/ligand_crawling.py
./data/rcsb_pdb/rename.py
</pre>
<code class="code-title">File I/O</code>
<pre class="code-path">
data/pdbbind_v2019_cross_screening/cal_docking.py:    with open("./remain.txt", "r") as f:
data/pdbbind_v2019_cross_screening/data/preprocess.py:    with open(data_dir + pdb_fn, "wb") as fp:
data/pdbbind_v2019_cross_screening/data/remove_noatom_protein.py:    with open(k, "rb") as f:
data/pdbbind_v2019_cross_screening/data/submit.py:    with open("./jobscript.x", "w") as w:
data/pdbbind_v2019_cross_screening/keys/generate_keys.py:with open("train_keys.pkl", "wb") as w:
data/pdbbind_v2019_cross_screening/keys/generate_keys.py:with open("test_keys.pkl", "wb") as w:
data/pdbbind_v2019_cross_screening/pdbqt_to_pdb.py:    with open("./remain.txt", "r") as f:
data/pdbbind_v2019_cross_screening/pdb_to_affinity.py:with open("./pdb_to_affinity.txt", "w") as f:
data/pdbbind_v2019_docking_nowater/cal_docking.py:    with open("./total.txt", "r") as f:
data/pdbbind_v2019_docking_nowater/data/preprocess.py:    with open(data_dir + pdb_fn, "wb") as fp:
data/pdbbind_v2019_docking_nowater/keys/generate_keys.py:with open("train_keys.pkl", "wb") as w:
data/pdbbind_v2019_docking_nowater/keys/generate_keys.py:with open("test_keys.pkl", "wb") as w:
data/pdbbind_v2019_docking_nowater/pdb_to_affinity.py:with open('../index_pdbbind_v2019/index/INDEX_refined_data.2019', 'r') as r:
data/pdbbind_v2019_docking_nowater/pdb_to_affinity.py:with open('./pdb_to_affinity.txt', 'w') as w:
data/pdbbind_v2019_random_screening/cal_docking.py:    with open('./id_smiles.txt', 'r') as f:
data/pdbbind_v2019_random_screening/cal_docking.py:    with open('./chembl_27_chemreps.txt', 'r') as f:
data/pdbbind_v2019_random_screening/cal_docking.py:    with open('./total.txt', 'r') as f:
data/pdbbind_v2019_random_screening/data/preprocess.py:    with open(data_dir + pdb_fn, "wb") as fp:
data/pdbbind_v2019_random_screening/keys/generate_keys.py:with open("train_keys.pkl", "wb") as w:
data/pdbbind_v2019_random_screening/keys/generate_keys.py:with open("test_keys.pkl", "wb") as w:
data/pdbbind_v2019_random_screening/pdb_to_affinity.py:with open("./pdb_to_affinity.txt", "w") as f:
data/pdbbind_v2019_refined/keys/generate_keys.py:with open("train_keys.pkl", "wb") as w:
data/pdbbind_v2019_refined/keys/generate_keys.py:with open("test_keys.pkl", "wb") as w:
data/pdbbind_v2019_refined/pdb_to_affinity.py:with open("../index_pdbbind_v2019/index/INDEX_refined_data.2019", "r") as f:
data/pdbbind_v2019_refined/pdb_to_affinity.py:with open("./pdb_to_affinity.txt", "w") as f:
data/pdbbind_v2019_refined/pp_test/preprocess.py:    with open(f'{data_dir}/{key}', 'wb') as fp:
data/pdbbind_v2019_refined/pp_test/preprocess.py:with open(fn, 'r') as r:
data/pdbbind_v2019_refined/pp_train/preprocess.py:    with open(data_dir + key, 'wb') as fp:
data/pdbbind_v2019_refined/pp_train/preprocess.py:with open(fn, 'r') as r:
</pre>


<code class="code-title">train dataset : ./data/pdbbind_v2019_refined/ligand_to_complex.txt</code>
<pre class="sudo-code">
2qzr    S79
5itp    6DB
5fck    5WC
5ot9    AOZ
3bxh    F6P
5nka    91H
5nxg    RA1
1c88    OTA
3gi4    K60
5j2x    6DL
...
...
...
</pre>
<code class="code-title">test dataset : ./data/pdbbind_v2019_refined/test.txt</code>
<pre class="sudo-code">
1a30
1bcu
1bzc
1c5z
1e66
1eby
1g2k
1gpk
1gpn
1h22
...
...
...
</pre>
<code class="code-title">rcsb crawling dataset : ./data/rcsb_pdb/refined_data/*/*.sdf</code>
<pre class="sudo-code">
184L_I4B_A_401
  RCSB PDB08012014323D
Coordinates from PDB:184L:A:401 Model:1 without hydrogens
 10 10  0  0  0  0            999 V2000
   27.3570    6.7720    3.3880   C 0  0  0  0  0  0  0  0  0  0  0  0
   27.3210    7.2930    4.6580   C 0  0  0  0  0  0  0  0  0  0  0  0
   26.5680    6.6500    5.6700   C 0  0  0  0  0  0  0  0  0  0  0  0
   25.8310    5.5260    5.3590   C 0  0  0  0  0  0  0  0  0  0  0  0
   25.8870    4.9870    4.0770   C 0  0  0  0  0  0  0  0  0  0  0  0
   26.6640    5.6070    3.0880   C 0  0  0  0  0  0  0  0  0  0  0  0
   28.1350    7.4950    2.3350   C 0  0  0  0  0  0  0  0  0  0  0  0
   27.1650    8.3380    1.5330   C 0  0  0  0  0  0  0  0  0  0  0  0
   27.8680    8.7990    0.2910   C 0  0  0  0  0  0  0  0  0  0  0  0
   26.6640    9.5080    2.3390   C 0  0  0  0  0  0  0  0  0  0  0  0
  1  2  2  0  0  0  0
  1  6  1  0  0  0  0
  1  7  1  0  0  0  0
  2  3  1  0  0  0  0
  3  4  2  0  0  0  0
  4  5  1  0  0  0  0
  5  6  2  0  0  0  0
  7  8  1  0  0  0  0
  8  9  1  0  0  0  0
  8 10  1  0  0  0  0
M  END
~ InstanceId
184L_I4B_A_401

~ ChemCompId
I4B

~ PdbId
184L

~ ChainId
A

~ ResidueNumber
401

~ InsertionCode
~ Model
1

~ AltIds
~ MissingHeavyAtoms
0

~ ObservedFormula
C10

~ Name
ISOBUTYLBENZENE

~ SystematicName
2-methylpropylbenzene

~ Synonyms
~ Type
NON-POLYMER

~ Formula
C10 H14

~ MolecularWeight
134.218

~ ModifiedDate
2011-06-04

~ Parent
~ OneLetterCode
~ SubcomponentList
~ AmbiguousFlag
N

~ InChI
InChI=1S/C10H14/c1-9(2)8-10-6-4-3-5-7-10/h3-7,9H,8H2,1-2H3

~ InChIKey
KXUHSQYYJYAXGZ-UHFFFAOYSA-N

~ SMILES
CC(C)Cc1ccccc1

$$$$
</pre>
<code class="code-title">original affinity dataset : ./data/pdbbind_v2019_refined/pdb_to_affinity.txt</code>
<pre class="sudo-code">
2r58    2.00
3c2f    2.00
3g2y    2.00
3pce    2.00
4qsu    2.00
4qsv    2.00
4u54    2.06
3ao4    2.07
4cs9    2.10
2w8w    2.12
...
...
...
</pre>
<code class="code-title">docking affinity dataset : ./data/pdbbind_v2019_docking_nowater/pdb_to_affinity.txt</code>
<pre class="sudo-code">
2r58_out_76     2.00
2r58_out_77     2.00
2r58_out_78     2.00
2r58_out_79     2.00
2r58_out_80     2.00
2r58_out_81     2.00
2r58_out_82     2.00
2r58_out_83     2.00
2r58_out_84     2.00
2r58_out_85     2.00
...
...
...
</pre>
<code class="code-title">random_screening affinity dataset : ./data/pdbbind_v2019_random_screening/pdb_to_affinity.txt</code>
<pre class="sudo-code">
STOCK4S-00529_4zl4      5
STOCK2S-63769_3q2j      5
STOCK4S-36534_3uz5      5
STOCK3S-34201_4o04      5
STOCK7S-22208_5cc2      5
STOCK2S-68433_4tte      5
STOCK6S-18695_2wm0      5
STOCK5S-00257_3myq      5
STOCK4S-66352_2fmb      5
STOCK3S-53058_4epy      5
...
...
...
</pre>
<code class="code-title">cross_screening affinity dataset : ./data/pdbbind_v2019_cross_screening/pdb_to_affinity.txt</code>
<pre class="sudo-code">
4jkw_3aqt       5
2iwx_1tsy       5
4k18_4xip       5
2vvv_1iy7       5
4cjq_2f7o       5
4xit_5oei       5
1p1n_4mme       5
1o2z_2v54       5
4att_3l0v       5
4jx9_1o2q       5
...
...
...
</pre>
<details markdown="1">
  <summary align="center">dataset.py</summary>
<pre class="sudo-code">
def get_torsion_energy(m):
def get_epsilon_sigma(m1, m2, mmff=True):
def get_epsilon_sigma_uff(m1, m2):
def get_epsilon_sigma_mmff(m1, m2):
def cal_torsion_energy(m):
def cal_internal_vdw(m):
def cal_charge(m):
def one_of_k_encoding(x, allowable_set):
def one_of_k_encoding_unk(x, allowable_set):
def atom_feature(m, atom_i, i_donor, i_acceptor):
def get_atom_feature(m, is_ligand=True):
def rotate(molecule, angle, axis, fix_com=False):
def dm_vector(d1, d2):
def extract_valid_amino_acid(m, amino_acids):
def position_to_index(positions, target_position):
def get_interaction_matrix(d1, d2, interaction_data):
def classifyAtoms(mol, polar_atoms=[7, 8, 15, 16]):
def cal_sasa(m):
def get_vdw_radius(a):
def cal_uff(m):
def get_hydrophobic_atom(m):
def get_A_hydrophobic(m1, m2):
def get_hbond_donor_indice(m):
def get_hbond_acceptor_indice(m):
def get_A_hbond(m1, m2):
def get_A_metal_complexes(m1, m2):
def mol_to_feature(m1, m1_uff, m2, interaction_data, pos_noise_std):
def is_atoms_in_same_ring(i, j, ssr):
def count_active_rotatable_bond(m, dm):
class MolDataset(Dataset):
    def __init__(self, keys, data_dir, id_to_y, random_rotation=0.0,
    def __len__(self):
    def __getitem__(self, idx):
class DTISampler(Sampler):
    This simply changes the __iter__ part of the dataset class.
    def __init__(self, weights, num_samples, replacement=True):
    def __iter__(self):
    def __len__(self):
def check_dimension(tensors):
def collate_tensor(tensor, max_tensor, batch_idx):
def tensor_collate_fn(batch):
</pre>
![image](https://user-images.githubusercontent.com/52376448/114423214-ebc65780-9bf1-11eb-9c99-21a0882b463d.png)

<code class="code-title">get_torsion_energy(m) : e</code><br>
m, mp ffTerms, iTerm, jTerm, state, setMethod, ff, e

<code class="code-title">get_epsilon_sigma(m1, m2, mmff=True) : get_epsilon_sigma_uff(m1, m2)/get_epsilon_sigma_mmff(m1, m2)</code><br>
m1, m2, mmff

<code class="code-title">get_epsilon_sigma_uff(m1, m2) : vdw_epsilon, vdw_sigma</code><br>
m1, m2, n1, n2, vdw_epsilon, vdw_sigma, m_combine, i1, i2, param, d, e

<code class="code-title">get_epsilon_sigma_mmff(m1, m2) : vdw_epsilon, vdw_sigma</code><br>
m1, m2, n1, n2, vdw_epsilon, vdw_sigma, m_combine, mp, i1, i2, param, d, e

<code class="code-title">cal_torsion_energy(m) : energy</code><br>
m, energy, torsion_list, torsion_list_ring, angles, idx, t, indice, angle, v, hs, i, n, pi_zero

<code class="code-title">cal_internal_vdw(m) : retval</code><br>
m, retval, n, c, d, dm, adj, topological_dm, i1, i2, param, e

<code class="code-title">cal_charge(m) : charges</code><br>
m, charges, i

<code class="code-title">one_of_k_encoding(x, allowable_set) : list(map(lambda s: x == s, allowable_set))</code><br>
x, allowable_set, s

<code class="code-title">one_of_k_encoding_unk(x, allowable_set) : list(map(lambda s: x == s, allowable_set))</code><br>
x, allowable_set, s

<code class="code-title">atom_feature(m, atom_i, i_donor, i_acceptor) : return</code><br>
m, atom_i, i_donor, i_acceptor, atom
```
return np.array(one_of_k_encoding_unk(atom.GetSymbol(),
                ["C", "N", "O", "S", "F", "P", "Cl", "Br", "X"]) +
                one_of_k_encoding_unk(atom.GetDegree(), [0, 1, 2, 3, 4, 5]) +
                one_of_k_encoding_unk(atom.GetTotalNumHs(), [0, 1, 2, 3, 4]) +
                one_of_k_encoding_unk(atom.GetImplicitValence(), [0, 1, 2, 3, 4, 5]) +
                [atom.GetIsAromatic()])  # (10, 6, 5, 6, 1) --> total 28
```

<code class="code-title">get_atom_feature(m, is_ligand=True) : H</code><br>
m, is_ligand, n, H

<code class="code-title">rotate(molecule, angle, axis, fix_com=False) : molecule</code><br>
molecule, angle, axis, fix_corn, c, d, ori_mean, d, atoms, i, new_d

<code class="code-title">dm_vector(d1, d2) : d1 - d2</code><br>
d1, d2, n1, n2

<code class="code-title">extract_valid_amino_acid(m, amino_acids) : ret_m</code><br>
m, amino_acids, ms, valid_ms, k, ret_m, i, ret_m

<code class="code-title">position_to_index(positions, target_position) : indice.tolist()</code><br>
positions, target_position, indice, diff

<code class="code-title">get_interaction_matrix(d1, d2, interaction_data) : A</code><br>
d1, d2, interaction_data, n1, n2, A, i_type, k, ps, p1, p2, i1, i2

<code class="code-title">classifyAtoms(mol, polar_atoms=[7, 8, 15, 16]) : (radii)</code><br>
mol, polar_atoms, symbol_radius, radii, atom

<code class="code-title">cal_sasa(m) : sasa</code><br>
m, radii, sasa

<code class="code-title">get_vdw_radius(a) : Chem.GetPeriodicTable().GetRvdw(atomic_number)</code><br>
a, metal_symbols, atomic_number, atomic_number_to_radius

<code class="code-title">cal_uff(m) : e</code><br>
m, ffu, e

<code class="code-title">get_hydrophobic_atom(m) : retval</code><br>
m, n, retval, i, a, s, n_a, x, diff

<code class="code-title">get_A_hydrophobic(m1, m2) : np.outer(indice1, indice2)</code><br>
m1, m2, indice1, indice2
    
<code class="code-title">get_hbond_donor_indice(m) : indice</code><br>
m, smarts, indice, s, i
    
<code class="code-title">get_hbond_acceptor_indice(m) : indice</code><br>
m, smarts, indice, s
    
<code class="code-title">get_A_hbond(m1, m2) : A</code><br>
m1, m2, h_acc_indice1, h_acc_indice2, A, i, j

<code class="code-title">get_A_metal_complexes(m1, m2) : A</code><br>
m1, m2, h_acc_indice1, h_acc_indice2, metal_symbols, metal_indice1, metal_indice2

<code class="code-title">mol_to_feature(m1, m1_uff, m2, interaction_data, pos_noise_std) : sample</code><br>
m1, m1_uff, m2, interaction_data, pos_noise_std, m1, m2, angle, axis, m1_rot, n1, d1, d1_rot, adf1, h1, n1, c2, d2, adj2, h2, dmv, dmv_rot, A_int, sasa, dsasa, rotor, charge1, charge2, valid1, valid2, metal_symbols, no_metal1, a, no_metal2, vdw_radius1, vdw_radius2, vdw_epsilon, vdw_sigma, delta_uff, sample
![image](https://user-images.githubusercontent.com/52376448/114428608-5c23a780-9bf7-11eb-982d-26668e5a5818.png)
<pre class="python-code">
def mol_to_feature(m1, m1_uff, m2, interaction_data, pos_noise_std):
    # Remove hydrogens
    m1 = Chem.RemoveHs(m1)
    m2 = Chem.RemoveHs(m2)

    # extract valid amino acids
    # m2 = extract_valid_amino_acid(m2, self.amino_acids)

    # random rotation
    angle = np.random.uniform(0, 360, 1)[0]
    axis = np.random.uniform(-1, 1, 3)
    # m1 = rotate(m1, angle, axis, False)
    # m2 = rotate(m2, angle, axis, False)

    angle = np.random.uniform(0, 360, 1)[0]
    axis = np.random.uniform(-1, 1, 3)
    m1_rot = rotate(copy.deepcopy(m1), angle, axis, True)
    
    # prepare ligand
    n1 = m1.GetNumAtoms()
    d1 = np.array(m1.GetConformers()[0].GetPositions())
    d1 += np.random.normal(0.0, pos_noise_std, d1.shape)
    d1_rot = np.array(m1_rot.GetConformers()[0].GetPositions())
    adj1 = GetAdjacencyMatrix(m1) + np.eye(n1)
    h1 = get_atom_feature(m1, True)

    # prepare protein
    n2 = m2.GetNumAtoms()
    c2 = m2.GetConformers()[0]
    d2 = np.array(c2.GetPositions())
    d2 += np.random.normal(0.0, pos_noise_std, d2.shape)
    adj2 = GetAdjacencyMatrix(m2) + np.eye(n2)
    h2 = get_atom_feature(m2, True)

    # prepare distance vector
    dmv = dm_vector(d1, d2)
    dmv_rot = dm_vector(d1_rot, d2)

    # get interaction matrix
    # A_int = get_interaction_matrix(d1, d2, interaction_data)
    A_int = np.zeros(
        (len(interaction_types), m1.GetNumAtoms(), m2.GetNumAtoms()))
    A_int[-2] = get_A_hydrophobic(m1, m2)
    A_int[1] = get_A_hbond(m1, m2)
    A_int[-1] = get_A_metal_complexes(m1, m2)

    # cal sasa
    sasa = cal_sasa(m1)
    dsasa = sasa - cal_sasa(m1_uff)

    # count rotatable bonds
    rotor = CalcNumRotatableBonds(m1)
    # dm = distance_matrix(d1, d2)
    # rotor = count_active_rotatable_bond(m1, dm)
    # charge
    # charge1 = cal_charge(m1)
    # charge2 = cal_charge(m2)
    charge1 = np.zeros((n1,))
    charge2 = np.zeros((n2,))
    
    """
    mp1 = AllChem.MMFFGetMoleculeProperties(m1)
    mp2 = AllChem.MMFFGetMoleculeProperties(m2)
    charge1 = [mp1.GetMMFFPartialCharge(i) for i in range(m1.GetNumAtoms())]
    charge2 = [mp2.GetMMFFPartialCharge(i) for i in range(m2.GetNumAtoms())]
    """

    # partial charge calculated by gasteiger
    charge1 = np.array(charge1)
    charge2 = np.array(charge2)

    # There is nan for some cases.
    charge1 = np.nan_to_num(charge1, nan=0, neginf=0, posinf=0)
    charge2 = np.nan_to_num(charge2, nan=0, neginf=0, posinf=0)

    # valid
    valid1 = np.ones((n1,))
    valid2 = np.ones((n2,))

    # no metal
    metal_symbols = ["Zn", "Mn", "Co", "Mg", "Ni", "Fe", "Ca", "Cu"]
    no_metal1 = np.array([1 if a.GetSymbol() not in metal_symbols else 0
                          for a in m1.GetAtoms()])
    no_metal2 = np.array([1 if a.GetSymbol() not in metal_symbols else 0
                          for a in m2.GetAtoms()])
    # vdw radius
    vdw_radius1 = np.array([get_vdw_radius(a) for a in m1.GetAtoms()])
    vdw_radius2 = np.array([get_vdw_radius(a) for a in m2.GetAtoms()])

    vdw_epsilon, vdw_sigma = get_epsilon_sigma(m1, m2, False)
    
    # uff energy difference
    # delta_uff = cal_uff(m1)-cal_uff(m1_uff)
    # delta_uff = get_torsion_energy(m1) - get_torsion_energy(m1_uff)
    # delta_uff = cal_torsion_energy(m1)+cal_internal_vdw(m1)
    delta_uff = 0.0
    sample = {
        "h1": h1,
        "adj1": adj1,
        "h2": h2,
        "adj2": adj2,
        "A_int": A_int,
        "dmv": dmv,
        "dmv_rot": dmv_rot,
        "pos1": d1,
        "pos2": d2,
        "sasa": sasa,
        "dsasa": dsasa,
        "rotor": rotor,
        "charge1": charge1,
        "charge2": charge2,
        "vdw_radius1": vdw_radius1,
        "vdw_radius2": vdw_radius2,
        "vdw_epsilon": vdw_epsilon,
        "vdw_sigma": vdw_sigma,
        "delta_uff": delta_uff,
        "valid1": valid1,
        "valid2": valid2,
        "no_metal1": no_metal1,
        "no_metal2": no_metal2,
    }
    return sample
</pre>

<code class="code-title">is_atoms_in_same_ring(i, j, ssr) : True/False</code><br>
i, j, ssr, s

<code class="code-title">count_active_rotatable_bond(m, dm) : sum(RT)</code><br>
m, dm, rot_atom_pairs, ssr, n, RT, pair, RT_copy, min_dm, hydrophobic_indice, i

<code class="code-title">MolDataset(keys, data_dir, id_to_y, random_rotation=0.0, pos_noise_std=0.0) : </code><br>
<pre class="python-code">
class MolDataset(Dataset):
    def __init__(self, keys, data_dir, id_to_y, random_rotation=0.0,
                 pos_noise_std=0.0):
        self.keys = keys
        self.data_dir = data_dir
        self.id_to_y = id_to_y
        self.random_rotation = random_rotation
        self.amino_acids = ["ALA", "ARG", "ASN", "ASP", "ASX", "CYS", "GLU", "GLN", "GLX",
                            "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER",
                            "THR", "TRP", "TYR", "VAL"]
        self.pos_noise_std = pos_noise_std

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, idx):
        key = self.keys[idx]
        with open(self.data_dir + "/" + key, "rb") as f:
            m1, m1_uff, m2, interaction_data = pickle.load(f)

        sample = mol_to_feature(
            m1, m1_uff, m2, interaction_data, self.pos_noise_std)
        sample["affinity"] = self.id_to_y[key] * -1.36
        sample["key"] = key
        return sample
</pre>
<code class="code-title">[DTISampler]__init__(self, weights, num_samples, replacement=True) : </code><br>

<code class="code-title">check_dimension(tensors) : np.max(size, 0)</code><br>
tensors, size, tensor
    
<code class="code-title">collate_tensor(tensor, max_tensor, batch_idx) : max_tensor</code><br>
tensor, max_tensor, batch_idx, dims, max_dims, slice_list

<code class="code-title">tensor_collate_fn(batch) : ret_dict</code><br>
batch, batch_items, e, it, dim_dict, total_key, total_value, batch_size, n_element, total_key, i, k, value_list, j, keys, key, value
    
</details>
<details markdown="1">
  <summary align="center">layers.py</summary>
<pre class="sudo-code">
class MPNN(torch.nn.Module):
    def __init__(self, n_edge_feature, n_atom_feature):
    def forward(self, x1, x2, edge):
class InteractionNet(torch.nn.Module):
    def __init__(self, n_edge_feature, n_atom_feature):
    def forward(self, x1, x2, edge, valid_edge):
class IntraNet(torch.nn.Module):
    def __init__(self, n_atom_feature, n_edge_feature):
    def forward(self, edge, adj, x):
class GAT_gate(torch.nn.Module):
    def __init__(self, n_in_feature, n_out_feature):
    def forward(self, x, adj):
class GConv_gate(torch.nn.Module):
    def __init__(self, n_in_feature, n_out_feature):
    def forward(self, x, adj):
class ConcreteDropout(nn.Module):
    def __init__(self, weight_regularizer=1e-6,
    def forward(self, x1, layer, additional_args=None):
    def _concrete_dropout(self, x, p):
class MultiHeadAttention(nn.Module):
    def __init__(self, args, ninfo):
    def forward(self, x):
    def _split_heads(self, x):
    def _multi_head_attention(self, xq, xk, xv):
class NewMultiHeadAttention(nn.Module):
    def __init__(self, args, ninfo):
    def forward(self, x):
    def _split_heads(self, x):
    def _multi_head_attention(self, xq, xk, xv):
class GraphAttention(nn.Module):
    def __init__(self, args, ninfo):
    def forward(self, x):
    def _arbit_embedding(self, vec):
    def _attn_matrix(self, q, k, info):
class ConvBlock(nn.Module):
    def __init__(self, in_feature, out_feature, do=0.0, stride=1, kernel=3,
    def forward(self, input):
class PredictBlock(nn.Module):
    def __init__(self, in_feature, out_feature, dropout, is_last):
    def forward(self, input):
</pre>
</details>
<details markdown="1">
  <summary align="center">model.py</summary>
<pre class="sudo-code">
class DTIHarmonic(nn.Module):
    def __init__(self, args):
    def vina_hbond(self, dm, h, vdw_radius1, vdw_radius2, A):
    def vina_hydrophobic(self, dm, h, vdw_radius1, vdw_radius2, A):
    def cal_vdw_interaction(self, dm, h, vdw_radius1, vdw_radius2,
    def cal_torsion_energy(self, torsion_energy):
    def cal_distance_matrix(self, p1, p2, dm_min):
    def get_embedding_vector(self, sample):
    def forward(self, sample, DM_min=0.5, cal_der_loss=False):
class GNN(nn.Module):
    def __init__(self, args):
    def cal_distance_matrix(self, p1, p2, dm_min):
    def forward(self, sample, DM_min=0.5, cal_der_loss=False):
    def _linear(tensor, layers, act=None):
class CNN3D(nn.Module):
    def __init__(self, args):
    def forward(self, sample, DM_min=0.5, cal_der_loss=False):
    def _get_lattice(self, batch_size, pos1, pos2, h1, h2, lattice_size):
    def _plot(self, lattice, idx):
class CNN3D_KDEEP(nn.Module):
    def __init__(self, args):
    def forward(self, sample, DM_min=0.5, cal_der_loss=False):
    def _get_lattice(self, pos1, pos2, vr1, vr2, h1, h2, lattice_dim):
    def _plot(self, lattice, idx):
    def _add_act(self, func, act="relu"):
</pre>
<code class="code-title">[DTIHarmonic]vina_hbond(self, dm, h, vdw_radius1, vdw_radius2, A)</code><br>

<code class="code-title">[DTIHarmonic]vina_hydrophobic(self, dm, h, vdw_radius1, vdw_radius2, A)</code><br>

<code class="code-title">[DTIHarmonic]cal_vdw_interaction(self, dm, h, vdw_radius1, vdw_radius2, vdw_epsilon, vdw_sigma, valid1, valid) : energy</code><br>
![image](https://user-images.githubusercontent.com/52376448/114346912-2357e400-9b9f-11eb-963b-1c75c200cb6d.png)

<code class="code-title">[DTIHarmonic]cal_torsion_energy(self, torsion_energy) : torsion_energy</code><br>
![image](https://user-images.githubusercontent.com/52376448/114348594-b98d0980-9ba1-11eb-9218-5a337ad52774.png)

<code class="code-title">[DTIHarmonic]cal_distance_matrix(self, p1, p2, dm_min) : dm</code><br>
![image](https://user-images.githubusercontent.com/52376448/114348097-0ae8c900-9ba1-11eb-8663-47e853f785fb.png)

<code class="code-title">[DTIHarmonic]get_embedding_vector(self, sample) : h1, h2</code><br>
![image](https://user-images.githubusercontent.com/52376448/114344784-67e18080-9b9b-11eb-83e0-17754fcc094e.png)

<code class="code-title">[DTIHarmonic]forward(self, sample, DM_min=0.5, cal_der_loss=False)</code><br>
![image](https://user-images.githubusercontent.com/52376448/114341875-b4c25880-9b95-11eb-8bd1-7eae9a555445.png)
</details>
<details markdown="1">
  <summary align="center">predict.py</summary>
<pre class="sudo-code">
def write(of, model, pred, time, args, extra_data=None):
    > Parameter : Local opt
    > Parameter : Hbond coeff
    > Parameter : Hydrophobic coeff
    > Parameter : Rotor coeff
    > Prediction : Total prediction
    > Prediction : VDW
    > Prediction : Hbond
    > Prediction : Metal
    > Prediction : Hydrophobic
def cal_vdw_energy(dm, dm_0, vdw_A, vdw_N, is_last=False):
def cal_hbond_energy(dm, dm_0, coeff, A, is_last=False):
def cal_hydrophobic_energy(dm, dm_0, coeff, A, is_last=False):
def cal_internal_vdw_energy(dm, topological_dm, epsilon, sigma, is_last=False):
def make_ring_matrix(m):
def make_conjugate_matrix(m):
def distance_fix_pair(m):
def write_molecule(filename, m, pos):
def local_optimize(model, lf, pf, of, loof, args, device):
def predict(model, lf, pf, of, args, device):
</pre>
</details>
<details markdown="1">
  <summary align="center">utils.py</summary>
<pre class="sudo-code">
def loss_var(pred_var, pred, affinity, log=True):
def dic_to_device(dic, device):
def load_data(filename):
def set_cuda_visible_device(ngpus):
def initialize_model(model, device, load_save_file=False):
def read_data(filename, key_dir):
def get_dataset_dataloader(train_keys, test_keys, data_dir, id_to_y,
def write_result(filename, pred, true):
def extract_binding_pocket(ligand, pdb):
    class GlySelect(Select):
        def accept_residue(self, residue):
def read_molecule(filename):
</pre>
</details>
<details markdown="1">
  <summary align="center">train.py</summary>
<pre class="sudo-code">
def run(model, data_iter, data_iter2, data_iter3, data_iter4, train_mode):
</pre>
<pre class="sudo-code">

args.filename, args.filename2, args.filename3, args.filename4, args.key_dir, args.key_dir2, args.key_dir3, args.key_dir4
----------v----------
utils.read_data
----------v----------
train_keys, test_keys, id_to_y, train_keys2, test_keys2, id_to_y2, train_keys3, test_keys3, id_to_y3, train_keys4, test_keys4, id_to_y4


train_keys, test_keys, args.data_dir, id_to_y, args.batch_size, args.num_workers, args.pos_noise_std
----------v----------                                 
utils.get_dataset_dataloader
----------v----------
train_dataset, train_dataloader, test_dataset, test_dataloader


train_dataloader, train_dataloader2, train_dataloader3, train_dataloader4, test_dataloader, test_dataloader2, test_dataloader3, test_dataloader4
----------v----------
iter
----------v----------
train_data_iter, train_data_iter2, train_data_iter3, train_data_iter4, test_data_iter, test_data_iter2, test_data_iter3, test_data_iter4


model, train_data_iter, train_data_iter2, train_data_iter3, train_data_iter4
----------v----------
run
----------v----------
train_losses, train_losses_der1, train_losses_der2, train_losses_docking, train_losses_screening, train_losses_var, train_pred, train_true, train_pred_docking, train_true_docking, train_pred_screening, train_true_screening, train_total_losses

</pre>
</details>
<details markdown="1">
  <summary align="center">train.sh</summary>
<pre class="sudo-code">
--train_result_filename=result_train.txt \
--test_result_filename=result_test.txt \
--train_result_docking_filename=result_docking_train.txt \
--test_result_docking_filename=result_docking_test.txt \
--train_result_screening_filename=result_screening_train.txt \
--test_result_screening_filename=result_screening_test.txt \
--data_dir=./data/pdbbind_v2019_refined/data/ \
--filename=./data/pdbbind_v2019_refined/pdb_to_affinity.txt \
--key_dir=./data/pdbbind_v2019_refined/keys/ \
--data_dir2=./data/pdbbind_v2019_docking_nowater/data/ \
--filename2=./data/pdbbind_v2019_docking_nowater/pdb_to_affinity.txt \
--key_dir2=./data/pdbbind_v2019_docking_nowater/keys/ \
--data_dir3=./data/pdbbind_v2019_random_screening/data/ \
--filename3=./data/pdbbind_v2019_random_screening/pdb_to_affinity.txt \
--key_dir3=./data/pdbbind_v2019_random_screening/keys/ \
--data_dir4=./data/pdbbind_v2019_cross_screening/data/ \
--filename4=./data/pdbbind_v2019_cross_screening/pdb_to_affinity.txt \
--key_dir4=./data/pdbbind_v2019_cross_screening/keys/ \
</pre>
</details>
<details markdown="1">
  <summary align="center">test.py</summary>
<pre class="sudo-code">
test_keys.pkl > MolDataset > test_dataset
test_dataset > DataLoader > test_data_loader
test_data_loader > iteration > sample
sample > model > pred
</pre>
</details>
<details markdown="1">
  <summary align="center">submit.py</summary>
<pre class="sudo-code">
</pre>
</details>


<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<!-- Content Block -->


---

<!-- Reference Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='REF'>Reference</b>
<ol>
  <li><a href="https://aceteamkaist.wixsite.com/home">ACE (Advanced Computational Engine) Team, Laboratory</a></li>
  <li><a href="https://github.com/jaechanglim/DTI_PDBbind">DTI_PDBbind, GitHub</a></li>
  <li><a href="http://www.pdbbind-cn.org/">PDBbind Dataset</a></li>
  <li><a href="http://www.csardock.org/">CSAR Dataset</a></li>
  <li><a href="https://www.rcsb.org/">RCSB Dataset</a></li>
  <li><a href="https://proteopedia.org/wiki/index.php/PDB_code">PDB code</a></li>
  <li><a href="https://en.wikipedia.org/wiki/Comparison_of_force-field_implementations">Comparison of force-field implementations</a></li>
</ol>
<ul>
  <li><a href="https://arxiv.org/pdf/2008.12249.pdf">(2020) PIGNet: A physics-informed deep learning model toward generalized drug-target interaction predictions</a></li>
  <li><a href="https://arxiv.org/ftp/arxiv/papers/1906/1906.02418.pdf">(2019) OnionNet: a multiple-layer inter-molecular contact based convolutional
neural network for protein-ligand binding affinity prediction</a></li>
  <li><a href="https://arxiv.org/pdf/1912.00318.pdf">(2019) DeepAtom: A Framework for Protein-Ligand Binding Affinity Prediction</a></li>
  <li><a href="https://link.springer.com/article/10.1007/s10822-020-00305-1">(2020) Improving the binding affinity estimations of protein–ligand complexes using machine-learning facilitated force field method</a></li>  
  <li><a href="https://pubs.acs.org/doi/10.1021/acs.jcim.7b00650">(2018) KDEEP: Protein-Ligand Absolute Binding Affinity Prediction via 3D-Convolutional Neural Networks</a></li>
  <li><a href="https://arxiv.org/abs/1904.08144">(2019) Predicting drug-target interaction using 3D structure-embedded graph representations from graph neural networks</a></li>
  <li><a href="https://www.nature.com/articles/s41570-018-0018-6">(2018) Metal–ligand interactions in drug design</a></li>
  <li><a href="https://www.nature.com/articles/s41467-019-10343-5">(2019) Physically informed artificial neural networks for atomistic modeling of materials</a></li>
  <li><a href="https://arxiv.org/abs/1906.01563">(2019) Hamiltonian Neural Networks</a></li>
  <li><a href="https://deepmind.com/research/publications/Hamiltonian-Generative-Networks">(2019) Hamiltonian Generative Networks</a></li>
  <li><a href="https://deepmind.com/research/publications/Hamiltonian-Graph-Networks-with-ODE-Integrators">(2019) Hamiltonian Graph Networks with ODE Integrators</a></li>
  <li><a href="https://deepmind.com/research/publications/Hamiltonian-descent-for-composite-objectives">(2019) Hamiltonian descent for composite objectives</a></li>
  <li><a href="https://deepmind.com/research/publications/Lagrangian-Neural-Networks">(2020) Lagrangian Neural Networks</a></li>
  <li><a href="https://deepmind.com/research/publications/hamiltonian-descent-methods">(2018) Hamiltonian Descent Methods</a></li>
  <li><a href="https://deepmind.com/research/publications/Equivariant-Hamiltonian-Flows">(2019) Equivariant Hamiltonian Flows</a></li>
  <li><a href="https://link.springer.com/article/10.1208/s12248-017-0092-6">(2017) Large-Scale Prediction of Drug-Target Interaction: a Data-Centric Review</a></li>
  <li><a href="https://www.sciencedirect.com/science/article/pii/S2405844020302899">(2020) FRnet-DTI: Deep convolutional neural network for drug-target interaction prediction</a></li>
  <li><a href="https://www.nature.com/articles/srep11539">(2015) Kinetics of protein-ligand unbinding via smoothed potential molecular dynamics simulations</a></li>
  <li><a href="https://pubs.rsc.org/en/Content/ArticleLanding/2021/CP/D1CP00206F#!divAbstract">(2021) Protein-ligand free energies of binding from full-protein DFT calculations: convergence and choice of exchange-correlation functional</a></li>
  <li><a href="https://www.pnas.org/content/102/19/6825">(2005) Calculation of absolute protein–ligand binding free energy from computer simulations</a></li>
  <li><a href="https://www.nature.com/articles/s41598-020-80769-1">(2021) Automation of absolute protein‑ligand binding free energy calculations for docking refnement and compound evaluation
</a></li>
  <li><a href="https://www.pnas.org/content/105/17/6290">(2008) Calculation of protein–ligand binding free energy by using a polarizable potential</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7369993/">(2020) Absolute Binding Free Energy Calculations for Highly Flexible Protein MDM2 and Its Inhibitors</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3816655/">(2012) Statistical Estimation of the Protein-Ligand Binding Free Energy Based On Direct Protein-Ligand Interaction Obtained by Molecular Dynamics Simulation</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2918242/">(2011) Current Status of the AMOEBA Polarizable Force Field</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5749230/">(2018) A bioinorganic approach to fragment-based drug discovery targeting metalloenzymes</a></li>
  <li><a href="https://www.nature.com/articles/nrd.2017.219">(2017) Mechanistic enzymology in drug discovery: a fresh perspective</a></li>
  <li><a href="http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1415-47572004000400022">(2004) A genetic algorithm for the ligand-protein docking problem</a></li>
  <li><a href="https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/cmdc.201000085">(2010) High-throughput virtual screening using quantum mechanical probes: discovery of selective kinase inhibitors</a></li>
  <li><a href="https://pubmed.ncbi.nlm.nih.gov/15163179/">(2004) The PDBbind database: collection of binding affinities for protein-ligand complexes with known three-dimensional structures</a></li>
  <li><a href="https://pubmed.ncbi.nlm.nih.gov/15943484/">(2005) The PDBbind database: methodologies and updates</a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-pc-en-drug-target-interaction/">Drug-Target Interaction</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-bt-en-bio-databases/">Bio-Databases</a></li>
</ol>
<ul>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-paper-en-mt-dti/">Self-Attention Based Molecule Representation for Predicting Drug-Target Interaction</a></li>
</ul>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-04-03-_BIO-paper-en-pignet.md" target="_blank" style="color:white">Edit</a></span>
</div>
<!-- Bottom Block -->

<!-- Notice
# Mathematical Expression
- outline : $  $
- inline  : $$  $$

# Default Div Tag
- align : left, right, center
- font-size : xx-small, x-small, small, medium, large, x-large, xx-large
- font-weight : normal, bold
- color : red, orange, yellow, green, cyan, blue, purple, pink, white, gray, brown
- background-color : red, orange, yellow, green, cyan, blue, purple, pink, white, gray, brown

# Html Ref
- color code : https://htmlcolorcodes.com/
- tags : https://www.w3schools.com/tags/default.asp
- attributes : https://www.w3schools.com/tags/ref_attributes.asp
Notice -->



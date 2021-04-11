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
[REF|<a href="#REF" style="font-size:xx-small;">2</a>]
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
├── test.py
├── train.py
├── train.sh
└── utils.py
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
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-paper-en-mt-dti/">Self-Attention Based Molecule Representation for Predicting Drug-Target Interaction</a></li>
  <li></li>
</ol>
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



---
title: PIGNet
prev1_title: PAPER REVIEW
prev2_title: Biology
date: 2021-04-03
description: A physics-informed deep learning model toward generalized drug-target interaction predictions
_previous: https://ailever.github.io/education/2020/05/30/Biology/
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
  <li><a href="https://arxiv.org/abs/1904.08144">(2019) Predicting drug-target interaction using 3D structure-embedded graph representations from graph neural networks</a></li>
  <li><a href="https://www.nature.com/articles/s41570-018-0018-6">(2018) Metal–ligand interactions in drug design</a></li>
  <li><a href="https://pubs.acs.org/doi/10.1021/acs.jcim.7b00650">(2018) KDEEP: Protein-Ligand Absolute Binding Affinity Prediction via 3D-Convolutional Neural Networks</a></li>
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
  <li></li>
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



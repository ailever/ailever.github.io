---
title: Drug-Target Interaction
prev1_title: Pharmacology
prev2_title: Biology
date: 2021-04-03
description: Drug-Target Interaction
_previous: https://ailever.github.io/education/2020/05/30/Biology/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Biology.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box"> 
  <button class="top_btn" type="button" onclick="location.href='https://www.accessdata.fda.gov/scripts/cder/daf/'">FDA-Approved Drugs</button>
  <button class="top_btn" type="button" onclick="location.href='https://ccsb.scripps.edu/autodock/'">AutoDock</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Help:Displaying_a_formula'">Latex Formula</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Drug_design'">Drug Design</button>  
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Equilibrium_chemistry'">Equilibrium Chemistry</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Chemical_equilibrium'">Chemical Equilibrium</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Free_energy_perturbation'">Free Energy Perturbation(FEP)</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Molecular_modelling'">Molecular modelling</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Biological_target'">Biological target</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Protein%E2%80%93ligand_complex'">Protein-Ligand Complex</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Protein%E2%80%93ligand_docking'">Protein-ligand docking</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Partition_function_(statistical_mechanics)'">Partition Function</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Ligand_(biochemistry)'">Ligand</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Umbrella_sampling'">Umbrella sampling</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Thermodynamic_integration'">Thermodynamic integration</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Bennett_acceptance_ratio'">Bennett acceptance ratio</button>
</div>
<!-- Top Block -->

## Set of small-molecule chemicals found within a biological sample
- Genome(DNA) > Transcriptome(RNA) > Proteome(Proteins) > Metabolome(Metabolities) > Phenome(Metabolic syndorme, Psychiatric disease)
![image](https://user-images.githubusercontent.com/52376448/113499702-02661200-9553-11eb-9371-c4d0237aff4c.png)

### Network Analysis
- (Based on Omics) Genomics, Transcriptomics, Proteomics, Lipidomics, Metabolomics

### Scaling Analysis

<br><br><br>
## Open Databases for Drug Development
- KEGG(Kyoto Encyclopedia of Genes and Genomes)
- CTD(Comperative toxicogenomics)
- ChEMBL(Chemical European Molecular Biology Laborotory)


<br><br><br>
## Drug Development Process
- Target Discovery
  - Expression analysis
  - in-vitro function, in-vivo validation(knockout)
  - Bioinformatics
- Discovery & Screening
  - Discovery : Structural drug desgin
  - Screening : In-vitro, Ex&In-vivo
- Lead Optimization
  - Traditional medicinal chemistry
  - Retional drug desgin
- ADMET
  - BA
  - Systemic exposure
  - Characteristic for ADMET
- Development
  - Clinic Phase
- Registration
  - MFDS
  - FDA
  - EMA
- Market

### Cost of Target Discovery
Drug > Target(Therapeutic Effect), off-Target(Side Effect)

### Drug-Target Network
- **Drug, Target, Disease, Gene**
- Interaction Type
  - Drug-Target, Drug-Drug, Target-Gene, Disease-Disease, Drug-Disease, ... 

### CADD : Computer-Aided Drug Discovery
- SBDD, Structure-based drug design(Direct drug design) : Molecular docking
- LBDD, Ligand-based drug design(Indirect drug design) : Quantitative structure-activity relationship (QSAR)


<br><br><br>
## Molecular Binding under Statistical Thermodynamic Perspective
### Definition of Free Energy
[REF|<a href="#REF" style="font-size:xx-small;">5, Calculation of Binding Free Energies</a>]
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Gibbs free energy gradient acts as a driving force for a biological system.
$$\begin{align*}
F &= U-TS = -\frac{1}{\beta}\ln{Q(N,V,T)} \\
G &= H-TS = -\frac{1}{\beta}\ln{Q(N,P,T)} \\
\end{align*}$$
<br><br></div>

### The free energy perturbation (FEP)
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\Delta G_{bind} = -\frac{1}{\beta} \ln{\frac{Q_{B}}{Q_{A}}} = - \frac{1}{\beta} \ln{\left \langle e^{-\beta(H_{B}-H_{A})} \right \rangle_{A}}$$
<br><br></div>

### Bennet’s Acceptance Ratio (BAR) 
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
From end state equilibrium sampling  
$$\Delta G_{bind} = \frac{1}{\beta} \frac{\left <f(H_{A}-H_{B}+C)\right >_{B}}{\left <f(H_{B}-H_{A}-C) \right >_{A}} + C$$
$$f(x)=\frac{1}{1+e^{\beta x}},\quad C=\frac{1}{\beta}\ln{\frac{Q_{A}}{Q_{B}}\frac{n_{B}}{n_{A}}}$$
<br><br></div>

### Thermodynamic integration (TI)
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Alchemical transition
$$\Delta G_{bind} = \int_{0}^{1} \left \langle \frac{\partial H}{\partial \lambda} \right \rangle_{\lambda}\, d\lambda$$

<br><br></div>

### The Quasi-Harmonic Approximation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\begin{align*}
  \Delta G_{bind} & = -k_{B}T \ln \frac{K}{V_{ref}} \\
  & = k_{B}T \ln {(8\pi^{2} V_{ref})} - k_{B}T \ln {\int {H(\mathbf{r},\boldsymbol{\Omega})e^{-\beta \omega(\mathbf{r},\boldsymbol{\Omega})}}\, d\mathbf{r}d\boldsymbol{\Omega}} \\
  & = k_{B}T \ln {(8\pi^{2} V_{ref}) + \omega_{min}-\frac{k_{B}T}{2} \ln{((2\pi)^{6}\det{C_{\mathbf{r}, \boldsymbol{\Omega}}}})} \\
\end{align*}$$
- $\Delta G_{bind}$ : Absolute binding free energy<br>
- $k_{B}$ : Boltzmann constant<br>
- $T$ : Absolute temperature<br>
- $V_{ref}$ : Reference volume in units consistent<br>
- $\beta=\frac{1}{k_{B}T}$<br>
- $\mathbf{r}, \boldsymbol{\Omega}$ : Relative position, orientation<br>
- $H$ : Ensemble average
- $C_{\mathbf{r}, \boldsymbol{\Omega}}$: 6 by 6 fluctuation covariance matrix of the three positional and three orientation coordinates
<br><br></div>


### Free Energy Caluations for Lead Optimization
[REF|<a href="#REF" style="font-size:xx-small;">Free-energy calculations in structure-based drug design</a>]
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$ L+R \rightleftharpoons C $$
$$\Delta F^{0}_{bind} = - RT \ln{K^{0}_{A}}$$
$$K^{0}_{A}=\frac{1}{K^{0}_{D}}=\frac{k_{on}}{k_{off}}=\frac{[C]}{[L][R]}$$
<br></div>


Soft-core potential[REF|<a href="#REF" style="font-size:xx-small;">Soft-Core Potentials in Thermodynamic Integration. Comparing One- and Two-Step Transformations</a>]
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$V_{ij} = 4\epsilon_{ij}(1-\lambda)^{t} ([\alpha_{LJ}\lambda^{s} + (r_{ij}/\sigma_{ij})^{n}]^{-12/n} - [\alpha_{LJ}\lambda^{s}+(r_{ij}/\sigma_{ij})^{n}]^{-6/n})$$
<br><br></div>

### IC50
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$IC_{50} = K^{I}_{D} \left ( 1 + \frac{[L_{0}]}{D^{L}_{D}} \right )$$  
<br><br></div>

### Binding Affinity Prediction
#### Experimental Approach
- NMR Methods for the Determination of Protein–Ligand Interactions
  - Detection and Verification of Ligand Binding
  - Interaction Site Mapping
  - Interaction Models and Binding Affinity
  - Molecular Recognition
  - Structure of Protein–Ligand Complexes

#### Theoretical Approach
- MM/PBSA : the molecule mechanics/Poisson–Boltzmann surface area 
- MM/GBSA : the molecule mechanics/generalized Born surface area
- LIE : Linear Interaction Methods
- Fragmentation Methods
  - the fragment molecular orbital (FMO) method
  - the polarized continuum model (PCM)
  - Poisson–Boltzmann (PB) solvation
  - the electrostatically embedded pairwise additive (EE-PA) model
  - the molecular fractionation with conjugate caps (MFCC) method
  - the electrostatically embedded generalized MFCC (EE-GMFCC)
  - the polarizable multipole interaction with supermolecular pairs (PMISP) method
![image](https://user-images.githubusercontent.com/52376448/114173211-c1fefd80-9971-11eb-9243-3b2f4a7de178.png)
[REF|<a href="#REF" style="font-size:xx-small;">Ligand-Binding Affinity Estimates Supported by Quantum-Mechanical Methods</a>]
- The QM-cluster approach
- Continuum-Solvation Methods


#### Emprical Approach


<br><br><br>
## Protein-Ligand Interaction
### Design Considerations
- Molecular Docking
  - Flexible docking / Rigid docking
  - Scoring Function
    - Force Field
    - Empirical scoring
      - solvent accessible surface area (SASA) value
    - Knowledge-Based scoring
  - Search Algorithm
    - Lamarckian Genetic Algorithm
    - Shape Matching
    - Evoluationary Optimization
    - Genetic Algorithm
    - Hybrid
    - Local Optimization
    - Simulated Annealing
    - Swarm-Intelligence Algorithm
- Binding Site and Molecular Interactions
  - protein–protein binding site
  - protein–nucleic acid binding site
  - protein–carbohydrate binding site
  - protein–lipid binding site
  - protein–small molecule binding site

### Thermodynamic cycle scheme for the confine-and-release by lock and key model
![image](https://user-images.githubusercontent.com/52376448/113856529-559ec580-97dc-11eb-92a7-06f6adae978d.png)
[REF|<a href="#REF" style="font-size:xx-small;">The Confine-and-Release Method: Obtaining Correct Binding Free Energies in the Presence of Protein Conformational Change</a>]

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\Delta G^{o}_{bind} = \Delta G_{conf} + \Delta G^{o}_{bind,C} + \Delta G_{rel}$$
- $\Delta G^{o}_{bind}$ : the true (standard) binding free energy <br>
- $\Delta G_{conf}$ : the free energy of confining the protein to this smaller region of configuration space in the unbound state <br> 
- $\Delta G^{o}_{bind,C}$ : the standard binding free energy of the ligand to the confined protein <br> 
- $\Delta G_{rel}$ : the free energy of releasing the protein from conformational confinement in the bound state <br> 
<br><br></div>

### G protein-coupled receptor

### Protein-Ligand Complex
- VDW interaction
- hydrogen bond interaction
- metal-ligand interaction
- hydrophobic interaction

<br><br><br>
### Evaluation Metric
- scoring power, ranking power, docking power, screening power

<br><br><br>
### Popular docking programs for DTI predictions
- X-Score10, AutoDock Vina8, ChemPLP@GOLD15, GlideScore



<br><br><br>
## Druggability Prediction



## Additionals
Big Firm in Pharmaceutical Industry
- Johnson & Johnson
- Pfizer
- Santen
- Merck
- Novartis


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
  <li><a href="https://en.wikipedia.org/wiki/List_of_protein-ligand_docking_software">List of protein-ligand docking software</a></li>  
  <li><a href="https://www.youtube.com/watch?v=2ewpDYW081Y">AutoDock Vina Installation (Tutorial)</a></li>
  <li><a href="https://m.ibric.org/trend/news/?listmode=publish&listmode2=publisher&PARA3=21">Computational Chemistry</a></li>
  <li><a href="https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Book%3A_Statistical_Thermodynamics_(Jeschke)/05%3A_Entropy/5.02%3A_The_Relation_of_State_Functions_to_the_Partition_Function">The Relation of State Functions to the Partition Function</a></li>
  <li><a href="https://scholar.harvard.edu/files/schwartz/files/8-freeenergy.pdf">Lecture 8: Free energy</a></li>
  <li><a href="https://www.cambridgemedchemconsulting.com/resources/">Cambridge MedChem Consulting</a></li>
  <li><a href="https://www.rcsb.org/pages/search_features">RCSB PDB Search</a></li>
</ol>
<ul>
  <li><a href="https://www.nature.com/articles/s41586-019-1923-7?fbclid=IwAR3k8qrx_q1mVDUFd_IF0RuVV9yfUVv30x-oYenFfiaqd8DtOdFdycZrnz8">(2020) Improved protein structure prediction using potentials from deep learning</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4783878/">(2016) Insights into Protein–Ligand Interactions: Mechanisms, Models, and Methods</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5749230/">(2018) A bioinorganic approach to fragment-based drug discovery targeting metalloenzymes</a></li>
  <li><a href="https://www.nature.com/articles/nrd.2017.219">(2017) Mechanistic enzymology in drug discovery: a fresh perspective</a></li>
  <li><a href="http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1415-47572004000400022">(2004) A genetic algorithm for the ligand-protein docking problem</a></li>
  <li><a href="https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/cmdc.201000085">(2010) High-throughput virtual screening using quantum mechanical probes: discovery of selective kinase inhibitors</a></li>
  <li><a href="https://link.springer.com/article/10.1007/s00214-012-1272-1">(2012) Binding free energy, energy and entropy calculations using simple model systems</a></li>
  <li><a href="https://pubmed.ncbi.nlm.nih.gov/25330964/">(2015) Calculation of Binding Free Energies</a></li>  
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7369993/">(2020) Absolute Binding Free Energy Calculations for Highly Flexible Protein MDM2 and Its Inhibitors</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4700411/">(2015) Accurate calculation of the absolute free energy of binding for drug molecules</a></li>
  <li><a href="https://dasher.wustl.edu/chem478/reading/free-energy-shirts.pdf">(2010) Free-energy calculations in structure-based drug design</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2562444/">(2007) The Confine-and-Release Method: Obtaining Correct Binding Free Energies in the Presence of Protein Conformational Change</a></li>
  <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187911/">(2011) Soft-Core Potentials in Thermodynamic Integration. Comparing One- and Two-Step Transformations</a></li>
  <li><a href="https://pubs.acs.org/doi/10.1021/acs.chemrev.5b00630">(2016) Ligand-Binding Affinity Estimates Supported by Quantum-Mechanical Methods</a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-ab-initio-methods/">Ab initio methods</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-density-functional-theory/">Density Functional Theory</a></li>  
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-molecular-mechanics-and-dynamics/">Molecular Mechanics and Dynamics</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-qm-mm/">QM/MM : Quantum Mechanics/Molecular Mechanics</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-prt-en-protein-structure/">Protein Structure</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-prt-en-protein-structure-prediction/">Protein Structure Prediction</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-prt-en-enzyme-catalysis/">Enzyme Catalysis</a></li>
</ol>
<ul>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-paper-en-pignet/">PIGNet: A physics-informed deep learning model toward generalized drug-target interaction predictions</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-paper-en-mt-dti/">Self-Attention Based Molecule Representation for Predicting Drug-Target Interaction</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-paper-en-new/">NEW</a></li>
</ul>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-04-03-_BIO-pc-en-drug-target-interaction.md" target="_blank" style="color:white">Edit</a></span>
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



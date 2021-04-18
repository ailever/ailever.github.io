---
title: Bio-Databases
prev1_title: Biotechnology
prev2_title: Biology
date: 2021-04-03
description: Bio-Databases
_previous: https://ailever.github.io/education/2020/05/30/Biology/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Biology.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/List_of_biological_databases'">List of biological databases</button>
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->


## Nucleic acid databases

<br><br><br>
## Amino acid / protein databases
### Protein Data Bank (PDB)
- [PDBbind-download](http://www.pdbbind-cn.org/download.php)
- [RCSB-stats](https://www.rcsb.org/stats/summary)
- [scPDB](http://bioinfo-pharma.u-strasbg.fr/scPDB/) : binding site database
- [Introduction to Protein Data Bank Format](https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html)
<pre class="code-path">
├── PDBbind_2019_plain_text_index.tar.gz
└── plain-text-index
    ├── index
    │   ├── 2019_index.lst
    │   ├── INDEX_general_NL.2019
    │   ├── INDEX_general_PL.2019
    │   ├── INDEX_general_PL_data.2019
    │   ├── INDEX_general_PL_name.2019
    │   ├── INDEX_general_PN.2019
    │   ├── INDEX_general_PP.2019
    │   ├── INDEX_refined_data.2019
    │   ├── INDEX_refined_name.2019
    │   ├── INDEX_refined_set.2019
    │   └── INDEX_structure.2019
    └── readme
        ├── PDBbind-101.txt
        └── pdbbind_2019_intro.pdf
</pre>
<details markdown="1">
  <summary align="center">2019_index.lst</summary>
<code class="code-title">2019_index.lst</code><br>
<pre class="sudo-code">
1chg  2.50  1976  0.430  -1.000  -1.000
155c  2.50  1976 -1.000  -1.000  -1.000
1cyc  2.30  1976 -1.000  -1.000  -1.000
1est  2.50  1976 -1.000  -1.000  -1.000
1fdh  2.50  1976 -1.000  -1.000  -1.000
1hip  2.00  1976 -1.000  -1.000  -1.000
1mbn  2.00  1976 -1.000  -1.000  -1.000
1rei  2.00  1976 -1.000  -1.000  -1.000
1srx  2.80  1976 -1.000  -1.000  -1.000
1tim  2.50  1976 -1.000  -1.000  -1.000
2pgk  3.00  1976 -1.000  -1.000  -1.000
2sbt  2.80  1976 -1.000  -1.000  -1.000
3cna  2.40  1976 -1.000  -1.000  -1.000
2pab  1.80  1977  0.290  -1.000  -1.000
1cpb  2.80  1977 -1.000  -1.000  -1.000
1gcn  3.00  1977 -1.000  -1.000  -1.000
1gpd  2.90  1977 -1.000  -1.000  -1.000
1lyz  2.00  1977 -1.000  -1.000  -1.000
1pad  2.80  1977 -1.000  -1.000  -1.000
1pgi  3.50  1977 -1.000  -1.000  -1.000
1sbt  2.50  1977 -1.000  -1.000  -1.000
2cha  2.00  1977 -1.000  -1.000  -1.000
2cna  2.00  1977 -1.000  -1.000  -1.000
2dhb  2.80  1977 -1.000  -1.000  -1.000
2lyz  2.00  1977 -1.000  -1.000  -1.000
2pad  2.80  1977 -1.000  -1.000  -1.000
3ldh  3.00  1977 -1.000  -1.000  -1.000
3lyz  2.00  1977 -1.000  -1.000  -1.000
4lyz  2.00  1977 -1.000  -1.000  -1.000
4pad  2.80  1977 -1.000  -1.000  -1.000
...
...
...
</pre>
</details>



<details markdown="1">
  <summary align="center">INDEX_general_PL.2019</summary>
<code class="code-title">INDEX_general_PL.2019</code><br>
<pre class="sudo-code">
# ==============================================================================
# List of protein-ligand complexes with known binding data in PDBbind v.2019
# 17679 protein-ligand complexes in total, sorted by their release year.
# Latest update: Dec 2019
# PDB code, resolution, release year, binding data, reference, ligand name
# ==============================================================================
2tpi  2.10  1982  Kd=49uM       // 2tpi.pdf (2-mer)
4cpa  2.50  1982  Kd=5nM        // 4cpa.pdf (GLY)
5tln  2.30  1982  Ki=0.43uM     // 5tln.pdf (BAN) incomplete ligand structure
4tln  2.30  1982  Ki=190uM      // 4tln.pdf (LNO)
4cts  2.90  1984  Kd<10uM       // 4cts.pdf (OAA)
6rsa   NMR  1986  Ki=40uM       // 6rsa.pdf (UVC)
1rnt  1.90  1987  Kd=6.5uM      // 1rnt.pdf (2GP)
6cha  1.80  1987  Ki=40uM       // 6cha.pdf (PBA) covalent complex
4ts1  2.50  1989  Kd=11.6uM     // 4ts1.pdf (TYR)
4tmn  1.70  1989  Ki=0.068nM    // 4tmn.pdf (0PK)
2tmn  1.60  1989  Ki=1.3uM      // 2tmn.pdf (0FA)
1tlp  2.30  1989  Ki=28nM       // 1tlp.pdf (RDF)
1tmn  1.90  1989  Ki=50nM       // 1tmn.pdf (0ZN)
5tmn  1.60  1989  Ki=9.1nM      // 5tmn.pdf (0PJ)
4fab  2.70  1990  Kd=8.8nM      // 4fab.pdf (FLU)
1p01  2.00  1990  Ki=0.35nM     // 1p01.pdf (0EG) covalent complex
3at1  2.80  1990  Ki=0.66mM     // 3at1.pdf (PCT)
1p05  2.10  1990  Ki=1100nM     // 1p05.pdf (5-mer) incomplete ligand structure
1p10  2.25  1990  Ki=200nM      // 1p10.pdf (5-mer) incomplete ligand structure
6gch  2.10  1990  Ki=20uM       // 6gch.pdf (APF) covalent complex
7gch  1.80  1990  Ki=2uM        // 7gch.pdf (LPF) covalent complex
1p04  2.55  1990  Ki=40nM       // 1p04.pdf (5-mer) incomplete ligand structure
1p06  2.34  1990  Ki=540nM      // 1p06.pdf (5-mer) incomplete ligand structure
1p03  2.15  1990  Ki=6.4nM      // 1p03.pdf (5-mer) incomplete ligand structure
...
...
...
</pre>
</details>


<details markdown="1">
  <summary align="center">INDEX_general_PL_data.2019</summary>
<code class="code-title">INDEX_general_PL_data.2019</code><br>
<pre class="sudo-code">
# ==============================================================================
# List of protein-ligand complexes with known binding data in PDBbind v.2019
# 17679 protein-ligand complexes in total, sorted by binding data
# Latest update: Dec 2019
# PDB code, resolution, release year, -logKd/Ki, Kd/Ki, reference, ligand name
# ==============================================================================
3zzf  2.20  2012   0.40  Ki=400mM      // 3zzf.pdf (NLG)
3gww  2.46  2009   0.45  IC50=355mM    // 3gwu.pdf (SFX)
1w8l  1.80  2004   0.49  Ki=320mM      // 1w8l.pdf (1P3)
3fqa  2.35  2009   0.49  IC50=320mM    // 3fq7.pdf (GAB&PMP)
1zsb  2.00  1996   0.60  Kd=250mM      // 1zsb.pdf (AZM)
4obv  2.84  2014   0.75  Ki=178mM      // 4obv.pdf (2SU)
1wkm  2.30  2005   0.82  Ki=150mM      // 1wkm.pdf (MET)
3k41  1.90  2009   0.82  Kd=150mM      // 3k41.pdf (M6D)
4eu3  1.58  2012   0.82  Ki=150mM      // 4eu3.pdf (CIT)
2w97  2.29  2010   0.96  Kd=110mM      // 2w97.pdf (GOL)
1p0y  2.55  2003   1.00  Ki=100.8mM    // 1p0y.pdf (MLZ)
2b1r  2.20  2006   1.00  Ki=101mM      // 2b1q.pdf (CBI)
2d2v  2.50  2006   1.00  Ki=100mM      // 2b1q.pdf (MAL)
1aw1  2.70  1998   1.05  Ki=89mM       // 1aw1.pdf (PGA)
1maw  3.00  2003   1.10  Kd=80mM       // 1maw.pdf (ATP)
3fl9  2.40  2009   1.11  IC50=77.2mM   // 3fl8.pdf (TOP)
5eb2  2.71  2016   1.11  Kd=76.9mM     // 5eb1.pdf (TRP)
4lh2  1.67  2013   1.24  Ki=58mM       // 4lh2.pdf (SIN)
4to8  2.10  2014   1.24  IC50=56.9mM   // 4to8.pdf (FLC)
4fci  1.82  2012   1.26  Ki~55mM       // 4fci.pdf (GPA)
4fck  1.90  2012   1.26  Ki~55mM       // 4fci.pdf (GPA)
4clp  1.90  2014   1.27  Kd=54.2mM     // 4clk.pdf (CMP)
1f9g  2.00  2001   1.28  Ki=53mM       // 1f9g.pdf (ASC)
1a0t  2.40  1998   1.30  Kd=50mM       // 1a0t.pdf (SUC)
...
...
...
</pre>
</details>


<details markdown="1">
  <summary align="center">INDEX_general_PL_name.2019</summary>
<code class="code-title">INDEX_general_PL_name.2019</code><br>
<pre class="sudo-code">
# ==============================================================================
# List of protein-ligand complexes with known binding data in PDBbind v.2019
# 17679 complexes in total, clustered by 95% protein sequence similarity
# latest update: Dec 2019
# PDB code, release year, Uniprot ID, protein name
# ==============================================================================
6mu1  2018  P29994  INOSITOL 1,4,5-TRISPHOSPHATE RECEPTOR TYPE 1
3t8s  2011  P29994  INOSITOL 1,4,5-TRISPHOSPHATE RECEPTOR TYPE 1
1n4k  2002  P11881  INOSITOL 1,4,5-TRISPHOSPHATE RECEPTOR TYPE 1
5urm  2017  O75643  U5 SMALL NUCLEAR RIBONUCLEOPROTEIN 200 KDA HELICASE
5urj  2017  O75643  U5 SMALL NUCLEAR RIBONUCLEOPROTEIN 200 KDA HELICASE
5urk  2017  O75643  U5 SMALL NUCLEAR RIBONUCLEOPROTEIN 200 KDA HELICASE
3eql  2008  Q9Z9H6  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
1zyr  2005  Q5SHR6  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
3dxj  2008  Q5SHR6  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
5uah  2017  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
5ual  2017  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4zh4  2015  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4zh3  2015  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4zh2  2015  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4xsx  2015  A7ZSI4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4xsy  2015  A7ZSI4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4xsz  2015  A7ZSI4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4mex  2014  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4kn4  2013  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4kn7  2013  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
4kmu  2013  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
5uac  2017  P0A7Z4  DNA-DIRECTED RNA POLYMERASE SUBUNIT ALPHA
5swg  2017  P42336  PHOSPHATIDYLINOSITOL 4,5-BISPHOSPHATE 3-KINASE
5sxk  2017  P42336  PHOSPHATIDYLINOSITOL 4,5-BISPHOSPHATE 3-KINASE
...
...
...
</pre>
</details>


<details markdown="1">
  <summary align="center">INDEX_refined_data.2019</summary>
<code class="code-title">INDEX_refined_data.2019</code><br>
<pre class="sudo-code">
# ==============================================================================
# List of the protein-ligand complexes in the PDBbind refined set v.2019
# 4,852 protein-ligand complexes in total, which are ranked by binding data
# Latest update: Dec 2019
# PDB code, resolution, release year, -logKd/Ki, Kd/Ki, reference, ligand name
# ==============================================================================
2r58  2.00  2007   2.00  Kd=10mM       // 2r58.pdf (MLY)
3c2f  2.35  2008   2.00  Kd=10.1mM     // 3c2f.pdf (PRP)
3g2y  1.31  2009   2.00  Ki=10mM       // 3g2y.pdf (GF4)
3pce  2.06  1998   2.00  Ki=10mM       // 3pce.pdf (3HP)
4qsu  1.90  2014   2.00  Kd=10mM       // 4qsu.pdf (TDR)
4qsv  1.90  2014   2.00  Kd=10mM       // 4qsv.pdf (THM)
4u54  2.41  2015   2.06  Kd=8.7mM      // 4u54.pdf (3C5)
3ao4  1.95  2011   2.07  Kd=8.5mM      // 3ao1.pdf (833)
4cs9  2.01  2014   2.10  Kd=8mM        // 4cs8.pdf (AMP)
2w8w  2.14  2009   2.12  Kd=7.5mM      // 2w8j.pdf (PLS)
3gv9  1.80  2009   2.12  Ki=7.5mM      // 3gqz.pdf (GV9)
4q90  1.54  2015   2.15  Ki=7.0mM      // 4q7p.pdf (4H2)
5cs3  2.50  2015   2.15  Kd=7.0mM      // 5cs3.pdf (EP1)
4tim  2.40  1992   2.16  Ki=6.9mM      // 4tim.pdf (2PG)
5fe6  1.77  2016   2.16  Kd=6910uM     // 5fdz.pdf (5WZ)
6ghj  2.26  2018   2.16  Kd=6.89mM     // 6ghj.pdf (3-mer)
3gqz  1.80  2009   2.17  Ki=6.7mM      // 3gqz.pdf (GF7)
4y3j  1.31  2016   2.17  Kd=6.8mM      // 4y38.pdf (HIC)
5oxk  2.38  2018   2.17  Kd=6.82mM     // 5oxk.pdf (2-mer)
5z5f  2.10  2018   2.17  Ki=6.8mM      // 5z5f.pdf (FUB)
4ahr  1.90  2012   2.19  Kd=6.5mM      // 3vq4.pdf (I2E)
4ahs  1.75  2012   2.19  Kd=6.4mM      // 3vq4.pdf (AKH)
4mre  1.58  2014   2.19  Kd=6.4mM      // 4mrd.pdf (2C9)
1x8d  1.80  2005   2.21  Kd=6.16mM     // 1x8d.pdf (RNS)
...
...
...
</pre>
</details>


<details markdown="1">
  <summary align="center">INDEX_refined_name.2019</summary>
<code class="code-title">INDEX_refined_name.2019</code>
<pre class="sudo-code">
# ==============================================================================
# List of protein-ligand complexes in the PDBbind refined set v.2019
# 4,852 complexes in total, clustered by 90% protein sequence similarity
# latest update: Dec 2019
# PDB code, release year, Uniprot ID, protein name
# ==============================================================================
1n4k  2002  P11881  INOSITOL 1,4,5-TRISPHOSPHATE RECEPTOR TYPE 1
5uk8  2017  P42336  PHOSPHATIDYLINOSITOL 4,5-BISPHOSPHATE 3-KINASE
5dxt  2016  P42336  PHOSPHATIDYLINOSITOL 4,5-BISPHOSPHATE 3-KINASE
1i1e  2001  P10844  BOTULINUM NEUROTOXIN TYPE B
1bxr  1999  P00968  CARBAMOYL-PHOSPHATE SYNTHASE
3i3b  2010  B8LFD6  BETA-GALACTOSIDASE
3dyo  2008  P00722  BETA-GALACTOSIDASE
3t0d  2012  P00722  BETA-GALACTOSIDASE
3vdb  2012  P00722  BETA-GALACTOSIDASE
3t08  2012  P00722  BETA-GALACTOSIDASE
1px4  2004  P00722  BETA-GALACTOSIDASE
3muz  2011  B8LFD6  BETA-GALACTOSIDASE
3t2q  2012  P00722  BETA-GALACTOSIDASE
3t09  2012  P00722  BETA-GALACTOSIDASE
3mv0  2011  B8LFD6  BETA-GALACTOSIDASE
3vd9  2012  P00722  BETA-GALACTOSIDASE
3t0b  2012  P00722  BETA-GALACTOSIDASE
3vd4  2012  P00722  BETA-GALACTOSIDASE
1ps3  2003  Q24451  ALPHA-MANNOSIDASE II
3d52  2008  Q24451  ALPHA-MANNOSIDASE II
3dx1  2009  Q24451  ALPHA-MANNOSIDASE II
3d51  2008  Q24451  ALPHA-MANNOSIDASE II
3ddf  2008  Q24451  ALPHA-MANNOSIDASE II
3d50  2008  Q24451  ALPHA-MANNOSIDASE II
...
...
...
</pre>
</details>


<details markdown="1">
  <summary align="center">INDEX_refined_set.2019</summary>
<code class="code-title">INDEX_refined_set.2019</code><br>
<pre class="sudo-code">
# ==============================================================================
# List of protein-ligand complexes in the PDBbind refined set v.2019
# 4,852 protein-ligand complexes in total, sorted by their release year.
# Latest update: Dec 2019
# PDB code, resolution, release year, binding data, reference, ligand name
# ==============================================================================
2tpi  2.10  1982  Kd=49uM       // 2tpi.pdf (2-mer)
4tln  2.30  1982  Ki=190uM      // 4tln.pdf (LNO)
1rnt  1.90  1987  Kd=6.5uM      // 1rnt.pdf (2GP)
4ts1  2.50  1989  Kd=11.6uM     // 4ts1.pdf (TYR)
4tmn  1.70  1989  Ki=0.068nM    // 4tmn.pdf (0PK)
2tmn  1.60  1989  Ki=1.3uM      // 2tmn.pdf (0FA)
1tlp  2.30  1989  Ki=28nM       // 1tlp.pdf (RDF)
1tmn  1.90  1989  Ki=50nM       // 1tmn.pdf (0ZN)
5tmn  1.60  1989  Ki=9.1nM      // 5tmn.pdf (0PJ)
1rbp  2.00  1991  Kd=0.19uM     // 1rbp.pdf (RTL)
1fkf  1.70  1991  Kd=0.4nM      // 1fkf.pdf (FK5)
4er1  2.00  1991  Ki=0.242uM    // 4er1.pdf (0ZP)
5er2  1.80  1991  Ki=0.27uM     // 5er2.pdf (0EK)
4er2  2.00  1991  Ki=0.5nM      // 4er2.pdf (6-mer)
2ypi  2.50  1991  Ki=15uM       // 2ypi.pdf (PGA)
6cpa  2.00  1991  Ki=3pM        // 6cpa.pdf (ZAF)
4sga  1.80  1991  Ki=50nM       // 4sga.pdf (5-mer)
5er1  2.00  1991  Ki=960nM      // 5er1.pdf (0HT)
4tim  2.40  1992  Ki=6.9mM      // 4tim.pdf (2PG)
1igj  2.50  1993  Kd=0.1nM      // 1igj.pdf (DGX)
1fkb  1.70  1993  Kd=0.2nM      // 1fkb.pdf (RAP)
1l83  1.70  1993  Kd=0.40mM     // 1l83.pdf (BNZ)
1atr  2.34  1993  Kd=110nM      // 1atr.pdf (ADP)
6rnt  1.80  1993  Kd=4.3mM      // 6rnt.pdf (2AM)
...
...
...
</pre>
</details>


<details markdown="1">
  <summary align="center">INDEX_structure.2019</summary>
<code class="code-title">INDEX_structure.2019</code><br>
<pre class="sudo-code">
4tln  2.30  1982  0.169  -1.000  -1.000
5tln  2.30  1982  0.179  -1.000  -1.000
2tpi  2.10  1982  0.200  -1.000  -1.000
4cts  2.90  1984  0.182  -1.000  -1.000
6rsa   NMR  1986 -1.000  -1.000  -1.000
1rnt  1.90  1987  0.191  -1.000  -1.000
6cha  1.80  1987  0.200  -1.000  -1.000
4tmn  1.70  1989  0.170  -1.000  -1.000
1tmn  1.90  1989  0.171  -1.000  -1.000
1tlp  2.30  1989  0.174  -1.000  -1.000
5tmn  1.60  1989  0.177  -1.000  -1.000
2tmn  1.60  1989  0.179  -1.000  -1.000
4ts1  2.50  1989  0.187  -1.000  -1.000
1p04  2.55  1990  0.134  -1.000  -1.000
1p01  2.00  1990  0.138  -1.000  -1.000
1p05  2.10  1990  0.139  -1.000  -1.000
1p06  2.34  1990  0.140  -1.000  -1.000
1p03  2.15  1990  0.142  -1.000  -1.000
1p10  2.25  1990  0.144  -1.000  -1.000
1p02  2.00  1990  0.147  -1.000  -1.000
6gch  2.10  1990  0.180  -1.000  -1.000
3at1  2.80  1990  0.181  -1.000  -1.000
7gch  1.80  1990  0.190  -1.000  -1.000
4fab  2.70  1990  0.215  -1.000  -1.000
4sga  1.80  1991  0.116  -1.000  -1.000
4er1  2.00  1991  0.143  -1.000  -1.000
5apr  2.10  1991  0.144  -1.000  -1.000
6apr  2.50  1991  0.149  -1.000  -1.000
3er5  1.80  1991  0.150  -1.000  -1.000
4apr  2.50  1991  0.154  -1.000  -1.000
...
...
...
</pre>
</details>



<br><br><br>
## Signal transduction pathway databases

<br><br><br>
## Metabolic pathway and protein function databases

<br><br><br>
## Additional databases
- PubChem database
  - SMILES sequence
- DrugBank database
- ZINC database
- BindingDB database
- Drug Target Common database
- Touchstone database
- Connectivity Map (CMap) database
- Drug screening database




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
  <li><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ol>
<ul>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ol>
<ul>
  <li><a href="https://ailever.github.io/education/2021/04/03/_BIO-paper-en-pignet/">PIGNet: A physics-informed deep learning model toward generalized drug-target interaction predictions</a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ul>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-04-03-_BIO-bt-en-bio-databases.md" target="_blank" style="color:white">Edit</a></span>
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



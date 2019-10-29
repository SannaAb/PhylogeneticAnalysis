# PhylogeneticAnalysis

Runs the phylogenetic analysis using Phylip, 

First step is to run the multiple alignment of the sequences of interest. Use the code below for this, using muscle alignment


```

```

When you have a multiple alignment that you are satisfied with you use it as an input into the script PhylogeneticTreeusingPhylip.py 
Important is that you have the emboss environment installed using coda. The script runs in python2.7

* Seqboot 1000 trees
* dnadist 
* neighbour 
* consense 
* dnapars
* consense


```

~/.conda/envs/EMBOSS/bin/python /home/xabras/Scripts/Phylo_analysis/PhylogeneticTreesusingPhylip.py Aureus.phyi 

```

### Plotting 

Plotting is run seperately as cannot open X11 on the nodes 


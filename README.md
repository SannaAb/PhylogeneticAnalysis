# Phylogenetic Analysis

Runs the phylogenetic analysis using Phylip, 

First step is to run the multiple alignment of the sequences of interest. Use the code below for this, using muscle alignment


```

~/Programs/Muscle/muscle3.8.31_i86linux32 -in Epidermidis_All.fasta -out Epidermidis -phyiout Epidermidis.phyi  -physout Epidermidis.phys

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


### 

Adding the branch length, 
There is an issue of adding the branch length to the consensus seperately. There is an issue in fdnaml so for some reason it removes some samples. Therefore we use dnaml seperately. Just type dnaml,input the original alignment from muscle, and change U. Then create the outtree which now contains branch length. 



### Plotting 

Plotting is run seperately as cannot open X11 on the nodes 
Input is the tree output from the previous script


```

~/.conda/envs/EMBOSS/bin/python /home/xabras/Scripts/Phylo_analysis/Plotting_PhylipOut.py Epidermidis.consensus_Neighbour.tree

```


# Distance matrix 

It might be of interest to check the distance between the different sequences. For this we can use the distance matrix based on identity. so if we have 1 change in one sequence the distance between the two sequences will be 1/10. 
The following script calculates the distance between multiple sequences from the phyi format. Output is the lower triangle distance matrix and a heatmap that plots this distance matrix. 0 means ofcourse no change. You might need the Correct conda environment for the packages 

Run it as follows 


```

# important as the input filenames ends with phyi as we are using the prefix of this string

python DistanceMatrix_fromPhylipMA.py in.phyi 

```

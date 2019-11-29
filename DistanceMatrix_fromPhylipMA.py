#!/usr/bin/py 

# This script calculates the distance matrix from a phyllip input
# The phyllip file is from the muscle alignment 


from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
import sys

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np


# Run like pythonn DistanceMatrix_fromPhylipMA.py file.phyi

def readphylipfile():
    """
    This reads the input phylip file, in this case the alignmentfile was created using muscle 
    """
    #phylipfile = "/jumbo/WorkingDir/B19-057/Data/Meta/Phylo/Aureus/MA/Aureus.phyi"
    phylipfile = sys.argv[1] # first user input is the phylip I file
    outbase = phylipfile.split("/")[-1].split(".phyi")[0]
    return (phylipfile,outbase)


def calculatedistance(phylipfile,outbase):
    """
    This part calculates the distance between the different samples
    """
    distout = outbase + ".distout.txt"
    distoutplot = outbase + ".distout.pdf"
    aln = AlignIO.read(open(phylipfile), 'phylip')
    calculator = DistanceCalculator('identity') # Create the calculatior based on the identity model 
    dm = calculator.get_distance(aln)
    
    with open(distout, "w") as out: 
        print >> out, dm
    
    samplenames = dm.names

    #dm = np.fromstring(dm)
    dm = np.array(dm)
    plt.figure(figsize=(40, 40))
    fig, ax = plt.subplots()
    fig.set_size_inches(75, 75)
    #ax = sns.heatmap(dm, cmap="YlGnBu",vmin=0, vmax=.5, xticklabels = dm.names, yticklabels=dm.names, linewidths=.5, linecolor = "black", annot=True)
    #plt.show()
    sns.heatmap(dm, cmap="YlGnBu",vmin=0, vmax=.5, xticklabels = samplenames, yticklabels=samplenames, linewidths=.5, linecolor = "black", annot=True,  cbar=False, square =True)
    sns.despine()
    fig.savefig(distoutplot)

    
    

    
def main():
    """
    Main module
    """
    (phylipfile,outbase)=readphylipfile()
    calculatedistance(phylipfile,outbase)




main()

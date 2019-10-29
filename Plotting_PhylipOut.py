#!/usr/bin/py 

# Make sure that you load the emboss environment for anaconda

# Needs matplot lib and emboss (make it in biopython)

from Bio import Phylo 
import matplotlib.pyplot as plt
import pylab
from pylab import rcParams
import sys
rcParams['figure.figsize'] = 15, 15


# Run like ~/.conda/envs/EMBOSS/bin/python Plotting_PhylipOut.py tree

def readphylipfileout():
    """
    This part reads the output from the phyloscript, the neighbour tree or the parsimoni tree     
    """
    print "Reading files"
    tree = sys.argv[1] # first user input is the phylip I file
    outbase = tree.split("/")[-1].split(".tree")[0]
    return (tree,outbase)

def runCreatePhyloTree(tree,outbase):
    """
    Plot the tree
    """
    print "Plotting tree"
    PDFout = outbase + "_Tree.pdf"
    treeplot = Phylo.read(tree, 'newick')
    Phylo.draw(treeplot, do_show=False)
    pylab.savefig(PDFout)
    plt.close()

def main():
    (tree,outbase)=readphylipfileout()
    runCreatePhyloTree(tree,outbase)

main()

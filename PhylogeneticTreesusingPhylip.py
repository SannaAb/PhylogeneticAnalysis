#!/usr/bin/py 

# Make sure that you load the emboss environment for anaconda

# Needs matplot lib and emboss (make it in biopython)

from Bio.Emboss.Applications import FSeqBootCommandline
from Bio.Emboss.Applications import FDNADistCommandline
from Bio.Emboss.Applications import FNeighborCommandline
from Bio.Emboss.Applications import FConsenseCommandline
#from Bio.Emboss.Applications import dnaml ??? Cannot do the maximum likelihood
# DNAML
from Bio.Emboss.Applications import FDNAParsCommandline
from Bio import Phylo 
import matplotlib.pyplot as plt
import pylab
from pylab import rcParams
import sys
rcParams['figure.figsize'] = 15, 15


# Run like ~/.conda/envs/EMBOSS/bin/python Phylips.py file.phyi

def readphylipfile():
    """
    This reads the input phylip file, in this case the alignmentfile was created using muscle 
    """
    #phylipfile = "/jumbo/WorkingDir/B19-057/Data/Meta/Phylo/Aureus/MA/Aureus.phyi"
    phylipfile = sys.argv[1] # first user input is the phylip I file
    outbase = phylipfile.split("/")[-1].split(".phyi")[0]
    return (phylipfile,outbase)

def runSeqBoot(phylipfile,outbase):
    """
    This part runs seqboot for the phylip file
    """
    print "Running Seqboot"
    seqout = outbase + ".fseqboot"
    seqboot_cline = FSeqBootCommandline(sequence=phylipfile, reps=1000,seed=333, outfile=seqout) 
    stdout, stderr = seqboot_cline()
    return seqout

def runDNAdist(seqout,outbase):
    """
    This part runs DNAdist for the seqboot output
    """
    print "running DNA distance"
    distout = outbase + ".dnadist"
    dnadist_cline=FDNADistCommandline(sequence=seqout,outfile=distout,method="j")
    stdout, stderr = dnadist_cline()
    return distout

def runNeighbour(distout,outbase):
    """
    This part runs the neighbour 
    """
    print "running neighbour"
    neighout = outbase + ".neighbour"
    tree = outbase + ".neighbour_NJ"
    Neigh_cline = FNeighborCommandline(datafile=distout,outfile=neighout,seed=333,treetype="n",outtreefile=tree)
    stdout, stderr = Neigh_cline()
    return(neighout, tree)

def runConsenseNeighbour(outbase,neighout, tree):
    """
    Creates your consensus tree for Neighbour
    """
    print "running Consensus For Neighbour"
    consensus = outbase + ".consensus_Neighbour.txt" 
    consensusNeighbourtree = outbase + ".consensus_Neighbour.tree"
    consensus_cline = FConsenseCommandline(intreefile=tree, outfile=consensus,outtreefile=consensusNeighbourtree, method='mre')
    stdout, stderr = consensus_cline()
    return consensusNeighbourtree

def runCreatePhyloTreeNeighbour(consensusNeighbourtree,outbase):
    """
    Plot the PhyloConsensusNeighbour tree
    """
    PDFout = outbase + "_NeighbourTree.pdf"
    tree = Phylo.read(consensusNeighbourtree, 'newick')
    Phylo.draw(tree, do_show=False)
    pylab.savefig(PDFout)
    plt.close()


def runDNAPars(seqout,outbase):
    """
    Here we run DNA Parsimony on the seqboot out
    """
    print "Creates DNA parsimony"
    DNAparsOut = outbase + ".fdnapars.txt"
    parstree = outbase + ".fdnapars.tree"
    pars_cline = FDNAParsCommandline(sequence=seqout,outfile=DNAparsOut, seed=333, outtreefile=parstree, auto=True)
    stdout, stderr = pars_cline()
    return (DNAparsOut, parstree)
    

def runConsenseParsimony(DNAparsOut,parstree,outbase): 
    """
    Creates the consensus from the parsimony 
    """
    print "Creates Consensus For DNA Parsimony"
    consensusPars = outbase + ".consensus_Parsimony.txt"
    consensusParstree = outbase + ".consensus_Parsimony.tree"
    consensus_cline = FConsenseCommandline(intreefile=parstree, outfile=consensusPars,outtreefile=consensusParstree, method='mre')
    stdout, stderr = consensus_cline()
    return consensusParstree

def runCreatePhyloTreeParsimony(consensusParstree,outbase):
    """
    Plot the Parsimony Tree
    """
    PDFout = outbase + "_Parsimony_Tree.pdf"
    tree = Phylo.read(consensusParstree, 'newick')
    Phylo.draw(tree, do_show=False)
    pylab.savefig(PDFout)
    plt.close()

def main():
    (phylipfile,outbase)=readphylipfile()
    seqout=runSeqBoot(phylipfile,outbase)
    distout=runDNAdist(seqout,outbase)
    (neighout, tree)=runNeighbour(distout,outbase)
    consensusNeighbourtree=runConsenseNeighbour(outbase,neighout, tree)
    #runCreatePhyloTreeNeighbour(consensusNeighbourtree,outbase)
    (DNAparsOut, parstree)=runDNAPars(seqout,outbase)
    consensusParstree=runConsenseParsimony(DNAparsOut,parstree,outbase)
    #runCreatePhyloTreeParsimony(consensusParstree,outbase)


main()

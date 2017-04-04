#NEXUS

BEGIN TAXA;
    DIMENSIONS NTAX=5;
    TAXLABELS
        taxon2
        taxon3
        taxon4
        taxon1
        taxon5
  ;
END;

BEGIN TREES;
    TREE 1 = ((taxon2:1.0,(taxon3:1.0,(taxon4:1.0,taxon1:1.0):1.0):1.0):1.0,taxon5:1.0);
    TREE 2 = ((taxon2:1.0,((taxon3:1.0,taxon4:1.0):1.0,taxon1:1.0):1.0):1.0,taxon5:1.0);
    TREE 3 = ((taxon2:1.0,((taxon3:1.0,taxon1:1.0):1.0,taxon4:1.0):1.0):1.0,taxon5:1.0);
    TREE 4 = ((taxon2:1.0,((taxon3:1.0,taxon1:1.0):1.0,taxon4:1.0):1.0):1.0,taxon5:1.0);
    TREE 5 = ((taxon5:1.0,taxon2:1.0):1.0,(taxon3:1.0,(taxon4:1.0,taxon1:1.0):1.0):1.0);
    TREE 6 = (((taxon2:1.0,(taxon4:1.0,taxon1:1.0):1.0):1.0,taxon3:1.0):1.0,taxon5:1.0);
    TREE 7 = ((taxon5:1.0,taxon2:1.0):1.0,(taxon3:1.0,(taxon4:1.0,taxon1:1.0):1.0):1.0);
    TREE 8 = ((taxon2:1.0,((taxon3:1.0,taxon1:1.0):1.0,taxon4:1.0):1.0):1.0,taxon5:1.0);
    TREE 9 = (((taxon2:1.0,taxon3:1.0):1.0,(taxon4:1.0,taxon1:1.0):1.0):1.0,taxon5:1.0);
    TREE 10 = (((taxon2:1.0,taxon3:1.0):1.0,(taxon4:1.0,taxon1:1.0):1.0):1.0,taxon5:1.0);
    TREE 11 = ((taxon2:1.0,((taxon3:1.0,taxon4:1.0):1.0,taxon1:1.0):1.0):1.0,taxon5:1.0);
END;


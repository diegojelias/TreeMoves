#NEXUS

BEGIN TAXA;
    DIMENSIONS NTAX=10;
    TAXLABELS
        taxon5
        taxon3
        taxon2
        taxon10
        taxon4
        taxon7
        taxon6
        taxon9
        taxon8
        taxon1
  ;
END;

BEGIN TREES;
    TREE 1 = (((((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0):1.0,((taxon6:1.0,taxon9:1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0):1.0);
    TREE 2 = ((((taxon6:1.0,taxon9:1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0):1.0,(((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0);
    TREE 3 = (((((taxon2:1.0,taxon5:1.0):1.0,taxon3:1.0):1.0,taxon10:1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0):1.0,((taxon6:1.0,taxon9:1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0):1.0);
    TREE 4 = ((((taxon4:1.0,taxon7:1.0):1.0,((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0):1.0,taxon10:1.0):1.0,((taxon6:1.0,taxon9:1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0):1.0);
    TREE 5 = (((((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0):1.0,(((taxon8:1.0,taxon1:1.0):1.0,taxon6:1.0):1.0,taxon9:1.0):1.0);
    TREE 6 = (((((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0):1.0,(((taxon6:1.0,taxon9:1.0):1.0,taxon1:1.0):1.0,taxon8:1.0):1.0);
    TREE 7 = ((((taxon6:1.0,taxon9:1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0):1.0,(((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0);
    TREE 8 = ((((taxon6:1.0,taxon9:1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0):1.0,(((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0);
    TREE 9 = ((((((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0):1.0,(taxon6:1.0,taxon9:1.0):1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0);
    TREE 10 = ((((((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0,taxon7:1.0):1.0,taxon4:1.0):1.0,((taxon6:1.0,taxon9:1.0):1.0,(taxon8:1.0,taxon1:1.0):1.0):1.0);
    TREE 11 = (((((taxon5:1.0,taxon3:1.0):1.0,taxon2:1.0):1.0,taxon10:1.0):1.0,(taxon4:1.0,taxon7:1.0):1.0):1.0,(((taxon8:1.0,taxon1:1.0):1.0,taxon6:1.0):1.0,taxon9:1.0):1.0);
END;


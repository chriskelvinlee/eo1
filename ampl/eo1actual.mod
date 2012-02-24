# Read in Data

param num_matrices >= 1, integer; # Number of matrices in the data file to be read
param num_rows >= 1, integer;     # Number of rows
param num_cols >= 1, integer;     # Number of columns 


# Set
set Rv   := 1 .. num_rows;     # Vertical columns
set Rh   := 1 .. num_cols;     # Horizontal resolution
set B := 1 .. num_matrices;      # Beamlets matrices
set T;      # Tumor matrices
set C;      # Crticical matrices

# Parameters
param maxc;                     # Max radiation allowed for critical
param mint;                     # Min radiation allowed for tumor
param b {B, Rh, Rv};     # Entry i,j of beam matrix Bk
param t {i in Rh, j in Rv};     # Entry i,j of tumor matrix T
param c {i in Rh, j in Rv};     # Entry i,j of critical matrix C

# Variables
var r {i in Rh, j in Rv} >= 0;  # Amount of radiation delivered
var q {k in B} >= 0, <= 25;            # Intensity of beamlet k

# Objective
maximize Therapy:
    sum{i in Rh, j in Rv} r[i,j]*t[i,j]- sum{i in Rh, j in Rv} r[i,j]*c[i,j];

# Constraints
subject to Master_updated {i in Rh, j in Rv}:
    sum{k in B} q[k]*b[k, i, j] = r[i,j];
    
subject to Tumor {i in Rh, j in Rv}:
    r[i,j] >= mint*t[i,j];
    
subject to Critical {i in Rh, j in Rv}:
    c[i,j]*r[i,j] <= maxc;




param num_matrices >= 1, integer; # Number of matrices in the data file to be read
param num_rows >= 1, integer;     # Number of rows
param num_cols >= 1, integer;     # Number of columns 

set MATS    := 1 .. num_matrices; # set of matrices
set ROWS    := 1 .. num_rows;	  # set of rows
set COLUMNS := 1 .. num_cols;	  # set of columns

param matrix_value {MATS, ROWS, COLUMNS} >= 0; # values for entries of each matrix

var MaxValue {ROWS, COLUMNS} >= 0; # variable capturing the maximum value at each 
				   # index across all matrices given

# Pushing all variables to the maximum value of their corresponding indices
minimize Maximum_Values: sum {i in ROWS, j in COLUMNS} MaxValue[i,j];

# Each variable at an index is >= to the maximum value at 
# the index across all matrices given.
subject to LargestElement {k in MATS, i in ROWS, j in COLUMNS}: 
	MaxValue[i, j]	>= matrix_value[k,i,j];

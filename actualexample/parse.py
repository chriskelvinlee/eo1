#!/usr/bin/env python
# encoding: utf-8
"""
parse.py

Created by Christopher K. Lee on 2012-02-23
"""

# Parse Tumor and Critical Matrix for AMPL
def parseSmall(inputMatrix, outMatrix):
  
  # Read input file
  try:
    f = open(inputMatrix, 'r')
  except IOError as e:
    print "File not found"
    formMatrix=[]
    return formMatrix
  raw = f.readlines()
  f.close

  # Count rows, append index to beginning
  post = []
  counter = 0
  for row in raw:
    counter += 1;
    row = str(counter)+'\t'+row
    post.append(row)

  # Count columns
  index = ''
  for i in range(1,81):
    index += '\t'
    index += str(i)
  index += '\n'  

  # Insert columns at head
  post.insert(0, index)
  
  # Write output file
  w = open(outMatrix, 'w')
  w.writelines(post)
  w.close()

  print "Formatted Matrix!"


# Parse Beamlets Matrix for AMPL
"""126 matrices of 80x60"""
def parseLarge(inputMatrix = "beam_raw.txt", outMatrix = "beam_out.txt"):

  # Read input file
  try:
    f = open(inputMatrix, 'r')
  except IOError as e:
    print "File not found"
    formMatrix=[]
    return formMatrix
  raw = f.readlines()
  f.close

  counter = []
  # Set skeleton for matrix
  for i in xrange(126):
    counter += [j  for j in range(1,61)]
    counter.append('\n')

  post = [] 
  ind = 0
  for row in raw:
    hold = str(counter[ind])+'\t'+row
    post.append(hold)
    ind += 1

  index = ''
  for i in range(1,81):
    index += '\t'
    index += str(i)
  index += '\t:=\n'  
  
  # 61*126 = 7686
  hackIndex = 0
  for i in range(1, 7687):
    
    if i%61  == 0:
      j = i/61
      parseIndex = '[*,*,'+str(j+1)+']:\t'+index
      post.insert(i+hackIndex, parseIndex)
      hackIndex += 1
    
  parseIndexZero = '[*,*,1]:\t'+index
  post.insert(0, parseIndexZero)
  
  w = open(outMatrix, 'w')
  w.writelines(post)
  w.close()

  print "Formatted Matrix!"
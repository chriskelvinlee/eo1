#!/usr/bin/env python
# encoding: utf-8
"""
parse.py

Created by Christopher K. Lee on 2012-02-23
"""

def parse(inputMatrix, outMatrix):
  
  try:
    f = open(inputMatrix, 'r')
  except IOError as e:
    print "File not found"
    formMatrix=[]
    return formMatrix

  raw = f.readlines()
  f.close

  post = []
  counter = 0
  for row in raw:
    counter += 1;
    row = str(counter)+'\t'+row
    post.append(row)

  index = ''
  for i in range(1,81):
    index += '\t'
    index += str(i)
  index += '\n'  

  post.insert(0, index)
    
  w = open(outMatrix, 'w')
  w.writelines(post)
  w.close()
  
  print "Formatted Matrix!"
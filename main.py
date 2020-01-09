#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:02:53 2019

@author: anujchaudhri
"""

import time
import sys
from pathlib import Path
from optimizer import Optimizer
import os

def write_output(out_file,out):
    if os.path.isfile(out_file):
        os.remove(out_file)
        print("old output file removed")
    f = open(out_file,"a+")
    for k in out:
        f.write((' '.join(['%1.5f '] * k.size) + '\n') % tuple(k))
    f.close()

def main(input_file_name, output_file_name,N):
    
    # keep track of start time
    start_time = time.time()
    
    # input file path
    input_file_path = "inputs/"
    input_file = Path(input_file_path + input_file_name)
    
    # output file path
    output_file_path = "outputs/"
    output_file = Path(output_file_path + output_file_name)

    # number of samples needed
    n_samples = N
    
    # Run optimizer and get output
    optimum = Optimizer(input_file,n_samples)
    out = optimum.get_output()
    # write output
    write_output(output_file,out)
    
    # print total time elapsed
    end_time = time.time()
    
    print("Total time taken: ", "%1.4f" % (end_time-start_time), "seconds")
    
if __name__ == "__main__":
    main(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
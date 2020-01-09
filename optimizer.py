#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:15:44 2019

@author: anujchaudhri
"""

import numpy as np
from pyDOE import *
from constraints import Constraint

class Optimizer():
    
    def __init__(self,input_file,N):
        self.input_constraints = Constraint(input_file)
        #print(self.input_constraints.get_ndim())
        #print(self.input_constraints.get_example())
        #print(self.input_constraints.get_constraints())
        #exam = np.array(list(self.input_constraints.get_example()), dtype=float)
        #print(self.input_constraints.apply(exam))
        self.x = self.sample(N)
        self.get_output()
        

    def sample(self,N):
        count = 0
        ndim = int(self.input_constraints.get_ndim())
        x = np.empty((0,ndim))
        while (count < int(N)):
            n_samples = int(N)*10
            smpls = lhs(ndim,samples=n_samples)
            for i in range(len(smpls)):
                if self.input_constraints.apply(smpls[i]) and (count < int(N)):
                    #print(smpls[i])
                    x = np.append(x,np.array([smpls[i]]),axis=0)
                    count += 1
        print(count)
        print(x.shape)
        return x
    
    def get_output(self):
        return self.x
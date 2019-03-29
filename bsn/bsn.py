# -*- coding: utf-8 -*-
"""
Create Date: 20-03-2019
Author: Marc Enthoven
"""
# Imports of modules
import numpy as np
import random

class bsn:
    
    def __init__(self):
        pass

#Function to define whether random generated number satisfies bsn algorithm
    def validate_bsn(self,bsn_number):
        bsn_position = np.array([int(x) for x in str(bsn_number)])
        bsn_digit = np.array(list(range(len(str(bsn_number)),0,-1)))
        bsn_digit[-1:] = bsn_digit[-1:]*(-1)
        product_bsn = np.sum(np.multiply(bsn_digit,bsn_position))
        if product_bsn % 11 == 0:
            return True
        else:
            return False

#Script runs until it has found the required number of BSN numbers
    def generate_bsn(self,bsn_numbers_count):
        #define variables
        valid_bsn = []
        chunks = 100
        limit = bsn_numbers_count
        
        # Run function until required number of bsn numbers are generated
        while len(valid_bsn) < limit:
            
            # Generate n random numbers
            random_input = random.sample(range(10000000, 999999999),chunks)
            
            # Apply the algorithm
            elf_proef_bin = list(map(self.validate_bsn,random_input))
            
            # Take the actual unique BSN number which are not generated in an earlier batch yet
            input_rslt = [random_input for random_input,elf_proef_bin in zip(random_input,elf_proef_bin) if elf_proef_bin == True]
            input_rslt_unique = set([gen_bsn for gen_bsn in input_rslt if gen_bsn not in valid_bsn])
            
            # Add to temporary store and create ouput list
            valid_bsn.extend(input_rslt_unique)

            if len(valid_bsn) >= limit:
                output_list = valid_bsn[:limit]
        
        # print output list, don't do this with large numbers
        output_txt = open('generate_'+ str(bsn_numbers_count) +'_bsn.txt','a')
        for item in output_list:
            output_txt.write(str(item) + '\r\n') # remove \r in linux environment
        output_txt.close()
        print(str(bsn_numbers_count) + ' bsn have been generated and written in your working directory.')

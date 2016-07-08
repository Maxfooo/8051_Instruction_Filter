'''
Created on Jul 8, 2016

@author: Max Ruiz
'''

from Parser import parse
import pickle

if __name__ == '__main__':
    fileName = '8051_Instruction_Set.csv'
    pickleFileName = 'instruction_table.p'
    pickle.dump(parse(fileName), open(pickleFileName, 'wb'))

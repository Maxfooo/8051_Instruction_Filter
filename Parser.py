'''
Created on Jul 7, 2016

@author: Max Ruiz
'''

from FileIO import FileIO as FIO
import re

PARAMETER_CONSTANTS = ['A', 'AB', '@A+DPTR', '@A+PC', '@DPTR', 'C', 'DPTR',
                      '@R0', '@R1', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7']

def parse(fileName, externalFile=False):
    try:
        if externalFile:
            fio = FIO()
            fio.openFile('.csv', ftypes=[('Comma/Semicolon Delimited', '.csv'), ('All Files', '.*')], ifilen = fileName + '.csv')
            instSetFile = fio.getOpenedFile()
            fio.closeOpened()
        else:
            instSetFile = open(fileName)
        noFile = False
    except:
        print("Could not open file.")
        noFile = True

    if not noFile:
        instruction_table = dict()
        for line in instSetFile:
            instLine = []
            opCode = ''
            bytes = 1
            mnemonic = ''
            instLine = line.split(';')
            instLine[2].replace('\n','')
            mnemFilter = re.findall(r'([\?\w]+\s*)([@.#.\+\w\d\s]*)\s*,*\s*([@.#.\+\w\d\s]*)', instLine[0])

            mnemFilter = mnemFilter[0]
            print ("instLine", instLine)

            print('mnemFilter', mnemFilter)



            mnemonic = mnemFilter[0]
            if mnemFilter[1] != '':
                if not any(param in mnemFilter[1] for param in PARAMETER_CONSTANTS):
                    mnemonic += '%s'
                else:
                    mnemonic += mnemFilter[1]
            if mnemFilter[2] != '':
                if not any(param in mnemFilter[2] for param in PARAMETER_CONSTANTS):
                    mnemonic += ', %s'
                else:
                    mnemonic += ', ' + mnemFilter[2]

            opCode = instLine[1].replace('0x', '')
            bytes = int(instLine[2])

            instruction_table[opCode] = (mnemonic, bytes)
        
        instSetFile.close()
        return instruction_table













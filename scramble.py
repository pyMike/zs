# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:12:22 2015

@author: mike
"""

import argparse, sys
#==============================================================================
#Supporting Functions:
def readFileByLines(filename):
    lineList = []
    try:
        aFile = open(filename)
        lineList = aFile.readlines()
    except:
        print 'Can not open or read lines in file: <' + filename +'>'
        #add print usage
        sys.exit()
    return lineList
#------------------------------------------------------------------------------
def readFileByChars(filename):
    inStr = ''
    try:
       aFile = open(filename,'r')
       inStr = aFile.read()
    except:
        print 'Can not open or read chars in file: <' + filename +'>'
        #add print usage
        sys.exit()
    return inStr
#------------------------------------------------------------------------------
def reverseList(aList):
    return aList[::-1]
#------------------------------------------------------------------------------
def reverseStrsInList(lineList):
    revStrsInList = []
    for line in lineList:
        revStrsInList.append(reverseList(line))
    return revStrsInList
#------------------------------------------------------------------------------
#Recall: sorted(iterable, cmp=None, key=None, reverse=False)
def sortLinesInList(lineList):
    sortedList = []
    for line in lineList:
        sortedList.append(''.join( sorted(line) ) )
    return sortedList
#------------------------------------------------------------------------------
def printLineList(lineList):
    for line in lineList:
        print line
    return    
#==============================================================================
#Obtaining Arguments:
#Usage Example: python scramble.py -f sample_file -c invert
#print "=======================Begin Script===================================="
parser = argparse.ArgumentParser(description="read file, transform data and outputs to stdout ")
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--char", action="store_true")
group.add_argument("-l", "--line", action="store_true")
parser.add_argument("-f",dest='filename',required=True, help="specify the filename")
parser.add_argument("act", choices=['invert', 'sort'], help="specify action to sort or invert data")
args = parser.parse_args()
#------------------------------------------------------------------------------
#Reading file: two Methods by line or by char
if args.char:
    inStr = readFileByChars(args.filename)
    #lineList = inStr.split('\n')
    lineList = inStr.splitlines()
else:
    #Default is to read lines...
    lineList = readFileByLines(args.filename)
    lineList = ''.join(lineList).splitlines()
#------------------------------------------------------------------------------
#Data structure: data stored in list of strings...   
#print type(lineList), lineList
#------------------------------------------------------------------------------
#Actions on data 
if args.char and args.act == 'invert':
    #print 'char & list invert as in provided use case'
    #UseCase:  python scramble.py -­f sample_file -­c invert
    lineList = reverseList(lineList)
    lineList = reverseStrsInList(lineList) 
elif args.char and args.act == 'sort':
    #print 'char & list sort consistant with invert case'
    aStr = ''
    lineList = sorted(lineList)
    lineList = sortLinesInList(lineList)
else:
    #UseCase: python scramble.py ­-f sample_file invert
    if args.act == 'invert':
    #Default case line mode: 
       #print 'invert lines'
       lineList = reverseList(lineList)    
       print '----3'
    #UseCase: python scramble.py ­f sample_file sort
    elif args.act == 'sort':
       #print 'sort lines'
       lineList = sorted(lineList)
       print '----4'

printLineList( lineList )
#print "=======================End Script===================================="
#------------------------------------------------------------------------------
        

    

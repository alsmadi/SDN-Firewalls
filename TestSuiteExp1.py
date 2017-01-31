#! /usr/bin/env python


import unittest
from reportlab.lib.testutils import setOutDir, printLocation
setOutDir(__name__)
import os, string, fnmatch, re, sys, unittest
import csv
import FirewallTester_Exp10

suite1 = FirewallTester_Exp10.suite()
EXTRA_FILE = 'tests.csv'
suite = unittest.TestSuite()

class ExternalTestCase():

 
#readInputs()


 def readInputs():
	 #from reportlab.lib.testutils import RL_HOME
	 #print RL_HOME
         #extraFilename = os.path.join(RL_HOME, 'test', EXTRA_FILE)
         #if not os.path.exists(extraFilename):
          #     return
	 #extraModulenames = open(extraFilename).readlines()
         #extraModulenames = list(map(string.strip, extraModulenames))
	 #for f in extraModulenames:
          #      if f == '':
           #         continue
            #    if f[0] == '#':
             #       continue
	 #with open('tests1.csv', 'rb') as csvfile:
          #inputsreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
          #for row in inputsreader:
          # print ', '.join(row)
           unittest.TextTestRunner(verbosity=2).run(suite)
 

 if __name__ == "__main__":
  print "start testing"
  
  #suite = unittest.TestSuite()

  suite.addTest(suite1)
  readInputs()
 # unittest.TextTestRunner(verbosity=2).run(suite)
#unittest.TextTestRunner(verbosity=2).run(suite)

 


from unittest import TestCase

import SourceModel.SM_File
from SmellDetector import EncSmellDectector


class TestModSmells(TestCase):
    def test_detectDefEnc(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/percona-xtradb-cluster-tutorial/manifests/master_slave.pp"
        outFileName = "tmp/DefEncTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')
        EncSmellDectector.detectDefEnc(fileObj, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

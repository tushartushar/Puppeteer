from unittest import TestCase

from SmellDetector import HieSmellDectector


class TestHieSmells(TestCase):
    def test_detectBroHierarchy(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/vagrant-baseline/puppet/"
        outFileName = "tmp/brokenHieTest.txt"
        outFile = open(outFileName, 'w')
        #fileObj = SourceModel.SM_File.SM_File("/Users/Tushar/Documents/Research/PuppetQuality/Repos/vagrant-baseline/puppet/modules/vendors/mongodb/manifests/repo/apt.pp")
        HieSmellDectector.detectBroHierarchy(folderName, outFile)
        #fileObj.getClassHierarchyInfo()
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertEquals(len(outFileRead.read()), 0)
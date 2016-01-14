from unittest import TestCase
import SourceModel.SM_File
import ModSmellDectector

class TestModSmells(TestCase):
    def test_detectInsModForm1(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/stig_misc/manifests/find_uneven.pp"
        outFileName = "tmp/insufficientModForm1Test.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')

        ModSmellDectector.detectInsModForm1(fileObj, outFile)
        outFile.close()

        outFileRead = open(outFileName, 'r')
        self.assertEquals(len(outFileRead.read()), 0)
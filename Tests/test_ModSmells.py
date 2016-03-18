from unittest import TestCase

import SourceModel.SM_File
from SmellDetector import ModSmellDectector


class TestModSmells(TestCase):
    def test_detectInsModForm1(self):
        self.insModForm1PositiveCase()
        self.insModForm1NegativeCase()

    def insModForm1PositiveCase(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/operations-puppet-production/manifests/role/authdns.pp"
        outFileName = "tmp/insufficientModForm1Test.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectInsModForm1(fileObj, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def insModForm1NegativeCase(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/stig_misc/manifests/find_uneven.pp"
        outFileName = "tmp/insufficientModForm1Test.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectInsModForm1(fileObj, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertEquals(len(outFileRead.read()), 0)

    def test_detectInsModForm2(self):
        self.insModPositiveCase()
        self.insModNegativeCase()

    def insModNegativeCase(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/stig_misc/manifests/run_control_scripts.pp"
        outFileName = "tmp/insufficientModForm2Test.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectInsModForm2(fileObj, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertEquals(len(outFileRead.read()), 0)

    def insModPositiveCase(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/searde_svn/manifests/server.pp"
        outFileName = "tmp/insufficientModForm2Test.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectInsModForm2(fileObj, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectInsModForm3(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/xserver/manifests/init.pp"
        outFileName = "tmp/insufficientModForm3Test.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectInsModForm3(fileObj, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectUnstructuredModForm1(self):
        self.detectUnsModForm1NegativeCase()
        self.detectUnsModForm1PositiveCase()

    def detectUnsModForm1NegativeCase(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/control-repo/"
        outFileName = "tmp/unstructuredModForm1Test.txt"
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectUnstructuredModForm1(folderName, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertEquals(len(outFileRead.read()), 0)

    def detectUnsModForm1PositiveCase(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/kickstack/"
        outFileName = "tmp/unstructuredModForm1Test.txt"
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectUnstructuredModForm1(folderName, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectUnsModForm2(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/kickstack/manifests/cinder"
        outFileName = "tmp/unstructuredModForm2Test.txt"
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectUnsModForm2(folderName, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectUnsModForm3(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/puppet-pyrocms/modules/firewall"
        outFileName = "tmp/unstructuredModForm3Test.txt"
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectUnsModForm3(folderName, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectTCMod(self):
        #fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/operations-puppet-production/manifests/role/authdns.pp"
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/searde_svn/manifests/server.pp"
        outFileName = "tmp/TCModTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(outFileName, 'w')
        ModSmellDectector.detectTCMod(fileObj, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectHairballStr(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/operations-puppet/"
        outFileName = "tmp/getGraphTest.txt"
        outFile = open(outFileName, 'w')
        graph = ModSmellDectector.getGraph(folderName)
        ModSmellDectector.detectHaiStr(graph, folderName, outFile)
        #graph.printGraph()
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectWeakendMod(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/devbox/modules/php/"
        outFileName = "tmp/WeakendModTest.txt"
        outFile = open(outFileName, 'w')
        graph = ModSmellDectector.getGraph(folderName)
        ModSmellDectector.detectWeakendMod(graph, folderName, outFile)
        #graph.printGraph()
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

from unittest import TestCase

import SourceModel.SM_File
from SmellDetector import AbsSmellDectector


class TestAbsSmells(TestCase):
    def test_checkWithFileResource(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/audio/manifests/no/darwin.pp"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open("tmp/multifacetedAbsForm1FileTest.txt", 'w')

        AbsSmellDectector.checkWithFileResource(fileObj, outFile)
        outFile.close()

        outFileRead = open("tmp/multifacetedAbsForm1FileTest.txt", 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_checkWithPackageResource(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/network/manifests/no_rds.pp"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open("tmp/multifacetedAbsForm1PackageTest.txt", 'w')

        AbsSmellDectector.checkWithPackageResource(fileObj, outFile)
        outFile.close()

        outFileRead = open("tmp/multifacetedAbsForm1PackageTest.txt", 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_checkWithServiceResource(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/hpc_cluster/manifests/node.pp"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open("tmp/multifacetedAbsForm1ServiceTest.txt", 'w')

        AbsSmellDectector.checkWithServiceResource(fileObj, outFile)
        outFile.close()

        outFileRead = open("tmp/multifacetedAbsForm1ServiceTest.txt", 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectMulAbsInClass(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/aide/manifests/redhat.pp"
        testFile = "tmp/multifacetedAbsForm2ClassTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')

        AbsSmellDectector.detectMulAbsInClass(fileObj, outFile)
        outFile.close()

        outFileRead = open(testFile, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectMulAbsInDefine(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/audit/manifests/darwin/permissions.pp"
        testFile = "tmp/multifacetedAbsForm2DefineTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')

        AbsSmellDectector.detectMulAbsInDefine(fileObj, outFile)
        outFile.close()

        outFileRead = open(testFile, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectMulAbsInModule(self):
        self.test_detectMulAbsInModule_NegativeCase()
        self.test_detectMulAbsInModule_PositiveCase()

    def test_detectMulAbsInModule_PositiveCase(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/operations-puppet-production/manifests/role/authdns.pp"
        testFile = "tmp/multifacetedAbsForm2ModuleTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')
        AbsSmellDectector.detectMulAbsInModule(fileObj, outFile)
        outFile.close()
        outFileRead = open(testFile, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectMulAbsInModule_NegativeCase(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/automount/manifests/subdir.pp"
        testFile = "tmp/multifacetedAbsForm2ModuleTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')
        AbsSmellDectector.detectMulAbsInModule(fileObj, outFile)
        outFile.close()
        outFileRead = open(testFile, 'r')
        self.assertEquals(len(outFileRead.read()), 0)

    def test_detectUnnAbsInClasses(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/location/manifests/no/redhat.pp"
        testFile = "tmp/unnecessaryAbsTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')
        AbsSmellDectector.detectUnnAbsInClasses(fileObj, outFile)
        outFile.close()
        outFileRead = open(testFile, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectUnnAbsInDefine(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/hpc_cluster/spec/fixtures/modules/proxy/manifests/yum.pp"
        testFile = "tmp/unnecessaryAbsTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')
        AbsSmellDectector.detectUnnAbsInDefine(fileObj, outFile)
        outFile.close()
        outFileRead = open(testFile, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectUnnAbsInModules(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/hpc_cluster/spec/fixtures/modules/proxy/manifests/yum.pp"
        testFile = "tmp/unnecessaryAbsTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')
        AbsSmellDectector.detectUnnAbsInModules(fileObj, outFile)
        outFile.close()
        outFileRead = open(testFile, 'r')
        self.assertEquals(len(outFileRead.read()), 0)

    def test_detectImpAbs(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/audit/manifests/remote/collect.pp"
        testFile = "tmp/imperativeAbsTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')
        AbsSmellDectector.detectImpAbs(fileObj, outFile)
        outFile.close()
        outFileRead = open(testFile, 'r')
        self.assertGreater(len(outFileRead.read()), 0)

    def test_detectMisAbs(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/searde_svn/manifests/server.pp"
        testFile = "tmp/missingAbsTest.txt"
        fileObj = SourceModel.SM_File.SM_File(fileName)
        outFile = open(testFile, 'w')
        AbsSmellDectector.detectMisAbs(fileObj, outFile)
        outFile.close()
        outFileRead = open(testFile, 'r')
        self.assertEquals(len(outFileRead.read()), 0)

    def test_detectDuplicateAbs(self):
        folderName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/"
        outFileName = "tmp/duplicateAbsTest.txt"
        outFile = open(outFileName, 'w')
        AbsSmellDectector.detectDuplicateAbs(folderName, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)
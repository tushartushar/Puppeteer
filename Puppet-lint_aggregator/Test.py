from unittest import TestCase

import Aggregator
from SmellDetector import Constants as CONSTS, Analyzer


class TestAggregator(TestCase):
    def test_aggregate(self):
        outFileName = "/Users/Tushar/Documents/Research/PuppetQuality/Puppet-lint_aggregator/testOut.csv"
        outFile = open(outFileName, 'w')
        outFile.write(CONSTS.HEADER)
        Aggregator.aggregate("/Users/Tushar/Documents/Research/PuppetQuality/Puppet-lint_aggregator/test1/", "test1", outFile)
        Aggregator.aggregate("/Users/Tushar/Documents/Research/PuppetQuality/Puppet-lint_aggregator/test2/", "test2", outFile)
        outFile.close()
        outReadFile = open(outFileName, 'r')
        self.assertGreater(len(outReadFile.read()), 0)

    def test_detectComplexExpr(self):
        fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/cmits/cmits-example/modules-unclass/user/manifests/valid.pp"
        #fileName = "/Users/Tushar/Documents/Research/PuppetQuality/Repos/percona-xtradb-cluster-tutorial/manifests/master_slave.pp"
        outFileName = "test1/DefEncTest.txt"

        outFile = open(outFileName, 'w')
        Analyzer.detectComplexExpr(fileName, outFile)
        outFile.close()
        outFileRead = open(outFileName, 'r')
        self.assertGreater(len(outFileRead.read()), 0)
# Puppeteer
Puppeteer is a design configuration smell detection tool for Puppet code.

## Steps to Execute
* Execute the cpdRunner.sh shell script to carry out clone detection using PMD-CPD tool. 
    * Download the PMD tool and update the path in the shell script. 
    * Update the folder path where all the Puppet repositories are placed. 
    * Execute the script. 
* Update the constant REPO_ROOT in Constants.py that represents the folder path where all the Puppet repositories are placed.
* Execute "Puppeteer.py".

**Optional - Analyze Puppet repos with Puppet-Lint**

* Execute puppet-lintRunner.py after setting the repo root
* Set the repo root in Puppet-lint_aggregator/PLConstants.py
* Execute PuppetLintRules.py - It will generate a consilidated summary of the analysis for all the analyzed projects.

## Supported Design Configuration Smells
The tool supports detection of following design configuration smells:

1. Multifaceted Abstraction
2. Unnecessary Abstraction
3. Imperative Abstraction
4. Missing Abstraction
5. Insufficient Modularization
6. Duplicate Block
7. Broken Hierarchy
8. Unstructured Module
9. Dense Structure
10. Deficient Encapsulation
11. Weakened Modularity

##More Details
You can find more details about the catalog of configuration smells [here](http://www.tusharma.in/research/a-catalog-of-configuration-smells/) and the paper that describes the catalog and attempts to answer a few research questions concerning the configuration smells [here] (http://www.tusharma.in/research/does-your-configuration-code-smell-msr-2016/).



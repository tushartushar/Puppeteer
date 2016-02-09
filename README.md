# Puppeteer
Puppeteer is a design configuration smell detection tool for Puppet code.

## Steps to Execute
* Execute the cpdRunner.sh shell script to carry out clone detection using PMD-CPD tool. 
    * Download the PMD tool and update the path in the shell script. 
    * Update the folder path where all the Puppet repositories are placed. 
    * Execute the script. 
* Update the constant REPO_ROOT in Constants.py that represents the folder path where all the Puppet repositories are placed.
* Execute "Puppeteer.py".

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
11. Weekend Modularity



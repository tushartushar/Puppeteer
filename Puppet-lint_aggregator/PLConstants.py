from getpass import getuser

SMELLS_DEP_STM = "Deprecated Statements"
SMELLS_INC_TSK = "Incomplete tasks"
SMELLS_COM_EXP = "Complex Expression"
SMELLS_MIS_ELS = "Missing Else"

#1 Missing default case
RULE1_1 = "case statement without a default case"

#2 Inconsistent naming convention
RULE2_1 = "class name containing a dash"
RULE2_2 = "variable contains a dash"
#3 Complex expression
RULE3_1 = SMELLS_COM_EXP

#4 Duplicate entity
RULE4_1 = "duplicate parameter found in resource"

#5 Misplaced attribute
RULE5_1 = "ensure found on line but it's not the first attribute"
RULE5_2 = "optional parameter listed before required parameter"

#6 improper alignment
RULE6_1 = "indentation of => is not properly aligned"
RULE6_2 = "tab character found"
RULE6_3 = "two-space soft tabs not used"
RULE6_4 = "right-to-left (<-) relationship"

#7 invalid property value
RULE7_1 = "mode should be represented as a 4 digit octal value"
RULE7_2 = "symlink target specified in ensure attr"
RULE7_3 = "puppet:// URL without modules/ found"

#8 incomplete tasks
RULE8_1 = SMELLS_INC_TSK

#9 deprecated statement usage
RULE9_1 = SMELLS_DEP_STM

#10 improper quote usage
RULE10_1 = "double quoted string containing no variables"
RULE10_2 = "unquoted file mode"
RULE10_3 = "quoted boolean value found"
RULE10_4 = "string containing only a variable"
RULE10_5 = "unquoted resource title"
RULE10_6 = "single quoted string containing a variable"
#11 Long statements
RULE11_1 = "line has more than 80 characters"
#12 incomplete conditional
RULE12_1 = SMELLS_MIS_ELS

#13 Unguarded variable
RULE13_1 = "variable not enclosed in {}"

HEADER = "RepoName,MissingDefault,InconsistentNaming,ComplexExpression,DuplicateEntity,MisplacedAttribute,ImproperAlignment,\
InvalidProperty,IncompleteTasks,DeprecatedStatement,ImproperQuoteUsage,LongStatement,IncompleteConditional,UnguardedVariable\n"

REPO_ROOT = "/Users/user/Desktop/puppetAnalysis"
AGGREGATOR_FILE = "PuppetLintAggregatedOutput.csv"
PUPPETLINT_OUT_FILE = "puppet-lint.log"





REPO_ROOT = "/Users/Tushar/Documents/Research/PuppetQuality/Repos"
AGGREGATOR_FILE = "AggregatedOutput.csv"
CSV_HEADER = "Repo_name,PuppetFileCount,ClassCount,DefineCount,FileResourceCount,PackageResourceCount,\
                     ServiceResourceCount,ExecCount,LOC,MultifacetedAbs,UnnecessaryAbs\n"
PUPPETEER_OUT_FILE = "Puppeteer_output.txt"
PUPPET_FILE_COUNT = "Puppet file count: "
TOTAL_CLASS_DECLS = "Total class declarations: "
TOTAL_DEFINE_DECLS = "Total define declarations: "
TOTAL_FILE_RES_DECLS = "Total file declarations: "
TOTAL_PACKAGE_RES_DECLS = "Total package declarations: "
TOTAL_SERVICE_RES_DECLS = "Total service declarations: "
TOTAL_EXEC_DECLS = "Total exec declarations: "
TOTAL_LOC = "Total LOC: "

DEBUG_ON = False

SMELL_MUL_ABS_1 = "Multifaceted Abstraction - Form 1"
SMELL_MUL_ABS_2 = "Multifaceted Abstraction - Form 2"
SMELL_UNN_ABS = "Unnecessary Abstraction"

FILE_RES = " File "
SERVICE_RES = " Service "
PACKAGE_RES = " Package "
CLASS_RES = " Class "
DEFINE_RES = " Define "

LCOM_THRESHOLD = 0.7
SIZE_THRESHOLD_UNNABS = 2
LOC_THRESHOLD_UNNABS = 3
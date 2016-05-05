from getpass import getuser

#REPO_ROOT = "/Users/%s/Documents/Research/PuppetQuality/popularRepoStore" % getuser()
REPO_ROOT = "/Users/user/Desktop/puppetAnalysis"
AGGREGATOR_FILE = "AggregatedOutput.csv"
CSV_HEADER = "Repo_name,PuppetFileCount,ClassCount,DefineCount,FileResourceCount,PackageResourceCount,\
ServiceResourceCount,ExecCount,LOC,MultifacetedAbs,UnnecessaryAbs,ImperativeAbs,MissingAbs,\
InsufficientMod,UnstructuredMod,TightlyCoupledMod,DuplicateAbs,MissingDep,BrokenHie,HairballStr,\
DeficientEnc,WeakendMod\n"

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
SMELL_IMP_ABS = "Imperative Abstraction"
SMELL_MIS_ABS = "Missing Abstraction"
SMELL_INS_MOD_1 = "Insufficient Modularization - Form 1"
SMELL_INS_MOD_2 = "Insufficient Modularization - Form 2"
SMELL_INS_MOD_3 = "Insufficient Modularization - Form 3"
SMELL_UNS_MOD_1 = "Unstructured Module - Form 1"
SMELL_UNS_MOD_2 = "Unstructured Module - Form 2"
SMELL_UNS_MOD_3 = "Unstructured Module - Form 3"
SMELL_TC_MOD = "Tightly-coupled Module"
SMELL_DUP_ABS = "Duplicate Abstraction"
SMELL_BRO_HIE = "Broken Hierarchy"
SMELL_MIS_DEP = "Missing Dependency"
SMELL_HAI_STR = "Hairball Structure"
SMELL_DEF_ENC = "Deficient Encapsulation"
SMELL_WEA_MOD = "Weakend Modularity"

FILE_RES = " File "
SERVICE_RES = " Service "
PACKAGE_RES = " Package "
CLASS_RES = " Class "
DEFINE_RES = " Define "
MODULE_RES = " Module "
REPO_RES = " Repo "
NODES_RES = " Node "
REPO_MANIFEST = " Manifest(Repo) "
MODULE_MANIFEST = " Manifest(Module) "
OTHERFILES = " Others "

MODULES = "modules"
MANIFESTS = "manifests"

LCOM_THRESHOLD = 0.7
SIZE_THRESHOLD_UNNABS = 2
LOC_THRESHOLD_UNNABS = 3
IMPABS_THRESHOLD = 0.2
IMPABS_MAXEXECCOUNT = 2
MISABS_MAX_NON_ABS_COUNT = 2
MAX_CLASS_LOC_THRESHOLD = 40
MAX_DEFINE_LOC_THRESHOLD = MAX_CLASS_LOC_THRESHOLD
MAX_MODULE_LOC_THRESHOLD = MAX_CLASS_LOC_THRESHOLD * 2
MAX_NESTING_DEPTH = 3
MAX_MANIFESTS_PUPPET_FILES = 5
MAX_ALLOWED_NONSTANDARD_FILES = 3
MAX_GRAPH_DEGREE_THRESHOLD = 0.5
MODULARITY_THRESHOLD = 1.0

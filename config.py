
lr = 0.01
batch_size= 512
reg_l1 = 2e-3
reg_l2 = 0
k = 5
# set the path-to-files
TRAIN_FILE = "./data/train_feature.csv"
TEST_FILE = "./data/test_feature.csv"

SUB_DIR = "./output"


OH_COLS = ['LBS','age','carrier','consumptionAbility','education','gender','house','os','ct','marriageStatus','advertiserId','campaignId', 'creativeId',
       'adCategoryId', 'productId', 'productType'
    # # binary
#,
    #"appIdAction", "appIdInstall"
]

CV_COLS = ['appIdAction','appIdInstall','interest1','interest2','interest3','interest4','interest5','kw1','kw2','kw3','topic1','topic2','topic3'
    #"id", "target",

]

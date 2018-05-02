import pandas as pd
import numpy as np
import config
from sklearn.feature_extraction.text import CountVectorizer

class FeatureDictionary(object):
    def __init__(self, dfTrain=None, dfTest=None, cv_cols=[], oh_cols=[]):
        self.dfTrain = dfTrain
        self.dfTest = dfTest
        self.cv_cols = cv_cols
        self.oh_cols = oh_cols
        self.gen_feat_dict()

    def gen_feat_dict(self):
        dfTrain = self.dfTrain
        dfTest = self.dfTest
        df = pd.concat([dfTrain, dfTest])
        self.feat_dict = {}
        
        # oh_tc = 0
        # cv_tc = 0
        tc = 0
        max_cols = 0
        cv=CountVectorizer()
        for col in df.columns:
            #print(1111111111)
            if col in self.cv_cols:
                # map to a single index
                cv.fit(df[col])
                item_names = cv.get_feature_names()
                field_len = len(item_names)
                self.feat_dict[col] = dict(zip(item_names, range(tc, field_len+tc)))
                tc +=field_len
                if col == 'interest1':
                    print('interest1')
                    print(item_names)
                    if '6' in item_names:
                        print('6 zai li mian')
                if field_len > max_cols:
                    max_cols = field_len
                # cv_tc += len(item_names)
            elif col in self.oh_cols:# oh_cols
                us = df[col].unique()
                self.feat_dict[col] = dict(zip(us, range(tc, len(us)+tc)))#label_encoder()
                tc += len(us)
            print
                # oh_tc += len(us)
        # self.cv_feat_dim = cv_tc
        # self.oh_feat_dim = oh_tc
        self.max_cols = max_cols
        self.all_feat_dim = tc


def sparse_representation(sample, fields_dict, array_length, max_cols):
    array = np.zeros([array_length + 1])
    array[array_length] = sample['label']
    temp_idx = np.zeros((1, 2), int)
    idx = []
    sp_value =[]
    tc = 0
    #tf = 0
    for field in fields_dict:

        if field in config.OH_COLS:

            field_value = sample[field]
            if field in fields_dict[field]:
                ind = fields_dict[field][field_value]
                array[ind] = 1
                temp_idx = [tc,0]
                sp_value.append(ind)
            else:
                temp_idx = [tc,0]
                sp_value.append(max_cols)
            #tf = tf+len(fields_dict[field])
            tc += 1

            idx.append(temp_idx)

        elif field in config.CV_COLS:

            field_value = sample[field]
            t = 0
            for value in str(field_value).split(' '):
                if value in fields_dict[field]:
                    ind = fields_dict[field][value]
                    array[ind] = 1
                    temp_idx = [tc,t]
                    sp_value.append(ind)
                else:
                    temp_idx = [tc,t]
                    sp_value.append(max_cols)
                t += 1
                idx.append(temp_idx)
            
            #tf = tf+len(fields_dict[field])
            tc += 1

    # sp_idx = np.array(idx)
    # sp_v = np.array(sp)
    # print(temp)
    # print('last idx', temp_idx)
    # print(np.array(idx).shape)
    # print(idx[10])
    return array, idx, sp_value


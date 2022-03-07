import os
import sys
import pandas as pd
import copy

from utility.helper import *
from utility.batch_test import *   

loss_loger, pre_loger, rec_loger, ndcg_loger, hit_loger = [], [], [], [], []

for epoch in range(args.epoch):
    for idx in range(n_batch):
        t0 = time()
        users_to_test = list(data_generator.test_set.keys())
        ret = test(sess, model, users_to_test, drop_flag=True)

        t1 = time()

        loss_loger.append(loss)
        rec_loger.append(ret['recall'])
        pre_loger.append(ret['precision'])
        ndcg_loger.append(ret['ndcg'])
        hit_loger.append(ret['hit_ratio'])
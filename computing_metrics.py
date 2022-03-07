# TODO:
# 计算Recall、Hit、NDCG
# 需要用每个user的embedding与所有item的embedding相乘，得到每个user与其他item的连边。然后这样再算recall与ndcg。

# 1. 记录所有user 的embedding
# 2. 记录所有item 的embedding
# 相乘得到这个二维矩阵，每个元素表征这个边上存在的概率
# 然后算指标


parser.add_argument('--Ks', nargs='?', default='[10, 50, 100]', help='K for Top-K list')

result = {'precision': np.zeros(len(Ks)), 'recall': np.zeros(len(Ks)), 'ndcg': np.zeros(len(Ks)),
              'hit_ratio': np.zeros(len(Ks)), 'auc': 0.}

user_batch_rating_uid = zip(rate_batch, user_batch)
batch_result = test_one_user(user_batch_rating_uid)

for re in batch_result:
            result['precision'] += re['precision']/n_test_users
            result['recall'] += re['recall']/n_test_users
            result['ndcg'] += re['ndcg']/n_test_users
            result['hit_ratio'] += re['hit_ratio']/n_test_users
            result['auc'] += re['auc']/n_test_users

return result
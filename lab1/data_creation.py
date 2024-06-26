import numpy as np
import pandas as pd
import os

def generate_data(items_cnt = 1000, base_value = 15, noize_coeff = 0.2):
    
    base_data = np.random.normal(loc=base_value, size=items_cnt)
    noize_data = np.random.normal(loc=base_value*3, scale=noize_coeff*100, size=(int(items_cnt*noize_coeff)))
    
    is_noize = np.zeros(len(base_data) + len(noize_data), dtype=int)
    is_noize[items_cnt:] = 1

    result_data = {
        'temp': np.concatenate((base_data, noize_data)),
        'is_noize': is_noize,
    }

    return result_data
    

os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

print('start: create train data')
train_data = generate_data(items_cnt = 1000)
df_train = pd.DataFrame(train_data)
df_train.to_csv('train/train_data.csv', index=False)
print('finish: create train data')

print('start: create test data')
test_data = generate_data(items_cnt = 300)
df_test = pd.DataFrame(test_data)
df_test.to_csv('test/test_data.csv', index=False)
print('finish: create test data')
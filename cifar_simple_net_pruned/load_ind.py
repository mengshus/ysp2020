import numpy as np
npz_file = 'cifar10_custom_filter_top1-83.880_ind.npz'
load_ind = np.load(npz_file)
for k in load_ind.files:
    print('{}, {} filters preserved'.format(k, len(load_ind[k])))
    print(load_ind[k])
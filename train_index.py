import sys
import utils
import params
import numpy as np
import pickle
import os

from sklearn.neighbors import BallTree
from scipy.spatial.distance import cosine


ficheros = utils.getFiles(params.DESCRIPTORS_FOLDER)
arrays = utils.loadNumpyArrays(ficheros)

if params.USE_PCA:
    from sklearn.decomposition import PCA
    pca = PCA(n_components = 100)
    pca.fit(arrays)
    arrays = pca.transform(arrays)
    with open('./INDEX/pca.pickle','wb') as handle:
        pickle.dump(pca, handle, 2)

tree = BallTree(arrays,leaf_size=40, metric=cosine)
with open('./INDEX/index.pickle','wb') as handle:
    pickle.dump(tree, handle, 2) 

print('INDEX  SAVED')
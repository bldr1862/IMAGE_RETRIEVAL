import utils
import params
import pickle
import matplotlib.pyplot as plt
import numpy as np

query_descriptor = utils.getDescriptor(params.QUERY_IMAGE)

if params.USE_PCA:

    with open('./INDEX/pca.pickle','rb') as handle:
        pca = pickle.load(handle)

with open('./INDEX/index.pickle','rb') as handle:
    tree = pickle.load(handle)

query_descriptor = pca.transform(query_descriptor)
dist, idxs = tree.query(query_descriptor[0], k=params.K)

ficheros = utils.getFiles(params.DATABASE_FOLDER)
selected_images = np.asarray(ficheros)[idxs]

plt.figure()
img = plt.imread(params.QUERY_IMAGE)
plt.imshow(img)


f, ax = plt.subplots(int(params.K/3) + 1, 3)

row = 0
column = 0
for i, image in enumerate(selected_images[0]):
    img = plt.imread(image)
    ax[row,column].imshow(img)
    ax[row,column].set_title(str(i+1)+ ' MATCH')
    if column == 2:
        row = row + 1
        column = 0
    else:
        column = column + 1

plt.tight_layout()
plt.show()
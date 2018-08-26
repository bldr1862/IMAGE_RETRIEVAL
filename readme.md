# IMAGE RETRIEVAL

En params.py se debe definir la carpeta donde estan las imagenes, la carpeta donde se guardaran los descriptores, la imagen de consulta y un flag para el uso de pca y el numero de vecinos

Primero se deben crear los descriptores con get_descriptors.py, luego de debe construir el indice con train_index.py y finalmente con retrieval se obtienen los vecinos mas cercanos data una imagen
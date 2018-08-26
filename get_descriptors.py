import utils
import params

ficheros = utils.getFiles(params.DATABASE_FOLDER)
utils.getDescriptors(ficheros, params.DESCRIPTORS_FOLDER,'vgg16')
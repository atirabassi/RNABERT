
import numpy as np
import h5py
filepath='path/to/emb.hdf5'
f = h5py.File(filepath,'r')
#uncomment next line to get all the ids
#f.keys()
#for 1 id:
id_emb='AE013139.1_7801-7700'
array=f[id_emb]['embedding'][:]
#for many ids you can run a for or while
list_of_ids=[] #fill machting ids and indices

for id in list_of_ids:
    print(f[id]['embedding'][:])
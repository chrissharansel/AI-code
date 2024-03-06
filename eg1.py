import numpy as np
from sklearn import preprocessing
inputdata=np.array([[5.1,-3.4,5.6],[-3.4,3.6,-9.2],[7.3,-9.9,-4.5]])
databinarized=preprocessing.Binarizer(threshold=2.1).transform(inputdata)
print("binarized data\n",databinarized)

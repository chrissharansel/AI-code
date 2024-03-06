#binarzing data(siting grater than 2 to 1 and lesser to 0)
import numpy as np
from sklearn import preprocessing
indata=np.array([[5.1,-2,3],[5.6,2,-2],[3.4,1.2,2],[1,-4,-8]])
print(indata,"\n\n")
dabin=preprocessing.Binarizer(threshold=2.1).transform(indata)
print("\n binarized data:\n",dabin)
print("\n\n")

#find mean & SD
print("\nBEFORE:")
print("Mean=",indata.mean(axis=0))
print("Std deviation=",indata.std(axis=0))
print("\n\n")

#makeing indata to be scaled and calculating mean & SD
data_scaled=preprocessing.scale(indata)
print("\nAFTER:")
print("Mean=",data_scaled.mean(axis=0))
print("Standatrd deviation=",data_scaled.std(axis=0))
print("\n\n")

#scaling and finding mean & SD
data_scaler_minmax=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax=data_scaler_minmax.fit_transform(indata)
print("\nMin Max scaled data=\n",data_scaled)
print("\n\n")

#normalizing data
data_normalized_l1=preprocessing.normalize(indata,norm='l1')
data_normalized_l2=preprocessing.normalize(indata,norm='l2')
print("L1 Normalized data=\n",data_normalized_l1)
print("L2 Normalized data=\n",data_normalized_l2)

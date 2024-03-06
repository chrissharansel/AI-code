import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from utilities import visualize_classifier
input_file='gdpWorld.csv'
data=np.loadtxt(input_file,delimiter=',')
X,y=data[:,:-1],data[:,-1]
classifier=GaussianNB
classifier.fit(x,y)
y_pred=classifier.predict(X)
accuracy=100.0*(y==y_pred).sum()/X.shape[0]
print("Accuracy of naive bayes classifier=",round(accuracy,2),"%")
visualize_classifier(classifier,X,y)
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2,random_state=3)
classfier_new=GuassianNB()
classifier_new.fit(X_train,y_train)
y_test_pred=classifier_new.predict(X_test)
accuracy=100.0*(y_test==y_test_pred).sum()/X_test.shape[0]
print("Accuracy of new classfier=",round(accuracy,2),"%")
visualize_classfier(classfier_new,X_test,y_test)
num_folds=3
accuracy_values=crossvalidation.cross_vals_score(classifier,X,y,scoring='accuracy',cv=num_folds)
print("Accuracy:"+str(round(100*accuracy_values.mean(),2))+"%")

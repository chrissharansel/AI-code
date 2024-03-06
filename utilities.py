import numpy as np
import matplotlib.pyplot as plt
#func def,labels inuput parameter
def visualize_classifier(classifier,X,y):
 #min and max value to evaluate funtion and to define boundries of fn&visualiuze boundries of classes
    min_x, max_x=X[:,0].min()-1.0, X[:,0].max()+1.0
    min_y, max_y=X[:,1].min()-1.0, X[:,1].max()+1.0
#define step size of grid and create using min and max value
    mesh_step_size=0.01
#run classifire on grid and reshape
    x_vals,y_vals=np.meshgrid(np.arange(min_x,max_x,mesh_step_size),np.arange(min_y, max_y, mesh_step_size))

    output=classifier.predict(np.c_[x_vals.ravel(),y_vals.ravel()])
    output=output.reshape(x_vals.shape)
    plt.figure()
    plt.pcolormesh(x_vals,y_vals,output,cmap=plt.cm.gray)
    plt.scatter(X[:,0],X[:,1],c=y,s=75,edgecolors='black',linewidth=1,cmap=plt.cm.Paired)
    plt.xlim(x_vals.min(),x_vals.max())
    plt.ylim(y_vals.min(),y_vals.max())
    plt.xticks((np.arange(int(X[:,0].min()-1),int(X[:,0].max()+1),1.0)))
    plt.yticks((np.arange(int(X[:,1].min()-1),int(X[:,0].max()+1),1.0)))
    plt.show()

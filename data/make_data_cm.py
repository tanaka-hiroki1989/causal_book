import numpy as np
from numpy.random import *
from scipy.special import expit
import pandas as pd

def make_data(num_data=200):
    x_1=np.random.randint(15,76,num_data) #age
    x_2=np.random.randint(0,2,num_data) #sex, 0:female,1:male
    
    e_z = randn(num_data)
    z_base = x_1 + (1-x_2)*10 - 40 + 5*e_z
    z_prob = expit(0.1*z_base)
    Z = np.array([choice(2, size=1, p=[1-z_prob[i], z_prob[i]])[0] for i in range(num_data)])
    e_y = randn(num_data)
    Y = -x_1 + 30*x_2 + 10*Z + 80 + 10*e_y
    
    data = np.array([[x_1[i],x_2[i],Z[i],Y[i]]for i in range(num_data)])
    return data

data = make_data(200)
np.savetxt("cm_purchase.csv",
           X=data,
           fmt=["%d", "%d", "%d","%f"],
           delimiter=","
)
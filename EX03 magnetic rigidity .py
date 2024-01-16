#!/usr/bin/env python
# coding: utf-8

# In[1]:


#code for examples given in the Ex03

import numpy as np

def get_rigidity(KE, m0, q):
    import math 
    c = 3e8  # m/s
    
    # Calculating rest Mass in kilogram and MeV
    m0_kg = m0 * 1.66e-27   #kilogram
    m0 = m0 * 931.5   #Mev
    
    
    # calculating the Gamma, Betta and Charge in SI units
    Gamma = (KE / m0) + 1
    Betta = math.sqrt ( 1-(1 / (Gamma ** 2)))
    q = q * 1.6e-19
    
    # Calculating the Magnetic rigidity in T.m
    Mag_rig = (Gamma * Betta * c * m0_kg ) / q
    return Mag_rig


# Use np.vectorize to create a vectorized version of the function
vectorized_get_rigidity = np.vectorize(get_rigidity)

# Input arrays
KE_values = np.array([45220, 80753.6 , 10000])
m0_values = np.array([238.05, 196.96 , 0.0005485])
q_values = np.array([28, 77 , 1])

# Calculate magnetic rigidities for each case using the vectorized function
Magnetic_rigidities = vectorized_get_rigidity(KE_values, m0_values, q_values)

# Print the results
for i, Mag_rig in enumerate(Magnetic_rigidities):
    print(f'Magnetic rigidity for case {i + 1}: {round(Mag_rig, 3)} T.m')



# In[ ]:





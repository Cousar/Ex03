#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def get_rigidity(KE, m0, q):
    import math 
    c = 3e8  # m/s
    
    # calculating KE and rest Mass in Joules
    KE_jouls = KE * m0 * 1.6e-19 * 1e06    # Joule
    m0c2_jouls = m0 * 931.5 * 1.6e-19 * 1e06    # Joule
    
    # calculating the Momentum and Charge in SI units
    p = np.sqrt(((KE_jouls ** 2) + (2 * KE_jouls * m0c2_jouls)) / c**2) 
    q = q * 1.6e-19
    
    # calculating the Magnetic rigidity in T.m
    Mag_rig = p / q
    return Mag_rig

# Use np.vectorize to create a vectorized version of the function
vectorized_get_rigidity = np.vectorize(get_rigidity)

# Input arrays
KE_values = np.array([190, 409.91, 18300000])
m0_values = np.array([238.05, 196.96, 5.48e-4])
q_values = np.array([28, 77, 1])

# Calculate magnetic rigidities for each case using the vectorized function
Magnetic_rigidities = vectorized_get_rigidity(KE_values, m0_values, q_values)

# Print the results
for i, Mag_rig in enumerate(Magnetic_rigidities):
    print(f'Magnetic rigidity for case {i + 1}: {round(Mag_rig, 3)} T.m')


# In[ ]:





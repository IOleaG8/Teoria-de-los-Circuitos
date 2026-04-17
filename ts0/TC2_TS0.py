"""
Created on Sat April 11 18:06 2026

@author: ignacio
"""
# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot


# Ejemplo:
#    
#           H(s) = (s + 1) / (s^2 + 3s + 2)
#
#           num = [1, 1]       # s + 1
#           den = [1, 3, 2]    # s^2 + 3s + 2
#           H = TransferFunction(num, den)


# Variables y Transferencia
#           T($) = ( $ - R2/R1 ) / ( $ + 1 )

R1 = 200
R2 = 200

rel = R2 / R1

my_tf = TransferFunction( [1,-rel], [1,1] )

# Gráficos

bodePlot(my_tf, fig_id=1, filter_description = rf"$\frac{{R_2}}{{R_1}} = {rel:.2f}$" )
#fig = plt.figure(1)
#fig.axes[0].set_ylim(-2, 2)

pzmap(my_tf, fig_id=2, filter_description = rf"$\frac{{R_2}}{{R_1}} = {rel:.2f}$") #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3, filter_description = rf"$\frac{{R_2}}{{R_1}} = {rel:.2f}$")


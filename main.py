import matplotlib.pyplot as plt
import numpy as np
import csv

from scipy.interpolate import CubicSpline, splrep, BSpline,splev
from matplotlib import cm
#adding x and y footage and channel numbers
Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/x_coordinates_Joint 216730 - Dent 000080.csv')
x_data=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/y_coordinates_Joint 216730 - Dent 000080.csv')
y_data=np.genfromtxt(Data,delimiter=",",dtype=float)

Data=open('/Users/Irving/Programming/Python Projects/Splinesparametric/Joint 216730 - Dent 000080.csv')
z_data=np.genfromtxt(Data,delimiter=",",dtype=float)

x_new=np.arange(x_data[0],x_data[len(x_data)-1],0.1)


#CALCULATE SPLINE FOR DATA SET
for iterator in range(len(z_data)):
    spline_coefficients=splrep(x_data,z_data[iterator],k=3,s=0.05)
    spline=BSpline(*spline_coefficients,extrapolate=True)(x_new)
    if(iterator==0):
        cubic_final=spline
    else:
        cubic_final=np.vstack((cubic_final,spline))
    # if(iterator==31):
    #     plt.scatter(x_data, z_data[iterator])
    #     plt.plot(x_new, cubic_final[iterator],"-",color="red")
    #     plt.show()

x_spline,y_spline=np.meshgrid(x_new,y_data)
# ax = plt.axes(projection ='3d')
# ax.plot_surface(x_spline,y_spline,cubic_final,cmap="magma", linewidth=0, antialiased=False, alpha=0.5)
plt.pcolormesh(x_spline,y_spline,cubic_final)


fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection="3d")
ax.plot_surface(x_spline, y_spline, cubic_final, rstride=1, cstride=1, cmap=cm.Greens,
                       linewidth=0, antialiased=False)

ax.set_zlim(-0.25,2)
ax.set_ylabel("Channel", fontsize=10)
ax.set_xlabel("Distance [ft]", fontsize=10)
ax.set_zlabel("Inflection [inches]", fontsize=10)
plt.show()
# plt.scatter(x_data,z_data[38])
# plt.scatter(x_data,)
# plt.show()
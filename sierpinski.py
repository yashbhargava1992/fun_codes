import numpy as np
import matplotlib.pyplot  as plt


# Sierpinski triangle.

# Given three original points, choose a point randomly inside a triangle.
# Now select the next point which is midway between the previous point and any one of the original point


def distance_computer (x1,y1,x2,y2):
	return np.sqrt((x1-x2)**2+(y1-y2)**2)

def midpoint (x1,x2):
	return (x1+x2)/2
	

# Selecting the initial triangle. Currently set to equilateral triangle of length 1

init_x = np.array([0,1,0.5])
init_y = np.array([0,0,np.sqrt(0.75)])

# PLotting the triangle
plt.figure(figsize=(4,4))
plt.plot(init_x,init_y, '.')
plt.xlim(-0.1,1.1)
plt.ylim(-0.1,1.1)


# Selecting a random point inside the triangle. Note the dependency of the y range on the x selection. 

g1_x = np.random.uniform(0,1)

if g1_x<=0.5: 	g1_y = np.random.uniform(0, g1_x*np.sqrt(3))
else: 	g1_y = np.random.uniform(0, (1-g1_x)*np.sqrt(3))

print (g1_x,g1_y)

# Selecting how many points should be mapped from the initial guess. 
number_of_runs = 10000

gx_array = np.zeros(number_of_runs)
gy_array = np.zeros(number_of_runs)

gx_array[0] = g1_x
gy_array[0] = g1_y


for i in range(1,number_of_runs):
	sel_point = np.random.randint(3)		# Selecting one of the initial three points. 
	
	# determining the midpoint
	
	mdx = midpoint(gx_array[i-1], init_x[sel_point])
	mdy = midpoint(gy_array[i-1], init_y[sel_point])
	gx_array[i] = mdx
	gy_array[i] = mdy

# Plotting the sierpinski fractal.

plt.plot(gx_array,gy_array, '.C2', markersize=1/np.log10(number_of_runs)) # the marker size is adjusted based on the number of points mapped. Larger the number of points, smaller the marker size
plt.xticks([])
plt.yticks([])
plt.show()

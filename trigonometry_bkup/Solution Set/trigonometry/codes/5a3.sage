x1,x2=var('x1,x2')
f=(x1-8)^2+(x2-6)^2#Objective function
g=x1+x2-18#Constraint 1
h=Graphics()#Creating an empty Graphics object
#region plot of constraint
h1=region_plot(g==0,(x1,0,15),(x2,0,15),incol='black')
for c in range(0,10):
#Plotting Series fo circles of radii ranging from 0 to 7.07
    h=h+implicit_plot(f-(c^2)/2,(x1,0,15),(x2,0,15))
h=h+h1#Adding both the plots into the graphics window
h.show()
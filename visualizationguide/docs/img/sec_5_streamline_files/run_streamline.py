import numpy as np
from visit import *

R = 5.; num_samples = 10
thetas = np.linspace(0, np.pi, num_samples)
phis = np.linspace(0, 2*np.pi, num_samples)
points = []
for phi in phis:
    for theta in thetas:
        x = R*np.cos(phi)*np.sin(theta)
        y = R*np.sin(phi)*np.sin(theta)
        z = R*np.cos(theta)
        points.extend([x, y, z])
        
OpenDatabase("sample_vector_field.vtk")
AddPlot("Pseudocolor", "vec_field")
AddOperator("IntegralCurve")

p = PseudocolorAttributes()
p.minFlag = 1; p.min = 0
SetPlotOptions(p)
l = IntegralCurveAttributes(); l.sourceType = l.PointList
l.pointList = tuple(points); l.integrationDirection = l.Both
SetOperatorOptions(l)

c = View3DAttributes()
c.viewNormal = (1.0, -0.35, 0.35); c.viewUp = (0, 0, 1)
SetView3D(c)
s = SaveWindowAttributes(); s.format = s.PNG
s.outputToCurrentDirectory = 1; s.fileName = "streamline_fol/output"
SetSaveWindowAttributes(s)
DrawPlots()
SaveWindow()
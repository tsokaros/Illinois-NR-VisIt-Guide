OpenDatabase("/path/to/data/h_*.vtk", 0)

AddPlot("Pseudocolor", "GW-FIELD")
Pseudo = PseudocolorAttributes()
Pseudo.colorTableName = "constant_colortable"
Pseudo.minFlag = 1; Pseudo.min = -100
Pseudo.maxFlag = 1; Pseudo.max = 100
Pseudo.smoothingLevel = 1 #(0, NONE); (1, Fast); (2, High)
Pseudo.legendFlag = 0
SetPlotOptions(Pseudo)
plots = [0]

AddPlot("Mesh", "mesh")
m = MeshAttributes()
m.foregroundFlag = 0; m.legendFlag = 0; m.smoothingLevel = m.Fast
SetPlotOptions(m)
plots += [1]

SetActivePlots(tuple(plots))

AddOperator("Resample")
rAtts = ResampleAttributes()
rAtts.is3D = 0; rAtts.samplesX = 200; rAtts.samplesY = 200
SetOperatorOptions(rAtts)

AddOperator("Elevate")
elevAtts = ElevateAttributes()
elevAtts.variable = "GW-FIELD"; elevAtts.useXYLimits = elevAtts.Never
SetOperatorOptions(elevAtts)

AddOperator("Cylinder")
CylinderAtts = CylinderAttributes()
CylinderAtts.point1 = (0, 0, 10000); CylinderAtts.point2 = (0, 0, -10000)
CylinderAtts.radius = wave_zone_r; CylinderAtts.inverse = 1
SetOperatorOptions(CylinderAtts)

SetActivePlots(0)
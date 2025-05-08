from visit import *

# plotting density data with isosurface rendering


#adding the pseudocolorplot
# loading the density data into visit
densityplot = ActivateDatabase(Path_to_Density_data)

#loading up the pseudocolorplot xml settings into the plot -> GUI equivilant to changing the Pseudocolor plot settings through the dropdown menu 
LoadAttribute(Path_to_Pseudocolor_plot_xmlfile, densityplot)

# adding the pseudocolor plot 
AddPlot("Pseudocolor", "density")
SetActivePlots(plot_idxs.index("density"))
#loading up plotting data
SetPlotOptions(densityplot)

# Adding the Isosurface operator

#loading in the isosurface operator
iso = IsosurfaceAttributes()
#adding isosurface operator settings
LoadAttribute(Path_to_iso_xml, iso)
#adding operator to plot
AddOperator("Isosurface")
#making sure the plot has the operator xml settings
SetOperatorOptions(iso)

from visit import *


# volume rendering in VisIT

#loading in the density data into VisIT
ActivateDatabase(path_to_density_data)
#creating an instance where we could set the volume attributes
density_atts = VolumeAttributes()
#loading in our xml settings for the density attributes
LoadAttribute(path_to_volume_xml_file, density_atts)
#creating a volume plot with the logrho variable
AddPlot("Volume", "logrho")
SetActivePlots(plot_idxs.index("density"))
#making sure the volume plot has the proper settings
SetPlotOptions(rho_atts)

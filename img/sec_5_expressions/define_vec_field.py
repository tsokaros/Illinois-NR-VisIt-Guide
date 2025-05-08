OpenDatabase("/path/to/data/Bx.file_* database", 0, "CarpetHDF5_2.1")
OpenDatabase("/path/to/data/By.file_* database", 0, "CarpetHDF5_2.1")
OpenDatabase("/path/to/data/Bz.file_* database", 0, "CarpetHDF5_2.1")

DefineScalarExpression(Bx, "conn_cmfe(</path/to/data/Bx.file_* \
    database[0]id:MHD_EVOLVE--Bx>, <Carpet AMR-grid>)")
DefineScalarExpression(Bx, "conn_cmfe(</path/to/data/By.file_* \
    database[0]id:MHD_EVOLVE--By>, <Carpet AMR-grid>)")
DefineScalarExpression(Bx, "conn_cmfe(</path/to/data/Bz.file_* \
    database[0]id:MHD_EVOLVE--Bz>, <Carpet AMR-grid>)")

DefineVectorExpression("Bvec", "{Bx, By, Bz}")
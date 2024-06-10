import arcpy

input_database = r"C:\Users\samirv\Desktop\Model\Geodatabase_20240403.gdb"
Output = r"C:\Users\samirv\Desktop\Model\Output.gdb"
Error = r"C:\Users\samirv\Desktop\Model\Error.gdb"

layer_List = ["Auxiliary_Building","Building","Occupation","Parcel","Pay"]
Intersect_Output = ["intersect_Auxilary","intersect_Building","intersect_Occupation","intersect_Parcel","intersect_Pay"]

intersect_layer_and_field = ["intersect_Auxilary","intersect_Building","intersect_Occupation","intersect_Parcel","intersect_Pay",
                     "Building_Aux_Intersect","Pay_Zebt_Intersect"]



n = 0
while n<5:
    arcpy.analysis.Intersect([input_database+"/" + layer_List[n]],Output+"/"+Intersect_Output[n], 'ALL')
    print("Proses Davam edir...")

    n+=1


arcpy.analysis.Intersect([input_database+"/Auxiliary_Building",input_database+"/Building"],Output+"/Building_Aux_Intersect", 'ALL')

arcpy.analysis.Intersect([input_database+"/Pay",input_database+"/Occupation"],Output+"/Pay_Zebt_Intersect", 'ALL')
print("Proses Davam edir...")

arcpy.management.CopyFeatures(input_database+"\History_Parcel",Output+"\History_Parcel_copy")

n = 0
for field_name in intersect_layer_and_field:
    
    arcpy.analysis.Intersect([Output+"/"+intersect_layer_and_field[n],Output+"/History_Parcel_copy"],Output+"/History_{}".format(intersect_layer_and_field[n]), 'ALL')
    arcpy.management.AddField(Output+"/History_{}".format(intersect_layer_and_field[n]),field_name, 'TEXT')


    n+=1
print("Proses Davam edir...")
arcpy.env.workspace = Output
        
featureclasses = arcpy.ListFeatureClasses()

for fc in featureclasses:
    if fc == "History_intersect_Auxilary":
        arcpy.management.CalculateField(Output + "/" +fc, "intersect_Auxilary" ,'str(!USERNAME!) + "_intersect_Auxilary"', 'PYTHON3')

        arcpy.management.Dissolve(Output + "/" +fc, Output+"/History_intersect_Auxilary_Dissolve","intersect_Auxilary")

        arcpy.analysis.Split(Output+"/History_intersect_Auxilary_Dissolve", Output+"/History_intersect_Auxilary_Dissolve", 'intersect_Auxilary',Error)
        print("Proses Davam edir...")


    if fc == "History_intersect_Building":
        arcpy.management.CalculateField(Output + "/" +fc, "intersect_Building" ,'str(!USERNAME!) + "_intersect_Building"', 'PYTHON3')

        arcpy.management.Dissolve(Output + "/" +fc, Output+"/History_intersect_Building_Dissolve","intersect_Building")

        arcpy.analysis.Split(Output+"/History_intersect_Building_Dissolve", Output+"/History_intersect_Building_Dissolve", 'intersect_Building',Error)
        print("Proses Davam edir...")

    if fc == "History_intersect_Occupation":
        arcpy.management.CalculateField(Output + "/" +fc, "intersect_Occupation" ,'str(!USERNAME!) + "_intersect_Occupation"', 'PYTHON3')

        arcpy.management.Dissolve(Output + "/" +fc, Output+"/History_intersect_Occupation_Dissolve","intersect_Occupation")

        arcpy.analysis.Split(Output+"/History_intersect_Occupation_Dissolve", Output+"/History_intersect_Occupation_Dissolve", 'intersect_Occupation',Error)
        print("Proses Davam edir...")


    if fc == "History_intersect_Parcel":
        arcpy.management.CalculateField(Output + "/" +fc, "intersect_Parcel" ,'str(!USERNAME!) + "_intersect_Parcel"', 'PYTHON3')

        arcpy.management.Dissolve(Output + "/" +fc, Output+"/History_intersect_Parcel_Dissolve","intersect_Parcel")

        arcpy.analysis.Split(Output+"/History_intersect_Parcel_Dissolve", Output+"/History_intersect_Parcel_Dissolve", 'intersect_Parcel',Error)
        print("Proses Davam edir...")

    if fc == "History_intersect_Pay":
        arcpy.management.CalculateField(Output + "/" +fc, "intersect_Pay" ,'str(!USERNAME!) + "_intersect_Pay"', 'PYTHON3')

        arcpy.management.Dissolve(Output + "/" +fc, Output+"/History_intersect_Pay_Dissolve","intersect_Pay")

        arcpy.analysis.Split(Output+"/History_intersect_Pay_Dissolve", Output+"/History_intersect_Pay_Dissolve", 'intersect_Pay',Error)
        print("Proses Davam edir...")

    if fc == "History_Building_Aux_Intersect":
        arcpy.management.CalculateField(Output + "/" +fc, "Building_Aux_Intersect" ,'str(!USERNAME!) + "_Building_Aux_Intersect"', 'PYTHON3')

        arcpy.management.Dissolve(Output + "/" +fc,Output+"/History_Building_Aux_Intersect_Dissolve","Building_Aux_Intersect")

        arcpy.analysis.Split(Output+"/History_Building_Aux_Intersect_Dissolve", Output+"/History_Building_Aux_Intersect_Dissolve", 'Building_Aux_Intersect',Error)
        print("Proses Davam edir...")

    if fc == "History_Pay_Zebt_Intersect":
        arcpy.management.CalculateField(Output + "/" +fc, "Pay_Zebt_Intersect" ,'str(!USERNAME!) + "_Pay_Zebt_Intersect"', 'PYTHON3')

        arcpy.management.Dissolve(Output + "/" +fc, Output+"/History_Pay_Zebt_Intersect_Dissolve","Pay_Zebt_Intersect")

        arcpy.analysis.Split(Output+"/History_Pay_Zebt_Intersect_Dissolve", Output+"/History_Pay_Zebt_Intersect_Dissolve", 'Pay_Zebt_Intersect',Error)

  
print("Proses davam edir..")
arcpy.analysis.Erase(input_database+"/Whole_polygon", input_database+"/Parcel",Output+"/Whole_erase_poly")
arcpy.analysis.Intersect([Output+"\History_Parcel_copy",Output+"/Whole_erase_poly"],Output+"/Whole_erase_Intersect", 'ALL')

arcpy.management.CalculateField(Output+"/Whole_erase_Intersect", "USERNAME" ,'str(!USERNAME!) + "_Parcel_bosluq"', 'PYTHON3')

arcpy.analysis.SplitByAttributes(Output+"/Whole_erase_Intersect",Error,'USERNAME')



print("Proses bitdi...")

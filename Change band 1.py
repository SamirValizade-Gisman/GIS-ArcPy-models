import arcpy
import os

# Qovluq parametrini alırıq (script tool kimi işlədirsinizsə, 0-cı parametr olacaq)
folder = arcpy.GetParameterAsText(0)
if not folder:
    # Əgər parametr verilməyibsə, default olaraq aşağıdakı qovluq istifadə olunacaq
    folder = r"C:\Users\AGS_ASC\Desktop\Folder"

# İş sahəsini (workspace) təyin edirik
arcpy.env.workspace = folder

# Qovluqdakı həm .tif, həm də .tiff uzantılı faylları siyahıya alırıq
tif_files = arcpy.ListRasters("*.tif")
tiff_files = arcpy.ListRasters("*.tiff")

# Hər iki siyahını birləşdiririk (əgər hər hansı biri boşdursa, boş siyahı kimi qəbul edilir)
raster_files = (tif_files if tif_files else []) + (tiff_files if tiff_files else [])

# Hər bir raster faylı üçün band adlarını yeniləyirik
for raster_file in raster_files:
    arcpy.AddMessage(f"{raster_file} faylı işlənir...")
    try:
        rast = arcpy.Raster(raster_file)
        # Mövcud band adlarını yeni adlarla əvəzləyirik
        rast.renameBand('Band_1', 'Red')
        rast.renameBand('Band_2', 'Green')
        rast.renameBand('Band_3', 'Blue')
        arcpy.AddMessage(f"{raster_file} faylının band adları uğurla dəyişdirildi.\n")
    except Exception as e:
        arcpy.AddError(f"{raster_file} faylında band adlarını dəyişdirmək mümkün olmadı: {e}\n")

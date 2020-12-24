"""Find all dimensions are not divisible by 5 of selected sheet"""
__author__='NguyenKhanhTien - khtien0107@gmail.com'
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, ViewSheet, Dimension, DimensionSegment
from pyrevit import revit, DB
from pyrevit import forms

doc = __revit__.ActiveUIDocument.Document
all_dimension = FilteredElementCollector(doc).OfClass(Dimension)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

viewsheet = forms.select_sheets(button_name='Check Dim')
def CheckDim(dim):
	check=True
	if len(dim)<>0:
		end=len(dim)-1
		if dim[end] <> "0" and dim[end] <> "5" and dim.isnumeric(): 
			check=False
	return check

dimension=[]
count = 0
for dm in all_dimension:
    y=doc.GetElement(dm.OwnerViewId)
    if dm.NumberOfSegments > 1:
        check2=True
        for a in dm.Segments:
            if not CheckDim(a.ValueString) and y:
                if check2:
                    dimension.append(dm)
                #count +=1
                check2=False
    elif dm.NumberOfSegments == 1:
        x=dm.ValueString
        if x and not CheckDim(x) and y:
            dimension.append(dm)
            #count +=1

divide = "**********************************************************************************************************************"
divide2 = "----------------------------------------------------"
prompt=''

for di in dimension:
    e=doc.GetElement(di.OwnerViewId)
    for vs in viewsheet:
        for eid in vs.GetAllPlacedViews():
            ev=doc.GetElement(eid)
            if ev.Id == e.Id:
                if di.NumberOfSegments > 1:
                    for x in di.Segments:
                        if not CheckDim(x.ValueString):
                            prompt += ('\n' + x. ValueString)
                            count +=1
                            #print x.ValueString
                else:
                    prompt += ('\n' + di. ValueString)
                    count+=1
                    #print di.ValueString
                prompt += ('\n' + "ID: " + str(di.Id))
                prompt += ('\n' + e.Title)
                prompt += ('\n' + "Sheet " + vs.SheetNumber + ": " + vs.Name)
                prompt += ('\n' + divide2)
                #print e.Title
                #print ("Sheet " + vs.SheetNumber + ": " + vs.Name)
                #print (divide2)
                break

print("TOTAL: " + str(count))
print(divide)
print("VALUE & LOCATION:")
print(prompt)
                
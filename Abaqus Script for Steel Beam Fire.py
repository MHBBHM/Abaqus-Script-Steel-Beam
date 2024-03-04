from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

#Input_Data
h=300
b=300
w=11
f=19
L=4400

#Fire_Duration
T=2100 

#Mesh_Size_Input
m=10

#Help_Cordinate
x=0.5*b
y=0.5*h

#Constant_Property_of_Heat

mdb.models.changeKey(fromName='Model-1', toName='HEB 300')
mdb.models['HEB 300'].setValues(absoluteZero=-273.16, stefanBoltzmann=5.667e-11)

#Create Part by COORDINATE

mdb.models['HEB 300'].ConstrainedSketch(name='__profile__', sheetSize=2000.0)
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(x, y), 
    point2=(-x, y))
mdb.models['HEB 300'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[2])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(-x, y), 
    point2=(-x, y-f))
mdb.models['HEB 300'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['HEB 300'].sketches['__profile__'].geometry[3])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[3])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(-x, y-f), 
    point2=(-0.5*w, y-f))
mdb.models['HEB 300'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[4])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[3], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[4])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(-0.5*w, y-f), 
    point2=(-0.5*w, -y+f))
mdb.models['HEB 300'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['HEB 300'].sketches['__profile__'].geometry[5])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[4], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[5])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(-0.5*w, -y+f), 
    point2=(-x, -y+f))
mdb.models['HEB 300'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[6])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[6])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(-x, -y+f), 
    point2=(-x, -y))
mdb.models['HEB 300'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['HEB 300'].sketches['__profile__'].geometry[7])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[7])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(-x, -y), 
    point2=(x, -y))
mdb.models['HEB 300'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[8])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[7], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[8])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(x, -y), 
    point2=(x, -y+f))
mdb.models['HEB 300'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['HEB 300'].sketches['__profile__'].geometry[9])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[8], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[9])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(x, -y+f), 
    point2=(0.5*w, -y+f))
mdb.models['HEB 300'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[10])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[9], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[10])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(0.5*w, -y+f), 
    point2=(0.5*w, y-f))
mdb.models['HEB 300'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['HEB 300'].sketches['__profile__'].geometry[11])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[10], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[11])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(0.5*w, y-f), point2=
    (x, y-f))
mdb.models['HEB 300'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[12])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[11], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[12])
mdb.models['HEB 300'].sketches['__profile__'].Line(point1=(x, y-f), 
    point2=(x, y))
mdb.models['HEB 300'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['HEB 300'].sketches['__profile__'].geometry[13])
mdb.models['HEB 300'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[12], entity2=
    mdb.models['HEB 300'].sketches['__profile__'].geometry[13])
mdb.models['HEB 300'].Part(dimensionality=THREE_D, name='HEB', type=
    DEFORMABLE_BODY)
mdb.models['HEB 300'].parts['HEB'].BaseSolidExtrude(depth=L, sketch=
    mdb.models['HEB 300'].sketches['__profile__'])
del mdb.models['HEB 300'].sketches['__profile__']

#Create Datum plane

mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=100, 
    principalPlane=XYPLANE)
mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=(2*L+1100)/6, 
    principalPlane=XYPLANE)
mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=0.5*L, 
    principalPlane=XYPLANE)
mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=(4*L-1100)/6, 
    principalPlane=XYPLANE)
mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=L-100, 
    principalPlane=XYPLANE)  
mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=0.0, 
    principalPlane=XZPLANE)
mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=0.25*b, 
    principalPlane=YZPLANE)
mdb.models['HEB 300'].parts['HEB'].DatumPlaneByPrincipalPlane(offset=-0.25*b, 
    principalPlane=YZPLANE)
  
#Create Partition

mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.5*w, 0.5*y, 25), )), datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[2])
mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.5*w, 0.5*y, 0.6*L), )), datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[3])
mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.5*w, 0.5*y, 0.6*L), )), datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[4])
mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.5*w, 0.5*y, 0.6*L), )), datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[5])
mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.5*w, 0.5*y, L-25), )), datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[6])
mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.5*w, 0.5*y, 25), ), ((0.5*w, 0.5*y, 0.9*L), ), ((0.5*w, 0.5*y, 0.5*L-25), ), ((0.5*w, 0.5*y, 0.5*L+25), ), ((0.5*w, 0.5*y, 0.1*L), ), ((0.5*w, 0.5*y, L-25), ), ),
    datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[7])
mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.5*x, -y, 25), ), ((0.5*x, -y, 0.1*L), ), ((0.5*x, -y, 0.5*L-25), ), ((0.5*x, -y, 0.5*L+25), ), ((0.5*x, -y, 0.9*L), ), ((0.5*x, -y, L-25), ),
    ((0.5*x, y, 25), ), ((0.5*x, y, 0.1*L), ), ((0.5*x, y, 0.5*L-25), ), ((0.5*x, y, 0.5*L+25), ), ((0.5*x, y, 0.9*L), ), ((0.5*x, y, L-25), ), ), datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[8])
mdb.models['HEB 300'].parts['HEB'].PartitionCellByDatumPlane(cells=
    mdb.models['HEB 300'].parts['HEB'].cells.findAt(((-0.5*x, -y, 25), ), ((-0.5*x, -y, 0.1*L), ), ((-0.5*x, -y, 0.5*L-25), ), ((-0.5*x, -y, 0.5*L+25), ), ((-0.5*x, -y, 0.9*L), ), ((-0.5*x, -y, L-25), ),
    ((-0.5*x, y, 25), ), ((-0.5*x, y, 0.1*L), ), ((-0.5*x, y, 0.5*L-25), ), ((-0.5*x, y, 0.5*L+25), ), ((-0.5*x, y, 0.9*L), ), ((-0.5*x, y, L-25), ), ), datumPlane=mdb.models['HEB 300'].parts['HEB'].datums[9])

#Material Property Input

mdb.models['HEB 300'].Material(name='Steel')
mdb.models['HEB 300'].materials['Steel'].Conductivity(table=((53.3, 20.0), (
    50.7, 100.0), (47.3, 200.0), (44.0, 300.0), (40.7, 400.0), (37.4, 500.0), (
    34.0, 600.0), (30.7, 700.0), (27.3, 800.0), (27.3, 900.0), (27.3, 1000.0), 
    (27.3, 1100.0), (27.3, 1200.0)), temperatureDependency=ON)
mdb.models['HEB 300'].materials['Steel'].SpecificHeat(table=((439801760.0, 
    20.0), (487620000.0, 100.0), (529760000.0, 200.0), (564740000.0, 300.0), (
    605880000.0, 400.0), (666500000.0, 500.0), (760217391.3, 600.0), (
    1008157895.0, 700.0), (5000000000.0, 735.0), (803260869.6, 800.0), (
    650000000.0, 900.0), (650000000.0, 1000.0), (650000000.0, 1100.0), (
    650000000.0, 1200.0)), temperatureDependency=ON)
mdb.models['HEB 300'].materials['Steel'].Density(table=((7.85e-09, ), ))
mdb.models['HEB 300'].HomogeneousSolidSection(material='Steel', name=
    'Steel Section', thickness=None)

#Assign_Material_Property

mdb.models['HEB 300'].parts['HEB'].SectionAssignment(offset=0.0, offsetField=''
    , offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.75*x, -y, 25), ), ((0.75*x, -y, 0.1*L), ), ((0.75*x, -y, 0.5*L-25), ), ((0.75*x, -y, 0.5*L+25), ), ((0.75*x, -y, 0.9*L), ), ((0.75*x, -y, L-25), ),
    ((0.75*x, y, 25), ), ((0.75*x, y, 0.1*L), ), ((0.75*x, y, 0.5*L-25), ), ((0.75*x, y, 0.5*L+25), ), ((0.75*x, y, 0.9*L), ), ((0.75*x, y, L-25), ),
    ((-0.75*x, -y, 25), ), ((-0.75*x, -y, 0.1*L), ), ((-0.75*x, -y, 0.9*L ), ), ((-0.75*x, -y, 0.5*L-25), ), ((-0.75*x, -y, 0.5*L+25), ), ((-0.75*x, -y, L-25), ), 
    ((-0.75*x, y, 25), ), ((-0.75*x, y, 0.1*L), ), ((-0.75*x, y, 0.9*L), ), ((-0.75*x, y, 0.5*L-25), ), ((-0.75*x, y, 0.5*L+25), ), ((-0.75*x, y, L-25), ), 
    ((0.25*x, y, 25), ), ((0.25*x, -y, 25), ), ((0.25*x, y, 0.1*L), ), ((0.25*x, -y, 0.1*L), ), ((0.25*x, y, 0.9*L), ), ((0.25*x, -y, 0.9*L), ), ((0.25*x, y, L-25), ), ((0.25*x, -y, L-25), ), 
    ((0.25*x, y, 0.5*L+25), ), ((0.25*x, -y, 0.5*L+25), ), ((0.25*x, y, 0.5*L-25), ), ((0.25*x, -y, 0.5*L-25), ), )), sectionName='Steel Section', 
    thicknessAssignment=FROM_SECTION)
    
mdb.models['HEB 300'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['HEB 300'].rootAssembly.Instance(dependent=ON, name='HEB-1', part=
    mdb.models['HEB 300'].parts['HEB'])
    
#Step_Creation

mdb.models['HEB 300'].HeatTransferStep(deltmx=25.0, initialInc=10.0, maxInc=
    200.0, maxNumInc=1000000, minInc=0.00001*T, name='Fire', previous='Initial', 
    timePeriod=T)
mdb.models['HEB 300'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'NT', ))
    
#ISO834_Fire_Data
mdb.models['HEB 300'].TabularAmplitude(data=((0.0, 20.0), (30.0, 261.14), (
    60.0, 349.21), (90.0, 404.31), (120.0, 444.5), (150.0, 476.17), (180.0, 
    502.29), (210.0, 524.53), (240.0, 543.89), (270.0, 561.03), (300.0, 
    576.41), (330.0, 590.36), (360.0, 603.12), (390.0, 614.88), (420.0, 
    625.78), (450.0, 635.94), (480.0, 645.46), (510.0, 654.4), (540.0, 662.85), 
    (570.0, 670.84), (600.0, 678.43), (630.0, 685.65), (660.0, 692.54), (690.0, 
    699.13), (720.0, 705.44), (750.0, 711.49), (780.0, 717.31), (810.0, 
    722.91), (840.0, 728.31), (870.0, 733.52), (900.0, 738.56), (930.0, 
    743.43), (960.0, 748.15), (990.0, 752.73), (1020.0, 757.17), (1050.0, 
    761.48), (1080.0, 765.67), (1110.0, 769.75), (1140.0, 773.72), (1170.0, 
    777.59), (1200.0, 781.35), (1230.0, 785.03), (1260.0, 788.62), (1290.0, 
    792.13), (1320.0, 795.55), (1350.0, 798.9), (1380.0, 802.17), (1410.0, 
    805.38), (1440.0, 808.52), (1470.0, 811.59), (1500.0, 814.6), (1530.0, 
    817.56), (1560.0, 820.45), (1590.0, 823.29), (1620.0, 826.08), (1650.0, 
    828.82), (1680.0, 831.5), (1710.0, 834.14), (1740.0, 836.74), (1770.0, 
    839.29), (1800.0, 841.8), (1830.0, 844.26), (1860.0, 846.69), (1890.0, 
    849.08), (1920.0, 851.43), (1950.0, 853.74), (1980.0, 856.02), (2010.0, 
    858.26), (2040.0, 860.48), (2070.0, 862.66), (2100.0, 864.8)), name='Fire', 
    smooth=SOLVER_DEFAULT, timeSpan=STEP)
    

#Mesh_Create
mdb.models['HEB 300'].parts['HEB'].seedPart(deviationFactor=0.1, minSizeFactor=
    0.1, size=m)
mdb.models['HEB 300'].parts['HEB'].generateMesh()
mdb.models['HEB 300'].parts['HEB'].setElementType(elemTypes=(ElemType(
    elemCode=DC3D8, elemLibrary=STANDARD), ElemType(elemCode=DC3D6, 
    elemLibrary=STANDARD), ElemType(elemCode=DC3D4, elemLibrary=STANDARD)), 
    regions=(mdb.models['HEB 300'].parts['HEB'].cells.findAt(((0.75*x, -y, 25), ), ((0.75*x, -y, 0.1*L), ), ((0.75*x, -y, 0.5*L-25), ), ((0.75*x, -y, 0.5*L+25), ), ((0.75*x, -y, 0.9*L), ), ((0.75*x, -y, L-25), ), 
    ((0.75*x, y, 25), ), ((0.75*x, y, 0.1*L), ), ((0.75*x, y, 0.5*L-25), ), ((0.75*x, y, 0.5*L+25), ), ((0.75*x, y, 0.9*L), ), ((0.75*x, y, L-25), ),
    ((-0.75*x, -y, 25), ), ((-0.75*x, -y, 0.1*L), ), ((-0.75*x, -y, 0.9*L ), ), ((-0.75*x, -y, 0.5*L-25), ), ((-0.75*x, -y, 0.5*L+25), ), ((-0.75*x, -y, L-25), ), 
    ((-0.75*x, y, 25), ), ((-0.75*x, y, 0.1*L), ), ((-0.75*x, y, 0.9*L), ), ((-0.75*x, y, 0.5*L-25), ), ((-0.75*x, y, 0.5*L+25), ), ((-0.75*x, y, L-25), ), 
    ((0.25*x, y, 0.1*L), ), ((0.25*x, -y, 0.1*L), ), ((0.25*x, y, 0.9*L), ), ((0.25*x, -y, 0.9*L), ), ((0.25*x, y, 25), ), ((0.25*x, -y, 25), ), ((0.25*x, y, L-25), ), ((0.25*x, -y, L-25), ),
    ((0.25*x, y, 0.5*L+25), ), ((0.25*x, -y, 0.5*L+25), ), ((0.25*x, y, 0.5*L-25), ), ((0.25*x, -y, 0.5*L-25), ), ), ))
mdb.models['HEB 300'].rootAssembly.regenerate()

#ThermoCouple_Locate
mdb.models['HEB 300'].rootAssembly.Set(name='TC9', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    0.5*x, y-f, (2*L+1100)/6), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC10', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    0.5*w, 0.0, (2*L+1100)/6), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC3', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    0.5*w, 0.0, 0.5*L), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC7', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    0.5*w, 0.0, (4*L-1100)/6), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC2', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    0.5*x, y-f, 0.5*L), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC5', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    0.5*x, -y+f, 0.5*L), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC8', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    0.5*x, -y+f, (4*L-1100)/6), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC11', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    -0.5*x, -y+f, (2*L+1100)/6), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC4', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    -0.5*x, -y+f, 0.5*L), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC6', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    -0.5*x, y-f, (4*L-1100)/6), )))
mdb.models['HEB 300'].rootAssembly.Set(name='TC1', vertices=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].vertices.findAt(((
    -0.5*x, y-f, 0.5*L), )))

#Step_History_Output_Request
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC1', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC1'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC2', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC2'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC3', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC3'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC4', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC4'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC5', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC5'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC6', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC6'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC7', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC7'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC8', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC8'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC9', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC9'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC10', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC10'], sectionPoints=DEFAULT, 
    variables=('NT', ))
mdb.models['HEB 300'].HistoryOutputRequest(createStepName='Fire', name=
    'TC11', rebar=EXCLUDE, region=
    mdb.models['HEB 300'].rootAssembly.sets['TC11'], sectionPoints=DEFAULT, 
    variables=('NT', ))

#Surface_Select
mdb.models['HEB 300'].rootAssembly.Surface(name='Fire_05', side1Faces=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].faces.findAt(
    ((0.75*x, -y+f, 0.1*L), ), ((0.25*x, -y+f, 0.1*L), ), ((-0.75*x, -y+f, 0.1*L), ), ((-0.25*x, -y+f, 0.1*L), ), 
    ((0.75*x, -y+f, 0.9*L), ), ((0.25*x, -y+f, 0.9*L), ), ((-0.75*x, -y+f, 0.9*L), ), ((-0.25*x, -y+f, 0.9*L), ), 
    ((0.75*x, -y+f, 0.5*L-25), ), ((0.25*x, -y+f, 0.5*L-25), ), ((-0.75*x, -y+f, 0.5*L-25), ), ((-0.25*x, -y+f, 0.5*L-25), ), 
    ((0.75*x, -y+f, 0.5*L+25), ), ((0.25*x, -y+f, 0.5*L+25), ), ((-0.75*x, -y+f, 0.5*L+25), ), ((-0.25*x, -y+f, 0.5*L+25), ),  
    ((0.75*x, y-f, 0.1*L), ), ((0.25*x, y-f, 0.1*L), ), ((-0.75*x, y-f, 0.1*L), ), ((-0.25*x, y-f, 0.1*L), ), 
    ((0.75*x, y-f, 0.9*L), ), ((0.25*x, y-f, 0.9*L), ), ((-0.75*x, y-f, 0.9*L), ), ((-0.25*x, y-f, 0.9*L), ), 
    ((0.75*x, y-f, 0.5*L-25), ), ((0.25*x, y-f, 0.5*L-25), ), ((-0.75*x, y-f, 0.5*L-25), ), ((-0.25*x, y-f, 0.5*L-25), ), 
    ((0.75*x, y-f, 0.5*L+25), ), ((0.25*x, y-f, 0.5*L+25), ), ((-0.75*x, y-f, 0.5*L+25), ), ((-0.25*x, y-f, 0.5*L+25), ), 
    ((0.5*w, 0.25*y, 0.1*L), ), ((0.5*w, -0.25*y, 0.1*L), ), ((-0.5*w, -0.25*y, 0.1*L), ), ((-0.5*w, 0.25*y, 0.1*L), ), 
    ((0.5*w, 0.25*y, 0.9*L), ), ((0.5*w, -0.25*y, 0.9*L), ), ((-0.5*w, -0.25*y, 0.9*L), ), ((-0.5*w, 0.25*y, 0.9*L), ), 
    ((0.5*w, 0.25*y, 0.5*L-25), ), ((0.5*w, -0.25*y, 0.5*L-25), ), ((-0.5*w, -0.25*y, 0.5*L-25), ), ((-0.5*w, 0.25*y, 0.5*L-25), ), 
    ((0.5*w, 0.25*y, 0.5*L+25), ), ((0.5*w, -0.25*y, 0.5*L+25), ), ((-0.5*w, -0.25*y, 0.5*L+25), ), ((-0.5*w, 0.25*y, 0.5*L+25), ),    
    ((x, y-0.5*f, 0.1*L), ), ((-x, y-0.5*f, 0.1*L), ),  ((x, y-0.5*f, 0.9*L), ), ((-x, y-0.5*f, 0.9*L), ), 
    ((x, y-0.5*f, 0.5*L-25), ), ((-x, y-0.5*f, 0.5*L-25), ),  ((x, y-0.5*f, 0.5*L+25), ), ((-x, y-0.5*f, 0.5*L+25), ),  ))
mdb.models['HEB 300'].rootAssembly.Surface(name='Fire_07', side1Faces=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].faces.findAt(
    ((0.75*x, -y, 0.1*L), ), ((-0.75*x, -y, 0.1*L), ), ((0, -y, 0.1*L), ), 
    ((0.75*x, -y, 0.5*L-25), ), ((-0.75*x, -y, 0.5*L-25), ), ((0, -y, 0.5*L-25), ), 
    ((0.75*x, -y, 0.5*L+25), ), ((-0.75*x, -y, 0.5*L+25), ), ((0, -y, 0.5*L+25), ), 
    ((0.75*x, -y, 0.9*L), ), ((-0.75*x, -y, 0.9*L), ), ((0, -y, 0.9*L), ),   
    ((-x, -y+0.5*f, 0.1*L), ), ((x, -y+0.5*f, 0.1*L), ), ((-x, -y+0.5*f, 0.9*L), ), ((x, -y+0.5*f, 0.9*L), ), 
    ((-x, -y+0.5*f, 0.5*L-25), ), ((x, -y+0.5*f, 0.5*L-25), ),  ((-x, -y+0.5*f, 0.5*L+25), ), ((x, -y+0.5*f, 0.5*L+25), ), ))
mdb.models['HEB 300'].rootAssembly.Surface(name='NoFire', side1Faces=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].faces.findAt(
    ((0.75*x, y, 0.1*L), ), ((-0.75*x, y, 0.1*L), ), ((0, y, 0.1*L), ), 
    ((0.75*x, y, 0.9*L), ), ((-0.75*x, y, 0.9*L), ), ((0, y, 0.9*L), ), 
    ((0.75*x, -y, 25), ), ((-0.75*x, -y, 25), ), ((0, -y, 25), ), 
    ((0.75*x, -y, L-25), ), ((-0.75*x, -y, L-25), ), ((0, -y, L-25), ),
    ((0.75*x, -y+f, 25), ), ((0.25*x, -y+f, 25), ), ((-0.75*x, -y+f, 25), ), ((-0.25*x, -y+f, 25), ),
    ((0.75*x, -y+f, L-25), ), ((0.25*x, -y+f, L-25), ), ((-0.75*x, -y+f, L-25), ), ((-0.25*x, -y+f, L-25), ),
    ((0.75*x, y-f, 25), ), ((0.25*x, y-f, 25), ), ((-0.75*x, y-f, 25), ), ((-0.25*x, y-f, 25), ),
    ((0.75*x, y-f, L-25), ), ((0.25*x, y-f, L-25), ), ((-0.75*x, y-f, L-25), ), ((-0.25*x, y-f, L-25), ),
    ((0.5*w, 0.25*y, 25), ), ((0.5*w, -0.25*y, 25), ), ((-0.5*w, -0.25*y, 25), ), ((-0.5*w, 0.25*y, 25), ), 
    ((0.5*w, 0.25*y, L-25), ), ((0.5*w, -0.25*y, L-25), ), ((-0.5*w, -0.25*y, L-25), ), ((-0.5*w, 0.25*y, L-25), ),
    ((x, y-0.5*f, 25), ), ((-x, y-0.5*f, 25), ), ((-x, -y+0.5*f, 25), ), ((x, -y+0.5*f, 25), ), 
    ((x, y-0.5*f, L-25), ), ((-x, y-0.5*f, L-25), ), ((-x, -y+0.5*f, L-25), ), ((x, -y+0.5*f, L-25), ),
    ((0.75*x, y, 25), ), ((-0.75*x, y, 25), ), ((0, y, 25), ),
    ((0.75*x, y, L-25), ), ((-0.75*x, y, L-25), ), ((0, y, L-25), ),
    ((0, 0.25*y, 0), ), ((0, -0.25*y, 0), ), ((0.75*x, y-0.5*f, 0), ), ((-0.75*x, y-0.5*f, 0), ), ((0.75*x, -y+0.5*f, 0), ), ((-0.75*x, -y+0.5*f, 0), ), 
    ((0, 0.25*y, L), ), ((0, -0.25*y, L), ), ((0.75*x, y-0.5*f, L), ), ((-0.75*x, y-0.5*f, L), ), ((0.75*x, -y+0.5*f, L), ), ((-0.75*x, -y+0.5*f, L), ),
    ((0.75*x, y, 0.5*L-25), ), ((-0.75*x, y, 0.5*L-25), ), ((0, y, 0.5*L-25), ), 
    ((0.75*x, y, 0.5*L+25), ), ((-0.75*x, y, 0.5*L+25), ), ((0, y, 0.5*L+25), ), ))

#Interaction_Create
mdb.models['HEB 300'].FilmConditionProp(dependencies=0, name='Fire', property=(
    (0.025, ), ), temperatureDependency=OFF)
mdb.models['HEB 300'].FilmConditionProp(dependencies=0, name='NoFire', 
    property=((0.004, ), ), temperatureDependency=OFF)
mdb.models['HEB 300'].FilmCondition(createStepName='Fire', definition=
    PROPERTY_REF, interactionProperty='Fire', name='F1', sinkAmplitude='Fire', 
    sinkDistributionType=UNIFORM, sinkFieldName='', sinkTemperature=1.0, 
    surface=mdb.models['HEB 300'].rootAssembly.surfaces['Fire_05'])
mdb.models['HEB 300'].FilmCondition(createStepName='Fire', definition=
    PROPERTY_REF, interactionProperty='Fire', name='F2', sinkAmplitude='Fire', 
    sinkDistributionType=UNIFORM, sinkFieldName='', sinkTemperature=1.0, 
    surface=mdb.models['HEB 300'].rootAssembly.surfaces['Fire_07'])
mdb.models['HEB 300'].FilmCondition(createStepName='Fire', definition=
    PROPERTY_REF, interactionProperty='NoFire', name='NF', sinkAmplitude='Fire'
    , sinkDistributionType=UNIFORM, sinkFieldName='', sinkTemperature=1.0, 
    surface=mdb.models['HEB 300'].rootAssembly.surfaces['NoFire'])
mdb.models['HEB 300'].RadiationToAmbient(ambientTemperature=1.0, 
    ambientTemperatureAmp='Fire', createStepName='Fire', distributionType=
    UNIFORM, emissivity=0.8, field='', name='Fire_07', radiationType=AMBIENT, 
    surface=mdb.models['HEB 300'].rootAssembly.surfaces['Fire_07'])
mdb.models['HEB 300'].RadiationToAmbient(ambientTemperature=1.0, 
    ambientTemperatureAmp='Fire', createStepName='Fire', distributionType=
    UNIFORM, emissivity=0.7, field='', name='Fire_05', radiationType=AMBIENT, 
    surface=mdb.models['HEB 300'].rootAssembly.surfaces['Fire_05'])

#Predefined Field
mdb.models['HEB 300'].rootAssembly.Set(cells=
    mdb.models['HEB 300'].rootAssembly.instances['HEB-1'].cells.findAt(((0.1*x, -y+f, 0.55*L), ), ((0.1*x, y-f, 0.45*L), ),  ((0.1*x, y-f, 0.55*L), ), ((0.1*x, -y+f, 0.45*L), ),
                                                                                                               ((0.1*x, -y+f, 0.75*L), ), ((0.1*x, y-f, 0.25*L), ),  ((0.1*x, y-f, 0.75*L), ), ((0.1*x, -y+f, 0.25*L), ),
                                                                                                               ((0.1*x, -y+f, 25), ), ((0.1*x, y-f, L-25), ),  ((0.1*x, y-f, 25), ), ((0.1*x, -y+f, L-25), ),
                                                                                                               ((0.9*x, -y+f, 0.55*L), ), ((0.9*x, y-f, 0.45*L), ),  ((0.9*x, y-f, 0.55*L), ), ((0.9*x, -y+f, 0.45*L), ),
                                                                                                               ((0.9*x, -y+f, 0.75*L), ), ((0.9*x, y-f, 0.25*L), ),  ((0.9*x, y-f, 0.75*L), ), ((0.9*x, -y+f, 0.25*L), ),
                                                                                                               ((0.9*x, -y+f, 25), ), ((0.9*x, y-f, L-25), ),  ((0.9*x, y-f, 25), ), ((0.9*x, -y+f, L-25), ),
                                                                                                               ((-0.9*x, -y+f, 0.55*L), ), ((-0.9*x, y-f, 0.45*L), ),  ((-0.9*x, y-f, 0.55*L), ), ((-0.9*x, -y+f, 0.45*L), ),
                                                                                                               ((-0.9*x, -y+f, 0.75*L), ), ((-0.9*x, y-f, 0.25*L), ),  ((-0.9*x, y-f, 0.75*L), ), ((-0.9*x, -y+f, 0.25*L), ),
                                                                                                               ((-0.9*x, -y+f, 25), ), ((-0.9*x, y-f, L-25), ),  ((-0.9*x, y-f, 25), ), ((-0.9*x, -y+f, L-25), ),
                                                                                                              ), name='Body')

mdb.models['HEB 300'].Temperature(createStepName='Initial', 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=
    UNIFORM, magnitudes=(20.0, ), name='Predefined Field-1', region=
    mdb.models['HEB 300'].rootAssembly.sets['Body'])

#Job
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='HEB 300', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Fire', nodalOutputPrecision=SINGLE, 
    numCpus=2, numDomains=2, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
    '', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

mdb.jobs['Fire'].submit(consistencyChecking=OFF)

#lets_Go
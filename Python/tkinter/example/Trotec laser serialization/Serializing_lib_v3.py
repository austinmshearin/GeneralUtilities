# Imports
import csv

### Define programs to make numbers and letters for Trotec Laser File
# These are based on 'txt.shx' in Autocad with a height of 0.5 mm and width factor of 0.8
# x and y are adjustments to move around the position of the letter or number
# These characters are written left to right on the bed of the laser
# x runs from left to right and y runs from back to front on laser bed
def write_0(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 9;255;0;255;'+str(3+x)+';'+str(19+y)+';'+str(x)+';'+str(16+y)+';'+str(x)+';'+str(3+y)+';'+str(3+x)+';'+str(y)+';'+str(6+x)+';'+str(y)+';'+\
    str(8+x)+';'+str(3+y)+';'+str(8+x)+';'+str(16+y)+';'+str(6+x)+';'+str(19+y)+';'+str(3+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_1(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(x)+';'+str(3+y)+';'+str(3+x)+';'+str(y)+';'+str(3+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(19+y)+';'+str(6+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_2(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 10;255;0;255;'+str(x)+';'+str(3+y)+';'+str(3+x)+';'+str(y)+';'+str(8+x)+';'+str(y)+';'+str(11+x)+';'+str(3+y)+';'+str(11+x)+';'+str(6+y)+\
    ';'+str(8+x)+';'+str(9+y)+';'+str(3+x)+';'+str(9+y)+';'+str(x)+';'+str(13+y)+';'+str(x)+';'+str(19+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_3(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 7;255;0;255;'+str(x)+';'+str(3+y)+';'+str(3+x)+';'+str(y)+';'+str(8+x)+';'+str(y)+';'+str(11+x)+';'+str(3+y)+';'+str(11+x)+';'+\
    str(6+y)+';'+str(8+x)+';'+str(9+y)+';'+str(6+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 6;255;0;255;'+str(8+x)+';'+str(9+y)+';'+str(11+x)+';'+str(13+y)+';'+str(11+x)+';'+str(16+y)+';'+str(8+x)+';'+str(19+y)+';'+str(3+x)+';'+\
    str(19+y)+';'+str(x)+';'+str(16+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_4(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 4;255;0;255;'+str(11+x)+';'+str(13+y)+';'+str(x)+';'+str(13+y)+';'+str(8+x)+';'+str(y)+';'+str(8+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_5(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 9;255;0;255;'+str(x)+';'+str(16+y)+';'+str(3+x)+';'+str(19+y)+';'+str(8+x)+';'+str(19+y)+';'+str(11+x)+';'+str(16+y)+';'+str(11+x)+';'+str(9+y)+';'+\
    str(8+x)+';'+str(6+y)+';'+str(x)+';'+str(6+y)+';'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_6(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 10;255;0;255;'+str(x)+';'+str(9+y)+';'+str(8+x)+';'+str(9+y)+';'+str(11+x)+';'+str(13+y)+';'+str(11+x)+';'+str(16+y)+';'+str(8+x)+';'+str(19+y)+';'+\
    str(3+x)+';'+str(19+y)+';'+str(x)+';'+str(16+y)+';'+str(x)+';'+str(6+y)+';'+str(6+x)+';'+str(y)+';'+str(8+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_7(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(y)+';'+str(3+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_8(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 12;255;0;255;'+str(3+x)+';'+str(19+y)+';'+str(x)+';'+str(16+y)+';'+str(x)+';'+str(13+y)+';'+str(3+x)+';'+str(9+y)+';'+str(8+x)+';'+str(9+y)+';'+\
    str(11+x)+';'+str(6+y)+';'+str(11+x)+';'+str(3+y)+';'+str(8+x)+';'+str(y)+';'+str(3+x)+';'+str(y)+';'+\
    str(x)+';'+str(3+y)+';'+str(x)+';'+str(6+y)+';'+str(3+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 5;255;0;255;'+str(8+x)+';'+str(9+y)+';'+str(11+x)+';'+str(13+y)+';'+str(11+x)+';'+str(16+y)+';'+\
    str(8+x)+';'+str(19+y)+';'+str(3+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_9(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 10;255;0;255;'+str(3+x)+';'+str(19+y)+';'+str(6+x)+';'+str(19+y)+';'+str(11+x)+';'+str(13+y)+';'+str(11+x)+';'+str(3+y)+';'+\
    str(8+x)+';'+str(y)+';'+str(3+x)+';'+str(y)+';'+str(x)+';'+str(3+y)+';'+\
    str(x)+';'+str(6+y)+';'+str(3+x)+';'+str(9+y)+';'+str(11+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_A(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 5;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(13+y)+';'+str(6+x)+';'+str(y)+';'+\
    str(11+x)+';'+str(13+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(13+y)+';'+str(11+x)+';'+str(13+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_B(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 6;255;0;255;'+str(x)+';'+str(19+y)+';'+str(8+x)+';'+str(19+y)+';'+str(11+x)+';'+str(16+y)+';'+\
    str(11+x)+';'+str(13+y)+';'+str(8+x)+';'+str(9+y)+';'+str(3+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 5;255;0;255;'+str(8+x)+';'+str(9+y)+';'+str(11+x)+';'+str(6+y)+';'+str(11+x)+';'+\
    str(3+y)+';'+str(8+x)+';'+str(y)+';'+str(x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    '<BegGroup: Family_'+str(fam+2)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(3+x)+';'+str(y)+';'+str(3+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+2)+'>\n'\
    )
    fam+=3
    return fam

def write_C(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 8;255;0;255;'+str(11+x)+';'+str(16+y)+';'+str(8+x)+';'+str(19+y)+';'+str(3+x)+';'+str(19+y)+';'+\
    str(x)+';'+str(16+y)+';'+str(x)+';'+str(3+y)+';'+str(3+x)+';'+str(y)+';'+str(8+x)+';'+str(y)+';'+str(11+x)+';'+str(3+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_D(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 6;255;0;255;'+str(x)+';'+str(19+y)+';'+str(8+x)+';'+str(19+y)+';'+str(11+x)+';'+str(16+y)+';'+\
    str(11+x)+';'+str(3+y)+';'+str(8+x)+';'+str(y)+';'+str(x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(3+x)+';'+str(y)+';'+str(3+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_E(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(9+y)+';'+str(6+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    '<BegGroup: Family_'+str(fam+2)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(19+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+2)+'>\n'\
    )
    fam+=3
    return fam

def write_F(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(9+y)+';'+str(6+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_G(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 8;255;0;255;'+str(8+x)+';'+str(9+y)+';'+str(11+x)+';'+str(9+y)+';'+str(11+x)+';'+str(19+y)+';'+\
    str(3+x)+';'+str(19+y)+';'+str(x)+';'+str(16+y)+';'+str(x)+';'+str(3+y)+';'+\
    str(3+x)+';'+str(y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_H(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(9+y)+';'+str(11+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    '<BegGroup: Family_'+str(fam+2)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(11+x)+';'+str(y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+2)+'>\n'\
    )
    fam+=3
    return fam

def write_I(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(y)+';'+str(6+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(3+x)+';'+str(y)+';'+str(3+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    '<BegGroup: Family_'+str(fam+2)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(19+y)+';'+str(6+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+2)+'>\n'\
    )
    fam+=3
    return fam

def write_J(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 5;255;0;255;'+str(x)+';'+str(16+y)+';'+str(3+x)+';'+str(19+y)+';'+\
    str(8+x)+';'+str(19+y)+';'+str(11+x)+';'+str(16+y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_K(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(11+x)+';'+str(y)+';'+str(3+x)+';'+str(9+y)+';'+str(x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    '<BegGroup: Family_'+str(fam+2)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(3+x)+';'+str(9+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+2)+'>\n'\
    )
    fam+=3
    return fam

def write_L(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(x)+';'+str(y)+';'+str(x)+';'+str(19+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_M(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 5;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+';'+str(6+x)+';'+str(13+y)+';'+\
    str(11+x)+';'+str(y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_N(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 4;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(19+y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_O(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 5;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(y)+';'+\
    str(11+x)+';'+str(19+y)+';'+str(x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_P(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 7;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+';'+str(8+x)+';'+str(y)+';'+\
    str(11+x)+';'+str(3+y)+';'+str(11+x)+';'+str(6+y)+';'+str(8+x)+';'+str(9+y)+';'+str(x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_Q(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 12;255;0;255;'+str(6+x)+';'+str(13+y)+';'+str(8+x)+';'+str(16+y)+';'+str(6+x)+';'+str(19+y)+';'+str(3+x)+';'+str(19+y)+';'+\
    str(x)+';'+str(16+y)+';'+str(x)+';'+str(3+y)+';'+str(3+x)+';'+str(y)+';'+str(8+x)+';'+str(y)+';'+\
    str(11+x)+';'+str(3+y)+';'+str(11+x)+';'+str(13+y)+';'+str(8+x)+';'+str(16+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_R(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 7;255;0;255;'+str(x)+';'+str(19+y)+';'+str(x)+';'+str(y)+';'+str(8+x)+';'+str(y)+';'+\
    str(11+x)+';'+str(3+y)+';'+str(11+x)+';'+str(6+y)+';'+str(8+x)+';'+str(9+y)+';'+str(x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(3+x)+';'+str(9+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_S(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 8;255;0;255;'+str(x)+';'+str(16+y)+';'+str(3+x)+';'+str(19+y)+';'+str(8+x)+';'+str(19+y)+';'+\
    str(11+x)+';'+str(16+y)+';'+str(x)+';'+str(3+y)+';'+str(3+x)+';'+str(y)+';'+str(8+x)+';'+str(y)+';'+str(11+x)+';'+str(3+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_T(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(6+x)+';'+str(y)+';'+str(6+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_U(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 6;255;0;255;'+str(x)+';'+str(y)+';'+str(x)+';'+str(16+y)+';'+str(3+x)+';'+str(19+y)+';'+\
    str(8+x)+';'+str(19+y)+';'+str(11+x)+';'+str(16+y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_V(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(x)+';'+str(y)+';'+str(8+x)+';'+str(19+y)+';'+str(16+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_W(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 5;255;0;255;'+str(x)+';'+str(y)+';'+str(6+x)+';'+str(19+y)+';'+\
    str(8+x)+';'+str(9+y)+';'+str(11+x)+';'+str(19+y)+';'+str(16+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_X(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(19+y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_Y(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 3;255;0;255;'+str(x)+';'+str(y)+';'+str(6+x)+';'+str(9+y)+';'+str(6+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    '<BegGroup: Family_'+str(fam+1)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(6+x)+';'+str(9+y)+';'+str(11+x)+';'+str(y)+'>\n'\
    '<EndGroup: Family_'+str(fam+1)+'>\n'\
    )
    fam+=2
    return fam

def write_Z(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 4;255;0;255;'+str(x)+';'+str(y)+';'+str(11+x)+';'+str(y)+';'+str(x)+';'+str(19+y)+';'+str(11+x)+';'+str(19+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

def write_hyph(x,y,fam):
    fileout.write(
    '<BegGroup: Family_'+str(fam)+'>\n'\
    '<DrawPolygon: 2;255;0;255;'+str(1+x)+';'+str(9+y)+';'+str(11+x)+';'+str(9+y)+'>\n'\
    '<EndGroup: Family_'+str(fam)+'>\n'\
    )
    fam+=1
    return fam

### Main program to perform serialization
def Serializing(julian,sheet_type,sheet_start,num_sheet):
    for sheet in range(int(num_sheet)):
        cur_sheet = str(int(sheet_start)+sheet).zfill(3)
        sheetname = str(julian) + '-' + cur_sheet
        file = sheetname + '.tsf' # Filename of output laser file
        sheet = str(julian) + '-' + cur_sheet # What will be serialized
        global fileout
        fileout = open(file, 'w+')
        # Generate header of file
        if sheet_type == 'Gas Sensor':
            fileout.write(
                '<!-- Version:Driver 10.7.0.222>\n'\
                '<!-- Version:Bezier 10.7.0.170>\n'\
                '<!-- PrintingApplication: acadlt.exe>\n'\
                '<BegGroup: Header>\n'\
                '<Version: 1.7>\n'\
                '<Speedy>\n'\
                '<ProcessMode: Standard>\n'\
                '<Resolution: 1000>\n'\
                '<Cutline: none>\n'\
                '<Size.Orig: 762.00;508.00>\n'\
                '<Size: 214.96;274.95>\n'\
                '<MaterialGroup: Standard>\n'\
                '<MaterialName: Standard>\n'\
                '<JobName: ' + sheetname + '>\n'\
                '<JobNumber: 251>\n'\
                '<EndGroup: Header>\n'\
                '<BegGroup: JobMeta>\n'\
                '<Meta: Halftoning; Color>\n'\
                '<EndGroup: JobMeta>\n'\
                '<BegGroup: Warnings>\n'\
                '<Warning: W_BITMAPS; W_BITMAP_IGNORED>\n'\
                '<EndGroup: Warnings>\n'\
                '<BegGroup: Vision>\n'\
                '<Regmark: 0;0;255;0;4232.00000;2208.00000;118.00000;>\n'\
                '<Regmark: 0;0;255;0;4231.00000;8605.00000;118.00000;>\n'\
                '<Regmark: 0;0;255;0;6908.00000;5406.00000;118.00000;>\n'\
                '<Regmark: 0;0;255;0;1555.00000;5406.00000;118.00000;>\n'\
                '<Regmark: 0;0;255;0;3247.00000;5413.00000;118.00000;>\n'\
                '<Regmark: 0;0;255;0;5216.00000;5413.00000;118.00000;>\n'\
                '<EndGroup: Vision>\n'\
                '<BegGroup: DrawCommands>\n'\
                )
        elif sheet_type == 'pH Sensor':
            fileout.write(
                '<!-- Version:Driver 10.7.0.222>\n'\
                '<!-- Version:Bezier 10.7.0.170>\n'\
                '<!-- PrintingApplication: acadlt.exe>\n'\
                '<BegGroup: Header>\n'\
                '<Version: 1.7>\n'\
                '<Speedy>\n'\
                '<ProcessMode: Standard>\n'\
                '<Resolution: 1000>\n'\
                '<Cutline: none>\n'\
                '<Size.Orig: 762.00;508.00>\n'\
                '<Size: 114.96;114.96>\n'\
                '<MaterialGroup: Standard>\n'\
                '<MaterialName: Standard>\n'\
                '<JobName: ' + sheetname + '>\n'\
                '<JobNumber: 253>\n'\
                '<EndGroup: Header>\n'\
                '<BegGroup: JobMeta>\n'\
                '<Meta: Halftoning; Color>\n'\
                '<EndGroup: JobMeta>\n'\
                '<BegGroup: Warnings>\n'\
                '<Warning: W_BITMAPS; W_BITMAP_IGNORED>\n'\
                '<EndGroup: Warnings>\n'\
                '<BegGroup: Vision>\n'\
                '<Regmark: 0;0;255;0;2273.00000;505.00000;98.00000;>\n'\
                '<Regmark: 0;0;255;0;2273.00000;4012.00000;98.00000;>\n'\
                '<Regmark: 0;0;255;0;3539.00000;3261.00000;98.00000;>\n'\
                '<Regmark: 0;0;255;0;1055.00000;1264.00000;98.00000;>\n'\
                '<EndGroup: Vision>\n'\
                '<BegGroup: DrawCommands>\n'\
                )
        elif sheet_type == 'Reference Electrode':
            fileout.write(
                '<!-- Version:Driver 10.7.0.222>\n'\
                '<!-- Version:Bezier 10.7.0.170>\n'\
                '<!-- PrintingApplication: acadlt.exe>\n'\
                '<BegGroup: Header>\n'\
                '<Version: 1.7>\n'\
                '<Speedy>\n'\
                '<ProcessMode: Standard>\n'\
                '<Resolution: 1000>\n'\
                '<Cutline: none>\n'\
                '<Size.Orig: 762.00;508.00>\n'\
                '<Size: 64.97;126.97>\n'\
                '<MaterialGroup: Standard>\n'\
                '<MaterialName: Standard>\n'\
                '<JobName: ' + sheetname + '>\n'\
                '<JobNumber: 255>\n'\
                '<EndGroup: Header>\n'\
                '<BegGroup: JobMeta>\n'\
                '<Meta: Halftoning; Color>\n'\
                '<EndGroup: JobMeta>\n'\
                '<BegGroup: Warnings>\n'\
                '<Warning: W_BITMAPS; W_BITMAP_IGNORED>\n'\
                '<EndGroup: Warnings>\n'\
                '<BegGroup: Vision>\n'\
                '<Regmark: 0;0;255;0;846.00000;4429.00000;98.00000;>\n'\
                '<Regmark: 0;0;255;0;1751.00000;4429.00000;98.00000;>\n'\
                '<Regmark: 0;0;255;0;846.00000;570.00000;98.00000;>\n'\
                '<Regmark: 0;0;255;0;1751.00000;570.00000;98.00000;>\n'\
                '<EndGroup: Vision>\n'\
                '<BegGroup: DrawCommands>\n'\
                )
        else:
            pass

        ### Generate the positions for sheet numbers
        if sheet_type == 'Gas Sensor':
            positions = [[7209,2572],[7209,3109.795566],[7209,3647.591132],[7209,6572.00216],[7209,7109.797726],[7209,7647.593292],
                        [6500.3382,1796.40903],[6500.3382,2334.204596],[6500.3382,2872.000162],[6500.3382,3409.795728],[6500.3382,3947.591294],[6500.3382,4485.38686],
                        [6500.3382,5794.31329],[6500.3382,6332.108856],[6500.3382,6869.904422],[6500.3382,7407.699988],[6500.3382,7945.495554],[6500.3382,8483.29112],
                        [5791.6764,1530.660855],[5791.6764,2068.456421],[5791.6764,2606.251987],[5791.6764,3144.047553],[5791.6764,3681.843119],[5791.6764,4219.638685],
                        [5791.6764,4757.434251],[5791.6764,5530.663015],[5791.6764,6068.458581],[5791.6764,6606.254147],[5791.6764,7144.049713],[5791.6764,7681.845279],
                        [5791.6764,8219.640845],[5791.6764,8757.436411],[5083.0146,1796.40903],[5083.0146,2334.204596],[5083.0146,2872.000162],[5083.0146,3409.795728],
                        [5083.0146,3947.591294],[5083.0146,4485.38686],[5083.0146,5794.31329],[5083.0146,6332.108856],[5083.0146,6869.904422],[5083.0146,7407.699988],
                        [5083.0146,7945.495554],[5083.0146,8483.29112],[4374.3528,2572],[4374.3528,3109.795566],[4374.3528,3647.591132],[4374.3528,6572.00216],
                        [4374.3528,7109.797726],[4374.3528,7647.593292],[3547.5807,2572],[3547.5807,3109.795566],[3547.5807,3647.591132],[3547.5807,6572.00216],
                        [3547.5807,7109.797726],[3547.5807,7647.593292],[2838.9189,1796.40903],[2838.9189,2334.204596],[2838.9189,2872.000162],[2838.9189,3409.795728],
                        [2838.9189,3947.591294],[2838.9189,4485.38686],[2838.9189,5794.31329],[2838.9189,6332.108856],[2838.9189,6869.904422],[2838.9189,7407.699988],
                        [2838.9189,7945.495554],[2838.9189,8483.29112],[2130.2571,1530.660855],[2130.2571,2068.456421],[2130.2571,2606.251987],[2130.2571,3144.047553],
                        [2130.2571,3681.843119],[2130.2571,4219.638685],[2130.2571,4757.434251],[2130.2571,5530.663015],[2130.2571,6068.458581],[2130.2571,6606.254147],
                        [2130.2571,7144.049713],[2130.2571,7681.845279],[2130.2571,8219.640845],[2130.2571,8757.436411],[1415.6391,1796.40903],[1415.6391,2334.204596],
                        [1415.6391,2872.000162],[1415.6391,3409.795728],[1415.6391,3947.591294],[1415.6391,4485.38686],[1415.6391,5794.31329],[1415.6391,6332.108856],
                        [1415.6391,6869.904422],[1415.6391,7407.699988],[1415.6391,7945.495554],[1415.6391,8483.29112],[706.9773,2572],[706.9773,3109.795566],
                        [706.9773,3647.591132],[706.9773,6572.00216],[706.9773,7109.797726],[706.9773,7647.593292]]
        elif sheet_type == 'pH Sensor':
            positions = [[3434,1719],[3434,2033.96],[3434,2348.92],[3434,2663.88],[2528.4877,774.1176],
                        [2528.4877,1089.0784],[2528.4877,1404.0392],[2528.4877,1719],[2528.4877,2033.9608],[2528.4877,2348.9216],
                        [2528.4877,2663.8824],[2528.4877,2978.8432],[2528.4877,3293.804],[2528.4877,3608.7648],[1622.9754,774.1176],
                        [1622.9754,1089.0784],[1622.9754,1404.0392],[1622.9754,1719],[1622.9754,2033.9608],[1622.9754,2348.9216],
                        [1622.9754,2663.8824],[1622.9754,2978.8432],[1622.9754,3293.804],[1622.9754,3608.7648],[717.4631,1719],
                        [717.4631,2033.9608],[717.4631,2348.9216],[717.4631,2663.8824]]
        elif sheet_type == 'Reference Electrode':
            positions = [[1321,1018],[1321,1332.9608],[1321,1647.9216],[1321,1962.8824],[1321,2277.8432],
                        [1321,2592.804],[1321,2907.7648],[1321,3222.7256],[1321,3537.6864],[1321,3852.6472],
                        [415.4877,1018],[415.4877,1332.9608],[415.4877,1647.9216],[415.4877,1962.8824],[415.4877,2277.8432],
                        [415.4877,2592.804],[415.4877,2907.7648],[415.4877,3222.7256],[415.4877,3537.6864],[415.4877,3852.6472]]
        else:
            pass

        ### Write sheet numbers to file
        global fam
        fam = 1 # Initialize family number iterator
        for position in positions:
            character_number = 1 # Initialize character counter
            for char in sheet: # Iterate through the characters in the sheet name
                x = position[0] + (0.35 * character_number * 39.3701) # Characters are spaced in the x by 0.35 mm and converter to mils
                y = position[1]
                character_number += 1
                if char == '0':
                    fam = write_0(x,y,fam)
                elif char == '1':
                    fam = write_1(x,y,fam)
                elif char == '2':
                    fam = write_2(x,y,fam)
                elif char == '3':
                    fam = write_3(x,y,fam)
                elif char == '4':
                    fam = write_4(x,y,fam)
                elif char == '5':
                    fam = write_5(x,y,fam)
                elif char == '6':
                    fam = write_6(x,y,fam)
                elif char == '7':
                    fam = write_7(x,y,fam)
                elif char == '8':
                    fam = write_8(x,y,fam)
                elif char == '9':
                    fam = write_9(x,y,fam)
                elif char == 'A':
                    fam = write_A(x,y,fam)
                elif char == 'B':
                    fam = write_B(x,y,fam)
                elif char == 'C':
                    fam = write_C(x,y,fam)
                elif char == 'D':
                    fam = write_D(x,y,fam)
                elif char == 'E':
                    fam = write_E(x,y,fam)
                elif char == 'F':
                    fam = write_F(x,y,fam)
                elif char == 'G':
                    fam = write_G(x,y,fam)
                elif char == 'H':
                    fam = write_H(x,y,fam)
                elif char == 'I':
                    fam = write_I(x,y,fam)
                elif char == 'J':
                    fam = write_J(x,y,fam)
                elif char == 'K':
                    fam = write_K(x,y,fam)
                elif char == 'L':
                    fam = write_L(x,y,fam)
                elif char == 'M':
                    fam = write_M(x,y,fam)
                elif char == 'N':
                    fam = write_N(x,y,fam)
                elif char == 'O':
                    fam = write_O(x,y,fam)
                elif char == 'P':
                    fam = write_P(x,y,fam)
                elif char == 'Q':
                    fam = write_Q(x,y,fam)
                elif char == 'R':
                    fam = write_R(x,y,fam)
                elif char == 'S':
                    fam = write_S(x,y,fam)
                elif char == 'T':
                    fam = write_T(x,y,fam)
                elif char == 'U':
                    fam = write_U(x,y,fam)
                elif char == 'V':
                    fam = write_V(x,y,fam)
                elif char == 'W':
                    fam = write_W(x,y,fam)
                elif char == 'X':
                    fam = write_X(x,y,fam)
                elif char == 'Y':
                    fam = write_Y(x,y,fam)
                elif char == 'Z':
                    fam = write_Z(x,y,fam)
                elif char =='-':
                    fam = write_hyph(x,y,fam)
                else:
                    print('incorrect character in sheet name')
        
        ### Sensor Numbers if needed
        if sheet_type == 'Gas Sensor':
            fileout.write('<EndGroup: DrawCommands>')
        elif sheet_type == 'pH Sensor':
            fileout.write(
            '<BegGroup: Family_1035>\n'\
            '<DrawPolygon: 3;255;0;255;3525;1831;3532;1824;3532;1864>\n'\
            '<EndGroup: Family_1035>\n'\
            '<BegGroup: Family_1037>\n'\
            '<DrawPolygon: 2;255;0;255;3525;1864;3538;1864>\n'\
            '<EndGroup: Family_1037>\n'\
            '<BegGroup: Family_1039>\n'\
            '<DrawPolygon: 10;255;0;255;3517;2145;3524;2139;3537;2139;3544;2145;3544;2152;3537;2158;3524;2158;3517;2165;3517;2178;3544;2178>\n'\
            '<EndGroup: Family_1039>\n'\
            '<BegGroup: Family_1041>\n'\
            '<DrawPolygon: 7;255;0;255;3513;2457;3519;2451;3532;2451;3539;2457;3539;2464;3532;2470;3526;2470>\n'\
            '<EndGroup: Family_1041>\n'\
            '<BegGroup: Family_1043>\n'\
            '<DrawPolygon: 6;255;0;255;3532;2470;3539;2477;3539;2484;3532;2490;3519;2490;3513;2484>\n'\
            '<EndGroup: Family_1043>\n'\
            '<BegGroup: Family_1045>\n'\
            '<DrawPolygon: 4;255;0;255;3538;2790;3512;2790;3532;2764;3532;2803>\n'\
            '<EndGroup: Family_1045>\n'\
            '<BegGroup: Family_1047>\n'\
            '<DrawPolygon: 9;255;0;255;2614;911;2621;918;2634;918;2641;911;2641;898;2634;892;2614;892;2614;878;2641;878>\n'\
            '<EndGroup: Family_1047>\n'\
            '<BegGroup: Family_1049>\n'\
            '<DrawPolygon: 3;255;0;255;1698;887;1704;880;1704;920>\n'\
            '<EndGroup: Family_1049>\n'\
            '<BegGroup: Family_1051>\n'\
            '<DrawPolygon: 2;255;0;255;1698;920;1711;920>\n'\
            '<EndGroup: Family_1051>\n'\
            '<BegGroup: Family_1053>\n'\
            '<DrawPolygon: 9;255;0;255;1724;913;1731;920;1744;920;1750;913;1750;900;1744;893;1724;893;1724;880;1750;880>\n'\
            '<EndGroup: Family_1053>\n'\
            '<BegGroup: Family_1055>\n'\
            '<DrawPolygon: 10;255;0;255;2613;1210;2633;1210;2639;1216;2639;1223;2633;1229;2620;1229;2613;1223;2613;1203;2626;1190;2633;1190>\n'\
            '<EndGroup: Family_1055>\n'\
            '<BegGroup: Family_1057>\n'\
            '<DrawPolygon: 3;255;0;255;1694;1198;1701;1192;1701;1231>\n'\
            '<EndGroup: Family_1057>\n'\
            '<BegGroup: Family_1059>\n'\
            '<DrawPolygon: 2;255;0;255;1694;1231;1707;1231>\n'\
            '<EndGroup: Family_1059>\n'\
            '<BegGroup: Family_1061>\n'\
            '<DrawPolygon: 10;255;0;255;1720;1212;1740;1212;1747;1218;1747;1225;1740;1231;1727;1231;1720;1225;1720;1205;1733;1192;1740;1192>\n'\
            '<EndGroup: Family_1061>\n'\
            '<BegGroup: Family_1063>\n'\
            '<DrawPolygon: 3;255;0;255;2608;1505;2634;1505;2614;1544>\n'\
            '<EndGroup: Family_1063>\n'\
            '<BegGroup: Family_1065>\n'\
            '<DrawPolygon: 3;255;0;255;1687;1513;1694;1507;1694;1546>\n'\
            '<EndGroup: Family_1065>\n'\
            '<BegGroup: Family_1067>\n'\
            '<DrawPolygon: 2;255;0;255;1687;1546;1701;1546>\n'\
            '<EndGroup: Family_1067>\n'\
            '<BegGroup: Family_1069>\n'\
            '<DrawPolygon: 3;255;0;255;1714;1507;1740;1507;1720;1546>\n'\
            '<EndGroup: Family_1069>\n'\
            '<BegGroup: Family_1071>\n'\
            '<DrawPolygon: 12;255;0;255;2609;1860;2603;1853;2603;1847;2609;1840;2623;1840;2629;1834;2629;1827;2623;1821;2609;1821;2603;1827;2603;1834;2609;1840>\n'\
            '<EndGroup: Family_1071>\n'\
            '<BegGroup: Family_1073>\n'\
            '<DrawPolygon: 5;255;0;255;2623;1840;2629;1847;2629;1853;2623;1860;2609;1860>\n'\
            '<EndGroup: Family_1073>\n'\
            '<BegGroup: Family_1075>\n'\
            '<DrawPolygon: 3;255;0;255;1678;1828;1685;1821;1685;1861>\n'\
            '<EndGroup: Family_1075>\n'\
            '<BegGroup: Family_1077>\n'\
            '<DrawPolygon: 2;255;0;255;1678;1861;1692;1861>\n'\
            '<EndGroup: Family_1077>\n'\
            '<BegGroup: Family_1079>\n'\
            '<DrawPolygon: 12;255;0;255;1711;1861;1705;1854;1705;1848;1711;1841;1724;1841;1731;1835;1731;1828;1724;1821;1711;1821;1705;1828;1705;1835;1711;1841>\n'\
            '<EndGroup: Family_1079>\n'\
            '<BegGroup: Family_1081>\n'\
            '<DrawPolygon: 5;255;0;255;1724;1841;1731;1848;1731;1854;1724;1861;1711;1861>\n'\
            '<EndGroup: Family_1081>\n'\
            '<BegGroup: Family_1083>\n'\
            '<DrawPolygon: 10;255;0;255;2606;2174;2613;2174;2626;2161;2626;2141;2620;2135;2606;2135;2600;2141;2600;2148;2606;2154;2626;2154>\n'\
            '<EndGroup: Family_1083>\n'\
            '<BegGroup: Family_1085>\n'\
            '<DrawPolygon: 3;255;0;255;1679;2143;1685;2136;1685;2176>\n'\
            '<EndGroup: Family_1085>\n'\
            '<BegGroup: Family_1087>\n'\
            '<DrawPolygon: 2;255;0;255;1679;2176;1692;2176>\n'\
            '<EndGroup: Family_1087>\n'\
            '<BegGroup: Family_1089>\n'\
            '<DrawPolygon: 10;255;0;255;1711;2176;1718;2176;1731;2162;1731;2143;1725;2136;1711;2136;1705;2143;1705;2149;1711;2156;1731;2156>\n'\
            '<EndGroup: Family_1089>\n'\
            '<BegGroup: Family_1091>\n'\
            '<DrawPolygon: 3;255;0;255;2591;2455;2598;2449;2598;2488>\n'\
            '<EndGroup: Family_1091>\n'\
            '<BegGroup: Family_1093>\n'\
            '<DrawPolygon: 2;255;0;255;2591;2488;2604;2488>\n'\
            '<EndGroup: Family_1093>\n'\
            '<BegGroup: Family_1095>\n'\
            '<DrawPolygon: 9;255;0;255;2624;2488;2617;2482;2617;2455;2624;2449;2630;2449;2637;2455;2637;2482;2630;2488;2624;2488>\n'\
            '<EndGroup: Family_1095>\n'\
            '<BegGroup: Family_1097>\n'\
            '<DrawPolygon: 10;255;0;255;1671;2455;1678;2449;1691;2449;1697;2455;1697;2462;1691;2468;1678;2468;1671;2475;1671;2488;1697;2488>\n'\
            '<EndGroup: Family_1097>\n'\
            '<BegGroup: Family_1099>\n'\
            '<DrawPolygon: 9;255;0;255;1717;2488;1711;2481;1711;2455;1717;2449;1724;2449;1730;2455;1730;2481;1724;2488;1717;2488>\n'\
            '<EndGroup: Family_1099>\n'\
            '<BegGroup: Family_10101>\n'\
            '<DrawPolygon: 3;255;0;255;2599;2774;2606;2768;2606;2807>\n'\
            '<EndGroup: Family_10101>\n'\
            '<BegGroup: Family_10103>\n'\
            '<DrawPolygon: 2;255;0;255;2599;2807;2612;2807>\n'\
            '<EndGroup: Family_10103>\n'\
            '<BegGroup: Family_10105>\n'\
            '<DrawPolygon: 3;255;0;255;2625;2774;2632;2768;2632;2807>\n'\
            '<EndGroup: Family_10105>\n'\
            '<BegGroup: Family_10107>\n'\
            '<DrawPolygon: 2;255;0;255;2625;2807;2639;2807>\n'\
            '<EndGroup: Family_10107>\n'\
            '<BegGroup: Family_10109>\n'\
            '<DrawPolygon: 10;255;0;255;1673;2771;1680;2764;1693;2764;1699;2771;1699;2778;1693;2784;1680;2784;1673;2791;1673;2804;1699;2804>\n'\
            '<EndGroup: Family_10109>\n'\
            '<BegGroup: Family_10111>\n'\
            '<DrawPolygon: 3;255;0;255;1712;2771;1719;2764;1719;2804>\n'\
            '<EndGroup: Family_10111>\n'\
            '<BegGroup: Family_10113>\n'\
            '<DrawPolygon: 2;255;0;255;1712;2804;1725;2804>\n'\
            '<EndGroup: Family_10113>\n'\
            '<BegGroup: Family_10115>\n'\
            '<DrawPolygon: 3;255;0;255;2588;3086;2595;3080;2595;3119>\n'\
            '<EndGroup: Family_10115>\n'\
            '<BegGroup: Family_10117>\n'\
            '<DrawPolygon: 2;255;0;255;2588;3119;2601;3119>\n'\
            '<EndGroup: Family_10117>\n'\
            '<BegGroup: Family_10119>\n'\
            '<DrawPolygon: 10;255;0;255;2615;3086;2621;3080;2634;3080;2641;3086;2641;3093;2634;3099;2621;3099;2615;3106;2615;3119;2641;3119>\n'\
            '<EndGroup: Family_10119>\n'\
            '<BegGroup: Family_10121>\n'\
            '<DrawPolygon: 10;255;0;255;1665;3086;1671;3079;1685;3079;1691;3086;1691;3093;1685;3099;1671;3099;1665;3106;1665;3119;1691;3119>\n'\
            '<EndGroup: Family_10121>\n'\
            '<BegGroup: Family_10123>\n'\
            '<DrawPolygon: 10;255;0;255;1704;3086;1711;3079;1724;3079;1730;3086;1730;3093;1724;3099;1711;3099;1704;3106;1704;3119;1730;3119>\n'\
            '<EndGroup: Family_10123>\n'\
            '<BegGroup: Family_10125>\n'\
            '<DrawPolygon: 3;255;0;255;2586;3402;2592;3395;2592;3434>\n'\
            '<EndGroup: Family_10125>\n'\
            '<BegGroup: Family_10127>\n'\
            '<DrawPolygon: 2;255;0;255;2586;3434;2599;3434>\n'\
            '<EndGroup: Family_10127>\n'\
            '<BegGroup: Family_10129>\n'\
            '<DrawPolygon: 7;255;0;255;2612;3402;2619;3395;2632;3395;2638;3402;2638;3408;2632;3415;2625;3415>\n'\
            '<EndGroup: Family_10129>\n'\
            '<BegGroup: Family_10131>\n'\
            '<DrawPolygon: 6;255;0;255;2632;3415;2638;3421;2638;3428;2632;3434;2619;3434;2612;3428>\n'\
            '<EndGroup: Family_10131>\n'\
            '<BegGroup: Family_10133>\n'\
            '<DrawPolygon: 10;255;0;255;1671;3401;1678;3395;1691;3395;1698;3401;1698;3408;1691;3414;1678;3414;1671;3421;1671;3434;1698;3434>\n'\
            '<EndGroup: Family_10133>\n'\
            '<BegGroup: Family_10135>\n'\
            '<DrawPolygon: 7;255;0;255;1711;3401;1717;3395;1730;3395;1737;3401;1737;3408;1730;3414;1724;3414>\n'\
            '<EndGroup: Family_10135>\n'\
            '<BegGroup: Family_10137>\n'\
            '<DrawPolygon: 6;255;0;255;1730;3414;1737;3421;1737;3428;1730;3434;1717;3434;1711;3428>\n'\
            '<EndGroup: Family_10137>\n'\
            '<BegGroup: Family_10139>\n'\
            '<DrawPolygon: 3;255;0;255;2593;3718;2599;3712;2599;3751>\n'\
            '<EndGroup: Family_10139>\n'\
            '<BegGroup: Family_10141>\n'\
            '<DrawPolygon: 2;255;0;255;2593;3751;2606;3751>\n'\
            '<EndGroup: Family_10141>\n'\
            '<BegGroup: Family_10143>\n'\
            '<DrawPolygon: 4;255;0;255;2645;3738;2619;3738;2639;3712;2639;3751>\n'\
            '<EndGroup: Family_10143>\n'\
            '<BegGroup: Family_10145>\n'\
            '<DrawPolygon: 10;255;0;255;1690;3717;1697;3710;1710;3710;1717;3717;1717;3723;1710;3730;1697;3730;1690;3737;1690;3750;1717;3750>\n'\
            '<EndGroup: Family_10145>\n'\
            '<BegGroup: Family_10147>\n'\
            '<DrawPolygon: 4;255;0;255;1756;3737;1730;3737;1749;3710;1749;3750>\n'\
            '<EndGroup: Family_10147>\n'\
            '<BegGroup: Family_10149>\n'\
            '<DrawPolygon: 10;255;0;255;776;1828;782;1822;796;1822;802;1828;802;1835;796;1841;782;1841;776;1848;776;1861;802;1861>\n'\
            '<EndGroup: Family_10149>\n'\
            '<BegGroup: Family_10151>\n'\
            '<DrawPolygon: 9;255;0;255;815;1855;822;1861;835;1861;841;1855;841;1841;835;1835;815;1835;815;1822;841;1822>\n'\
            '<EndGroup: Family_10151>\n'\
            '<BegGroup: Family_10153>\n'\
            '<DrawPolygon: 10;255;0;255;778;2141;785;2134;798;2134;805;2141;805;2148;798;2154;785;2154;778;2161;778;2174;805;2174>\n'\
            '<EndGroup: Family_10153>\n'\
            '<BegGroup: Family_10155>\n'\
            '<DrawPolygon: 10;255;0;255;818;2154;837;2154;844;2161;844;2167;837;2174;824;2174;818;2167;818;2148;831;2134;837;2134>\n'\
            '<EndGroup: Family_10155>\n'\
            '<BegGroup: Family_10157>\n'\
            '<DrawPolygon: 10;255;0;255;778;2457;785;2450;798;2450;805;2457;805;2464;798;2470;785;2470;778;2477;778;2490;805;2490>\n'\
            '<EndGroup: Family_10157>\n'\
            '<BegGroup: Family_10159>\n'\
            '<DrawPolygon: 3;255;0;255;818;2450;844;2450;824;2490>\n'\
            '<EndGroup: Family_10159>\n'\
            '<BegGroup: Family_10161>\n'\
            '<DrawPolygon: 10;255;0;255;764;2772;771;2765;784;2765;790;2772;790;2778;784;2785;771;2785;764;2791;764;2804;790;2804>\n'\
            '<EndGroup: Family_10161>\n'\
            '<BegGroup: Family_10163>\n'\
            '<DrawPolygon: 12;255;0;255;810;2804;803;2798;803;2791;810;2785;823;2785;830;2778;830;2772;823;2765;810;2765;803;2772;803;2778;810;2785>\n'\
            '<EndGroup: Family_10163>\n'\
            '<BegGroup: Family_10165>\n'\
            '<DrawPolygon: 5;255;0;255;823;2785;830;2791;830;2798;823;2804;810;2804>\n'\
            '<EndGroup: Family_10165>\n'\
            '<BegGroup: Family_10167>\n'\
            '<DrawPolygon: 5;0;0;255;0;0;0;4526;4526;4526;4526;0;0;0>\n'\
            '<EndGroup: Family_10167>\n'\
            '<EndGroup: DrawCommands>\n'\
            )
        elif sheet_type == 'Reference Electrode':
            fileout.write(
            '<BegGroup: Family_10191>\n'\
            '<DrawPolygon: 3;255;0;255;1321;1132;1323;1129;1323;1149>\n'\
            '<EndGroup: Family_10191>\n'\
            '<BegGroup: Family_10193>\n'\
            '<DrawPolygon: 2;255;0;255;1321;1149;1326;1149>\n'\
            '<EndGroup: Family_10193>\n'\
            '<BegGroup: Family_10195>\n'\
            '<DrawPolygon: 10;255;0;255;1321;1447;1323;1444;1329;1444;1331;1447;1331;1451;1329;1454;1323;1454;1321;1457;1321;1464;1331;1464>\n'\
            '<EndGroup: Family_10195>\n'\
            '<BegGroup: Family_10197>\n'\
            '<DrawPolygon: 7;255;0;255;1321;1762;1323;1759;1329;1759;1331;1762;1331;1765;1329;1769;1326;1769>\n'\
            '<EndGroup: Family_10197>\n'\
            '<BegGroup: Family_10199>\n'\
            '<DrawPolygon: 6;255;0;255;1329;1769;1331;1772;1331;1775;1329;1779;1323;1779;1321;1775>\n'\
            '<EndGroup: Family_10199>\n'\
            '<BegGroup: Family_10201>\n'\
            '<DrawPolygon: 4;255;0;255;1331;2087;1321;2087;1329;2074;1329;2094>\n'\
            '<EndGroup: Family_10201>\n'\
            '<BegGroup: Family_10203>\n'\
            '<DrawPolygon: 9;255;0;255;1321;2405;1323;2409;1329;2409;1331;2405;1331;2399;1329;2395;1321;2395;1321;2389;1331;2389>\n'\
            '<EndGroup: Family_10203>\n'\
            '<BegGroup: Family_10205>\n'\
            '<DrawPolygon: 10;255;0;255;1321;2714;1329;2714;1331;2717;1331;2720;1329;2723;1323;2723;1321;2720;1321;2710;1326;2704;1329;2704>\n'\
            '<EndGroup: Family_10205>\n'\
            '<BegGroup: Family_10207>\n'\
            '<DrawPolygon: 3;255;0;255;1321;3019;1331;3019;1323;3038>\n'\
            '<EndGroup: Family_10207>\n'\
            '<BegGroup: Family_10209>\n'\
            '<DrawPolygon: 12;255;0;255;1323;3353;1321;3350;1321;3347;1323;3344;1329;3344;1331;3340;1331;3337;1329;3334;1323;3334;1321;3337;1321;3340;1323;3344>\n'\
            '<EndGroup: Family_10209>\n'\
            '<BegGroup: Family_10211>\n'\
            '<DrawPolygon: 5;255;0;255;1329;3344;1331;3347;1331;3350;1329;3353;1323;3353>\n'\
            '<EndGroup: Family_10211>\n'\
            '<BegGroup: Family_10213>\n'\
            '<DrawPolygon: 10;255;0;255;1323;3668;1326;3668;1331;3662;1331;3652;1329;3649;1323;3649;1321;3652;1321;3655;1323;3659;1331;3659>\n'\
            '<EndGroup: Family_10213>\n'\
            '<BegGroup: Family_10215>\n'\
            '<DrawPolygon: 3;255;0;255;1321;3967;1323;3964;1323;3983>\n'\
            '<EndGroup: Family_10215>\n'\
            '<BegGroup: Family_10217>\n'\
            '<DrawPolygon: 2;255;0;255;1321;3983;1326;3983>\n'\
            '<EndGroup: Family_10217>\n'\
            '<BegGroup: Family_10219>\n'\
            '<DrawPolygon: 9;255;0;255;1334;3983;1331;3980;1331;3967;1334;3964;1337;3964;1339;3967;1339;3980;1337;3983;1334;3983>\n'\
            '<EndGroup: Family_10219>\n'\
            '<BegGroup: Family_10221>\n'\
            '<DrawPolygon: 3;255;0;255;415;1132;418;1129;418;1149>\n'\
            '<EndGroup: Family_10221>\n'\
            '<BegGroup: Family_10223>\n'\
            '<DrawPolygon: 2;255;0;255;415;1149;421;1149>\n'\
            '<EndGroup: Family_10223>\n'\
            '<BegGroup: Family_10225>\n'\
            '<DrawPolygon: 3;255;0;255;426;1132;428;1129;428;1149>\n'\
            '<EndGroup: Family_10225>\n'\
            '<BegGroup: Family_10227>\n'\
            '<DrawPolygon: 2;255;0;255;426;1149;431;1149>\n'\
            '<EndGroup: Family_10227>\n'\
            '<BegGroup: Family_10229>\n'\
            '<DrawPolygon: 3;255;0;255;415;1447;418;1444;418;1464>\n'\
            '<EndGroup: Family_10229>\n'\
            '<BegGroup: Family_10231>\n'\
            '<DrawPolygon: 2;255;0;255;415;1464;421;1464>\n'\
            '<EndGroup: Family_10231>\n'\
            '<BegGroup: Family_10233>\n'\
            '<DrawPolygon: 10;255;0;255;426;1447;428;1444;434;1444;436;1447;436;1451;434;1454;428;1454;426;1457;426;1464;436;1464>\n'\
            '<EndGroup: Family_10233>\n'\
            '<BegGroup: Family_10235>\n'\
            '<DrawPolygon: 3;255;0;255;415;1762;418;1759;418;1779>\n'\
            '<EndGroup: Family_10235>\n'\
            '<BegGroup: Family_10237>\n'\
            '<DrawPolygon: 2;255;0;255;415;1779;421;1779>\n'\
            '<EndGroup: Family_10237>\n'\
            '<BegGroup: Family_10239>\n'\
            '<DrawPolygon: 7;255;0;255;426;1762;428;1759;434;1759;436;1762;436;1765;434;1769;431;1769>\n'\
            '<EndGroup: Family_10239>\n'\
            '<BegGroup: Family_10241>\n'\
            '<DrawPolygon: 6;255;0;255;434;1769;436;1772;436;1775;434;1779;428;1779;426;1775>\n'\
            '<EndGroup: Family_10241>\n'\
            '<BegGroup: Family_10243>\n'\
            '<DrawPolygon: 3;255;0;255;415;2077;418;2074;418;2094>\n'\
            '<EndGroup: Family_10243>\n'\
            '<BegGroup: Family_10245>\n'\
            '<DrawPolygon: 2;255;0;255;415;2094;421;2094>\n'\
            '<EndGroup: Family_10245>\n'\
            '<BegGroup: Family_10247>\n'\
            '<DrawPolygon: 4;255;0;255;436;2087;426;2087;434;2074;434;2094>\n'\
            '<EndGroup: Family_10247>\n'\
            '<BegGroup: Family_10249>\n'\
            '<DrawPolygon: 3;255;0;255;415;2392;418;2389;418;2409>\n'\
            '<EndGroup: Family_10249>\n'\
            '<BegGroup: Family_10251>\n'\
            '<DrawPolygon: 2;255;0;255;415;2409;421;2409>\n'\
            '<EndGroup: Family_10251>\n'\
            '<BegGroup: Family_10253>\n'\
            '<DrawPolygon: 9;255;0;255;426;2405;428;2409;434;2409;436;2405;436;2399;434;2395;426;2395;426;2389;436;2389>\n'\
            '<EndGroup: Family_10253>\n'\
            '<BegGroup: Family_10255>\n'\
            '<DrawPolygon: 3;255;0;255;415;2707;418;2704;418;2723>\n'\
            '<EndGroup: Family_10255>\n'\
            '<BegGroup: Family_10257>\n'\
            '<DrawPolygon: 2;255;0;255;415;2723;421;2723>\n'\
            '<EndGroup: Family_10257>\n'\
            '<BegGroup: Family_10259>\n'\
            '<DrawPolygon: 10;255;0;255;426;2714;434;2714;436;2717;436;2720;434;2723;428;2723;426;2720;426;2710;431;2704;434;2704>\n'\
            '<EndGroup: Family_10259>\n'\
            '<BegGroup: Family_10261>\n'\
            '<DrawPolygon: 3;255;0;255;415;3022;418;3019;418;3038>\n'\
            '<EndGroup: Family_10261>\n'\
            '<BegGroup: Family_10263>\n'\
            '<DrawPolygon: 2;255;0;255;415;3038;421;3038>\n'\
            '<EndGroup: Family_10263>\n'\
            '<BegGroup: Family_10265>\n'\
            '<DrawPolygon: 3;255;0;255;426;3019;436;3019;428;3038>\n'\
            '<EndGroup: Family_10265>\n'\
            '<BegGroup: Family_10267>\n'\
            '<DrawPolygon: 3;255;0;255;415;3337;418;3334;418;3353>\n'\
            '<EndGroup: Family_10267>\n'\
            '<BegGroup: Family_10269>\n'\
            '<DrawPolygon: 2;255;0;255;415;3353;421;3353>\n'\
            '<EndGroup: Family_10269>\n'\
            '<BegGroup: Family_10271>\n'\
            '<DrawPolygon: 12;255;0;255;428;3353;426;3350;426;3347;428;3344;434;3344;436;3340;436;3337;434;3334;428;3334;426;3337;426;3340;428;3344>\n'\
            '<EndGroup: Family_10271>\n'\
            '<BegGroup: Family_10273>\n'\
            '<DrawPolygon: 5;255;0;255;434;3344;436;3347;436;3350;434;3353;428;3353>\n'\
            '<EndGroup: Family_10273>\n'\
            '<BegGroup: Family_10275>\n'\
            '<DrawPolygon: 3;255;0;255;415;3652;418;3649;418;3668>\n'\
            '<EndGroup: Family_10275>\n'\
            '<BegGroup: Family_10277>\n'\
            '<DrawPolygon: 2;255;0;255;415;3668;421;3668>\n'\
            '<EndGroup: Family_10277>\n'\
            '<BegGroup: Family_10279>\n'\
            '<DrawPolygon: 10;255;0;255;428;3668;431;3668;436;3662;436;3652;434;3649;428;3649;426;3652;426;3655;428;3659;436;3659>\n'\
            '<EndGroup: Family_10279>\n'\
            '<BegGroup: Family_10281>\n'\
            '<DrawPolygon: 10;255;0;255;415;3967;418;3964;423;3964;426;3967;426;3970;423;3973;418;3973;415;3977;415;3983;426;3983>\n'\
            '<EndGroup: Family_10281>\n'\
            '<BegGroup: Family_10283>\n'\
            '<DrawPolygon: 9;255;0;255;434;3983;431;3980;431;3967;434;3964;436;3964;439;3967;439;3980;436;3983;434;3983>\n'\
            '<EndGroup: Family_10283>\n'\
            '<BegGroup: Family_10285>\n'\
            '<DrawPolygon: 5;0;0;255;0;4999;2558;4999;2558;0;0;0;0;4999>\n'\
            '<EndGroup: Family_10285>\n'\
            '<EndGroup: DrawCommands>\n'\
            )
        else:
            pass

        ### Close file
        fileout.close()

i1, j1, x1, y1 = map(int,input().split())
i2, j2, x2, y2 = map(int,input().split())

startx1 = i1
endx1 = i1+x1
starty1 = j1
endy1 = j1+y1

startx2 = i2
endx2 = i2+x2
starty2 = j2
endy2 = j2+y2

if (endx1==startx2 and endy1==starty2) or (endx1==startx2 and endy2==starty1) or (endx2==startx1 and endy1==starty2) or (endx2==startx1 and endy2==starty1):
    print(1)
elif (startx1==endx2 and starty1!=endy2) or (startx1==endx2 and starty2!=endy1) or (startx2==endx1 and starty1!=endy2) or (startx2==endx1 and starty2!=endy1):
    print(2)
elif (starty1==endy2 and startx1!=endx2) or (starty1==endy2 and startx2!=endx1) or (starty2==endy1 and startx1!=endx2) or (starty2==endy1 and startx2!=endx1):
    print(2)
elif (startx1<=startx2<=endx1 or startx1<=endx2<=endx1) and (starty1<=starty2<=endy1 or starty1<=endy2<=endy1):
    print(3)
else:
    print(4)
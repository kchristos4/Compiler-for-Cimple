L1:
j main
sw ra,-0(sp)
L2:
L3:
lw t1,-0(gp)
sw t1-20(gp)
L4:
lw t1,-0(gp)
sw t1-16(gp)
L5:
lw t1,-16(gp)
lw t2,-12(gp)
ble t1,t2,7
L6:
J 12
L7:
lw t1,-20(gp)
lw t2,-16(gp)
mul t1,t1,t2
sw t1-24(gp)
L8:
lw t1,-24(gp)
sw t1-20(gp)
L9:
lw t1,-16(gp)
lw t2,-0(gp)
add t1,t1,t2
sw t1-28(gp)
L10:
lw t1,-28(gp)
sw t1-16(gp)
L11:
J 5
L12:
L13:
L14:
lw ra,-0(sp)
jr ra

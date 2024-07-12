
import numpy as np

# Raw Pins

ALU_EMUX    = 0x01
ALU_OP0     = 0x02
ALU_OP1     = 0x04
ALU_OP2     = 0x08
ALU_OP3     = 0x10
ALU_ECIN    = 0x20

PC_OP0      = 0x40
PC_OP1      = 0x80
PC_E8       = 0x0100
PC_E16      = 0x0200

SP_OP0      = 0x0400
SP_OP1      = 0x0800

M_WE        = 0x1000
M_OE        = 0x2000

REG_CD_OP0  = 0x4000
REG_CD_OP1  = 0x8000
REG_CD_OP2  = 0x010000

REG_AB_OP0  = 0x020000
REG_AB_OP1  = 0x040000
REG_AB_OP2  = 0x080000

CTRL_RST    = 0x100000
CTRL_SIR    = 0x200000
CTRL_SFLG   = 0x400000

# Combination Pins
ALU_ADD = 0|0
ALU_SUB = ALU_OP0|0
ALU_AND = ALU_OP1|0
ALU_OR  = ALU_OP1|ALU_OP0
ALU_XOR = ALU_OP2|0
ALU_NOT = ALU_OP2|ALU_OP0
ALU_ROL = ALU_OP2|ALU_OP1
ALU_ROR = ALU_OP2|ALU_OP1|ALU_OP0

PC_STR = PC_OP0|0
PC_INC = PC_OP1|0
PC_DEC = PC_OP1|PC_OP0

SP_SHF = SP_OP0|0
SP_WT8 = SP_OP1|0
SP_W16 = SP_OP1|SP_OP0

REG_SA  = REG_AB_OP1|0
REG_SB  = REG_AB_OP1|REG_AB_OP0
REG_EA  = REG_AB_OP2|0
REG_EB  = REG_AB_OP2|REG_AB_OP0
REG_EAB = REG_AB_OP2|REG_AB_OP1|REG_AB_OP0

REG_SC  = REG_CD_OP1|0
REG_SD  = REG_CD_OP1|REG_CD_OP0
REG_EC  = REG_CD_OP2|0
REG_ED  = REG_CD_OP2|REG_CD_OP0
REG_ECD = REG_CD_OP2|REG_CD_OP1|REG_CD_OP0

insts = np.zeros((256,8), dtype=np.uint32)

# Next instruction
insts[::, :1] = [ PC_E16|PC_INC|M_OE|CTRL_SIR ]

## NOPs
# Buffer NOP
insts[0x00, 1:] = [ CTRL_RST, 0, 0, 0, 0, 0, 0 ]
# NOP
insts[0x08, 1:] = [ CTRL_RST, 0, 0, 0, 0, 0, 0 ]
## LOD DIRECT
# lod a direct
insts[0x10, 1:] = [ PC_E16|PC_INC|M_OE|REG_SA, CTRL_RST, 0, 0, 0, 0, 0 ]
# lod b, direct
insts[0x11, 1:] = [ PC_E16|PC_INC|M_OE|REG_SB, CTRL_RST, 0, 0, 0, 0, 0 ]
# lod c, direct
insts[0x12, 1:] = [ PC_E16|PC_INC|M_OE|REG_SC, CTRL_RST, 0, 0, 0, 0, 0 ]
# lod d, direct
insts[0x13, 1:] = [ PC_E16|PC_INC|M_OE|REG_SD, CTRL_RST, 0, 0, 0, 0, 0 ]
## LOD INDIRECT
# lod a indirect CD
insts[0x14, 1:] = [ REG_ECD|M_OE|REG_SA, CTRL_RST, 0, 0, 0, 0, 0 ]
# # lod b indirect CD
insts[0x15, 1:] = [ REG_ECD|M_OE|REG_SB, CTRL_RST, 0, 0, 0, 0, 0 ]
# insts[0x15, 1:] = [ REG_ECD|M_SMAR, M_EADR|REG_SB, CTRL_RST, 0, 0, 0 ]
# # lod c indirect AB
insts[0x16, 1:] = [ REG_EAB|M_OE|REG_SC, CTRL_RST, 0, 0, 0, 0, 0 ]
# insts[0x16, 1:] = [ REG_EAB|M_SMAR, M_EADR|REG_SC, CTRL_RST, 0, 0, 0 ]
# # lod d indirect AB
insts[0x17, 1:] = [ REG_EAB|M_OE|REG_SD, CTRL_RST, 0, 0, 0, 0, 0 ]
# insts[0x17, 1:] = [ REG_EAB|M_SMAR, M_EADR|REG_SD, CTRL_RST, 0, 0, 0 ]


print(insts[:0x20])

np.savetxt("/home/ripjackie/tslinkard/microcode.txt", insts, "%08lx", header="v3.0 hex words plain", comments="")

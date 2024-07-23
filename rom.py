
import numpy as np

# Raw Pins

ALU_EMUX    = 0x01
ALU_OP0     = 0x02
ALU_OP1     = 0x04
ALU_OP2     = 0x08
ALU_OP3     = 0x10
ALU_ECIN    = 0x20

AB_OP0      = 0x40
AB_OP1      = 0x80
AB_OP2      = 0x0100
AB_OP3      = 0x0200

CD_OP0      = 0x0400
CD_OP1      = 0x0800
CD_OP2      = 0x1000
CD_OP3      = 0x2000

LCH_ST       = 0x4000
LCH_EN       = 0x8000

SP_OP0      = 0x010000
SP_OP1      = 0x020000
SP_OP2      = 0x040000
SP_OP3      = 0x080000

PC_OP0      = 0x100000
PC_OP1      = 0x200000
PC_OP2      = 0x400000
PC_OP3      = 0x800000

ADR_WE     = 0x01000000
ADR_OE     = 0x02000000

CTRL_SRST   = 0x04000000
CTRL_SINR   = 0x08000000
CTRL_SFLG   = 0x10000000


# Combination Pins
ALU_ADD = 0
ALU_SUB = ALU_OP0
ALU_AND = ALU_OP1
ALU_OR  = ALU_OP1|ALU_OP0
ALU_XOR = ALU_OP2
ALU_NOT = ALU_OP2|ALU_OP0
ALU_ROL = ALU_OP2|ALU_OP1
ALU_ROR = ALU_OP2|ALU_OP1|ALU_OP0

REG_SA = AB_OP2
REG_SB = AB_OP3
REG_EA = AB_OP1
REG_EB = AB_OP1|AB_OP0

REG_SC = CD_OP2
REG_SD = CD_OP3
REG_EC = CD_OP1
REG_ED = CD_OP1|CD_OP0

SP_LD = SP_OP0
SP_INC = SP_OP1
SP_DEC = SP_OP1|SP_OP0
SP_E8 = SP_OP2
SP_E16 = SP_OP3

PC_LD = PC_OP0
PC_INC = PC_OP1
PC_DEC = PC_OP1|PC_OP0
PC_E8 = PC_OP2
PC_E16 = PC_OP3

STEP_MAX = 0x08

NEXT = [ PC_E16|PC_INC|ADR_OE|CTRL_SINR ]


insts = np.zeros((256, STEP_MAX), dtype=np.uint32)

insts[:, :len(NEXT)] = NEXT
step = insts[:, len(NEXT):]

## NOPs
# # Buffer NOP
step[0x00, :1] = [ CTRL_SRST ]
# # NOP
step[0x08, :1] = [ CTRL_SRST ]
# ## LD DIRECT
# # ld a, direct
step[0x10, :2] = [ PC_E16|PC_INC|ADR_OE|REG_SA, CTRL_SRST ]
# ld b, direct
step[0x11, :2] = [ PC_E16|PC_INC|ADR_OE|REG_SB, CTRL_SRST ]
# # ld c, direct
step[0x12, :2] = [ PC_E16|PC_INC|ADR_OE|REG_SC, CTRL_SRST ]
# # ld d, direct
step[0x13, :2] = [ PC_E16|PC_INC|ADR_OE|REG_SD, CTRL_SRST ]

# ## LOD INDIRECT
# # lod a indirect CD
# insts[0x14, 1:] = [ REG_ECD|M_OE|REG_SA, CTRL_RST, 0, 0, 0, 0, 0 ]
# # # lod b indirect CD
# insts[0x15, 1:] = [ REG_ECD|M_OE|REG_SB, CTRL_RST, 0, 0, 0, 0, 0 ]
# # insts[0x15, 1:] = [ REG_ECD|M_SMAR, M_EADR|REG_SB, CTRL_RST, 0, 0, 0 ]
# # # lod c indirect AB
# insts[0x16, 1:] = [ REG_EAB|M_OE|REG_SC, CTRL_RST, 0, 0, 0, 0, 0 ]
# # insts[0x16, 1:] = [ REG_EAB|M_SMAR, M_EADR|REG_SC, CTRL_RST, 0, 0, 0 ]
# # # lod d indirect AB
# insts[0x17, 1:] = [ REG_EAB|M_OE|REG_SD, CTRL_RST, 0, 0, 0, 0, 0 ]
# # insts[0x17, 1:] = [ REG_EAB|M_SMAR, M_EADR|REG_SD, CTRL_RST, 0, 0, 0 ]


np.savetxt("microcode.txt", insts, "%08lx", header="v3.0 hex words plain", comments="")

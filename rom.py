
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

ADR_WE      = 0x0400

SP_OP0     = 0x0800
SP_OP1     = 0x1000
SP_OP2     = 0x2000
SP_OP3     = 0x4000

HL_OP0     = 0x8000
HL_OP1     = 0x010000
HL_OP2     = 0x020000
HL_OP3     = 0x040000

AB_OP0     = 0x080000
AB_OP1     = 0x100000
AB_OP2     = 0x200000
AB_OP3     = 0x400000

CD_OP0     = 0x800000
CD_OP1     = 0x01000000
CD_OP2     = 0x02000000
CD_OP3     = 0x04000000

CTRL_SRST  = 0x08000000
CTRL_SIR   = 0x10000000
CTRL_SFLG  = 0x20000000

# Combination Pins
ALU_ADD = 0
ALU_SUB = ALU_OP0
ALU_AND = ALU_OP1
ALU_OR  = ALU_OP1|ALU_OP0
ALU_XOR = ALU_OP2
ALU_NOT = ALU_OP2|ALU_OP0
ALU_ROL = ALU_OP2|ALU_OP1
ALU_ROR = ALU_OP2|ALU_OP1|ALU_OP0

PC_STR = PC_OP0
PC_INC = PC_OP1
PC_DEC = PC_OP1|PC_OP0

SP_E16  = SP_OP0
SP_EL   = SP_OP1
SP_EH   = SP_OP1|SP_OP0
SP_S16  = SP_OP2
SP_SL   = SP_OP3
SP_SH   = SP_OP3|SP_OP2

HL_E16  = HL_OP0
HL_EL   = HL_OP1
HL_EH   = HL_OP1|HL_OP0
HL_S16  = HL_OP2
HL_SL   = HL_OP3
HL_SH   = HL_OP3|HL_OP2

AB_E16  = AB_OP0
AB_EL   = AB_OP1
AB_EH   = AB_OP1|AB_OP0
AB_S16  = AB_OP2
AB_SL   = AB_OP3
AB_SH   = AB_OP3|AB_OP2

CD_E16  = CD_OP0
CD_EL   = CD_OP1
CD_EH   = CD_OP1|CD_OP0
CD_S16  = CD_OP2
CD_SL   = CD_OP3
CD_SH   = CD_OP3|CD_OP2

HL_E16  = HL_EOP0
HL_EL   = HL_EOP1
HL_EH   = HL_EOP1|HL_EOP0
HL_S16  = HL_SOP0
HL_SL   = HL_SOP1
HL_SH   = HL_SOP1|HL_SOP0

AB_E16  = AB_EOP0
AB_EL   = AB_EOP1
AB_EH   = AB_EOP1|AB_EOP0
AB_S16  = AB_SOP0
AB_SL   = AB_SOP1
AB_SH   = AB_SOP1|AB_SOP0

CD_E16  = CD_EOP0
CD_EL   = CD_EOP1
CD_EH   = CD_EOP1|CD_EOP0
CD_S16  = CD_SOP0
CD_SL   = CD_SOP1
CD_SH   = CD_SOP1|CD_SOP0

STEP_MAX = 0x08

NEXT = [ PC_E16|PC_INC|CTRL_SIR ]


insts = np.zeros((256, STEP_MAX), dtype=np.uint32)

insts[:, :len(NEXT)] = NEXT
step = insts[:, len(NEXT):]

## NOPs
# # Buffer NOP
step[0x00, :1] = [ CTRL_SRST ]
# # NOP
step[0x08, :1] = [ CTRL_SRST ]
# ## LD DIRECT
# # ld a direct
step[0x10, :2] = [ PC_E16|PC_INC|AB_SL, CTRL_SRST ]
# insts[0x10, 1:] = [ PC_E16|PC_INC|M_OE|REG_SA, CTRL_RST, 0, 0, 0, 0, 0 ]
# # ld b, direct
# insts[0x11, 1:] = [ PC_E16|PC_INC|M_OE|REG_SB, CTRL_RST, 0, 0, 0, 0, 0 ]
# # ld c, direct
# insts[0x12, 1:] = [ PC_E16|PC_INC|M_OE|REG_SC, CTRL_RST, 0, 0, 0, 0, 0 ]
# # ld d, direct
# insts[0x13, 1:] = [ PC_E16|PC_INC|M_OE|REG_SD, CTRL_RST, 0, 0, 0, 0, 0 ]
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


np.savetxt("/home/ripjackie/tslinkard/microcode.txt", insts, "%08lx", header="v3.0 hex words plain", comments="")

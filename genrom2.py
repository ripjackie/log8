import numpy as np

MM_OP0      = 0x01
MM_OP1      = 0x02
MM_OP2      = 0x04

CTRL_SRST   = 0x08
CTRL_SINR   = 0x10
CTRL_SDIN   = 0x20
CTRL_SFLG   = 0x40

UNUSED      = 0x80

ALU_EMX     = 0x0100
ALU_OP0     = 0x0200
ALU_OP1     = 0x0400
ALU_OP2     = 0x0800
ALU_OP3     = 0x1000
ALU_CIN     = 0x2000

ADR_EN      = 0x4000
ADR_ST      = 0x8000

C_ST        = 0x010000
C_EN        = 0x020000
D_ST        = 0x040000
D_EN        = 0x080000
A_ST        = 0x100000
A_EN        = 0x200000
B_ST        = 0x400000
B_EN        = 0x800000

PC_ID       = 0x01000000
PC_LD       = 0x02000000
PC_CT       = 0x04000000
PC_EN       = 0x08000000

SP_ID       = 0x10000000
SP_LD       = 0x20000000
SP_CT       = 0x40000000
SP_EN       = 0x80000000

MM_E16 = MM_OP1
MM_S16 = MM_OP0
MM_SLO = MM_OP2
MM_SHI = MM_OP2|MM_OP0
MM_ELO = MM_OP2|MM_OP1
MM_EHI = MM_OP2|MM_OP1|MM_OP0

PC_INC = PC_ID|PC_CT
PC_DEC = PC_CT

SP_INC = PC_ID|PC_CT
SP_DEC = PC_CT

ALU_ADD = 0
ALU_SUB = ALU_OP0
ALU_AND = ALU_OP1
ALU_OR  = ALU_OP1|ALU_OP0
ALU_XOR = ALU_OP2
ALU_NOT = ALU_OP2|ALU_OP0
ALU_RTL = ALU_OP2|ALU_OP1
ALU_RTR = ALU_OP2|ALU_OP1|ALU_OP0

insts = np.zeros((256, 8), dtype=np.uint32)

NEXT = [ PC_EN|PC_INC|ADR_EN|CTRL_SINR ]

insts[:, :len(NEXT)] = NEXT
step = insts[:, len(NEXT):]

# NOP
step[0x08, :1] = [ CTRL_SRST ]
# lda, direct
step[0x10, :1] = [ PC_EN|PC_INC|ADR_EN|A_ST|CTRL_SRST ]
# ldb, direct
# ldc, direct
# ldd, direct

np.savetxt("microcode2.txt", insts, "%08lx", header="v3.0 hex words plain", comments="")

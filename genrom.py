import numpy as np

# Raw Pins

ADR_EN      = 0x01 << 0
CTRL_SINT   = 0x02 << 0
CTRL_SRST   = 0x04 << 0
CTRL_SINR   = 0x08 << 0
CTRL_SFLG   = 0x10 << 0
HL_OP0      = 0x20 << 0
HL_OP1      = 0x40 << 0
HL_OP2      = 0x80 << 0

PC_ID       = 0x01 << 8
PC_LD       = 0x02 << 8
PC_CT       = 0x04 << 8
PC_EN       = 0x08 << 8
SP_ID       = 0x10 << 8
SP_LD       = 0x20 << 8
SP_CT       = 0x40 << 8
SP_EN       = 0x80 << 8

ALU_EN      = 0x01 << 16
ALU_OP0     = 0x02 << 16
ALU_OP1     = 0x04 << 16
ALU_OP2     = 0x08 << 16
ALU_OP3     = 0x10 << 16
ALU_CIN     = 0x20 << 16
ADR_OUT     = 0x40 << 16

RAW_OP0     = 0x01 << 24
RAW_OP1     = 0x02 << 24
RAW_OP2     = 0x04 << 24
RAW_EN      = 0x08 << 24
REGB_LD     = 0x10 << 24
REGB_EN     = 0x20 << 24
REGA_LD     = 0x40 << 24
REGA_EN     = 0x80 << 24

# Combo Pins
PC_INC = PC_ID|PC_CT
PC_DEC = PC_CT

SP_INC = SP_ID|PC_CT
SP_DEC = SP_CT

HL_EN = HL_OP1
HL_LD = HL_OP0
HL_LDL = HL_OP2
HL_LDH = HL_OP2|HL_OP0
HL_ENL = HL_OP2|HL_OP1
HL_ENH = HL_OP2|HL_OP1|HL_OP0

RAW_FC = RAW_EN|RAW_OP2
RAW_FD = RAW_EN|RAW_OP2|RAW_OP0
RAW_FE = RAW_EN|RAW_OP2|RAW_OP1
RAW_FF = RAW_EN|RAW_OP2|RAW_OP1|RAW_OP0


rom1 = np.zeros((2, 8), dtype=np.uint64)
rom1[0, :3] = [ RAW_FE|HL_LDL|ADR_OUT, RAW_FF|HL_LDH|ADR_OUT, HL_EN|PC_LD|SP_DEC|CTRL_SINT|CTRL_SRST ]
rom1[1, :6] = [ PC_EN|HL_LD, HL_ENL|SP_EN|SP_DEC|ADR_EN|ADR_OUT, HL_ENH|SP_EN|SP_DEC|ADR_EN|ADR_OUT, RAW_FC|HL_LDL|ADR_OUT, RAW_FD|HL_LDH|ADR_OUT, HL_EN|PC_LD|CTRL_SRST ]

rom2 = np.zeros((64, 8), dtype=np.uint64)

NEXT = [ PC_EN|PC_INC|ADR_OUT|CTRL_SINR ]

rom2[:, :len(NEXT)] = NEXT
rom2[:, len(NEXT):len(NEXT)+1] = CTRL_SRST

step = rom2[:, len(NEXT):]
step[0x10>>2, :1] = [ PC_EN|PC_INC|ADR_OUT|REGA_LD|CTRL_SRST ]
step[0x15>>2, :3] = [ PC_EN|PC_INC|ADR_OUT|HL_LDL, PC_EN|PC_INC|ADR_OUT|HL_LDH, HL_EN|ADR_OUT|REGA_LD|CTRL_SRST ]
step[0x18>>2, :3] = [ PC_EN|PC_INC|ADR_OUT|HL_LDL, PC_EN|PC_INC|ADR_OUT|HL_LDH, HL_EN|ADR_OUT|ADR_EN|REGA_EN|CTRL_SRST ]


np.savetxt("microcode1.txt", rom1, "%016lx", header="v3.0 hex words plain", comments="")
np.savetxt("microcode2.txt", rom2, "%016lx", header="v3.0 hex words plain", comments="")

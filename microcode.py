# ALU
EN_OP0  = 0x01
EN_OP1  = 0x02
EN_OP2  = 0x04
EN_CIN  = 0x08
EN_ACC  = 0x10
ST_ACC  = 0x20
EN_ALU  = 0x40
# RAM
ST_RAM  = 0x80
EN_RAM  = 0x0100
# PC
EN_PC16 = 0x0200
EN_PC08 = 0x0400
EN_PCLD = 0x0800
EN_PCCT = 0x1000
# REGISTER
EN_RS0  = 0x2000
EN_RS1  = 0x4000
EN_RS2  = 0x8000
ST_RX   = 0x010000
EN_RX   = 0x020000
EN_RHL  = 0x040000
# CTRL
ST_INR  = 0x080000
ST_FLG  = 0x100000

INST_STEP = [
    EN_PC16|EN_RAM, EN_PC16|EN_PCCT|EN_RAM|ST_INR
]
instructions = bytearray([0x00]*0xff*0x10)

INSTS = [
    [EN_PC16|EN_RAM, EN_PC16|EN_RAM|EN_RX]
]

def write_microcode() -> None:
    with open("./microcode.txt", "w") as f:
        _ = f.write("v3.0 hex words addressed\n")


if __name__ == "__main__":
    print(instructions)
    # write_microcode()

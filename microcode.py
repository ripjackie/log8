import numpy as np

# ALU
sTMP   = 0x01
eACC   = 0x02
sACC   = 0x04
sACCMx = 0x08
eCIN   = 0x10
eOP0   = 0x20
eOP1   = 0x40
eOP2   = 0x80
# RAM
sMAR   = 0x0100
eRAM   = 0x0200
sRAM   = 0x0400
# PRG
ePRG16 = 0x0800
ePRG08 = 0x1000
ePRGld = 0x2000
ePRGct = 0x4000
# STP
eSTP16 = 0x8000
eSTP08 = 0x010000
sSTP   = 0x020000
# RFILE
sRX    = 0x040000
eRX    = 0x080000
eRXY   = 0x100000
eRX0   = 0x200000
eRX1   = 0x400000
eRX2   = 0x800000
# CTRL
sDATA  = 0x01000000
sINR   = 0x02000000
sRST   = 0x04000000


nxt = [ ePRG16|ePRGct|sMAR, eRAM|sINR ]

instructions = [
    # nop
    [ sRST ],
    # data ra, %NB
    [ ePRG16|ePRGct|sMAR, eRAM|sRX, sRST ],
    # data rb, %NB
    [ ePRG16|ePRGct|sMAR, eRAM|sRX|eRX0, sRST ],
    # data rl, %NB
    [ ePRG16|ePRGct|sMAR, eRAM|sRX|eRX1, sRST ],
    # data rh, %NB
    [ ePRG16|ePRGct|sMAR, eRAM|sRX|eRX1|eRX0, sRST ],
    # data rA, %NB %NB
    [ ePRG16|ePRGct|sMAR, eRAM|sRX, ePRG16|ePRGct|sMAR, eRAM|sRX|eRX0, sRST ],
    # data rH, %NB %NB
    [ ePRG16|ePRGct|sMAR, eRAM|sRX|eRX1, ePRG16|ePRGct|sMAR, eRAM|sRX|eRX0|eRX1, sRST ],
]

def format():
    for i, inst in enumerate(instructions):
        instructions[i] = nxt + inst
        instructions[i] += [0] * (16 - len(instructions[i]))

if __name__ == "__main__":
    format()
    arr = np.zeros((256, 16), dtype=int)
    print(instructions[0])
    arr[0x00:0x10] = instructions[0]
    arr[0x10:0x16] = instructions[1:7]

    np.savetxt("./microcode2.txt", arr, fmt="%08x", delimiter=" ", header="v3.0 hex words plain", comments="")
    print(arr)

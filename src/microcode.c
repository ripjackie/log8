#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define ALU_OE   0x01
#define ALU_OP0  0x02
#define ALU_OP1  0x04
#define ALU_OP2  0x08
#define TMP_WE   0x10
#define RAM_WE   0x20
#define RAM_OE   0x40
#define SHF_WE   0x80
#define SHF_OE   0x0100
#define PC_16_WE 0x0200
#define PC_08_WE 0x0400
#define PC_LD_EN 0x0800
#define PC_CT_EN 0x1000
#define RX_WE    0x2000
#define RX_OE    0x4000
#define FLG_WE   0x8000
#define IR_WE    0x010000
#define RX0      0x020000
#define RX1      0x040000
/*               0x080000
 *               0x100000
 *               0x200000
 *               0x400000
 *               0x800000
 */

#define add8 0
#define sll8 ALU_OP0
#define slr8 ALU_OP1
#define not8 ALU_OP1 | ALU_OP0
#define and8 ALU_OP2
#define or8  ALU_OP2 | ALU_OP0
#define xor8 ALU_OP2 | ALU_OP1
#define cmp8 ALU_OP2 | ALU_OP1 | ALU_OP0
/*
 * 0X NOP
 * 1X data RA <- Next Byte
 * 2X load 
 * 3X stor
 * 4X jump
 * 5X jmpc
 * 6X XX
 * 7X XX
 * 8X add
 * 9X sll
 * AX slr
 * BX not
 * CX and
 * DX or
 * EX xor
 * FX cmp
 */

static const uint32_t insts[][16] = {
  // Data
  {PC_16_WE|RAM_OE, PC_CT_EN|PC_16_WE|RAM_OE|IR_WE, PC_16_WE|RAM_OE, PC_CT_EN|PC_16_WE|RAM_OE|RX_WE},
};

void write_microcode(FILE *file) {
  // fprintf(file, "v3.0 hex words addressed\n");
  // fprintf(file, "0000: %06X %06X\n\n", next[0], next[1]);
  for (int inst = 0; inst < sizeof(insts) / sizeof(insts[0]); inst++) {
    for (int i = 0; i < 16; i++) {
      if (i % 8 == 0) {
        if (i != 0) {
          printf("\n");
        }
        printf("%04x:", (inst * 16 + i));
      }
      printf(" %06x", insts[inst][i]);
    }
    printf("\n");
  }
}

int main(void) {
  FILE *file = fopen("./Desktop/microcode.txt", "w");
  if (file == NULL) {
    perror(NULL);
    exit(1);
  }

  write_microcode(file);

  fclose(file);
}

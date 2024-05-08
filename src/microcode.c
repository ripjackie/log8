/*
 * Instructions are two byte:
 * 
 * 
 *
 */


#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef uint32_t inst;

/* ALU */
#define sACC   0x01
#define eACC   0x02
#define eACCMx 0x04
#define sCin   0x08
#define eOP0   0x10
#define eOP1   0x20
#define eOP2   0x40
#define eOP3   0x80

/* RAM */
#define sMAR 0x0100
#define eRAM 0x0200
#define sRAM 0x0400

/* PC */
#define ePC16 0x0800
#define ePC08 0x1000
#define ePCld 0x2000
#define ePCct 0x4000

/* SP */
#define eSP16 0x8000
#define eSP08 0x010000
#define sSP   0x020000

/* RFILE */
#define sRX   0x040000
#define eRX   0x080000
#define eR16  0x100000
#define eRAB  0x200000
#define eRLH  0x400000
#define sRsel 0x800000

/* Ctrl */
#define sData 0x0100000
#define sINR  0x02000000
#define sRST  0x04000000

/* Complex */
#define eRA8   eRX
#define sRA8   sRX
#define eRA16  eRX|eR16
#define sRA16L sRX|eR16
#define sRA16H sRX|eR16|eRLH
#define eRB8   eRX|eRAB
#define sRB8   sRX|eRAB
#define eRB16  sRX|eRAB|eR16
#define sRB16L sRX|eRAB|eR16
#define sRB16H sRX|eRAB|eR16|eRLH
#define add8 0
#define sll8 eOP0
#define slr8 eOP1
#define not8 eOP1|eOP0
#define and8 eOP2
#define or8  eOP2|eOP0
#define xor8 eOP2|eOP1
#define cmp8 eOP2|eOP1|eOP0

inst next[] = {
  ePC16|ePCct|sMAR, eRAM|sINR, ePC16|ePCct|sMAR, eRAM|sRsel
};
size_t next_len = sizeof(next) / sizeof(inst);

inst insts[0x100][0x10] = {0};
inst nop[] = { sRST };
inst data8[] = { ePC16|ePCct|sMAR, eRAM|sRA8, sRST };
inst data16[] = { ePC16|ePCct|sMAR, eRAM|sRA16L, ePC16|ePCct|sMAR, eRAM|sRA16H, sRST };
inst load[] = {};

void insert(inst start, inst end, inst *instruction, size_t inst_len) {
  for (int i = start; i <= end; i++) {
    int j;
    for (j = 0; j < next_len; j++) {
      insts[i][j] = next[j];
    }
    for (; j < 0x10 && j - next_len < inst_len / sizeof(inst); j++) {
      insts[i][j] = instruction[j - next_len];
    }
  }
}

void fill_instructions() {
  insert(0x00, 0x0f, nop, sizeof(nop));
  insert(0x10, 0x10, data8, sizeof(data8));
  insert(0x14, 0x14, data16, sizeof(data16));
}

void write_output(FILE* output) {
  fprintf(output, "v3.0 hex words addressed\n");
  printf("v3.0 hex words addressed\n");
  for (int i = 0; i < 0x100; i++) {
    for (int j = 0; j < 0x10; j++) {
      if (j % 8 == 0) {
        fprintf(output, "\n%04x:", i*16 + j);
        printf("\n%04x:", i*16 + j);
      }
      fprintf(output, " %08x", insts[i][j]);
      printf(" %08x", insts[i][j]);
    }
  }
  fprintf(output, "\n");
  printf("\n");
}

int main(void) {
  fill_instructions();

  FILE* output = fopen("./microcode.txt", "w");
  if (output == NULL) {
    perror(NULL);
    return 1;
  }

  write_output(output);

  fclose(output);

  return 0;
};

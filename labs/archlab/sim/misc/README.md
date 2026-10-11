# Y86-64 Assembler, Instruction Simulator, and HCL Translator

## Tools

> This directory contains all of the source files for the following:

本目录包含以下工具的全部源文件（source files）。

| Tool | Description |
| --- | --- |
| `YAS` | Y86-64 assembler |
| `YIS` | Y86-64 instruction level simulator |
| `HCL2C` | HCL to C translator |
| `HCL2V` | HCL to Verilog translator |

## Building the Tools

```bash
make clean
make
```

## Files

| File | Description |
| --- | --- |
| `Makefile` | Builds yas, yis, hcl2c, hcl2v |
| `README` | This file |

### Versions of Makefile in the Student's Distribution

| File | Distribution |
| --- | --- |
| `Makefile-sim` | Instructor distribution only |

### Example Programs for Part A of the CS:APP Architecture Lab

| File | Description |
| --- | --- |
| `examples.c` | C versions of three Y86-64 functions |
| `ans-copy.ys` | Solution copy function; instructor distribution only |
| `ans-sum.ys` | Solution sum function; instructor distribution only |
| `ans-rsum.ys` | Solution rsum function; instructor distribution only |

### Instruction Simulator Code Shared by yas, yis, ssim, ssim+, and psim

| File |
| --- |
| `isa.c` |
| `isa.h` |

### Files Used to Build the yas Assembler

| File | Description |
| --- | --- |
| `yas` | The YAS binary |
| `yas.c` | yas source file |
| `yas.h` | yas header file |
| `yas-grammar.lex` | Y86-64 lexical scanner spec |
| `yas-grammar.c` | Lexical scanner generated from yas-grammar.lex |

### Files Used to Build the yis Instruction Simulator

| File | Description |
| --- | --- |
| `yis` | The YIS binary |
| `yis.c` | yis source file |

### Files Used to Build the hcl2c Translator

| File | Description |
| --- | --- |
| `hcl2c` | The HCL2C binary |
| `node.c` | Auxiliary routines |
| `node.h` | Header file for auxiliary routines |
| `hcl.lex` | HCL lexical scanner spec |
| `lex.yy.c` | HCL lexical scanner generated from hcl.lex |
| `hcl.y` | HCL grammar |
| `hcl.tab.c` | HCL parser generated from hcl.y |
| `hcl.tab.h` | Token definitions |

### Example HCL Programs Used During the Writing of the CS:APP Book

| File | Distribution |
| --- | --- |
| `frag.{hcl,c}` | Instructor distribution only |
| `mux4.{hcl,c}` | Instructor distribution only |
| `reg-file.{hcl,c}` | Instructor distribution only |

## License

> Copyright (c) 2002, R. Bryant and D. O'Hallaron, All rights reserved. May not be used, modified, or copied without permission.

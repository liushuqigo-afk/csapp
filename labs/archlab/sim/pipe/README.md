# Pipelined Y86-64 Simulator

> This directory contains the code to construct simulators for PIPE and the variants of it described in the homework exercises.

本目录包含 PIPE 流水线处理器及课后练习中相关变体的模拟器代码。

## 1. Building the simulator

### Versions and interfaces

> Different versions of the PIPE simulator can be constructed to use different HCL files when working on the different homework problems.

| Binary | VERSION | HCL File | Description |
| --- | --- | --- | --- |
| `psim` | `std` | `pipe-std.hcl` | Standard simulator (default) |
| `psim` | `broken` | `pipe-broken.hcl` | Does not handle any hazards |
| `psim` | `full` | `pipe-full.hcl` | For adding iaddq |
| `psim` | `nobypass` | `pipe-nobypass.hcl` | For implementing PIPE- (called pipe-stall.hcl in text) |
| `psim` | `lf` | `pipe-lf.hcl` | For implementing load forwarding |
| `psim` | `nt` | `pipe-nt.hcl` | For implementing NT branch prediction |
| `psim` | `btfnt` | `pipe-btfnt.hcl` | For implementing BTFNT branch pred. |
| `psim` | `1w` | `pipe-1w.hcl` | For implementing single write port |
| `psim` | `super` | `pipe-super.hcl` | Implements iaddq & load forwarding |

> The Makefile can be configured to build simulators that support GUI and/or TTY interfaces. A simulator running in TTY mode prints all information about its runtime behavior on the terminal. It's hard to understand what's going on, but useful for automated testing, and doesn't require any special installation features. A simulator running in GUI mode uses a fancy graphical user interface. Nice for visualizing and debugging, but requires installation of Tcl/Tk on your system.

做不同习题时，可以选用相应的硬件控制语言文件（HCL，Hardware Control Language）来构建不同版本的 PIPE 模拟器。`Makefile` 可配置终端界面（TTY）、图形用户界面（GUI）或同时支持两者：TTY 打印完整运行信息，适合自动化测试，不需要特殊安装配置；GUI 更便于观察和调试，但需要 Tcl/Tk。

### Build a selected version

> The Makefile has simple instructions for building the TTY and GUI forms. In either case, once you've configured the Makefile, you can build different versions of the simulators with different HCL files with commands of the form:

```bash
make clean; make psim VERSION=xxx
```

> where "xxx" is one of the versions listed above. To save typing, you can set the Makefile's VERSION variable. For example, if you are working on Problems 4.52 and 4.53, which require to modify pipe-full.hcl, then you could set VERSION=full in the Makefile. Typing

```bash
make clean; make psim
```

> would then make the pipe-full.hcl version of PIPE.

配置好 `Makefile` 后，将 `xxx` 换成版本表中的值即可构建对应模拟器，也可以直接设置 `Makefile` 中的 `VERSION`。例如，习题 4.52 和 4.53 要求修改 `pipe-full.hcl`；将 `VERSION` 设为 `full` 后，直接运行第二条命令就会构建使用该控制逻辑的 PIPE 版本。

## 2. Using the simulators

> The simulator recognizes the following command line arguments:
>
> file.yo required in GUI mode, optional in TTY mode (default stdin)

**Usage**

```text
psim [-htg] [-l m] [-v n] file.yo
```

模拟器识别下面列出的命令行参数。GUI 模式必须提供 `file.yo`；TTY 模式可以省略该文件，此时默认从标准输入（stdin）读取。

| Option | Description |
| --- | --- |
| `-h` | Print this message |
| `-g` | Run in GUI mode instead of TTY mode (default TTY mode) |
| `-l m` | Set instruction limit to m [TTY mode only] (default 10000) |
| `-v n` | Set verbosity level to 0 <= n <= 2 [TTY mode only] (default 2) |
| `-t` | Test result against the ISA simulator (yis) [TTY model only] |

## 3. Files

| File | Description |
| --- | --- |
| `Makefile` | Build the simulator |
| `Makefile-sim` | Makefile for the student distribution |
| `README` | This file |

### Files related to the CS:APP Architecture Lab

#### Sample programs

| File | Description |
| --- | --- |
| `ncopy.ys` | The default version of ncopy that the students optimize |
| `ncopy.c` | C version of ncopy that defines its semantics |

#### Preconstructed driver programs (by gen-driver.pl)

| File | Description |
| --- | --- |
| `sdriver.ys` | Driver that calls ncopy.ys on a short (4-word) array |
| `ldriver.ys` | Driver that calls ncopy.ys on a longer (63-word) array |

> Both drivers are generated automatically by the Makefile by typing "make drivers".

运行 `make drivers` 后，`Makefile` 会自动生成表中的两个驱动程序（driver programs）。

#### Solution files (Instructors only)

| File | Description |
| --- | --- |
| `gen-ncopy.pl` | Generates versions of benchmark program with various optimizations. See comments in file for explanation. |

#### Testing scripts

| File | Description |
| --- | --- |
| `gen-driver.pl` | Generate a driver program for an arbitrary ncopy implementation (default ncopy.ys). Type "make drivers" to construct sdriver.ys and ldriver.ys. |
| `benchmark.pl` | Runs an implementation of ncopy on array sizes 1 to 64 (default ncopy.ys) and computes its performance in units of CPE (cycles per element). |
| `correctness.pl` | Runs an implementation of ncopy on array sizes 0 to 64, and several longer ones and checks each for correctness. |
| `check-len.pl` | Determines number of bytes in .yo representation of ncopy function. |

### HCL files for different versions of the simulators

| File | Description |
| --- | --- |
| `pipe-std.hcl` | The standard PIPE processor described in the text |
| `pipe-broken.hcl` | A simulator that does not detect or handle hazards (useful when explaining hazards in lectures) |

#### HCL files for various CS:APP Homework Problems

| File | Description |
| --- | --- |
| `pipe-nobypass.hcl` | 4.51: Build version of PIPE without bypassing (called pipe-stall.hcl in the text) |
| `pipe-full.hcl` | 4.52-53: Add iaddq instruction to PIPE |
| `pipe-nt.hcl` | 4.54: Implement branch not taken strategy |
| `pipe-btfnt.hcl` | 4.55: Implement back-taken forward-not-taken strategy |
| `pipe-lf.hcl` | 4.56: Implement load forwarding logic |
| `pipe-1w.hcl` | 4.57: Implement single ported register file |

#### HCL solution files for the CS:APP Homework Problems (Instructors only)

| File | Description |
| --- | --- |
| `pipe-nobypass-ans.hcl` | 4.51 solution |
| `pipe-full-ans.hcl` | 4.52-53 solutions |
| `pipe-nt-ans.hcl` | 4.54 solution |
| `pipe-btfnt-ans.hcl` | 4.55 solution |
| `pipe-lf-ans.hcl` | 4.56 solutions |
| `pipe-1w-ans.hcl` | 4.57 solutions |
| `pipe-super.hcl` | Gives best performance for lab |

### PIPE simulator source files

| File | Description |
| --- | --- |
| `psim.c` | Base simulator code |
| `sim.h`, `pipeline.h`, `stages.h` | PIPE header files |
| `pipe.tcl` | TCL script for the GUI version of PIPE |

## License

> Copyright (c) 2002, 2010, 2015 R. Bryant and D. O'Hallaron, All rights reserved. May not be used, modified, or copied without permission.

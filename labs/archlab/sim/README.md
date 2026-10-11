# Y86-64 Tools (Student Distribution)

> This directory contains the student distribution of the Y86-64 tools. It is a proper subset of the master distribution, minus the solution files found in the master distribution.

本目录提供 Y86-64 工具的学生发行版（student distribution），它是完整发行版的真子集（proper subset），不包含教师使用的答案文件。

| Tool | Description |
| --- | --- |
| `yas` | Y86-64 assembler |
| `yis` | Y86-64 instruction (ISA) simulator |
| `hcl2c` | HCL to C translator |
| `hcl2v` | HCL to Verilog translator |
| `ssim` | SEQ simulator |
| `ssim+` | SEQ+ simulator |
| `psim` | PIPE simulator |

## 1. Building the Y86-64 tools

### GUI and TTY interfaces

> The Y86-64 simulators can be configured to support TTY and GUI interfaces. A simulator running in TTY mode prints all information about its run-time behavior on the terminal. It's harder to understand what's going on, but useful for automated testing, and doesn't require any special installation features. A simulator running in GUI mode uses a fancy graphical user interface. Nice for visualizing and debugging, but requires installation of Tcl/Tk on your system.

模拟器可以使用终端界面（TTY）或图形用户界面（GUI）。TTY 会在终端打印完整的运行信息，阅读起来较费力，但适合自动化测试，也不需要特殊安装配置；GUI 更便于观察执行过程和调试，需要系统安装 Tcl/Tk。

### Configure and build

> To build the Y86-64 tools, perform the following steps:
>
> NOTE: If your instructor prepared this distribution for you, then you can skip Step 1 and proceed directly to Step 2. The Makefile will already have the proper values for GUIMODE, TKLIBS, and TKINC for your system.
>
> Step 1. Decide whether you want the TTY or GUI form of the simulators, and then modify ./Makefile in this directory accordingly. (The changes you make to the variables in this Makefile will override the values already assigned in the Makefiles in the seq and pipe directories.)
>
> Building the GUI simulators: If you have Tcl/Tk installed on your system, then you can build the GUI form by initializing the GUIMODE, TKLIBS, and TKINC variables, as appropriate for your system. (The default values work for Linux systems.)
>
> Assigning GUIMODE=-DHAS_GUI causes the necessary GUI support code in the simulator sources to be included. The TKLIBS variable tells gcc where to look for the libtcl.so and libtk.so libraries. And the TKINC variable tells gcc where to find the tcl.h and tk.h header files.
>
> Building the TTY simulators: If you don't have Tcl/Tk installed on your system, then build the TTY form by commenting out all three of these variables (GUIMODE, TKLIBS, and TKINC) in the Makefile.
>
> Step 2: Once you've modified the Makefile to build either the GUI or TTY form, then you can construct the entire set of Y86-64 tools by typing

```bash
make clean; make
```

先选择界面形式并配置本目录的 `Makefile`；这里设置的变量会覆盖 `seq/` 和 `pipe/` 中的同名配置。如果教师已经完成配置，可跳过这一步。构建 GUI 版本时，`GUIMODE=-DHAS_GUI` 会启用界面支持代码，`TKLIBS` 指定 `libtcl.so`、`libtk.so` 的查找位置，`TKINC` 指定 `tcl.h`、`tk.h` 头文件（header files）的查找位置，原说明中的默认值适用于 Linux；没有 Tcl/Tk 时，将这三个变量的设置注释掉即可构建 TTY 版本。配置完成后，运行上述清理与构建命令，生成整套 Y86-64 工具。

## 2. Files

| File or directory | Description |
| --- | --- |
| `Makefile` | Builds the Y86-64 tools |
| `README` | This file |
| `misc/` | Source files for the Y86-64 assembler yas, the Y86-64 instruction simulator yis, and the isa.c file that is used by the -t option of the processor simulators to check the results against the ISA simulation. Also contains files for the programs hcl2c and hcl2v |
| `seq/` | Code for the SEQ and SEQ+ simulators. Contains HCL files for labs and homework problems that involve modifying SEQ. |
| `pipe/` | Code for the PIPE simulator. Contains HCL files for labs and homework problems that involve modifying PIPE. |
| `y86-code/` | Example .ys files from CS:APP and scripts for conducting automated benchmark teseting of the new processor designs. |
| `ptest/` | Automated regression testing scripts for testing processor designs. |
| `verilog/` | System for producing Verilog designs from HCL code |

## License

> Copyright (c) 2002, 2010, 2015, R. Bryant and D. O'Hallaron, All rights reserved. May not be used, modified, or copied without permission.

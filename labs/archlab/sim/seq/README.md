# Sequential Y86-64 Simulators

> This directory contains the code to construct simulators for SEQ, SEQ+, and the variants of it described in the homework exercises.

本目录包含 SEQ 顺序处理器、SEQ+ 及课后练习中相关变体的模拟器代码。

## 1. Building the simulators

### Versions and interfaces

> Different versions of the SEQ and SEQ+ simulators can be constructed to use different HCL files when working on the different homework problems.

| Binary | VERSION | HCL File | Description |
| --- | --- | --- | --- |
| `ssim` | `std` | `seq-std.hcl` | Standard SEQ simulator described in textbook. |
| `ssim` | `full` | `seq-full.hcl` | For adding iaddq to SEQ. |
| `ssim+` | `std` | `seq+-std.hcl` | Standard SEQ+ simulator described in textbook. |

> The simulators run in either TTY or GUI mode:
>
> o TTY mode: A simulator running in TTY mode prints all information about its runtime behavior on the terminal. It's hard to understand what's going on, but useful for automated testing, and doesn't require any special installation features.
>
> o GUI mode: A simulator running in GUI mode uses a fancy graphical user interface. Nice for visualizing and debugging, but requires installation of Tcl/Tk on your system.
>
> The Makefile has simple instructions for building TTY or GUI simulators. A TTY simulator runs in TTY mode only. A GUI simulator can run in either TTY mode or GUI mode, according to a command line argument.

做不同习题时，可以选用相应的硬件控制语言文件（HCL，Hardware Control Language）来构建 SEQ 或 SEQ+ 的不同版本。终端模式（TTY）会打印完整运行信息，适合自动化测试，不需要特殊安装配置；图形用户界面模式（GUI）便于观察和调试，但需要 Tcl/Tk。TTY 版本只能在终端运行，GUI 版本则可以通过命令行参数（command line argument）选择两种运行模式。具体构建配置见 `Makefile`。

### Build a selected version

> Once you've configured the Makefile, you can build the different simulators with commands of the form

```bash
make clean; make ssim VERSION=xxx
```

> where "xxx" is one of the versions listed above. For example, to build the version of SEQ described in the CS:APP text based on the control logic in seq-std.hcl, type

```bash
make clean; make ssim VERSION=std
```

> To save typing, you can also set the Makefile's VERSION variable.

配置好 `Makefile` 后，将 `xxx` 换成版本表中的值即可构建对应模拟器。例如，`VERSION=std` 使用 `seq-std.hcl` 的控制逻辑（control logic），构建教材介绍的标准 SEQ 版本；也可以直接在 `Makefile` 中设置 `VERSION`，减少重复输入。

## 2. Using the simulators

> The simulators take identical command line arguments:
>
> file.yo required in GUI mode, optional in TTY mode (default stdin)

**Usage**

```text
ssim [-htg] [-l m] [-v n] file.yo
```

这些模拟器接受相同的命令行参数。GUI 模式必须提供 `file.yo`；TTY 模式可以省略该文件，此时默认从标准输入（stdin）读取。参数及默认值如下。

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
| `Makefile` | Builds the SEQ and SEQ+ simulators |
| `Makefile-sim` | Makefile for student distribution |
| `README` | This file |
| `seq+.tcl` | TCL script for GUI version of SEQ+ |
| `seq.tcl` | TCL script for GUI version of SEQ |
| `ssim.c`, `sim.h` | Base sequential simulator code and header file |
| `seq-std.hcl` | Standard SEQ control logic |
| `seq+-std.hcl` | Standard SEQ+ control logic |
| `seq-full.hcl` | Template for the iaddq problem (4.34-35) |
| `seq-full-ans.hcl` | Solution for the iaddq problems (4.34-35) (Instructor distribution only) |

## License

> Copyright (c) 2002, 2010, 2013, 2015 R. Bryant and D. O'Hallaron, All rights reserved. May not be used, modified, or copied without permission.

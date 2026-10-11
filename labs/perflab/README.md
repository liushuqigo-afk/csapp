# CS:APP Performance Lab

## Overview

> This directory contains the files you will need for the CS:APP Performance Lab.
>
> **kernels.c** — This is the file you will be modifying and handing in.

本目录提供性能实验（Performance Lab）所需的文件。你需要在 `kernels.c` 中完成实现，并在完成后提交该文件。

## Student's Source Files

### File to modify

| File | Description |
| --- | --- |
| `kernels.c` | Student implementation |

### Support files

> You shouldn't modify any of these files.
>
> The driver (driver.c) tests the performance of all versions of the rotate and smooth kernels in your kernels.c file. The site-specific configuration file (config.h) was created by your instructor for your system.
>
> The timing routines (clock.{c,h} and fcyc.{c,h}) measure the performance of your code with our k-best measurement scheme using IA32 cycle counters.

以下支持文件不应修改。`driver.c` 会测试 `kernels.c` 中旋转（rotate）和图像平滑（smooth）运算核心（kernels）的全部实现版本；`config.h` 是教师为当前教学环境创建的配置。计时例程通过 IA32 周期计数器（cycle counters）测量性能，并采用 k 个最佳样本测量方案（k-best measurement scheme）。

| File | Description |
| --- | --- |
| `driver.c` | Performance driver for rotate and smooth kernels |
| `config.h` | Site-specific configuration file |
| `defs.h` | Various definitions needed by kernels.c and driver.c |
| `clock.{c,h}` | Timing routines |
| `fcyc.{c,h}` | Timing routines |
| `Makefile` | This is the makefile that builds the driver program |

## License

> Copyright (c) 2002, R. Bryant and D. O'Hallaron, All rights reserved.
> May not be used, modified, or copied without permission.

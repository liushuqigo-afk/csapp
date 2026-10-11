# CS:APP Malloc Lab

## Handout files for students

### Main Files

| File | Description |
| --- | --- |
| `mm.{c,h}` | Your solution malloc package |
| `mdriver.c` | The malloc driver that tests your mm.c file |
| `short{1,2}-bal.rep` | Two tiny tracefiles to help you get started |
| `Makefile` | Builds the driver |

> mm.c is the file that you will be handing in, and is the only file you should modify.

你需要在 `mm.c` 中实现内存分配程序，并提交这个文件；按原实验要求，它也是唯一应修改的文件。

### Other support files for the driver

| File | Description |
| --- | --- |
| `config.h` | Configures the malloc lab driver |
| `fsecs.{c,h}` | Wrapper function for the different timer packages |
| `clock.{c,h}` | Routines for accessing the Pentium and Alpha cycle counters |
| `fcyc.{c,h}` | Timer functions based on cycle counters |
| `ftimer.{c,h}` | Timer functions based on interval timers and gettimeofday() |
| `memlib.{c,h}` | Models the heap and sbrk function |

## Building and running the driver

> To build the driver, type "make" to the shell.
> To run the driver on a tiny test trace, use the short1-bal.rep command below. The -V option prints out helpful tracing and summary information.
> To get a list of the driver flags, use the -h command below.

先在命令行执行 `make` 构建测试驱动程序（driver），再用小型操作轨迹（test trace）`short1-bal.rep` 测试实现。`-V` 会打印详细的轨迹跟踪及汇总信息，`-h` 用于查看所有选项。下面保留原材料的命令；当前项目的本地运行入口和完整测试路径见 [ENVIRONMENT.md](../../ENVIRONMENT.md)。

```bash
make
mdriver -V -f short1-bal.rep
mdriver -h
```

## License

> Copyright (c) 2002, R. Bryant and D. O'Hallaron, All rights reserved.
> May not be used, modified, or copied without permission.

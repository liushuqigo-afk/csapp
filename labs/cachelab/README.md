# CS:APP Cache Lab

## Overview

> This is the handout directory for the CS:APP Cache Lab.
> **csim.c and trans.c** — You will be modifying and handing in these two files.

本目录提供 CS:APP 缓存实验（Cache Lab）的学生材料。实现集中在 `csim.c` 和 `trans.c` 中，完成后提交这两个文件。

## Running the autograders

> Before running the autograders, compile your code.
> Check the correctness of your simulator.
> Check the correctness and performance of your transpose functions.
> Check everything at once (this is the program that your instructor runs).

先编译代码，再分别测试缓存模拟器（cache simulator）的正确性，以及矩阵转置函数（transpose functions）的正确性和性能。转置测试覆盖 `32 × 32`、`64 × 64` 和 `61 × 67` 三种尺寸；最后的 `driver.py` 会一次完成全部检查，也是教师使用的评分入口。旧版 Python 入口的兼容运行方式见 [ENVIRONMENT.md](../../ENVIRONMENT.md)。

```bash
make
./test-csim
./test-trans -M 32 -N 32
./test-trans -M 64 -N 64
./test-trans -M 61 -N 67
./driver.py
```

## Files

### Student files

| File | Description |
| --- | --- |
| `csim.c` | Your cache simulator |
| `trans.c` | Your transpose function |

### Tools for evaluating your simulator and transpose function

| File | Description |
| --- | --- |
| `Makefile` | Builds the simulator and tools |
| `README` | This file |
| `driver.py*` | The driver program, runs test-csim and test-trans |
| `cachelab.c` | Required helper functions |
| `cachelab.h` | Required header file |
| `csim-ref*` | The executable reference cache simulator |
| `test-csim*` | Tests your cache simulator |
| `test-trans.c` | Tests your transpose function |
| `tracegen.c` | Helper program used by test-trans |
| `traces/` | Trace files used by test-csim.c |

# Y86-64 Assembly Examples

## Assembly

> This directory contains examples of Y86-64 assembly code programs (extension `.ys`) used in Chapter 4 of CS:APP3e. Given an assembly code file "file.ys", you can assemble it with the command "make file.yo". The resulting file is in the "object code" format described in the book.

本目录提供 CS:APP 第三版第 4 章使用的 Y86-64 汇编代码（assembly code）示例，扩展名为 `.ys`。对 `file.ys` 运行 `make file.yo`，便可生成教材中介绍的目标代码（object code）格式文件。

```bash
make file.yo
```

## Simulation

> You can assemble and simulate all the test programs in this directory. First, you need to make the different simulators in the pipe (psim) and seq (ssim and ssim+) directories. Then use the following commands. Each of these commands will cause a number of programs to be assembled and simulated. Lots of things will scroll by, but you should see the message "ISA Check Succeeds" for each of the programs tested.

可以批量汇编并模拟（simulate）本目录中的全部测试程序。先在 `pipe` 目录构建 `psim`，并在 `seq` 目录构建 `ssim` 和 `ssim+`，再执行相应命令。运行时会滚动显示大量信息；每个被测试的程序都应显示 `ISA Check Succeeds`，表示指令集架构检查（ISA Check）成功。

### PIPE

```bash
make testpsim
```

### SEQ

```bash
make testssim
```

### SEQ+

```bash
make testssim+
```

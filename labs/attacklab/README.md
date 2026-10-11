# Attack Lab

## Targets

> This file contains materials for one instance of the attacklab.
>
> **ctarget**
> Linux binary with code-injection vulnerability. To be used for phases
> 1-3 of the assignment.
>
> **rtarget**
> Linux binary with return-oriented programming vulnerability. To be
> used for phases 4-5 of the assignment.

本目录提供一个具体实验实例（instance）的配套材料。`ctarget` 是具有代码注入漏洞（code-injection vulnerability）的 Linux 可执行程序，用于第 1–3 阶段；`rtarget` 具有返回导向编程（return-oriented programming，ROP）漏洞，用于第 4–5 阶段。

## Supporting material

> **cookie.txt**
> Text file containing 4-byte signature required for this lab instance.
>
> **farm.c**
> Source code for gadget farm present in this instance of rtarget. You
> can compile (use flag -Og) and disassemble it to look for gadgets.
>
> **hex2raw**
> Utility program to generate byte sequences. See documentation in lab
> handout.

`cookie.txt` 保存当前实验所需的 4 字节签名（signature）。`farm.c` 是 `rtarget` 的指令片段库（gadget farm）源码，可用 `-Og` 编译后反汇编（disassemble），查找可用片段。`hex2raw` 用于生成字节序列（byte sequences），具体用法见实验材料。

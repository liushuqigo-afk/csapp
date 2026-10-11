# CS:APP 课程课件索引

本目录保存 [CMU 15-213 Fall 2015 官方课程表](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html) 中的全部授课 PDF，共 26 份，覆盖第 1–27 讲（第 2、3 讲共用一份课件）。编号按官方课程顺序保留；配套阅读章节均指 CS:APP 第三版。

| 讲次 | 内容与本地 PDF | 第三版阅读 | 配套课堂代码 |
| --- | --- | --- | --- |
| 1 | [课程概览](01-overview.pdf) | 第 1 章 | — |
| 2–3 | [位、字节与整数](02-03-bits-ints.pdf) | 2.1–2.3 | [02-03-bits-ints](../../examples/lectures/02-03-bits-ints/) |
| 4 | [浮点数](04-float.pdf) | 2.4 | — |
| 5 | [机器级编程：基础](05-machine-basics.pdf) | 3.1–3.5 | [05-machine-basics](../../examples/lectures/05-machine-basics/) |
| 6 | [机器级编程：控制流](06-machine-control.pdf) | 3.6 | [06-machine-control](../../examples/lectures/06-machine-control/) |
| 7 | [机器级编程：过程与调用](07-machine-procedures.pdf) | 3.7 | [07-machine-procedures](../../examples/lectures/07-machine-procedures/) |
| 8 | [机器级编程：数据](08-machine-data.pdf) | 3.8–3.9 | [08-machine-data](../../examples/lectures/08-machine-data/) |
| 9 | [机器级编程：进阶](09-machine-advanced.pdf) | 3.10 | [09-machine-advanced](../../examples/lectures/09-machine-advanced/) |
| 10 | [代码优化](10-optimization.pdf) | 第 5 章 | [10-optimization](../../examples/lectures/10-optimization/) |
| 11 | [存储器层次结构](11-memory-hierarchy.pdf) | 6.1–6.3 | — |
| 12 | [高速缓存](12-cache-memories.pdf) | 6.4–6.7 | [12-cache-memories](../../examples/lectures/12-cache-memories/) |
| 13 | [链接](13-linking.pdf) | 第 7 章 | [13-linking](../../examples/lectures/13-linking/) |
| 14 | [异常控制流：异常与进程](14-ecf-procs.pdf) | 8.1–8.4 | [14-ecf-procs](../../examples/lectures/14-ecf-procs/) |
| 15 | [异常控制流：信号](15-ecf-signals.pdf) | 8.5–8.8 | [15-ecf-signals](../../examples/lectures/15-ecf-signals/) |
| 16 | [系统级 I/O](16-io.pdf) | 第 10 章 | [16-io](../../examples/lectures/16-io/) |
| 17 | [虚拟内存：概念](17-vm-concepts.pdf) | 9.1–9.6 | — |
| 18 | [虚拟内存：系统](18-vm-systems.pdf) | 9.7–9.8 | [18-vm-systems](../../examples/lectures/18-vm-systems/) |
| 19 | [动态内存分配：基础](19-malloc-basic.pdf) | 9.9 | [19-malloc-basic](../../examples/lectures/19-malloc-basic/) |
| 20 | [动态内存分配：进阶](20-malloc-advanced.pdf) | 9.9–9.11 | [20-malloc-advanced](../../examples/lectures/20-malloc-advanced/) |
| 21 | [网络编程：第一部分](21-netprog1.pdf) | 11.1–11.4 | — |
| 22 | [网络编程：第二部分](22-netprog2.pdf) | 11.5–11.6 | [22-netprog2](../../examples/lectures/22-netprog2/) |
| 23 | [并发编程](23-concprog.pdf) | 12.1–12.3 | [23-concprog](../../examples/lectures/23-concprog/) |
| 24 | [同步：基础](24-sync-basic.pdf) | 12.4、12.5.1–3 | [24-sync-basic](../../examples/lectures/24-sync-basic/) |
| 25 | [同步：进阶](25-sync-advanced.pdf) | 12.5.4–5、12.7 | [25-sync-advanced](../../examples/lectures/25-sync-advanced/) |
| 26 | [线程级并行](26-parallelism.pdf) | 12.6 | [26-parallelism](../../examples/lectures/26-parallelism/) |
| 27 | [计算的未来](27-future.pdf) | — | — |

每份 PDF 的官方原始地址为课程表目录下的 `lectures/<本地同名文件>`。课堂代码来自官方 [associated code files 总包](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/code.tar)，原包保存在 [archives/examples/code.tar](../../archives/examples/code.tar)，随包附带的各讲 `.tar` 也保存在该目录；解压时仅跳过一项原作者编辑器锁符号链接。代码按上游内容保留，部分示例包含预编译程序、反汇编或实验数据，学习时应以源码重新编译。

# CS:APP 学习内容与 Lab 完成顺序

以《Computer Systems: A Programmer's Perspective》第三版（CS:APP3e）和 CMU 15-213 Fall 2015 为主线。推荐边学边做：**Data → Bomb → Attack → Cache → Shell → Malloc → Proxy**。每个阶段先读书、看课、运行对应例子，再开始 Lab；达到该阶段的完成标准后进入下一项作业。

官方课表使用第三版内容，并因实验依赖把第 10 章 I/O 提前到虚拟内存之前。不同视频平台会拆分或合并课堂录像，请按下面的英文课程标题定位，不把视频分 P 号当成统一课号。[CMU Fall 2015 课表](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html)

## 1. 先准备环境与 C 基础

先阅读 [环境说明](ENVIRONMENT.md)。在 x86-64 Linux 中进行编译和实验；Windows 用户在 WSL2 的 Linux 终端中操作，项目优先放在 WSL 的 Linux 文件系统。PowerShell 中安装的软件、Windows 路径和 Windows 进程，与 WSL 中的 Linux 软件、路径和进程分别维护。

主线至少需要熟悉 C 的指针、数组、结构体、函数调用和基本文件操作，能用 `gcc`、`make` 编译，能读终端错误。起点是 `examples/textbook/intro/` 中的 `hello.c`，随后运行 `examples/textbook/data/` 中的字节表示示例。教材示例的章节归属见 [官方示例索引](https://csapp.cs.cmu.edu/3e/code.html)。

## 2. 课程、教材、示例与作业对照

下表中的目录相对于 `csapp_learning/`。`examples/textbook/` 是教材例子，`examples/lectures/` 是课程演示代码。课程目录名前的数字属于官网归档命名，不保证与视频平台编号一致。

| 阶段 | 上课内容（按标题定位） | 第三版阅读范围 | 先运行或阅读的示例目录 | 何时开始、何时完成作业 |
| --- | --- | --- | --- | --- |
| 0 | Overview | 第 1 章 | `examples/textbook/intro/` | 建立 C 编译、运行、调试流程，无对应主线 Lab |
| 1 | Bits, Bytes, and Ints；Floating Point | 第 2 章 | `examples/textbook/data/`；`examples/lectures/02-03-bits-ints/` | 整数表示后开始 Data 整数题；浮点表示后完成 Data 全部题 |
| 2 | Machine Prog: Basics / Control / Procedures / Data | 3.1–3.9 | `examples/textbook/asm/`；`examples/lectures/05-machine-basics/` 至 `08-machine-data/` | 控制流后开始 Bomb；掌握调用、递归、数组和结构体后完成 6 个常规 phase |
| 3 | Machine Prog: Advanced | 3.10，重点 3.10.3–3.10.4 | `examples/lectures/09-machine-advanced/` | Bomb 完成、能跟踪栈帧后开始 Attack；进入 Cache 作业前完成 5 个 phase |
| 4 | Code Optimization；The Memory Hierarchy；Cache Memories | 第 5 章、第 6 章 | `examples/textbook/opt/`、`mem/`；`examples/lectures/10-optimization/`、`12-cache-memories/` | 学完 Cache 后开始 Cache；先模拟器、后转置优化，完成再进入 Shell |
| 5 | Linking；ECF: Exceptions & Processes / Signals；System Level I/O | 第 7 章、第 8 章、第 10 章 | `examples/textbook/link/`、`ecf/`、`io/`；`examples/lectures/13-linking/` 至 `16-io/` | 学完进程和信号后开始 Shell；完成全部 trace，再开始 Malloc；期间可以继续学习虚拟内存 |
| 6 | Virtual Memory: Concepts / Systems；Storage Allocation: Basic / Advanced | 第 9 章，分配器重点 9.9–9.11 | `examples/textbook/vm/`；`examples/lectures/18-vm-systems/`、`19-malloc-basic/`、`20-malloc-advanced/` | 理解简单分配器之后开始 Malloc；正确性全通过、堆检查器可靠后优化，完成再进入 Proxy |
| 7 | Network Programming: Part 1 / Part 2 | 第 11 章 | `examples/textbook/netp/`，先 echo 后 Tiny；`examples/lectures/22-netprog2/` | 开始 Proxy 的顺序转发部分；并发和缓存部分等待下一阶段 |
| 8 | Concurrent Programming；Synchronization: Basic / Advanced；Thread-Level Parallelism | 第 12 章 | `examples/textbook/conc/`；`examples/lectures/23-concprog/` 至 `26-parallelism/` | 把 Proxy 扩展为并发代理、再加入共享缓存；全部阶段通过后结束主线 |

上表的课程与章节对应依据 [官方课表](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html)；作业功能与分阶段要求分别见下面各 Lab 的官方 writeup。

### Shell 和 Malloc 为什么这样排

Fall 2015 的实际安排是 Shell 先于 Malloc：Shell 在 2015-10-22 发布，2015-11-03 截止；Malloc 在 2015-11-03 发布。这里采用同一顺序。[官方课表](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html)

如果按书的章节顺序学习，容易看到“第 8 章 → 第 9 章 Malloc → 第 10 章 I/O”的路线。自学时两种顺序都可行：Shell 依赖进程与信号，Malloc 依赖虚拟内存与分配器，各自的前置知识满足即可。本目录建议先 Shell，跟随课程录像，并让每次只有一个主要作业处于实现阶段。

## 3. 每个 Lab 的动手入口与完成标准

先读各 Lab 的 `README`、官方 writeup，以及待实现函数上方的规则。学生 handout 是练习起点；各 Lab 都位于 `labs/<lab名称>/`，对应说明书链接见下面各 Lab 段落。保留自己写的过程笔记。下面命令在对应 Lab 目录内运行；旧 handout 的兼容性处理见 [环境说明](ENVIRONMENT.md)。

### Data Lab：位运算、补码与浮点表示

目录：[labs/datalab/](labs/datalab/)，说明：[datalab.pdf](materials/lab-writeups/datalab.pdf)。

修改 `bits.c`。先做整数题，再做浮点题；每个函数都要同时满足功能要求、允许的操作符和操作次数上限。

```bash
make
./btest
./dlc -e bits.c
./driver.pl
```

**完成标准：**所有题的功能测试通过，`dlc` 不报告规则违反或操作数超限；能解释边界输入为什么成立。仅 `btest` 通过还不够。[官方 Data Lab writeup](https://csapp.cs.cmu.edu/3e/datalab.pdf)

### Bomb Lab：理解机器代码

目录：[labs/bomblab/](labs/bomblab/)，说明：[bomblab.pdf](materials/lab-writeups/bomblab.pdf)。

以可执行文件 `bomb` 为分析对象，用 `gdb`、`objdump` 看控制流、调用约定和数据布局。`bomb.c` 只包含驱动部分，不能靠重新编译它获得完整炸弹。

```bash
gdb ./bomb
objdump -d ./bomb > bomb.disasm
# answers.txt 是你自行分析后写下的输入；每个 phase 占一行。
./bomb answers.txt
```

**完成标准：**6 个常规 phase 全部通过，每个 phase 能写出判断逻辑和推导过程。隐藏 phase 可作拓展。官方自学炸弹已关闭向评分服务器报告结果的功能。[官方 Bomb Lab 学生说明](https://csapp.cs.cmu.edu/3e/bomblab.pdf)、[官方自学 handout 入口](https://csapp.cs.cmu.edu/3e/labs.html)

### Attack Lab：栈、机器指令与 ROP

目录：[labs/attacklab/](labs/attacklab/)，说明：[attacklab.pdf](materials/lab-writeups/attacklab.pdf)。

使用官方自学包内的 `ctarget`、`rtarget` 与 `hex2raw`。先完成 `ctarget` 的 3 个 phase，再完成 `rtarget` 的 2 个 phase；只根据自己目标文件中的地址和 cookie 构造输入。

```bash
# payload.txt 是你为当前阶段自行构造的十六进制输入。
./hex2raw < payload.txt | ./ctarget -q
./hex2raw < payload.txt | ./rtarget -q
```

**完成标准：**5 个 phase 的对应目标均验证输入有效；能解释每段字节、返回地址、寄存器和栈布局。`-q` 关闭向课程评分服务器提交。当前 Ubuntu 24.04 上的启动兼容性与已验证的运行方式见 [环境说明](ENVIRONMENT.md#attack-lab-旧二进制兼容性)。[官方 Attack Lab writeup](https://csapp.cs.cmu.edu/3e/attacklab.pdf)

### Cache Lab：缓存模拟器与矩阵转置

目录：[labs/cachelab/](labs/cachelab/)，说明：[cachelab.pdf](materials/lab-writeups/cachelab.pdf)。

先实现 `csim.c` 并对照参考模拟器，之后优化 `trans.c`。优化前先确保结果正确，再比较 miss 数量。

```bash
make
./test-csim
./test-trans -M 32 -N 32
./test-trans -M 64 -N 64
./test-trans -M 61 -N 67
python3 ../../scripts/cachelab_driver.py
```

**完成标准：**模拟器全部参考 trace 通过；三种指定矩阵大小转置结果正确，遵守局部变量等限制；记录优化前后 miss 变化。本地评分 driver 的满分性能门槛为 32×32 不超过 300、64×64 不超过 1300、61×67 不超过 2000 次 miss，最终以本地 writeup 和 driver 为准。完整转置测试需要 Valgrind 的 Lackey 工具。[官方 Cache Lab writeup](https://csapp.cs.cmu.edu/3e/cachelab.pdf)、[官方 Cache Lab requirements](https://csapp.cs.cmu.edu/3e/README-cachelab)

### Shell Lab：进程、作业控制与信号

目录：[labs/shelllab/](labs/shelllab/)，说明：[shlab.pdf](materials/lab-writeups/shlab.pdf)。

修改 `tsh.c`。从最简单 trace 开始，逐步实现前台/后台执行、`jobs`、`bg`、`fg` 和信号处理；不要一次写完所有函数再调试。

```bash
make
make test01
make rtest01
```

后续按同样方式执行 `test02` 至 `test16`，并对照相应 `rtest02` 至 `rtest16`；也可直接使用 `sdriver.pl`。

**完成标准：**全部 16 个 trace 的行为与 `tshref` 一致，允许 PID 差异；交互检查 `Ctrl-C`、`Ctrl-Z`、前后台切换；反复运行复杂 trace 时无僵尸进程或丢失作业。参考可执行文件用于行为比较。[官方 Shell Lab writeup](https://csapp.cs.cmu.edu/3e/shlab.pdf)

### Malloc Lab：动态内存分配

目录：[labs/malloclab/](labs/malloclab/)，说明：[malloclab.pdf](materials/lab-writeups/malloclab.pdf)。

修改 `mm.c`。建议顺序是：理解教材的隐式空闲链表例子 → 完成 `malloc/free` → 编写堆一致性检查器 → 完成 `realloc` → 改进空间利用率和吞吐量。

```bash
make
./mdriver -V -f short1-bal.rep
./mdriver -V -f short2-bal.rep
./mdriver -V -t traces
```

本目录已补齐 `config.h` 默认列出的 11 个 trace；来自 Rice University 公开课程，格式已核验。`-t traces` 覆盖失效的 CMU 内部 AFS 路径，来源与适用范围见 [测试数据说明](labs/malloclab/traces/README.md)。

**完成标准：**全部 trace 的正确性通过；检查器能验证对齐、块边界、链表和空闲块状态；记录利用率与吞吐量改进。不把特定机器上的性能分数当成通用合格线。[官方 Malloc Lab writeup](https://csapp.cs.cmu.edu/3e/malloclab.pdf)

### Proxy Lab：I/O、网络与并发的综合练习

目录：[labs/proxylab/](labs/proxylab/)，说明：[proxylab.pdf](materials/lab-writeups/proxylab.pdf)。

修改 `proxy.c`，按顺序完成 HTTP GET 转发、并发处理和对象缓存。先让 Tiny 服务器与 echo 例子跑通，再实现代理。

```bash
make
python3 ../../scripts/proxylab_driver.py
```

**完成标准：**driver 的 BasicCorrectness、Concurrency、Cache 三项全部通过；自测二进制对象、显式端口、错误请求、客户端中断和重复并发请求；持续运行没有崩溃或明显文件描述符泄漏。额外测试是自学建议，因为自动评分不能覆盖全部健壮性与竞争问题。这个 Lab 的协议范围以 handout 为准，不把现代 HTTPS 网站是否能打开当成评分依据。[官方 Proxy Lab writeup](https://csapp.cs.cmu.edu/3e/proxylab.pdf)、[官方 Proxy Lab README](https://csapp.cs.cmu.edu/3e/README-proxylab)

## 4. Architecture / Performance 放在什么位置

这两项作为拓展，不打断首次完成 7 个主线 Lab 的节奏。

| 可选实验 | 建议插入位置 | 补充知识与完成标准 |
| --- | --- | --- |
| Architecture Lab（Y86-64） | Attack 后、Cache 前；或完成主线后单独补学 | 补第 4 章处理器体系结构，参考 `examples/textbook/arch/`，依次做 Part A/B/C；Y86-64 程序正确、SEQ/PIPE 回归测试通过，再降低 CPE。`correctness.pl` 与 `benchmark.pl` 分别检查正确性与性能；它们通常在模拟器的 `pipe/` 目录内。[官方 Arch Lab writeup](https://csapp.cs.cmu.edu/3e/archlab.pdf) |
| Performance Lab | 学完第 5、6 章、完成 Cache 后 | 参考 `examples/textbook/perf/`；修改 `kernels.c`，运行 `make driver` 和 `./driver`；先保证 rotate/smooth 正确，再记录 CPE 和 speedup。指标与机器、编译器及 handout 版本有关。[官方 Perf Lab writeup](https://csapp.cs.cmu.edu/3e/perflab.pdf) |

第三版应选 Y86-64 的 Architecture handout；不要混用第二版的 Y86。CMU 使用 Cache Lab 替代 Performance Lab；旧 IA32 Buffer Lab 已被 x86-64 Attack Lab 取代，所以 Buffer 不列入本学习主线。[官方 Lab 总览](https://csapp.cs.cmu.edu/3e/labs.html)

## 5. 建议的学习循环

每次只推进一个小知识点或一个测试阶段：

1. 看课前先读对应小节，列出不理解的问题。
2. 看课时打开示例，先预测输出或汇编，再实际运行核对。
3. 当阶段前置知识到位，阅读 handout；先实现能运行的最小版本。
4. 每做完一个函数/phase/trace，运行对应检查并记录错误原因。
5. 全部功能正确后才做性能优化，每次保留基线结果用于比较。
6. 写一页自己的阶段笔记：机制、踩坑、测试结果、还有哪些疑问。

旧实验可能含 32 位检查器、`-m32` 构建选项、旧 Python driver 或旧系统二进制；按 [环境说明](ENVIRONMENT.md) 处理依赖与兼容性，不通过改题目或删除测试来掩盖环境错误。上面的“全部通过”是你完成作业后的标准，不代表未填答 handout 已通过检查。

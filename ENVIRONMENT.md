# 环境准备与运行命令

整理时实际环境为 **WSL2、Ubuntu 24.04、x86-64、Bash、GCC 13**。资料采用第三版自学 handout；其中仍有旧版构建选项与测试脚本。

## 1. 安装依赖

在 Ubuntu / WSL 的 Linux 终端内执行：

```bash
sudo apt update
sudo apt install build-essential gcc-multilib libc6-dev-i386 \
  gdb binutils valgrind perl python3 curl net-tools
```

可选 Architecture Lab 还需要：

```bash
sudo apt install flex bison libfl-dev
```

`net-tools` 提供 Proxy 测试脚本使用的 `netstat`。Data、Malloc、Performance 的官方 Makefile 默认带 `-m32`，需要 32 位 C 头文件和链接库。保留这些选项可沿用 handout 的数据布局假设。

检查当前环境：

```bash
cd /home/david/projects/csapp_learning
bash scripts/check_environment.sh
```

检查脚本只读取工具状态，并在临时目录测试 `gcc -m32` 编译与运行。退出码 `1` 表示依赖尚不完整。整理时缺少 `gdb`、`valgrind`、`netstat`、32 位编译库，以及可选的 `flex`、`bison`、`libfl`；本次未修改系统软件。

Windows 的 PowerShell/CMD 与 WSL 的路径、软件和进程分别维护。上述命令在 WSL 内运行；本项目路径是 `/home/david/projects/csapp_learning`。官方预编译目标面向 Linux/x86-64，ARM 平台需要使用相应的 x86-64 Linux 环境。

## 2. 教材与课堂示例

下面命令均从项目根目录运行。官方包中有旧的预编译文件，以重新编译的输出为准；按当前学习内容选择单个例子，顶层 Makefile 只提示选择目标。

```bash
mkdir -p build

# 第 1 章：编译与运行
gcc -Wall -g examples/textbook/intro/hello.c -o build/hello
./build/hello

# 第 2 章：字节表示
gcc -Wall -O1 examples/textbook/data/show-bytes.c -o build/show-bytes
./build/show-bytes

# 第 10 章：标准输入复制到标准输出
gcc -Wall -g -I examples/textbook/include \
  examples/textbook/io/cpstdin.c examples/textbook/src/csapp.c \
  -pthread -o build/cpstdin
printf 'CSAPP\n' | ./build/cpstdin

# 第 12 章：创建并等待线程
gcc -Wall -g -I examples/textbook/include \
  examples/textbook/conc/hello.c examples/textbook/src/csapp.c \
  -pthread -o build/thread-hello
./build/thread-hello
```

使用 `csapp.h` 的示例通常还要链接 `src/csapp.c` 与线程库；单独编译源文件出现 undefined reference 时先检查对应目录的 Makefile。部分课程示例用于演示错误、数据竞争或未定义行为，结合课件判断预期结果。

## 3. 主线 Lab 的环境处理

下列各代码块独立执行，开始时先回到项目根目录。

### Data / Malloc / Performance 的 32 位构建

安装 multilib 后在各自 Lab 目录使用 `make`。如果出现 `bits/libc-header-start.h` 缺失或找不到 32 位启动对象，重新检查上面的依赖与环境检测结果。

Malloc 的完整测试路径已经补齐，运行：

```bash
cd labs/malloclab
make
./mdriver -V -f short1-bal.rep
./mdriver -V -f short2-bal.rep
./mdriver -V -t traces
```

最后一条命令通过 `-t traces` 覆盖上游仅适用于 CMU 内部环境的 AFS 路径。[补充测试数据说明](labs/malloclab/traces/README.md)

### Cache 的 Python 3 评分入口

官方 `labs/cachelab/driver.py` 使用 Python 2 的语法。保留该文件，并在 [scripts/cachelab_driver.py](scripts/cachelab_driver.py) 提供 Python 3 副本：转换语法、将子进程输出解码为文本，沿用原评分公式和测试参数。

```bash
cd labs/cachelab
make
./test-csim
./test-trans -M 32 -N 32
./test-trans -M 64 -N 64
./test-trans -M 61 -N 67
python3 ../../scripts/cachelab_driver.py
```

转置测试依赖 `valgrind --tool=lackey`。兼容入口也可以从根目录执行 `python3 scripts/cachelab_driver.py`。

### Proxy 的 Python 3 辅助服务

官方 `driver.sh` 使用 Bash，但它直接运行的 `nop-server.py` 采用旧的 `/usr/bin/python` 入口。独立入口 [scripts/proxylab_driver.py](scripts/proxylab_driver.py) 在内存中适配该调用，使其使用 Python 3，清除测试子进程中的代理环境变量，使本地请求经过指定的测试代理，并跳过原 driver 中会终止其他同名进程的 `killall`。测试进程在独立会话中运行，正常结束、超时或键盘中断时清理本次启动的服务。上游文件保持原样。

```bash
cd labs/proxylab
make
make -C tiny
python3 ../../scripts/proxylab_driver.py
```

评分脚本会启动本地 Tiny、你的 Proxy 和辅助服务，需要 `curl`、`netstat`。测试对象是 handout 定义的 HTTP GET 转发、并发与缓存。

### Attack Lab 旧二进制兼容性

使用本目录自学目标运行时带 `-q`：

```bash
cd labs/attacklab
./ctarget -h
./rtarget -h
./hex2raw < payload.txt | ./ctarget -q
```

`payload.txt` 由你完成当前 phase 时自行构造。整理时 `ctarget`、`rtarget` 的帮助信息及 `-q` 下空输入的正常返回均已验证；具体 phase 由学习者完成后测试。无需为启动这两个目标更改系统设置。

## 4. Architecture Lab 命令行构建

Y86-64 模拟器已从 handout 内的 `sim.tar` 解压到 `labs/archlab/sim/`。在该目录构建，而非使用上层的提交模板。

```bash
cd labs/archlab/sim
make GUIMODE= TKLIBS= TKINC= \
  CFLAGS='-Wall -O2 -fcommon' LCFLAGS='-O1 -fcommon'
```

空的 GUI 选项选择命令行版本，避开旧 Tcl/Tk 8.5 配置。`-fcommon` 兼容旧源码中对 `lineno` 等全局变量的重复暂定定义；它不修改题目逻辑。后续在 `seq/`、`pipe/` 重新构建时也传递相同参数。安装 `flex`、`bison`、`libfl-dev` 后再构建；Part B/C 的测试方法见 [archlab.pdf](materials/lab-writeups/archlab.pdf) 和 [模拟器说明](labs/archlab/simguide.pdf)。

## 5. 验证范围

本次完成资源校验、代表性教材/课堂例子的编译运行，以及能在现有依赖下构建的 Lab 检查。完整结果见 [验证记录](docs/VALIDATION.md)。安装缺少的依赖后，随学习进度运行各 Lab 的测试；“材料已准备”与“作业已完成”是两个阶段。

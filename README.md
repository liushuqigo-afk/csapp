# CS:APP 学习资料

以 **CS:APP 第三版 + CMU 15-213 Fall 2015** 为学习主线。教材示例、课堂示例、Lab 起始代码和说明书已经下载到本目录。

**先读 [学习内容与 Lab 完成顺序](STUDY_ORDER.md)**，再按 [环境准备](ENVIRONMENT.md) 检查依赖。

建议的主线作业顺序：

**Data → Bomb → Attack → Cache → Shell → Malloc → Proxy**

## 本地资料

| 路径 | 内容 |
| --- | --- |
| [examples/textbook/](examples/textbook/) | 官方完整教材示例包，含 C 源码、头文件、Makefile、汇编和配套数据 |
| [examples/lectures/](examples/lectures/) | CMU Fall 2015 的 20 个课堂示例目录 |
| [materials/lectures/INDEX.md](materials/lectures/INDEX.md) | 26 份课程 PDF 的中文索引，覆盖 27 次授课，其中整数部分共用一份 |
| [labs/](labs/) | 7 个主线 Lab + Architecture、Performance 两个选做 Lab |
| [materials/lab-writeups/](materials/lab-writeups/) | 9 份官方 Lab 说明书 PDF |
| [labs/malloclab/traces/](labs/malloclab/traces/) | 补充的 11 个 Malloc 测试输入及来源说明 |
| [archives/](archives/) | 官方原始压缩包，可用于恢复练习起点 |
| [SOURCES.md](SOURCES.md) | 来源、版本、整理说明 |
| [docs/VALIDATION.md](docs/VALIDATION.md) | 资源检查与本机编译验证结果 |

Lab 保留官方学生 handout 的起始状态；测试输出中的错误或低分可能来自尚未实现的函数。参考可执行文件用于官方测试和行为比较。你需要在 `bits.c`、`csim.c`、`trans.c`、`tsh.c`、`mm.c`、`proxy.c` 等入口自己完成实现。

## 从这里开始

在 WSL 的 Bash 终端执行：

```bash
cd /home/david/projects/csapp_learning
bash scripts/check_environment.sh
```

安装依赖后，先编译一个教材例子，再按学习顺序开始 Data Lab：

```bash
mkdir -p build
gcc -Wall -g examples/textbook/intro/hello.c -o build/hello
./build/hello

cd labs/datalab
make
./btest
./dlc -e bits.c
```

Cache 和 Proxy 的旧测试脚本提供独立兼容入口，使用方法见 [环境说明](ENVIRONMENT.md)。

原始下载文件的完整性检查可在项目根目录执行：

```bash
python3 scripts/verify_resources.py
# 或使用系统工具：
sha256sum -c SHA256SUMS
```

这些检查覆盖原始包、PDF 与补充测试输入；你修改 Lab 学生源码后仍可运行。

课程录像与公开资料入口：[CMU Fall 2015 官方课表](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html)、[CS:APP 官方示例](https://csapp.cs.cmu.edu/3e/code.html)、[CS:APP 官方自学 Lab](https://csapp.cs.cmu.edu/3e/labs.html)。

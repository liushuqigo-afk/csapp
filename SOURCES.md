# 来源与整理说明

获取日期：**2026-10-04（北京时间）**。版本：**CS:APP 第三版、CMU 15-213 Fall 2015**。

## 教材与课程

| 本地资料 | 来源 |
| --- | --- |
| `examples/textbook/` | [官方示例页面](https://csapp.cs.cmu.edu/3e/code.html) 的 [完整源码包 code-all.tar](https://csapp.cs.cmu.edu/3e/code-all.tar) |
| `examples/lectures/` | [Fall 2015 官方课表](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html) 的 [配套代码总包 code.tar](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/code.tar) |
| `materials/lectures/` | 同一课表链接的 26 份 lecture PDF；逐份地址见 `sources.json`，本地导航见 [课件索引](materials/lectures/INDEX.md) |
| `STUDY_ORDER.md` | 按官方课表、教材章节与各 Lab writeup 整理的自学路线 |

课堂总包中附带的 19 个单讲 `.tar` 存放于 `archives/examples/`。解压后的两个示例目录去掉了上游顶层 `code/`，其余普通文件保留；原包中的 4 个 Emacs 编辑器锁符号链接未展开。教材和课堂包可能包含历史预编译文件、反汇编、练习片段和演示错误的程序，它们属于官方材料。

## Lab

全部起始包与说明书来自 [CS:APP3e 官方 Lab 页面](https://csapp.cs.cmu.edu/3e/labs.html) 的公开 **Self-Study Handout** 和 **Writeup** 链接。

| Lab | 本地练习目录 | 原始包 | 本地说明 |
| --- | --- | --- | --- |
| Data | `labs/datalab/` | `datalab-handout.tar` | [datalab.pdf](materials/lab-writeups/datalab.pdf) |
| Bomb | `labs/bomblab/` | `bomb.tar` | [bomblab.pdf](materials/lab-writeups/bomblab.pdf) |
| Attack | `labs/attacklab/` | `target1.tar` | [attacklab.pdf](materials/lab-writeups/attacklab.pdf) |
| Cache | `labs/cachelab/` | `cachelab-handout.tar` | [cachelab.pdf](materials/lab-writeups/cachelab.pdf) |
| Shell | `labs/shelllab/` | `shlab-handout.tar` | [shlab.pdf](materials/lab-writeups/shlab.pdf) |
| Malloc | `labs/malloclab/` | `malloclab-handout.tar` | [malloclab.pdf](materials/lab-writeups/malloclab.pdf) |
| Proxy | `labs/proxylab/` | `proxylab-handout.tar` | [proxylab.pdf](materials/lab-writeups/proxylab.pdf) |
| Architecture（Y86-64，选做） | `labs/archlab/` | `archlab-handout.tar` | [archlab.pdf](materials/lab-writeups/archlab.pdf) |
| Performance（选做） | `labs/perflab/` | `perflab-handout.tar` | [perflab.pdf](materials/lab-writeups/perflab.pdf) |

原始 Lab 包均位于 `archives/labs/`。解压时去掉上游包裹目录，以保持本地目录名统一；Architecture 的内嵌 `sim.tar` 保留并另行展开。实验代码保持下载时的原样。2026-10-06 将 Lab 说明统一整理为 `README.md`：按语义合并短段落，英文引用块下接中文综合译文，专业术语随文保留英文对照；文件与参数清单使用英文表格。原 `README`、`README.txt` 作为兼容入口指向同目录的 Markdown 文件。英文说明、命令参数及版权声明保留；原始 README 快照见 [README 备份](archives/readme-backups/20261006-170255/lab-readmes.tar.gz)。

Malloc 官方包仅附两个短 trace。本目录从 [Rice University COMP 321 的公开测试数据](https://www.clear.rice.edu/comp321/labs/lab08/) 补充 11 个默认名称的 `.rep`，只获取数据文件。具体 URL 和 SHA-256 见 [sources.json](sources.json)，适用范围见 [traces/README.md](labs/malloclab/traces/README.md)。

## 本地兼容入口与校验

`scripts/cachelab_driver.py` 是官方 Cache driver 的 Python 3 兼容副本；`scripts/proxylab_driver.py` 调用官方 Proxy grader 并适配 Python 入口与本地测试环境。它们只处理测试工具兼容性，学生作业函数由学习者实现。[使用方式](ENVIRONMENT.md)

本次官网可以直接下载，示例和 Lab 无需 GitHub 镜像。原资源的版权与使用条件以文件中的上游声明为准。

[sources.json](sources.json) 记录下载地址、文件路径、大小、SHA-256 和压缩包来源；[SHA256SUMS](SHA256SUMS) 可由 `sha256sum -c SHA256SUMS` 校验。哈希为下载后本地计算，用于检测后续文件变化；上游未提供独立签名。

需要恢复某个 Lab 时，可将对应原包解压到新目录，再比较或复制需要恢复的文件，保留自己的解题代码和笔记。

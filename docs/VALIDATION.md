# 资源与本机验证记录

验证日期：2026-10-04。环境：Ubuntu 24.04 / WSL2 / x86-64 / GCC 13。编译验证在临时副本或临时输出目录中进行，保留练习目录的起始状态。

## 材料检查

- 9 个官方 Lab 原始包和 9 份官方 writeup 已下载，学生入口与测试工具齐全。
- 26 份授课 PDF 的大小、PDF 文件头和尾标记已核对。
- 压缩包解压前检查绝对路径、`..` 路径及链接；仅跳过示例包中的 4 个编辑器锁符号链接，原始包保留。
- Malloc 的 11 个补充 trace 已核对声明操作数、格式、编号范围及分配/释放顺序，共 112,372 个操作。
- `sources.json` 和 `SHA256SUMS` 覆盖 76 个原始下载文件及随包的单讲压缩包；可通过 `scripts/verify_resources.py` 重复校验。

## 编译与启动检查

| 对象 | 结果 |
| --- | --- |
| 教材 `intro/hello.c` | 编译运行成功，输出 `hello, world` |
| 教材 `data/show-bytes.c` | 编译运行成功，输出字节表示示例 |
| 教材 `io/cpstdin.c` + `csapp.c` | 编译运行成功，标准输入内容正确复制到输出 |
| 教材 `conc/hello.c` + `csapp.c` | 编译运行成功，线程创建与等待正常 |
| 课堂 `02-03-bits-ints/show-bytes.c` | 编译运行成功；原源码有格式参数警告 |
| Data | `dlc -h` 正常；默认 `make` 因缺少 32 位头文件停止 |
| Bomb | 启动并输出欢迎信息，空输入以预期的 EOF 错误退出 |
| Attack | 两个目标的 `-h` 与 `-q` 空输入正常；尚未求解 phase |
| Cache | 默认 `make -B` 成功，参考模拟器运行成功；转置测量等待安装 Valgrind |
| Shell | 默认 `make -B` 成功，学生/参考 `trace01` 可执行；其余 trace 待实现后验证 |
| Malloc | 默认 `make` 因缺少 32 位头文件停止；全部 trace 文件格式已核对 |
| Proxy | 默认 `make -B` 及 Tiny 构建成功；Tiny 上游示例有编译警告；完整 grader 等待 `netstat` 及学生实现 |
| Architecture | 普通命令行构建遇到 GCC 的 `lineno` 重复定义和缺少 `libfl`；已在环境说明给出 `-fcommon` 与依赖安装方式，完整构建尚未验证 |
| Performance | 默认 `make` 因缺少 32 位头文件停止 |
| 兼容脚本 | Cache Python 3 入口的帮助命令正常；Proxy 入口正确提示缺少 `netstat`，模拟异常退出确认清理本次后台子进程且保留无关进程；环境检测正确报告缺少工具和 multilib |

这是材料完整性和运行入口的检查。各 Lab 的最终正确性、性能和 phase 通过情况，在学习者完成实现后按 [学习顺序](../STUDY_ORDER.md) 中的标准验证。

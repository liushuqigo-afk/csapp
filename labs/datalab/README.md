# The CS:APP Data Lab

## Directions to Students

> Your goal is to modify your copy of bits.c so that it passes all the tests in btest without violating any of the coding guidelines.

你的目标是修改 `bits.c`，使它通过 `btest` 中的全部测试，同时遵守实验的编码规则（coding guidelines）。

## 0. Files

| File | Description |
| --- | --- |
| `Makefile` | Makes btest, fshow, and ishow |
| `README` | This file |
| `bits.c` | The file you will be modifying and handing in |
| `bits.h` | Header file |
| `btest.c` | The main btest program |
| `btest.h` | Used to build btest |
| `decl.c` | Used to build btest |
| `tests.c` | Used to build btest |
| `tests-header.c` | Used to build btest |
| `dlc*` | Rule checking compiler binary (data lab compiler) |
| `driver.pl*` | Driver program that uses btest and dlc to autograde bits.c |
| `Driverhdrs.pm` | Header file for optional "Beat the Prof" contest |
| `fshow.c` | Utility for examining floating-point representations |
| `ishow.c` | Utility for examining integer representations |

## 1. Modifying bits.c and checking it for compliance with dlc

> IMPORTANT: Carefully read the instructions in the bits.c file before you start. These give the coding rules that you will need to follow if you want full credit.
>
> Use the dlc compiler (./dlc) to automatically check your version of bits.c for compliance with the coding guidelines:

开始前先仔细阅读 `bits.c` 中的说明，其中的编码规则决定你的实现能否获得满分。完成实现后，用 `dlc` 编译器自动检查代码是否符合这些规则（compliance）；检查命令如下。

```bash
./dlc bits.c
```

> dlc returns silently if there are no problems with your code. Otherwise it prints messages that flag any problems. Running dlc with the -e switch causes dlc to print counts of the number of operators used by each function.
>
> Once you have a legal solution, you can test it for correctness using the ./btest program.

代码没有规则问题时，`dlc` 会静默返回；发现问题时，它会输出相应提示。加上 `-e` 可以查看每个函数使用的运算符数量（operator counts）。先确保实现符合规则，再使用 `btest` 检查结果是否正确。

```bash
./dlc -e bits.c
```

## 2. Testing with btest

### Building and rebuilding

> The Makefile in this directory compiles your version of bits.c with additional code to create a program (or test harness) named btest. To compile and run the btest program, type the commands below.
>
> You will need to recompile btest each time you change your bits.c program. When moving from one platform to another, you will want to get rid of the old version of btest and generate a new one. Use the clean and build commands below.

本目录的 `Makefile` 会把 `bits.c` 与测试支持代码一起编译，生成测试框架（test harness）`btest`。每次修改 `bits.c` 都必须重新编译；切换运行平台时，应先清理旧的构建产物，再生成新版本。运行时可以按需添加命令行参数。

```bash
make btest
```

```text
./btest [optional cmd line args]
```

```bash
make clean
make btest
```

### Test coverage and command line options

> Btest tests your code for correctness by running millions of test cases on each function. It tests wide swaths around well known corner cases such as Tmin and zero for integer puzzles, and zero, inf, and the boundary between denormalized and normalized numbers for floating point puzzles. When btest detects an error in one of your functions, it prints out the test that failed, the incorrect result, and the expected result, and then terminates the testing for that function.
>
> Btest does not check your code for compliance with the coding guidelines. Use dlc to do that.
>
> Here are the command line options for btest:

`btest` 会为每个函数运行数百万个测试用例，广泛覆盖边界情形（corner cases）附近的输入：整数题目包括 `Tmin` 和零，浮点数题目包括零、无穷大 `inf`，以及非规格化数（denormalized numbers）与规格化数（normalized numbers）的分界。发现错误后，它会打印失败的用例、错误结果和预期结果，然后停止测试该函数。它只检查计算结果，编码规则仍由 `dlc` 检查；下面列出可用选项。

```bash
./btest -h
```

```text
Usage: ./btest [-hg] [-r <n>] [-f <name> [-1|-2|-3 <val>]*] [-T <time limit>]
```

| Option | Description |
| --- | --- |
| `-1 <val>` | Specify first function argument |
| `-2 <val>` | Specify second function argument |
| `-3 <val>` | Specify third function argument |
| `-f <name>` | Test only the named function |
| `-g` | Format output for autograding with no error messages |
| `-h` | Print this message |
| `-r <n>` | Give uniform weight of n for all problems |
| `-T <lim>` | Set timeout limit to lim |

### Examples

> Test all functions for correctness and print out error messages.
> Test all functions in a compact form with no error messages.
> Test function foo for correctness.
> Test function foo for correctness with specific arguments.

下面四条命令依次用于：测试全部函数并显示错误信息；以精简格式测试全部函数并隐藏错误信息；只测试 `foo`；使用指定实参（arguments）测试 `foo`，其中第一个实参为 `27`，第二个实参为 `0xf`。

```bash
./btest
./btest -g
./btest -f foo
./btest -f foo -1 27 -2 0xf
```

## 3. Helper Programs

> We have included the ishow and fshow programs to help you decipher integer and floating point representations respectively. Each takes a single decimal or hex number as an argument. To build them type the command below.

`ishow` 和 `fshow` 分别用于解读整数表示（integer representations）和浮点数表示（floating-point representations）。它们都接收一个十进制或十六进制数字作为实参，使用 `make` 构建即可。

```bash
make
```

### Example usages

```bash
./ishow 0x27
```

```text
Hex = 0x00000027, Signed = 39, Unsigned = 39
```

```bash
./ishow 27
```

```text
Hex = 0x0000001b, Signed = 27, Unsigned = 27
```

```bash
./fshow 0x15213243
```

```text
Floating point value 3.255334057e-26
Bit Representation 0x15213243, sign = 0, exponent = 0x2a, fraction = 0x213243
Normalized.  +1.2593463659 X 2^(-85)
```

```bash
./fshow 15213243
```

```text
Floating point value 2.131829405e-38
Bit Representation 0x00e822bb, sign = 0, exponent = 0x01, fraction = 0x6822bb
Normalized.  +1.8135598898 X 2^(-126)
```

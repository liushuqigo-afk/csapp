# Y86-64 Simulator Regression Tests

## Test Suite

> This directory contains Perl scripts that provide comprehensive regression testing of the different Y86-64 simulators. There are four basic test types, implemented as four different scripts:

本目录提供四类 Perl 测试脚本，对不同的 Y86-64 模拟器（simulators）进行全面的回归测试（regression testing）。

| Script | Description |
| --- | --- |
| `optest.pl` | Tests each individual instruction type |
| `jtest.pl` | Tests all of the jump types under different conditions |
| `ctest.pl` | Tests different pipeline control combinations |
| `htest.pl` | Tests many different hazard possibilities. This involves running 864+ tests, so it takes a while. |

## Running the Tests

> Each of the tests has the following optional arguments. You can use make to run all four test programs. Options to make include the settings below. For example, you could say "make SIM=../pipe/psim TFLAGS=-i" to test the pipeline simulator including the iaddq instruction. (Note that this test will fail for the default implementation of pipe, since it does not implement the iaddq instruction.)

每个测试脚本都支持可选参数（optional arguments），也可以用 `make` 一次运行全部四个测试程序，并通过下表的设置传入参数。例如，`make SIM=../pipe/psim TFLAGS=-i` 会测试包含 `iaddq` 指令的流水线模拟器（pipeline simulator）。默认的 `pipe` 实现没有实现 `iaddq`，因此这项测试会失败。

### Script Arguments

| Argument | Description |
| --- | --- |
| `-s simfile` | Use simfile as simulator; default ../pipe/psim |
| `-i` | Test the iaddq instruction |

### Make Options

| Setting | Value |
| --- | --- |
| `SIM` | `simfile` |
| `TFLAGS` | `<any flags you want to give to the testing scripts>` |

```bash
make SIM=../pipe/psim TFLAGS=-i
```

## Debugging and Validation

> When the test program detects an erroneous simulation, it leaves the .ys file in the directory (ordinarily it deletes the test code it generates). You can then run a simulator (the GUI version is especially helpful here) on one of these failing cases. Suppose the failing test is in file bad-test.ys. Then you can execute "make bad-test.yo" to create the object code, and simulate it with one of the simulators. Note that the standard test code only detects functional bugs, where the processor simulation produces different results than would be predicted by simulating at the ISA level.

测试检测到模拟错误时，会保留失败用例（failing case）的 `.ys` 文件；正常情况下，生成的测试代码会被删除。可以用模拟器运行这些用例，其中图形界面（GUI）尤其便于排查。若失败测试是 `bad-test.ys`，执行 `make bad-test.yo` 即可生成目标代码（object code），再用模拟器运行。标准测试只检查功能性错误（functional bugs），即处理器模拟结果与指令集架构级（ISA level）模拟所预测的结果不一致。

```bash
make bad-test.yo
```

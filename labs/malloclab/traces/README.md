# Malloc Lab 补充测试数据

官方 CS:APP3e 自学 handout 仅附 `short1-bal.rep`、`short2-bal.rep`；本目录补齐 `config.h` 中列出的 11 个默认 trace 名称，数据取自 [Rice University COMP 321 课程公开的测试数据](https://www.clear.rice.edu/comp321/labs/lab08/)。每个文件均保持下载时的原始内容，来源 URL 与 SHA-256 见项目来源清单。

已核对这批文件采用官方 `mdriver.c` 支持的四行头部和 `a` / `r` / `f` 操作格式，并检查操作数量、编号范围及分配/释放顺序。这里只含测试输入，不包含分配器答案。它们是其他大学公开的同系列教学 trace，不能保证等同于任意学期 CMU 的评分数据或性能基准。

在 `labs/malloclab/` 目录编译好 `mdriver` 后执行：

```bash
./mdriver -V -f short1-bal.rep
./mdriver -V -f short2-bal.rep
./mdriver -V -t traces
```

`-t traces` 覆盖上游 `config.h` 中仅适用于 CMU 内部环境的默认 AFS 路径。前 9 个正式 trace 检查 `malloc` / `free`；后 2 个还检查 `realloc`。评分仍使用本地官方 handout 的配置，不能照搬 Rice 课程网页上的分数阈值。

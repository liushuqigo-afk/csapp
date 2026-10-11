# CS:APP Proxy Lab

## Student Source Files

> This directory contains the files you will need for the CS:APP Proxy Lab. These are starter files. csapp.c and csapp.h are described in your textbook. You may make any changes you like to these files. And you may create and handin any additional files you like.

本目录提供代理实验（Proxy Lab）的起始文件（starter files），其中 `csapp.c` 和 `csapp.h` 已在教材中介绍。你可以按需要修改这些文件，也可以创建并提交（hand in）额外文件。

| File | Description |
| --- | --- |
| `proxy.c` | Starter file |
| `csapp.h` | Starter file; described in the textbook |
| `csapp.c` | Starter file; described in the textbook |
| `Makefile` | Builds the proxy program |
| `port-for-user.pl` | Generates a random port for a particular user |
| `free-port.sh` | Handy script that identifies an unused TCP port for your proxy or tiny |
| `driver.sh` | The autograder for Basic, Concurrency, and Cache |
| `nop-server.py` | Helper for the autograder |
| `tiny` | Tiny Web server from the CS:APP text |

## Building and Submitting

> This is the makefile that builds the proxy program. Type "make" to build your solution, or "make clean" followed by "make" for a fresh build. Type "make handin" to create the tarfile that you will be handing in. You can modify it any way you like. Your instructor will use your Makefile to build your proxy from source.

使用 `Makefile` 构建代理程序：直接运行 `make`，或先执行 `make clean` 再执行 `make`，进行全新构建（fresh build）。完成后，`make handin` 会生成用于提交的 tar 归档文件（tarfile）。你可以按需要修改 `Makefile`，教师将用它从源码（source）构建你的代理。

```bash
make
```

```bash
make clean
make
```

```bash
make handin
```

## Port Selection

> Please use `port-for-user.pl` or `free-port.sh` to generate unique ports for your proxy or tiny server.

请使用 `port-for-user.pl` 或 `free-port.sh`，为代理（proxy）或 Tiny 服务器生成唯一端口（unique ports）。

```text
./port-for-user.pl <userID>
```

```bash
./free-port.sh
```

## Autograder

```bash
./driver.sh
```

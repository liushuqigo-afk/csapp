# Tiny Web Server

> Dave O'Hallaron — Carnegie Mellon University

## Overview

> This is the home directory for the Tiny server, a 200-line Web server that we use in "15-213: Intro to Computer Systems" at Carnegie Mellon University. Tiny uses the GET method to serve static content (text, HTML, GIF, and JPG files) out of ./ and to serve dynamic content by running CGI programs out of ./cgi-bin. The default page is home.html (rather than index.html) so that we can view the contents of the directory from a browser. Tiny is neither secure nor complete, but it gives students an idea of how a real Web server works. Use for instructional purposes only.

Tiny 是卡内基梅隆大学计算机系统导论课程使用的一个约 200 行的 Web 服务器，本目录是它的主目录。它通过 GET 方法提供 `./` 中的静态内容（static content），包括文本、HTML、GIF 和 JPG 文件；运行 `./cgi-bin` 中的 CGI 程序则可提供动态内容（dynamic content）。默认页面是 `home.html` 而非 `index.html`，以便从浏览器查看目录内容。Tiny 仅用于教学（instructional purposes）：它既不安全，也不完整，但能帮助理解真实 Web 服务器的工作方式。

## Installation and Running

> The code compiles and runs cleanly using gcc 2.95.3 on a Linux 2.2.20 kernel. To install Tiny: Type "tar xvf tiny.tar" in a clean directory. To run Tiny: Run "tiny <port>" on the server machine, e.g., "tiny 8000". Point your browser at Tiny:

代码使用 gcc 2.95.3，在 Linux 2.2.20 内核（kernel）上可以顺利编译和运行。安装时，在一个干净目录中解压 `tiny.tar`；启动时，在服务器机器上运行 `tiny <port>`，例如使用端口 8000，随后让浏览器访问下表中的静态或动态内容地址。

```bash
tar xvf tiny.tar
```

```text
tiny <port>
```

```bash
tiny 8000
```

| Content | URL |
| --- | --- |
| Static content | `http://<host>:8000` |
| Dynamic content | `http://<host>:8000/cgi-bin/adder?1&2` |

## Files

| File | Description |
| --- | --- |
| `tiny.tar` | Archive of everything in this directory |
| `tiny.c` | The Tiny server |
| `Makefile` | Makefile for tiny.c |
| `home.html` | Test HTML page |
| `godzilla.gif` | Image embedded in home.html |
| `README` | This file |
| `cgi-bin/adder.c` | CGI program that adds two numbers |
| `cgi-bin/Makefile` | Makefile for adder.c |

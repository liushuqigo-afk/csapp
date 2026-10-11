#!/usr/bin/env bash
# Check tools and 32-bit compilation without changing system configuration.
set -u

printf '系统：%s / %s\n' "$(uname -s)" "$(uname -m)"
printf '内核：%s\n' "$(uname -r)"
missing=0
for name in gcc make gdb objdump valgrind perl python3 curl tar sha256sum netstat; do
    if command -v "$name" >/dev/null 2>&1; then
        printf '[可用] %s\n' "$name"
    else
        printf '[缺少] %s\n' "$name"
        missing=1
    fi
done

if command -v gcc >/dev/null 2>&1; then
    check_dir=$(mktemp -d /tmp/csapp-env.XXXXXX) || exit 1
    trap 'rm -rf "$check_dir"' EXIT
    printf '#include <stdio.h>\nint main(void) { puts("ok"); return 0; }\n' > "$check_dir/check.c"
    if gcc -m32 "$check_dir/check.c" -o "$check_dir/check" > "$check_dir/build.log" 2>&1 \
        && "$check_dir/check" > /dev/null 2>&1; then
        printf '[可用] gcc -m32 编译与运行\n'
    else
        printf '[缺少] 32 位 C 编译/运行环境；参照 ENVIRONMENT.md 安装 multilib\n'
        missing=1
    fi
fi

if [ "$missing" -ne 0 ]; then
    printf '环境尚未完整，详见 ENVIRONMENT.md。\n'
fi
exit "$missing"

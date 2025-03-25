# python hook

​	在 Itzik Kotler的《InYourPythonPath.pdf》[1]中提到了一种 hook 方法，这里仅通过实验的方式展示 pdf 中所叙述的大部分内容，具体剩下的内容可以去翻阅相应文章。

## PYTHONPATH 控制包路径查找顺序

​	这里尝试 hook 原生库中的 string 库的内容，在 /tmp 目录下执行 python 解释器，导入 string 库没有发生任何非预期结果。

![](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/11.png)

尝试在 /tmp 目录下创建一个同名的 string.py 文件，将环境变量 PYTHONPATH 设置为 tmp 目录

```bash
echo 'print("just for test")' > string.py
PYTHONPATH=tmp
```

![](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/12.png)

​	再次执行 python 解释器，导入 string 库发生任何非预期结果：在导入库的时候，控制台面板打印了字符串"just for test"，这是我在 /tmp/string.py 上写入的 print 相关的代码，它被执行了。

​	通过`python -m site` 查看 python 解释器在查找包时的路径顺序，发现我们通过 PYTHONPATH 设置的 /tmp 目录被放在 sys.path 的列表的第一个元素的位置，并且原来的 /usr/lib/python3/dist-packages/ 路径并没有消失。

![](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/18.png)

​	这说明通过修改 PYTHONPATH 路径，我们可以修改 import 导入包的顺序。这就为我们 hook 函数奠定了基础。

## hook python 原生函数

​	在 string 库中我们发现了如下函数

```python
def capwords(s, sep=None):
    """capwords(s [,sep]) -> string

    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join.  If the optional second argument sep is absent or None,
    runs of whitespace characters are replaced by a single space
    and leading and trailing whitespace are removed, otherwise
    sep is used to split and join the words.

    """
    return (sep or ' ').join(x.capitalize() for x in s.split(sep))
```

capwords 函数用于将字符串中每个单词的首字母转换成大写字母，调用示例如下所示：

![](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/14.png)

那么我们根据上一节的内容，在 /tmp/string.py 中重构capwords 函数

```python
def capwords(s):
    return "This is a hook function named capwords"
```

![](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/16.png)

同样的打开 python 解释器后导入 string 库执行 capwords 方法，发现出现了非预期的结果：这次她并没有将我们输入的字符串中的单词首字母大写，而是执行了我们自定义的 capwords 的内容，但是我们要 hook 函数至少需要做到：

1.如何从Hook函数中调用原始函数
2.如果这种挂钩技术需要“覆盖”整个模块，确保其他模块的其他函数、类、常量等不用手动重写或复制粘贴的模块

```python
def capwords(s):
    print("This is a example that seemed to be normal")
    
    orig_capwords = getattr(get_mod("string"), "capwords")
    return orig_capwords(s)


def get_mod(mod_name):
    import sys, imp
    fd, path, desc = imp.find_module(mod_name, sys.path[::-1])
    return imp.load_module(mod_name, fd, path, desc)
```

​	第二个问题是第一个问题的衍生，只要解决了第一个问题，第二个问题无非就是把原生库中的内容做个映射，主要关注点就是上面代码中的 get_mod 函数，他的实现方式就类似于 *GetProcAddress()* 方法。

​	我这里就简单的还原了一下 capwords 函数，

![](https://github.com/thedarknessdied/.pth_study/blob/main/screen_shot/17.png)

# 参考资料：

[1] https://www.ikotler.org/docs/InYourPythonPath.pdf

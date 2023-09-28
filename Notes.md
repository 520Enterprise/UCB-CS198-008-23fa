# Linux System Administration Decal

A course covering the basics of setting up and administering a production-quality Linux server environment.

# Lab1

找出隐藏文件

```bash
ls -a
```

连接输出，然后删除文件

```bash
cat naming_is_hard* | xargs
#s t a n f o r d > b e r k e l e y
rm -rf nonsense/
```

从大文件里面找东西(`-A`是之后，``-B`是之前)

```bash
grep "http" -C 2 big_data.txt
```



![image-20230928182905095](https://img2023.cnblogs.com/blog/1892247/202309/1892247-20230928182907658-512842136.png)

增加执行权限

```bash
chmod +x a_script
```

查看文件详细，时间倒序

```bash
ls -ltr
```



`cat foo > out.txt`和`cat foo >> out.txt`的区别: 前者覆盖，后者追加



用`head`打印前几行(`-n` 选项用于指定要显示的行数)

```bash
head -n 4 big_data.txt
```





# Lab2

## Vim

Vim: [cheat sheet](https://devhints.io/vim)

删除10行: `d10`

暂停Vim，然后重新进入`Ctrl-Z`，然后`fg %i`其中`i`是实际进程数

同时编辑多个文件

```bash
# 分成上下两部分 用Ctrl+W和jk(或者箭头)进行上下切换
:split filename2
# 左右
:vsplit filename2
```

缩进: 先把光标停在要缩进的地方，然后Shift+V进入可视模式，上下移动箭头选择，然后用`>`或者`<`缩进

## tmux

[cheat sheet](https://gist.github.com/MohamedAlaa/2961058)

拆分: `Ctrl-b %` (左右两个) or `Ctrl-b "` (上下两个)

退出: `Ctrl-D`

列出当前session: `tmux ls`

回到指定session: `tmux a -t filename`

终止指定session: `tmux kill-session -t filename`

进入新的session: `tmux new -s filename`

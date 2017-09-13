# msys2 源使用帮助

## 收录架构

* MingGW: x86\_64, i686
* MSYS: x86\_64, i686

## 同步频率

每12小时

## 安装

访问[https://mirrors.hustunique.com/msys2/distrib/](https://mirrors.hustunique.com/msys2/distrib/)，选择需要的版本进行下载即可。

## pacman的配置

编辑`/etc/pacman.d/mirrorlist.mingw32`，在文件开头添加：

```
  Server = https://mirrors.hustunique.com/msys2/mingw/i686
```

编辑`/etc/pacman.d/mirrorlist.mingw64`，在文件开头添加：

```
  Server = https://mirrors.hustunique.com/msys2/mingw/x86_64
```

编辑`/etc/pacman.d/mirrorlist.msys`，在文件开头添加：

```
  Server = https://mirrors.hustunique.com/msys2/msys/$arch
```

然后执行`pacman -Sy`刷新软件包数据即可。

注:本帮助参考自[USTC开源镜像站](https://lug.ustc.edu.cn/wiki/mirrors/help/msys2)


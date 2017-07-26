# Arch Linux 源使用帮助

## 收录架构

x86\_64, i686

## 用法

用任何你喜欢的工具编辑`/etc/pacman.d/mirrorlist`文件，将以下行添加到文件的最顶端

```
Server = https://mirrors.hustunique.com/archlinux/$repo/os/$arch
```

可以用下面的命令立即更新pacman的缓存

```
sudo pacman -Syy
```




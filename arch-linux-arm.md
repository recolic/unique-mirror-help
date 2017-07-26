# Arch Linux ARM 源使用帮助

## 用法

用任何你喜欢的工具编辑`/etc/pacman.d/mirrorlist`文件，将以下行添加到文件的最顶端

```
Server = https://mirrors.hustunique.com/archlinuxarm/$repo/$arch
```

可以用下面的命令立即更新pacman的缓存

```
sudo pacman -Syy
```




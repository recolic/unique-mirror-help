# Arch Linux 源使用帮助

## 同步频率

每8小时

## 用法

用任何你喜欢的工具编辑`/etc/pacman.conf`文件，将以下行添加到文件尾端

```
[archlinuxcn]
Server = https://mirrors.hustunique.com/archlinuxcn/$arch
```

然后安装`archlinuxcn-keyring`包以导入 GPG key。

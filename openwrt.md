# openwrt 源使用帮助

## 收录架构

* Chaos Calmer 15.05.1

## 同步频率

每12小时

## 使用方法

先找到你的配置文件，它一般位于/etc/opkg.conf，也可能在/etc/opkg/目录下的某一个.conf文件。配置文件会有类似以下内容的部分

```
src/gz chaos_calmer_base http://downloads.openwrt.org/chaos_calmer/15.05.1/ar71xx/nand/packages/base
src/gz chaos_calmer_luci http://downloads.openwrt.org/chaos_calmer/15.05.1/ar71xx/nand/packages/luci
src/gz chaos_calmer_packages http://downloads.openwrt.org/chaos_calmer/15.05.1/ar71xx/nand/packages/packages
src/gz chaos_calmer_routing http://downloads.openwrt.org/chaos_calmer/15.05.1/ar71xx/nand/packages/routing
src/gz chaos_calmer_telephony http://downloads.openwrt.org/chaos_calmer/15.05.1/ar71xx/nand/packages/telephony
src/gz chaos_calmer_management http://downloads.openwrt.org/chaos_calmer/15.05.1/ar71xx/nand/packages/management
```

将`http://downloads.openwrt.org/chaos_calmer/15.05.1`更改为`https://mirrors.hustunique.com/openwrt`即可。

如果你的opkg不支持https访问，可直接更改为`http://mirrors.hustunique.com/openwrt`，效果完全相同。

更改后的配置文件可能像这样

```
src/gz chaos_calmer_base http://mirrors.hustunique.com/openwrt/ar71xx/nand/packages/base
src/gz chaos_calmer_luci http://mirrors.hustunique.com/openwrt/ar71xx/nand/packages/luci
src/gz chaos_calmer_packages http://mirrors.hustunique.com/openwrt/ar71xx/nand/packages/packages
src/gz chaos_calmer_routing http://mirrors.hustunique.com/openwrt/ar71xx/nand/packages/routing
src/gz chaos_calmer_telephony http://mirrors.hustunique.com/openwrt/ar71xx/nand/packages/telephony
src/gz chaos_calmer_management http://mirrors.hustunique.com/openwrt/ar71xx/nand/packages/management
```

如果你的opkg默认使用的不是`chaos_calmer/15.05.1`，**请勿使用此镜像源**。

建议阅读[官方文档](https://wiki.openwrt.org/zh-cn/doc/techref/opkg#配置)。


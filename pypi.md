# pypi \(pip\) 源使用帮助

## 同步频率

每12小时

## 临时使用

```
pip install -i https://mirrors.hustunique.com/pypi/web/simple <package name>
```

## 设为pip默认镜像源

编辑`~/.pip/pip.conf`\(若文件不存在，新建即可\)，修改`[global]`下的`index-url`为

```
[global]
index-url = https://mirrors.hustunique.com/pypi/web/simple
```

pip3和pip会共用同一个配置文件，无需额外配置。


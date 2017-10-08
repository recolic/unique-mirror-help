#!/bin/env python3

#template='https://mirrors.hustunique.com/ubuntu-release/$ver/'
#_vers=[12.04, '12.04.5', 14.04, '14.04.5', 15.04, 16.04, '16.04.3', 17.04]
template='https://mirrors.hustunique.com/linuxmint-cd/stable/$ver/'
_vers=[i for i in range(7,18)] + [17.1, 17.2, 17.3, 18, 18.1, 18.2]

vers=[str(_v) for _v in _vers]

s=''

for v in vers:
    s+="[{}]({}) ".format(v, template.replace('$ver', v))

print(s)

#!/bin/env python3

template='https://mirrors.hustunique.com/ubuntu-release/$ver/'
_vers=[12.04, '12.04.5', 14.04, '14.04.5', 15.04, 16.04, '16.04.3', 17.04]
vers=[str(_v) for _v in _vers]

s=''

for v in vers:
    s+="[{}]({}) ".format(v, template.replace('$ver', v))

print(s)

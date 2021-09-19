#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    alp = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    swapped = {v: k for k, v in alp.items()}
    print(swapped)
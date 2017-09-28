# -*- coding: utf-8 -*-
# Author: pomelo
# Pw @ 2017-09-28 17:26:27

import bluetooth as bt


nearby_devices = bt.discover_devices(lookup_names=True)
print(nearby_devices)

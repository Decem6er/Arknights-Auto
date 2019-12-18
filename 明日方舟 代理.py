# -*- encoding=utf8 -*-
__author__ = "Xuyy1"

from airtest.core.api import *

auto_setup(__file__)
t=0
while t<5:
    t+=1
    touch(Template(r"tpl1576586836702.png", record_pos=(0.392, 0.227), resolution=(1440, 810)))
    wait(Template(r"tpl1576586904325.png", record_pos=(0.367, 0.105), resolution=(1440, 810)))
    touch(Template(r"tpl1576587041414.png", record_pos=(0.362, 0.11), resolution=(1440, 810)))

    touch(wait(Template(r"tpl1576587665895.png", record_pos=(-0.394, -0.128), resolution=(1440, 810)),timeout=30000,interval=3.0))
    
    touch((890,340))
    
    sleep(3)

    if t==5:
        break

        
    

# -*- encoding=utf8 -*-
__author__ = "Xuyy1"

from airtest.core.api import *

auto_setup(__file__)
wait(Template(r"tpl1578839898437.png", record_pos=(0.419, 0.229), resolution=(1440, 810)))

i=0
while i<5:
    i+=1
    touch(wait(Template(r"tpl1578839898437.png", record_pos=(0.419, 0.229), resolution=(1440, 810))))
    wait(Template(r"tpl1576586904325.png", record_pos=(0.367, 0.105), resolution=(1440, 810)))
    touch(Template(r"tpl1576587041414.png", record_pos=(0.362, 0.11), resolution=(1440, 810)))

#仅剿灭作战
    touch(wait(Template(r"tpl1576587665895.png", record_pos=(-0.394, -0.128), resolution=(1440, 810)),timeout=30000,interval=3.0))

    wait(Template(r"tpl1578841429494.png", record_pos=(-0.328, 0.208), resolution=(1440, 810)),timeout=30000,interval=3.0)
    sleep(5.0)
    touch(Template(r"tpl1578841429494.png", record_pos=(-0.328, 0.208), resolution=(1440, 810)))
    touch((666,289))
    sleep(5.0)
    if i==8:
        break
    

        
    

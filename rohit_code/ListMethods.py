l1 = ["gabba","goi","gap"]
l1.insert(1,"famn") # will insert at 1st position
print(l1)
l1.append("lulll")  # will append at end of the list
print(l1)
l2 = ["sas","sata","scsi"]
l1.extend(l2) # it will add the items of l2 in l1 at end of list
print(l1)
t1 = ("vswitch","uplink","nic")
l2.extend(t1) # you can also add tuple to the lists
print(l2)
l1.remove("gabba") # removes the first string
l1.pop(3) # remove the third index
print(l1)
l3 = [1,6,5,6,8,6,5,49,2]
l3.sort()
print(l3)
l3.reverse()
print(l3)

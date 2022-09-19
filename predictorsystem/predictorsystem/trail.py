def ca_marks(os,cc,dip,oos,st,spm):
    marks=0
    marks=os+cc+dip+oos+st+spm
    return marks
def mid_marks(os_mid,cc_mid,dip_mid,oos_mid,st_mid,spm_mid):
    marks=0
    marks=os_mid+cc_mid+dip_mid+oos_mid+st_mid+spm_mid
    return marks

    
def marks(os_ca,os_mid,cc_ca,cc_mid,dip_ca,dip_mid,oos_ca,oos_mid,st_ca,st_mid,spm_ca,spm_mid):
    total_result=0
    ca_result=ca_marks(os_ca//2,cc_ca//2,dip_ca//2,oos_ca//2,st_ca//2,spm_ca//2)
    mid_result=mid_marks(os_mid,cc_mid,dip_mid,oos_mid,st_mid,spm_mid)
    total_result=(ca_result+mid_result)/180*100
    return total_result
os_ca=int(input("os ca"))
os_mid=int(input("os_mid"))
cc_ca=int(input("cc_ca"))
cc_mid=int(input("cc_mid"))
dip_ca=int(input("dip_ca"))
dip_mid=int(input("dip_mid"))
oos_ca=int(input("oos_ca"))
oos_mid=int(input("oos_mid"))
st_ca=int(input("st_ca"))
st_mid=int(input("st_mid"))
spm_ca=int(input("spm_ca"))
spm_mid=int(input("spm_mid"))
result=marks(os_ca,os_mid,cc_ca,cc_mid,dip_ca,dip_mid,oos_ca,oos_mid,st_ca,st_mid,spm_ca,spm_mid)
print(result)


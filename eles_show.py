import numpy as np
import plot_device
eles=np.load('eles.npy')
ele=eles[2942]
fin_t=ele[1]
fin_l2=ele[4]
fin_l1=ele[3]
n=int(round(ele[5]))

n_up = int(0.02 / 2 / (fin_l2 + fin_t))
plot_device.plot_type2(0.02,0.01,fin_l1,fin_l2,fin_t,n,n_up)
print(ele)
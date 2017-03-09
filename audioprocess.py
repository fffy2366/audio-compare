# coding:utf-8

import numpy
import pylab as pl
import wave

###open wave file (from zhenzhen)
#f = wave.open("d:\\audioprocess\\wave\\P11-9T.wav","rb")
f = wave.open(".\\P11-9T.wav","rb")



###返回wav的格式信息
###一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采  
###样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息 
### params 共有6个参数 
params = f.getparams()

nchannels,sampwidth,framerate,nframes = params[:4]


###读取波形数据  
###读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）  
str_data = f.readframes(nframes)
f.close()


###将波形数据转换成数组  
###需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组  
wave_data = numpy.fromstring(str_data,dtype = numpy.short)
wave_data.shape = -1,2
wave_data = wave_data.T
time = numpy.arange(0,nframes)*(1.0/framerate)
###len_time = len(time)/2
###time = time[0:len_time]

wave_data_avg = (wave_data[0]+wave_data[1])/2
####左右声道合一后的绝对值，用于计算平均音高#####
wave_data_avg_abs = map(abs,wave_data_avg)
wave_data_avg_max = numpy.amax(wave_data_avg_abs)
#total_avg

#print "new wave avg",wave_data_avg
# print "wave 0",wave_data[0]
# print "wave 1",wave_data[1]
# print "avgavg",sum(wave_data_avg_abs)/len(wave_data_avg_abs)


####寻找音频开始点和结束点##############
###寻找音频文件的极值
# wave_data_abs = map(abs,wave_data)

# wave_data_max = numpy.amax(wave_data_abs)

# print "max data = ",wave_data_max

###设定开始点为最大值的10%
e = 0.1
start_value = wave_data_avg_max * e

print start_value

#new_wave_data = wave_data - start_value

print "time length = ",len(time)
print "wave_data[0] length = ",len(wave_data[0])

###绘制波形

# pl.subplot(211)
# pl.plot(time,wave_data[0])
# pl.plot(time,wave_data[1],c="r")
# pl.xlabel("time")
# pl.show()
#pl.subplot(212)

###播放音频


####---2017-02-24---更新--#####
####有效音频部分处理#####
####寻找有效部分起止点####
####只对【0】通道进行处理#####

#i = 0
for i in range(0,len(wave_data_avg),1):
	if wave_data_avg[i]>=start_value:
		print "i=",i
		break
#	else:
#		i+=1

#j = len(wave_data[0])-1
for j in range(len(wave_data_avg)-1,0,-1):
	if wave_data_avg[j]>=start_value:
		print "j=",j
		break
#	else:
#		j-=1



#####绘图部分问题已经解决#########
arr = wave_data_avg[i:j+1]
time2 = numpy.arange(0,(j+1-i))*1.0/framerate
print j-i+1
step =(j+1-i)//1000
idx_range = range(i,j-1,step)
arrnew = wave_data_avg[idx_range]
arr_std = arrnew[0:1000]
print len(arr_std)


######计算平均音高，处理学员音频时会用到######
arr_std2 = map(abs,arr_std)
avg_std = sum(arr_std2)/len(arr_std2)
print "avg is",avg_std

################说明#######################################
########  time2   和 arr_std  是用来评分用的。#############
######## avg_std  是用来计算进行放大倍数 ##################

# print "time2 length",len(time2)
# print "arr length",len(arr)

# ####画图######
# pl.subplot(211)
# pl.plot(time2,arr)
# pl.xlabel("time2")
# pl.show()

# #####平均取1000个值组成新的数组#####

# step = len(arr)/1000
# print step

# ii = range(0,len(arr)-1,step)
# print "1000point=",len(ii)

# arr1 = arr[ii]
# print arr1
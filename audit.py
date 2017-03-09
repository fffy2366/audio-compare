#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
https://github.com/xdyuchen/AudioScore
https://github.com/fffy2366/audio-compare
[音频相似度对比 Demo](http://blog.csdn.net/xdyuchen/article/details/50014351)
[余弦距离、欧氏距离和杰卡德相似性度量的对比分析](http://www.cnblogs.com/chaosimple/archive/2013/06/28/3160839.html)
'''
import librosa
import librosa.display
from dtw import dtw
from numpy.linalg import norm
from scipy import spatial
import numpy as np
import matplotlib.pyplot as plt

def my_custom_norm(x, y):
    return spatial.distance.cosine(x, y)

def get_distance():
    y1, sr1 = librosa.load('./P11-9T.wav')
    librosa.display.waveplot(y1, sr=sr1, alpha=0.25)
    plt.show()  #To display the plots graphically
    # y2, sr2 = librosa.load('./P11-9T.wav')
    # mfcc1 = librosa.feature.mfcc(y1, sr1)
    # mfcc2 = librosa.feature.mfcc(y2, sr2)
    print mfcc2
    # dist, cost, accumulated_cost, path = dtw(mfcc1.T, mfcc2.T, dist=my_custom_norm)
    # print '%.4f' %dist
    # print cost
if __name__ == '__main__':
    get_distance()
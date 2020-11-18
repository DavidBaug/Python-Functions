# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:23:58 2020

@author: baugd
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

a = 1
if a == 0:
    k = cv2.imread("kohler.png", 1)
    g = cv2.imread("gopro.png", 1)
    
    
    kr = k[:,:,0]
    kg = k[:,:,1]
    kb = k[:,:,2]
    
    gr = g[:,:,0]
    gg = g[:,:,1]
    gb = g[:,:,2]
    
    
    cv2.imwrite("kr.png", kr)
    cv2.imwrite("kg.png", kg)
    cv2.imwrite("kb.png", kb)
    
    cv2.imwrite("gr.png", gr)
    cv2.imwrite("gg.png", gg)
    cv2.imwrite("gb.png", gb)
    
else:
    kr = cv2.imread("red/0.png", 0)
    kg = cv2.imread("red/1.png", 0)
    kb = cv2.imread("red/2.png", 0)
    
    gr = cv2.imread("red/3.png", 0)
    gg = cv2.imread("red/4.png", 0)
    gb = cv2.imread("red/5.png", 0)
    
    k = np.ndarray((800,800,3))
    g = np.ndarray((720, 1280, 3))
    
    k[:,:,0] = kr
    k[:,:,1] = kg
    k[:,:,2] = kb

    g[:,:,0] = gr
    g[:,:,1] = gg
    g[:,:,2] = gb
    
    cv2.imwrite("kohler_dublid.png", k)
    cv2.imwrite("gopro_dublid.png", g)
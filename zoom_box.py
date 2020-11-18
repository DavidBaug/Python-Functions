# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:27:33 2020

@author: baugd
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

levin1 = (20,145)

def add_zoom_box(src, crop):

    img = cv2.imread(src)



    # Check if is a color image    
    if len(img.shape) > 2:
        
        # Zoom box with 10% size source image        
        zoom = img[crop[0]:crop[0]+np.int(img.shape[0]*0.1), crop[1]:crop[1]+np.int(img.shape[0]*0.1),:]
        
        zoom = cv2.resize(zoom, (np.int(img.shape[0]*0.3), np.int(img.shape[0]*0.3)))
        
        if np.int(img.shape[0]*0.005) > 2:
            aux = np.int(img.shape[0]*0.005)
        else:
            aux = 2
        
        zoom[0:aux,:] = (0,255,0)
        zoom[-aux:-1,:] = (0,255,0)
        zoom[:,0:aux] = (0,255,0)
        zoom[:,-aux:-1] = (0,255,0)
        
        new_img = img.copy()
        new_img[-np.int(img.shape[0]*0.3):, -np.int(img.shape[0]*0.3):, :] = zoom.copy()
        
    else:
        zoom = img[crop[0]:crop[0]+np.int(img.shape[0]*0.1), crop[1]:crop[1]+np.int(img.shape[0]*0.1)]
        
        zoom = cv2.resize(zoom, (np.int(img.shape[0]*0.3), np.int(img.shape[0]*0.3)))
        new_img = img.copy()
        new_img[-np.int(img.shape[0]*0.3):, -np.int(img.shape[0]*0.3):] = zoom.copy()



    return new_img


def add_kernel_box(src, kernel):

    img = cv2.imread(src)    
    k = cv2.imread(kernel)

    k = cv2.resize(k, (np.int(img.shape[0]*0.3), np.int(img.shape[0]*0.3)))

    if np.int(img.shape[0]*0.005) > 2:
        aux = np.int(img.shape[0]*0.005)
    else:
        aux = 2

    k[0:aux,:] = (0,255,0)
    k[-aux:-1,:] = (0,255,0)
    k[:,0:aux] = (0,255,0)
    k[:,-aux:-1] = (0,255,0)

    new_img = img.copy()
    new_img[0:np.int(img.shape[0]*0.3), 0:np.int(img.shape[0]*0.3), :] = k.copy()
    
    return new_img

def add_kernel_zoom_box(src, kernel, crop):

    img = add_zoom_box(src, crop)

    k = cv2.imread(kernel)

    k = cv2.resize(k, (np.int(img.shape[0]*0.3), np.int(img.shape[0]*0.3)))

    if np.int(img.shape[0]*0.005) > 2:
        aux = np.int(img.shape[0]*0.005)
    else:
        aux = 2

    k[0:aux,:] = (0,255,0)
    k[-aux:-1,:] = (0,255,0)
    k[:,0:aux] = (0,255,0)
    k[:,-aux:-1] = (0,255,0)

    new_img = img.copy()
    new_img[0:np.int(img.shape[0]*0.3), 0:np.int(img.shape[0]*0.3), :] = k.copy()
    
    return new_img



# cap 3

imgs = ["li_li.png", "li_fort.png", "li_zhou.png", "zhou_zhou.png", "zhou_li.png","zhou_fort.png", "deblur.png", "dmphn.png", "srn.png", "dublid.png", "original.png"]
datasets = ["sun", "kohler", "gopro", "levin"]
crops = [(150,420),(350,290), (160,180), (20,145)]
path = "D:/Descargas/PRUEBA/RESULTADOS/OVERLEAF_IMAGES"
cap = "cap3"

'''
imgs = ["li_li.png", "li_fort.png", "zhou_zhou.png", "zhou_fort.png", "original.png", "RBNet.png"]
path = "D:/Descargas/PRUEBA/result/imgs"
datasets = ["sun", "kohler"]
crops = [(425,610),(390,270)]
cap = "cap5"
'''


for d in datasets:
    for i in imgs:
    
        src = "{}/{}/{}".format(path,d, i)

        aux = i.split('_')
        
        if aux[0] == "li":
            ker = "{}/{}/li_kernel.png".format(path,d)
            a = add_kernel_zoom_box(src, ker, crops[datasets.index(d)])
        elif aux[0] == "zhou":
            ker = "{}/{}/zhou_kernel.png".format(path,d)
            a = add_kernel_zoom_box(src, ker, crops[datasets.index(d)])
        elif i == "RBNet.png":
            ker = "{}/{}/zhou_kernel.png".format(path,d)
            a = add_kernel_zoom_box(src, ker, crops[datasets.index(d)])
        elif i == "dublid.png":
            ker = "{}/{}/dublid_kernel.png".format(path,d)
            a = add_kernel_zoom_box(src, ker, crops[datasets.index(d)])
        elif i == "original.png" and (d == "levin" or d == "sun"):
            ker = "{}/{}/original_kernel.png".format(path,d)
            a = add_kernel_zoom_box(src, ker, crops[datasets.index(d)])
        else:
            a = add_zoom_box(src, crops[datasets.index(d)])
        
        
        cv2.imwrite("D:/Descargas/PRUEBA/IMAGENES LATEX/{}/{}_{}".format(cap,d,i), a)
        

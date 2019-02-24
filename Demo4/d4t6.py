# -*- coding: utf-8 -*-
# Ohjelma vertaa kahta kuvaa ORB-menetelmällä ja näyttää kuvien välitä
# löytyneet yhtäläisyydet

import matplotlib.pyplot as plt
import numpy as np
import cv2

kuva1 = cv2.imread('d4t6_kuva1.png',0)
kuva2 = cv2.imread('d4t6_kuva2.png',0)

# ORB detectorin alustus
orb = cv2.ORB_create()

# Etsitään kuvista keypointit ja descriptionit
kp1, des1 = orb.detectAndCompute(kuva1,None)
kp2, des2 = orb.detectAndCompute(kuva1,None)

# tekee BFMatcherin
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Vertailee descriptioneita
matches = bf.match(des1,des2)

# Järjestää vertailun osumat etäisyyden mukaan
matches = sorted(matches, key = lambda x:x.distance)
# Piirtää 20 matchia
vertailu = cv2.drawMatches(kuva1,kp1,kuva2,kp2,matches[:20],None, flags=2)
plt.imshow(vertailu),plt.show()
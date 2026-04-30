# Task_3
open cv
```python
import cv2 as cv
# استدعاء مكتبة OpenCV لمعالجة الصور والرؤية الحاسوبية

import numpy as np
# استدعاء مكتبة NumPy للتعامل مع المصفوفات والقيم الرقمية

import matplotlib.pyplot as plt
# استدعاء مكتبة Matplotlib لعرض الصور والرسومات

img = cv.imread(r'E:\PHOTOS\R1.jpeg')
# قراءة الصورة من المسار وتحويلها لمصفوفة Pixels

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# تحويل الصورة من نظام ألوان BGR إلى RGB لأن Matplotlib يعرض RGB

cv.cvtColor()
# تحويل الصورة من Color Space إلى Color Space آخر

cv.COLOR_BGR2RGB
# تحويل من BGR إلى RGB

cv.COLOR_BGR2GRAY
# تحويل الصورة إلى تدرج رمادي Grayscale

cv.COLOR_BGR2HSV
# تحويل الصورة إلى نظام HSV

cv.COLOR_BGR2LAB
# تحويل الصورة إلى نظام LAB

cv.COLOR_BGR2YCrCb
# تحويل الصورة إلى نظام YCrCb

plt.figure(figsize=(15,4))
# إنشاء نافذة رسم وتحديد حجمها

plt.subplot(1,5,1)
# تقسيم نافذة العرض إلى صف و5 أعمدة واختيار مكان الصورة

plt.imshow()
# عرض الصورة

plt.title()
# وضع عنوان للصورة

plt.axis('off')
# إخفاء المحاور والأرقام حول الصورة

plt.savefig("partA.png")
# حفظ الشكل كصورة

plt.show()
# إظهار جميع الصور المعروضة

img.shape
# إرجاع أبعاد الصورة (الارتفاع والعرض وعدد القنوات)

img.shape[:2]
# إرجاع الارتفاع والعرض فقط بدون القنوات

print()
# طباعة البيانات على الشاشة

np.array()
# إنشاء Array باستخدام NumPy

cv.inRange(hsv_img, lower, upper)
# إنشاء Mask لتحديد Pixels ضمن Range لوني معين

cv.bitwise_and(img_rgb, img_rgb, mask=mask)
# استخراج الجزء المحدد بالـ Mask فقط من الصورة

mask1 + mask2
# دمج Maskين معًا للحصول على نطاقين لونيين

h//2 , w//2
# إيجاد مركز الصورة باستخدام القسمة الصحيحة Integer Division

gray[center]
# قراءة قيمة Pixel من الصورة الرمادية عند المركز

hsv[center]
# قراءة قيمة Pixel من صورة HSV عند المركز

lab[center]
# قراءة قيمة Pixel من صورة LAB عند المركز

ycrcb[center]
# قراءة قيمة Pixel من صورة YCrCb عند المركز
```

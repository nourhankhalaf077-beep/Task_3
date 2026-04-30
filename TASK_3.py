import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread(r'E:\PHOTOS\R1.jpeg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# -------------------------------
# Part A: تحويل الصورة لكل Color Spaces
# -------------------------------
# BGR (الأصل)=img
bgr=img
# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# YCrCb
ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
# -------------------------------
# عرض الصور الخمسة جنب بعض
# -------------------------------
plt.figure(figsize=(15,4))

plt.subplot(1,5,1)
plt.imshow(img_rgb)
plt.title("BGR (as RGB)")
plt.axis('off')

plt.subplot(1,5,2)
plt.imshow(gray, cmap='gray')  # مهم: gray
plt.title("Grayscale")
plt.axis('off')

plt.subplot(1,5,3)
plt.imshow(hsv)
plt.title("HSV")
plt.axis('off')

plt.subplot(1,5,4)
plt.imshow(lab)
plt.title("LAB")
plt.axis('off')

plt.subplot(1,5,5)
plt.imshow(ycrcb)
plt.title("YCrCb")
plt.axis('off')

plt.savefig("partA.png")  # حفظ الشكل
plt.show()

# -------------------------------
# طباعة قيمة البكسل في المنتصف
# -------------------------------
h, w = img.shape[:2]
center = (h//2, w//2)

print("Center Pixel Values:")
print("BGR:", bgr[center])
print("HSV:", hsv[center])
print("LAB:", lab[center])
print("YCrCb:", ycrcb[center])
print("Gray:", gray[center])

# -------------------------------
# Part B: HSV Isolation (مثلاً لون أحمر)
# ------------------------------

# تحويل لـ HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# تحديد اللون (مثال: الأحمر)
# الأحمر ليه نطاقين
lower1 = np.array([0, 120, 70])  # 0:10 range color red , 120:255 power color ,70:255 deg light (for mask1)
upper1 = np.array([10, 255, 255])

lower2 = np.array([170, 120, 70]) # 170:180 range color red , 120:255 power color ,70:255 deg light (for mask2)
upper2 = np.array([180, 255, 255])

# عمل mask
mask1 = cv.inRange(hsv_img, lower1, upper1)
mask2 = cv.inRange(hsv_img, lower2, upper2)
mask = mask1 + mask2

# استخراج الجزء الملون فقط
result = cv.bitwise_and(img_rgb, img_rgb, mask=mask)

# -------------------------------
# عرض النتائج
# -------------------------------
plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(mask, cmap='gray')
plt.title("Mask")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(result)
plt.title("Segmented")
plt.axis('off')

plt.savefig("partB.png")
plt.show()


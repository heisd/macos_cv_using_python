import cv2
# 这个代码是opencv的基础部分
# 下面这段代码标识修改一个范围的像素点
ImagePath="opencv/image/image.png"
Image=cv2.imread(ImagePath)
# 检查图片是否正确加载
if Image is None:
    print(f"错误：无法加载图片，请检查路径是否正确: {ImagePath}")
    exit()
# copy 一份方便对比
ImageCopy=Image.copy()
# 获取图像的要修改的范围
ROI=ImageCopy[50:150, 50:150]
# 范围修改成为绿色
ROI[:]=[0,255,0]
cv2.imshow("Image",Image)
cv2.imshow("ModImage",ImageCopy)
key=cv2.waitKey(0)
if key ==ord('s'):
    print("保存图像")
    SaveImage=cv2.imwrite("opencv/output/image/RIOImage.png",ImageCopy)
if key ==ord('q'):
    print("成功退出")








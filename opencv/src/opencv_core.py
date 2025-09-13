import cv2
# 这个代码是opencv的基础部分
# 下面的代码展示了修改图片上的某一个像素点
ImagePath='opencv/image/image.png'
Image=cv2.imread(ImagePath)
# 检查图片是否正确加载
if Image is None:
    print(f"错误：无法加载图片，请检查路径是否正确: {ImagePath}")
    exit()
# 获取像素值
PixelImage=Image[100,100]
# 修改像素值->将100,100修改成白色
Image[100,100]=[255,255,255]
cv2.imshow("DisplayImage",Image)
key=cv2.waitKey(0)
if key ==ord('s'):
    print("保存图像")
    SaveImage=cv2.imwrite('opencv/output/image/PixelImage.png',Image)
if key ==ord('q'):
    print("成功退出")








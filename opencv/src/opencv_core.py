import cv2
# 这个代码是opencv的基础部分
# 下面的代码是图像的缩放
ImagePath='opencv/image/image.png'
Image=cv2.imread(ImagePath)
# 检查图片是否正确加载
if Image is None:
    print(f"错误：无法加载图片，请检查路径是否正确: {ImagePath}")
    exit()
ImageSize=Image.size
print(ImageSize)
print("***********************")
# 将图像缩放为100*100
# size=height*width*PipeNum
ResizeImage=cv2.resize(Image,(100,100))
ResizeImageSize=ResizeImage.size
print(ResizeImageSize)
cv2.imshow("DisplayImage",ResizeImage)
key=cv2.waitKey(0)
if key ==ord('s'):
    print("保存图像")
    SaveImage=cv2.imwrite('opencv/output/image/ReszieImage.png',Image)
if key ==ord('q'):
    print("成功退出")








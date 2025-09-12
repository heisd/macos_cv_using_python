import cv2
# 选取图片路径
image_path='opencv/image/image.png'
# 使用cv2读取图像
image=cv2.imread(image_path)
if image is None:
    print("图像打开错误")
    exit(1)
# 创建窗口打开opencv文件
cv2.imshow("DisplayImage",image)
# 等待按键按下
# 参数 0 表示无限等待，直到用户按下任意键
key = cv2.waitKey(0)
if key == ord('s'):  
    output_path='opencv/output/image/saved_image.png'
    cv2.imwrite(output_path, image)  
    print('save')
elif key == ord('q'):  
    print('quit')
    print('no save')
cv2.destroyAllWindows()







   
    




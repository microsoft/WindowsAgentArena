# Microsoft Paint 测试用例总结

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 15f8de6e-3d39-40e4-af17-bdbb2393c0d9-WOS | 绘制红色圆圈 | 1. 等待2秒钟<br>2. 在Paint中进行绘制操作 | 1. 激活"Untitled - Paint"窗口<br>2. 休眠1秒<br>3. 使用Python脚本截图并保存到`C:\Users\Docker\Downloads\Screenshot.png`<br>4. 关闭Paint<br>5. 使用`is_red_circle_present_on_canvas`函数检查截图中是否存在红色圆圈 | Microsoft Corporation |
| 44dbac63-32bf-4cd2-81b4-ad6803ec812d-WOS | 修改画布尺寸为800x600像素 | 1. 打开Paint应用程序<br>2. 等待1秒<br>3. 修改画布尺寸 | 1. 激活Paint窗口<br>2. 使用Python脚本保存图片到`C:\Users\Docker\Downloads\CanvasSize.png`<br>3. 关闭Paint<br>4. 使用`image_dimension_matches_input`函数验证图片尺寸是否为800x600 | Microsoft Corporation |
| 3544ac9a-6aee-4a0b-a203-bc7b59b272b6-WOS | 将Paint图片保存为circle.png | 1. 打开Paint应用程序<br>2. 等待1秒<br>3. 执行保存操作 | 使用`vm_file_exists_in_vm_folder`函数检查`C:\Users\Docker\Downloads`目录下是否存在`circle.png`文件 | Microsoft Corporation |

注意事项：
1. 所有测试用例都在Windows操作系统环境下运行
2. 测试过程中使用了Python脚本进行自动化操作和验证
3. 测试结果的评估都采用了`exact_match`函数进行精确匹配
4. 测试过程中包含了适当的延时以确保操作的稳定性 
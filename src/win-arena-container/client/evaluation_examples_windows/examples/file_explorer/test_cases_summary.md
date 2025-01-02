| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 0c9dda13-428c | 创建Archive文件夹并移动.docx文件 | 1. 下载两个.docx文件到Documents目录<br>2. 启动文件浏览器打开Documents目录 | 检查是否所有.docx文件都在Archive文件夹中 | Microsoft Corporation |
| 2b0c0844 | 打开文件浏览器并导航到Documents文件夹 | 直接启动文件浏览器 | 验证活动窗口标题是否为"Documents" | null |
| 2d292a2d | 检查Downloads文件夹大小并生成大文件报告 | 1. 下载示例文件到Downloads目录<br>2. 创建15MB的测试文件 | 检查Desktop上的report.txt是否包含testing.bin | Microsoft Corporation |
| 3bad5766 | 创建Arena库并添加相关文件夹 | 1. 创建多个Arena相关文件夹<br>2. 下载示例文件到各个文件夹 | 验证Arena库是否包含指定的三个Arena相关文件夹 | null |
| 7AB09EF1 | 为Projects文件夹创建桌面快捷方式 | 1. 在Documents中创建Projects文件夹<br>2. 创建快捷方式 | 检查Desktop上是否存在"Projects - Shortcut.lnk" | null |
| 7c70e16b | 按修改日期排序Documents中的文件 | 1. 下载三个示例文件<br>2. 设置不同的修改时间 | 验证文件是否按修改时间排序 | null |
| 016c9a9d | 搜索并列出Pictures中的PNG文件 | 1. 下载三个PNG文件到Pictures目录<br>2. 创建文件列表 | 检查png_files.txt是否包含所有PNG文件名 | Microsoft Corporation |
| 22e529ff | 为照片添加自定义标签 | 1. 创建Summer Trip文件夹<br>2. 下载测试图片<br>3. 添加标签 | 验证所有图片是否都添加了"2023Vacation"标签 | null |
| 34a4fee9 | 将文件浏览器视图更改为"详细信息"视图 | 启动文件浏览器并更改视图设置 | 检查Documents文件夹是否使用详细信息视图 | Microsoft Corporation |
| 1876fe7f | 移动文件夹从Desktop到Documents | 1. 在Desktop创建MyFolder<br>2. 移动文件夹 | 检查MyFolder是否存在于Documents中 | null |
| 5316686e | 显示隐藏文件和系统文件 | 修改注册表设置以显示隐藏文件 | 检查注册表值是否为0x1 | Microsoft Corporation |
| 5548314e | 创建Downloads文件夹的压缩包 | 1. 下载示例文件到Downloads<br>2. 创建zip文件 | 比较生成的zip文件与标准zip文件 | https://www.elevenforum.com/t/zip-compress-files-and-folders-in-windows-11.8235/ |
| ac46b5cb | 移动Downloads内容到OldDownloads | 1. 创建目标文件夹<br>2. 移动所有内容 | 验证文件是否正确移动并保持结构 | Microsoft Corporation |
| b0c9dac6 | 创建加密的7z压缩包 | 1. 创建测试文件夹和文件<br>2. 使用7-zip创建加密压缩包 | 检查是否创建了密码保护的压缩文件 | Microsoft Corporation |
| b12b2d3a | 删除Downloads中的空文件夹 | 1. 创建测试文件夹结构<br>2. 删除空文件夹 | 验证空文件夹是否被删除 | Microsoft Corporation |
| b12921b2 | 设置文件夹共享权限 | 1. 创建测试文件夹<br>2. 添加测试用户<br>3. 设置权限 | 检查指定用户是否具有只读权限 | null |
| b8ab0ae1 | 复制并重命名文件 | 1. 下载示例文件到Desktop<br>2. 复制到Documents并重命名 | 比较源文件和目标文件内容 | null |
| e27984c7 | 设置文件为隐藏属性 | 1. 下载测试文件<br>2. 设置隐藏属性 | 检查文件是否设置为隐藏 | https://www.xda-developers.com/how-hide-files-windows-11/#:~:text=Click%20Properties%2C%20or%20use%20the,sub%2Dfolders%2C%20and%20files. |
| f934d80d | 从回收站还原文件 | 1. 创建测试文件<br>2. 删除文件到回收站<br>3. 还原文件 | 检查文件是否还原到原始位置 | Microsoft Corporation | 
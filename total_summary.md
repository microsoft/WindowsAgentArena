# Windows 应用程序测试用例总结

目录
- [Windows 应用程序测试用例总结](#windows-应用程序测试用例总结)
  - [Chrome 浏览器测试用例](#chrome-浏览器测试用例)
  - [Windows 时钟应用测试用例](#windows-时钟应用测试用例)
  - [LibreOffice Calc 测试用例](#libreoffice-calc-测试用例)
  - [LibreOffice Writer 测试用例](#libreoffice-writer-测试用例)
  - [文件资源管理器测试用例](#文件资源管理器测试用例)
  - [Windows Paint 测试用例](#windows-paint-测试用例)
  - [Edge浏览器测试用例](#edge浏览器测试用例)
  - [Notepad 测试用例](#notepad-测试用例)
  - [Windows 设置测试用例](#windows-设置测试用例)
  - [VLC 播放器测试用例](#vlc-播放器测试用例)
    - [不可执行的测试用例](#不可执行的测试用例)
  - [VS Code 测试用例](#vs-code-测试用例)
    - [以下是被标记为不可行(Infeasible)的测试用例：](#以下是被标记为不可行infeasible的测试用例)
  - [Windows 计算器测试用例](#windows-计算器测试用例)
  - [注意事项](#注意事项)


## Chrome 浏览器测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 2ae9ba84-3a0d-4d4c-8338-3a1478dc5fe3 | 修改Chrome配置文件用户名 | 1. 启动Chrome并开启远程调试端口<br>2. 使用socat转发端口<br>3. 修改用户名为"Thomas" | 检查profile_name是否为"Thomas" | https://superuser.com/questions/1393683/how-to-change-the-username-in-google-chrome-profiles?rq=1 |
| 06fe7178-4491-4589-810f-2e2bc9502122 | 恢复最近关闭的标签页 | 1. 启动Chrome<br>2. 打开3个指定网页<br>3. 关闭tripadvisor页面<br>4. 恢复关闭的标签页 | 检查打开的标签页是否包含所有指定URL | https://www.wikihow.com/Switch-Tabs-in-Chrome |
| 7a5a7856-f1b6-42a4-ade9-1ca81ca0f263 | 将当前页面添加到书签栏 | 1. 启动Chrome<br>2. 打开两个指定页面<br>3. 将当前页面添加到书签栏 | 检查书签栏是否包含指定URL | https://www.youtube.com/watch?v=ZaZ8GcTxjXA |
| 7b6c7e24-c58a-49fc-a5bb-d57b80e5b4c3 | 删除Amazon网站的Cookie | 1. 启动Chrome<br>2. 访问Amazon相关页面<br>3. 删除指定域名的Cookie | 检查.amazon.com域名的Cookie是否被删除 | https://support.google.com/chrome/answer/95647?hl=en&ref_topic=7438325&sjid=16867045591165135686-AP |
| 030eeff7-b492-4218-b312-701ec99ee0cc | 启用"请勿跟踪"功能 | 1. 启动Chrome<br>2. 开启"Do Not Track"设置 | 检查"Do Not Track"设置是否为true | https://support.google.com/chrome/answer/2790761?hl=en&co=GENIE.Platform%3DDesktop |
| 44ee5668-ecd5-4366-a6ce-c1c9b8d4e938 | 清除YouTube浏览记录 | 1. 启动Chrome<br>2. 预设大量浏览历史<br>3. 清除YouTube相关记录 | 检查历史记录中是否还存在YouTube相关记录 | https://superuser.com/questions/1787991/clear-browsing-history-from-specific-site-on-chrome |
| 82bc8d6a-36eb-4d2d-8801-ef714fb1e55a | 搜索特定航班 | 1. 启动Chrome<br>2. 访问航空公司网站<br>3. 搜索孟买到斯德哥尔摩的航班 | 检查URL中是否包含正确的出发地(BOM)和目的地(STO)参数 | test_task_1 |
| 121ba48f-9e17-48ce-9bc6-a4fb17a7ebba | 将Dota 2原声带加入Steam购物车 | 1. 启动Chrome<br>2. 打开Dota 2和Steam商店页面<br>3. 添加原声带到购物车 | 检查购物车中是否包含"The Dota 2 Official Soundtrack" | Mind2Web |
| 480bcfea-d68f-4aaa-a0a9-2589ef319381 | 启用性能指标HUD显示 | 1. 启动Chrome<br>2. 启用性能指标HUD标志 | 检查是否启用了show-performance-metrics-hud实验 | https://beebom.com/enable-chromes-benchmark-hud-track-performance-metrics/ |
| 99146c54-4f37-4ab8-9327-5f3291665e1e | 设置自动删除站点数据 | 1. 启动Chrome<br>2. 配置关闭浏览器时自动删除站点数据 | 检查自动删除数据设置是否为true | https://www.youtube.com/watch?v=v0kxqB7Xa6I |
| a96b564e-dbe9-42c3-9ccf-b4498073438a | 查找并打开特定论坛帖子 | 1. 启动Chrome<br>2. 访问FlightAware网站<br>3. 导航到指定讨论帖 | 检查当前URL是否为目标帖子URL | test_task_0 |
| af630914-714e-4a24-a7bb-f9af687d3b91 | 调整默认字体大小 | 1. 启动Chrome<br>2. 设置最大默认字体大小 | 检查字体大小是否大于等于16 | https://www.howtogeek.com/680260/how-to-change-chromes-default-text-size/ |
| b070486d-e161-459b-aa2b-ef442d973b92 | 查找Tamiflu药物副作用 | 1. 启动Chrome<br>2. 访问drugs.com<br>3. 搜索Tamiflu副作用 | 检查URL是否包含tamiflu和side-effects关键词 | online_tasks |
| bb5e4c0d-f964-439c-97b6-bdb9747de3f4 | 将Bing设为默认搜索引擎 | 1. 启动Chrome<br>2. 修改默认搜索引擎设置 | 检查默认搜索引擎是否为"Bing" | https://support.google.com/chrome/answer/95426?sjid=16867045591165135686-AP |
| e1e75309-3ddb-4d09-92ec-de869c928143 | 将网页保存为PDF | 1. 启动Chrome<br>2. 打开指定页面<br>3. 将页面另存为PDF到桌面 | 比较生成的PDF与预期PDF是否一致 | https://in5stepstutorials.com/google-chrome/save-web-page-as-pdf-in-chrome.php | 

## Windows 时钟应用测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 02F10F89-7171-4D37-8550-A00BA8930CDF-WOS | 设置3小时定时器 | 1. 使用`ms-clock://Timers`协议启动时钟应用的定时器页面<br>2. 等待1秒让应用加载<br>3. 激活"Clock"窗口<br>4. 等待0.5秒进行检查 | 使用`check_if_timer_started`函数检查定时器是否设置为3小时(hours=3, minutes=0, seconds=0) | None |
| 02F10F89-7171-4D37-8550-A00BA8930CDF-2-WOS | 设置30分钟定时器 | 1. 使用`ms-clock://Timers`协议启动时钟应用的定时器页面<br>2. 等待1秒让应用加载<br>3. 激活"Clock"窗口<br>4. 等待0.5秒进行检查 | 使用`check_if_timer_started`函数检查定时器是否设置为30分钟(hours=0, minutes=30, seconds=0) | None |
| 91A30BE9-0E11-4374-8D43-41D4D097080A-WOS | 添加慕尼黑世界时钟 | 1. 使用`ms-clock://`协议启动时钟应用<br>2. 等待1秒让应用加载<br>3. 激活"Clock"窗口<br>4. 等待0.5秒进行检查 | 使用`check_if_world_clock_exists`函数检查是否添加了慕尼黑(Munich, Germany)的世界时钟 | None |
| 91A30BE9-0E11-4374-8D43-41D4D097080A-WOS-2 | 添加京都世界时钟 | 1. 使用`ms-clock://`协议启动时钟应用<br>2. 等待1秒让应用加载<br>3. 激活"Clock"窗口<br>4. 等待0.5秒进行检查 | 使用`check_if_world_clock_exists`函数检查是否添加了京都(Kyoto, Japan)的世界时钟 | None |

## LibreOffice Calc 测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 0a2e43bf | 计算月度总销售额并创建折线图 | 1. 新增"Total"行计算每月总销售额<br>2. 创建折线图，X轴为月份 | 1. 比较表格数据<br>2. 验证图表类型 | SheetCopilot@154 |
| 0acbd372 | 计算净收入并格式化为会计数字类型 | 1. 添加"Net Income"列<br>2. 将所有数据格式化为会计数字类型 | 比较表格数据 | SheetCopilot@121 |
| 0bf05a7d | 将ID号补零至7位数 | 在"New 7 Digit ID"列中填充补零后的ID | 比较表格数据 | https://www.youtube.com/shorts/FPAQaDTS8VY |
| 0cecd4f3 | 重命名和复制工作表 | 1. 将"Sheet1"重命名为"LARS Resources"<br>2. 复制并插入到Sheet2之前<br>3. 添加"(Backup)"后缀<br>4. 为"Sheet2"添加"(Offline)"后缀 | 1. 验证工作表名称<br>2. 比较工作表数据 | https://www.libreofficehelp.com/add-insert-delete-copy-move-rename-a-worksheet-in-libreoffice-calc/ |
| 01b269ae | 用上方单元格的值填充空白单元格 | 将空白单元格填充为其上方单元格的值 | 比较表格数据 | https://www.youtube.com/shorts/VrUzPTIwQ04 |
| 1d17d234 | 创建新工作表并合并单元格 | 1. 创建"Sheet2"<br>2. 合并A1:C1写入标题<br>3. 合并A2:B2和C2:D2写入文本 | 比较工作表数据 | SheetCopilot@73 |
| 1de60575 | 按促销类型汇总收入 | 在新工作表中创建以促销名称为列标题的汇总表 | 比较工作表数据 | SheetCopilot@55 |
| 1e8df695 | 计算每周利润 | 添加"Profit"列，用Sales减去COGS计算利润 | 比较表格数据 | SheetCopilot@203 |
| 4de54231 | 计算加速度并合并数据 | 1. 填充B列和D列的加速度<br>2. 新增列合并A-D列数据，保留2位小数 | 比较表格数据 | SheetCopilot@147 |
| 4e6fcf72 | 根据生日计算年龄 | 使用生日计算员工年龄 | 比较表格数据 | https://www.youtube.com/shorts/0uxJccNCKcE |
| 4f07fbe9 | 在文本中使用带固定小数位的数值 | 在文本公式中使用2位小数的数值 | 比较表格数据 | https://superuser.com/questions/1081048/libreoffice-calc-how-to-pad-number-to-fixed-decimals-when-used-within-formula |
| 5d353deb | 创建指标汇总表和聚类条形图 | 1. 新建工作表汇总2010-2013年各指标总值<br>2. 创建聚类条形图，图例置于底部 | 1. 比较数据透视表<br>2. 验证图表类型和图例位置 | SheetCopilot@32 |
| 5f8601f8 | 汇总支出账户并创建条形图 | 1. 在新工作表中汇总各支出账户的小计<br>2. 创建条形图显示结果 | 1. 比较数据透视表<br>2. 验证图表类型 | SheetCopilot@68 |
| 7a4e4bc8 | 重新排列列顺序 | 按指定顺序重排列："Date", "First Name", "Last Name", "Order ID", "Sales" | 比较表格数据 | https://www.youtube.com/shorts/bvUhr1AHs44 |
| 7e429b8d | 使用查找表填充数据 | 根据分支名称查找并填充相应的主管名称 | 比较表格数据 | https://medium.com/@divyangichaudhari17/how-to-use-vlookup-and-hlookup-in-libre-calc-3370698bb3ff |
| 7efeb4b1 | 填充序列号 | 在"Seq No."列中填充格式为"No. #"的序列号 | 比较表格数据 | https://www.youtube.com/shorts/4jzXfZNhfmk |
| 8b1ce5f2 | 突出显示周末 | 将周六和周日的单元格背景设置为红色(#ff0000) | 1. 比较表格数据<br>2. 验证单元格样式 | https://www.youtube.com/shorts/Hbcwu6IQ1ns |
| 9ed02102 | 计算收入并创建数据透视表和图表 | 1. 计算考虑折扣的收入<br>2. 创建销售网站统计的数据透视表<br>3. 创建无图例的条形图 | 1. 比较表格数据<br>2. 验证数据透视表<br>3. 验证图表属性 | SheetCopilot@0 |
| 21ab7b40 | 计算周期率并突出显示最高值 | 1. 计算周期率并转换为数字类型<br>2. 用绿色(#00ff00)标注最高值 | 1. 比较表格数据<br>2. 验证单元格样式 | SheetCopilot@124 |
| 26a8440e | 创建月度销售总额表 | 在新工作表中创建包含"Month"和"Total"两列的销售总额表 | 比较工作表数据 | SheetCopilot@152 |
| 30e3e107 | 创建人口统计数据透视表 | 1. 创建新工作表并设置标题样式<br>2. 创建性别、婚姻状况和教育程度的百分比数据透视表 | 1. 验证单元格样式<br>2. 比较数据透视表 | SheetCopilot@9 |
| 035f41ba | 计算毛利并组合年份数据 | 1. 填充毛利列<br>2. 在新工作表中创建年份和毛利的组合文本 | 比较工作表数据 | SheetCopilot@92 |
| 39aa4e37 | 重命名工作表 | 将"sheet1"重命名为"LARS_Science_Assessment" | 1. 验证工作表名称<br>2. 比较工作表数据 | https://www.libreofficehelp.com/add-insert-delete-copy-move-rename-a-worksheet-in-libreoffice-calc/ | 

## LibreOffice Writer 测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 0a0faba3-5580-44df-965d-f562a99b291c | 设置段落中前三个词左对齐，其余右对齐 | 1. 下载并打开指定文档<br>2. 使用制表位(tabstops)设置对齐方式 | 使用check_tabstops函数检查制表位设置是否正确，并验证前三个词是否左对齐 | https://stackoverflow.com/questions/64528055/how-to-make-part-of-my-sentence-left-aligned-and-rest-as-right-aligned |
| 0b17a146-2934-46c7-8727-73ff6b6483e8 | 将"H2O"中的"2"设置为下标 | 1. 下载并打开指定文档<br>2. 选择数字"2"<br>3. 设置为下标格式 | 1. compare_docx_files比较文件内容<br>2. compare_subscript_contains检查下标是否正确设置 | https://askubuntu.com/questions/245695/how-do-you-insert-subscripts-and-superscripts-into-ordinary-non-formula-text-i |
| 0e47de2a-32e0-456c-a366-8c607ef7a9d2 | 在每页底部左侧添加页码 | 1. 下载并打开指定文档<br>2. 在页脚中插入页码<br>3. 设置左对齐 | 使用has_page_numbers_in_footers函数检查页脚中是否存在页码 | https://ask.libreoffice.org/t/how-to-start-page-numbering-on-a-certain-page/39931/4 |
| 0e763496-b6bb-4508-a427-fad0b6c3e195 | 将整个文档字体更改为Times New Roman | 1. 下载并打开指定文档<br>2. 全选文本<br>3. 更改字体为Times New Roman | 使用compare_font_names函数检查字体是否为Times New Roman | https://ask.libreoffice.org/t/how-do-i-change-the-font-for-the-whole-document-in-writer/9220 |
| 3ef2b351-8a84-4ff2-8724-d86eae9b842e | 将标题居中对齐 | 1. 下载并打开指定文档<br>2. 选择标题<br>3. 应用居中对齐 | 使用is_first_line_centered函数检查第一行是否居中对齐 | https://askubuntu.com/questions/1066351/how-do-you-center-align-in-libreoffice |
| 41c621f7-3544-49e1-af8d-dafd0f834f75 | 突出显示以"#"开头的注释文本并移除"#"符号 | 1. 下载并打开指定文档<br>2. 查找以"#"开头的文本<br>3. 移除"#"并高亮显示文本 | 使用compare_highlighted_text函数比较高亮文本是否正确 | https://superuser.com/questions/1668018/how-to-auto-format-lines-in-libre-office-writer |
| 4bcb1253-a636-4df4-8cb0-a35c04dfef31 | 将文档导出为PDF格式 | 1. 下载并打开指定文档<br>2. 使用"导出为PDF"功能<br>3. 保持原文件名 | 使用compare_pdfs函数比较生成的PDF与预期结果 | https://www.libreofficehelp.com/save-export-writer-documents-in-pdf-epub-format/ |
| 72b810ef-4156-4d09-8f08-a0cf57e7cefe | 为最后一段添加删除线 | 1. 下载并打开指定文档<br>2. 选择最后一段<br>3. 应用删除线格式 | 使用evaluate_strike_through_last_paragraph函数检查删除线格式 | https://superuser.com/questions/657792/libreoffice-writer-how-to-apply-strikethrough-text-formatting |
| 88fe4b2d-3040-4c70-9a70-546a47764b48 | 在第一段的每个句子之间添加空行 | 1. 下载并打开指定文档<br>2. 在每个句子后添加空行 | 使用compare_docx_files函数比较文档内容 | https://stackoverflow.com/questions/56554555/libreoffice-writer-how-to-create-empty-line-space-after-every-period-in-a-par |
| 936321ce-5236-426a-9a20-e0e3c5dc536f | 将逗号分隔的文本转换为表格 | 1. 下载并打开指定文档<br>2. 选择文本<br>3. 转换为表格，以逗号为分隔符 | 使用compare_docx_tables函数比较表格内容 | https://www.youtube.com/watch?v=l25Evu4ohKg |
| adf5e2c3-64c7-4644-b7b6-d2f0167927e7 | 添加参考文献并在文中添加交叉引用 | 1. 下载并打开指定文档<br>2. 添加参考文献<br>3. 在标记处添加交叉引用 | 使用compare_docx_files函数比较文档内容 | https://seekstar.github.io/2022/04/11/libreoffice%E5%BC%95%E7%94%A8%E6%96%87%E7%8C%AE/ |
| b21acd93-60fd-4127-8a43-2f5178f4a830 | 为不同段落设置不同的行距 | 1. 下载并打开指定文档<br>2. 为引言设置单倍行距<br>3. 为正文设置双倍行距<br>4. 为结论设置1.5倍行距 | 使用compare_line_spacing函数检查行距设置 | https://superuser.com/questions/1097199/how-can-i-double-space-a-document-in-libreoffice |
| d53ff5ee-3b1a-431e-b2be-30ed2673079b | 将所有大写文本转换为小写 | 1. 下载并打开指定文档<br>2. 全选文本<br>3. 转换为小写 | 使用compare_docx_files函数比较文档内容 | https://ask.libreoffice.org/t/how-to-convert-all-uppercase-to-lowercase/53341 |
| e246f6d8-78d7-44ac-b668-fcf47946cb50 | 将斜体文本的字号改为14 | 1. 下载并打开指定文档<br>2. 查找所有斜体文本<br>3. 将字号改为14 | 使用check_italic_font_size_14函数检查斜体文本字号 | https://ask.libreoffice.org/t/how-to-change-text-size-color-of-italic-font/77712 |
| e528b65e-1107-4b8c-8988-490e4fece599 | 将每个单词的首字母改为大写 | 1. 下载并打开指定文档<br>2. 全选文本<br>3. 应用首字母大写格式 | 使用compare_docx_files函数比较文档内容 | https://www.youtube.com/watch?v=l25Evu4ohKg |
| f178a4a9-d090-4b56-bc4c-4b72a61a035d | 将Times New Roman设置为默认字体 | 1. 下载并打开指定文档<br>2. 修改LibreOffice Writer的默认字体设置 | 使用find_default_font函数检查默认字体设置 | https://ask.libreoffice.org/t/how-do-i-make-times-new-roman-the-default-font-in-lo/64604 |
| INF-bb8ccc78-479f-4a2f-a71e-d565e439436b | 实现文档的实时协作编辑 | 不可行 - LibreOffice Writer不支持实时协作编辑功能 | 使用infeasible函数标记该功能不可实现 | https://ask.libreoffice.org/t/can-lo-be-used-for-collaboration-multi-person-real-time-document-editing/9392/6 | 


## 文件资源管理器测试用例

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

## Windows Paint 测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 15f8de6e-3d39-40e4-af17-bdbb2393c0d9-WOS | 绘制红色圆圈 | 1. 等待2秒钟<br>2. 在Paint中进行绘制操作 | 1. 激活"Untitled - Paint"窗口<br>2. 休眠1秒<br>3. 使用Python脚本截图并保存到`C:\Users\Docker\Downloads\Screenshot.png`<br>4. 关闭Paint<br>5. 使用`is_red_circle_present_on_canvas`函数检查截图中是否存在红色圆圈 | Microsoft Corporation |
| 44dbac63-32bf-4cd2-81b4-ad6803ec812d-WOS | 修改画布尺寸为800x600像素 | 1. 打开Paint应用程序<br>2. 等待1秒<br>3. 修改画布尺寸 | 1. 激活Paint窗口<br>2. 使用Python脚本保存图片到`C:\Users\Docker\Downloads\CanvasSize.png`<br>3. 关闭Paint<br>4. 使用`image_dimension_matches_input`函数验证图片尺寸是否为800x600 | Microsoft Corporation |
| 3544ac9a-6aee-4a0b-a203-bc7b59b272b6-WOS | 将Paint图片保存为circle.png | 1. 打开Paint应用程序<br>2. 等待1秒<br>3. 执行保存操作 | 使用`vm_file_exists_in_vm_folder`函数检查`C:\Users\Docker\Downloads`目录下是否存在`circle.png`文件 | Microsoft Corporation |


## Edge浏览器测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|------|
| 1a1ec621 | 修改Edge配置文件用户名为Thomas | 1. 启动Edge浏览器(--remote-debugging-port=1337)<br>2. 启动socat进行端口转发<br>3. 修改配置文件用户名 | 通过profile_name_from_edge检查用户名是否为"Thomas" | - |
| 1c9d2c6c | 设置Edge在关闭时自动删除站点数据 | 1. 启动Edge浏览器<br>2. 配置隐私设置中的自动删除选项 | 通过data_delete_automacally_from_edge检查设置是否启用(期望值1.0) | https://www.howtogeek.com/718265/how-to-automatically-clear-browsing-data-when-you-close-microsoft-edge/ |
| 2acd62b4 | 为老年人增大Edge默认字体大小 | 1. 启动Edge浏览器<br>2. 修改字体大小设置 | 通过check_edge_font_size检查字体大小是否在合适范围(24-99999) | - |
| 4d34ff3b | 删除Amazon网站的追踪Cookie | 1. 启动Edge浏览器并访问Amazon<br>2. 删除特定网站的Cookie | 通过is_cookie_deleted检查.amazon.com域名的Cookie是否被删除 | https://support.google.com/chrome/answer/95647 |
| 5b46f4a4 | 将DuckDuckGo设为默认搜索引擎 | 1. 启动Edge浏览器<br>2. 修改默认搜索引擎设置 | 通过default_search_engine_from_edge检查是否为"DuckDuckGo" | - |
| 049d3788 | 将当前页面添加到书签栏 | 1. 启动Edge浏览器<br>2. 访问指定页面<br>3. 添加书签 | 通过is_expected_bookmarks检查书签栏是否包含指定URL | - |
| 58f493b5 | 修改默认下载文件夹为C盘 | 1. 启动Edge浏览器<br>2. 修改下载设置 | 通过edge_default_download_folder检查下载路径是否为"C:\\" | https://support.microsoft.com/en-us/microsoft-edge/change-the-downloads-folder-location-in-microsoft-edge-4049e93b-0ef6-e44f-aca0-7d5f37a39294 |
| 98cfcec4 | 启用安全浏览警告功能 | 1. 启动Edge浏览器<br>2. 开启增强安全浏览功能 | 通过enable_enhanced_safety_browsing_from_edge检查是否启用(期望值1.0) | https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-browse-safer |
| 1376d5e7 | 清除YouTube浏览历史记录 | 1. 预先填充浏览历史<br>2. 启动Edge浏览器<br>3. 清除特定网站历史 | 通过check_history_deleted检查是否删除包含"youtube"关键词的历史记录 | https://superuser.com/questions/1787991/clear-browsing-history-from-specific-site-on-chrome |
| 004587f8 | 启用"请勿跟踪"功能 | 1. 启动Edge浏览器<br>2. 开启Do Not Track设置 | 通过enable_do_not_track_from_edge检查是否启用(期望值1.0) | - |
| b27399ae | 安装PWA Builder网站为应用 | 1. 启动Edge浏览器<br>2. 将网站安装为PWA | 通过validate_pwa_installed检查是否成功安装(期望值"app_installed") | https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/ux |
| bd3e9ea0 | 为当前网站创建桌面快捷方式 | 1. 启动Edge并访问指定网站<br>2. 创建桌面快捷方式 | 通过is_url_shortcut_on_desktop检查快捷方式是否存在且URL正确 | https://www.hellotech.com/guide/for/how-to-create-a-desktop-shortcut-to-a-website |
| ccb22f83 | 设置维基百科为主页 | 1. 启动Edge浏览器<br>2. 修改主页设置 | 通过edge_home_page检查主页是否为"www.wikipedia.org" | https://support.microsoft.com/en-us/microsoft-edge/change-your-browser-home-page-a531e1b8-ed54-d057-0262-cc5983a065c6 |

## Notepad 测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|------|
| 366de66e-cbae-4d72-b042-26390db2b145-WOS | 测试记事本基本文件创建和保存功能 | 1. 打开记事本<br>2. 创建新文件<br>3. 输入指定文本<br>4. 保存为draft.txt | 1. 验证文件存在性<br>2. 比对文件内容 | - |
| a7d4b6c5-569b-452e-9e1d-ffdb3d431d15-WOS | 测试记事本文件搜索和计数功能 | 1. 打开记事本<br>2. 加载largefile.txt<br>3. 搜索"example"出现次数<br>4. 将结果保存到example_count.txt | 比对结果文件内容 | - |

## Windows 设置测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 37e10fc4-b4c5-4b02-a65c-bfae8bc51d3f | 关闭系统通知 | 1. 打开系统设置<br>2. 导航到通知设置<br>3. 关闭系统通知 | 使用exact_match函数验证system_notifications的状态是否为True（已关闭） | https://support.microsoft.com/en-us/windows/change-notification-settings-in-windows-8942c744-6198-fe56-4639-34320cf9444e |
| 46adf721-2949-4426-b069-010b7c128d8f | 配置夜间模式 | 1. 打开系统设置<br>2. 启用夜间模式<br>3. 设置开启时间为晚上7点<br>4. 设置关闭时间为早上7点 | 使用exact_match函数验证night_light_state的三个参数：<br>- 是否启用<br>- 开启时间是否为7:00 PM<br>- 关闭时间是否为7:00 AM | https://support.microsoft.com/en-us/windows/set-your-display-for-night-time-in-windows-18fe903a-e0a1-8326-4c68-fd23d7aaf136 |
| 9504989a-0d6e-4017-aefb-d359f6c752aa | 更改系统时区 | 1. 打开系统设置<br>2. 导航到时间和时区设置<br>3. 将时区更改为太平洋时间 | 使用exact_match函数验证system_timezone是否设置为"(UTC-08:00) Pacific Time (US & Canada)" | https://support.microsoft.com/en-us/windows/how-to-set-your-time-and-time-zone-dfaa7122-479f-5b98-2a7b-fa0b6e01b261 |
| a659b26e-4e31-40c1-adaf-34742b6c44ac | 更改桌面背景 | 1. 打开系统设置<br>2. 导航到个性化设置<br>3. 选择纯色背景 | 使用exact_match函数验证desktop_background的更改状态是否为True | https://support.microsoft.com/en-us/windows/change-desktop-background-and-colors-176702ca-8e24-393b-15f2-b15b38f69de6 |
| e8f68f22-1f6a-4cba-a97a-ac611bb4c67b | 配置存储感知 | 1. 使用命令启动存储感知设置(ms-settings:storagesense)<br>2. 启用存储感知<br>3. 设置每周运行一次 | 使用exact_match函数验证storage_sense_run_frequency是否设置为"7"（天） | https://support.microsoft.com/en-us/windows/manage-drive-space-with-storage-sense-654f6ada-7bfc-45e5-966b-e24aded96ad5 |


## VLC 播放器测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 8ba5ae7a-5ae5-4eab-9fcc-5dd4fe3abf89-2-WOS | 修改VLC录制文件保存位置到Downloads文件夹 | 通过VLC配置修改录制目录路径 | 检查vlcrc配置文件中recording_file_path是否为"C:\Users\Docker\Downloads" | https://docs.videolan.me/vlc-user/desktop/3.0/en/basic/recording/playing.html#choose-your-recordings-folder |
| 8ba5ae7a-5ae5-4eab-9fcc-5dd4fe3abf89-WOS | 修改VLC录制文件保存位置到Desktop | 通过VLC配置修改录制目录路径 | 检查vlcrc配置文件中recording_file_path是否为"C:\Users\Docker\Desktop" | https://docs.videolan.me/vlc-user/desktop/3.0/en/basic/recording/playing.html#choose-your-recordings-folder |
| 8f080098-ddb1-424c-b438-4e96e5e4786e-WOS | 从视频中提取MP3音频 | 使用VLC将视频转换为MP3格式并保存 | 比较生成的MP3文件与标准音频文件的相似度 | https://medium.com/@jetscribe_ai/how-to-extract-mp3-audio-from-videos-using-vlc-media-player-beeef644ebfb |
| 215dfd39-f493-4bc3-a027-8a97d72c61bf-WOS | 禁用启动画面的锥形图标 | 修改VLC界面设置以禁用背景锥形图标 | 检查vlcrc配置文件中qt_bgcone设置是否为0 | https://superuser.com/questions/1224784/how-to-change-vlcs-splash-screen |
| 386dbd0e-0241-4a0a-b6a2-6704fba26b1c-WOS | 设置全局快捷键控制播放/暂停 | 配置VLC全局热键设置 | 检查vlcrc配置文件中global_key_play_pause设置是否为1 | https://superuser.com/questions/1708415/pause-and-play-vlc-in-background?rq=1 |
| 9195653c-f4aa-453d-aa95-787f6ccfaae9-2-WOS | 将最大音量限制为100% | 修改VLC音量设置 | 检查vlcrc配置文件中qt_max_volume是否为100 | https://superuser.com/questions/1513285/how-can-i-increase-the-maximum-volume-output-by-vlc?rq=1 |
| 9195653c-f4aa-453d-aa95-787f6ccfaae9-WOS | 将最大音量提高到200% | 修改VLC音量设置 | 检查vlcrc配置文件中qt_max_volume是否为200 | https://superuser.com/questions/1513285/how-can-i-increase-the-maximum-volume-output-by-vlc?rq=1 |
| a5bbbcd5-b398-4c91-83d4-55e1e31bbb81-WOS | 在窗口模式下隐藏底部工具栏 | 启用VLC最小化视图模式 | 检查vlcrc配置文件中qt_minimal_view设置是否为1 | https://superuser.com/questions/776056/how-to-hide-bottom-toolbar-in-vlc |
| aa4b5023-aef6-4ed9-bdc9-705f59ab9ad6-WOS | 翻转视频并保存 | 使用VLC的视频转换功能添加翻转滤镜 | 比较生成的视频文件与标准视频文件 | https://www.dedoimedo.com/computers/vlc-rotate-videos.html |
| d06f0d4d-2cd5-4ede-8de9-598629438c6e-WOS | 将音量滑块颜色改为黑色系 | 修改VLC界面颜色设置 | 检查vlcrc配置文件中滑块颜色值是否小于等于100 | https://superuser.com/questions/1039392/changing-colour-of-vlc-volume-slider |
| efcf0d81-0835-4880-b2fd-d866e8bc2294-WOS | 将当前视频帧设置为桌面背景 | 从视频中截取当前帧并设置为壁纸 | 比较设置的壁纸图片与标准图片 | https://www.youtube.com/watch?v=XHprwDJ0-fU&t=436s |
| f3977615-2b45-4ac5-8bba-80c17dbe2a37-WOS | 允许运行多个VLC实例 | 修改VLC播放列表设置 | 检查vlcrc配置文件中one_instance_when_started_from_file设置是否为0 | https://www.reddit.com/r/Fedora/comments/rhljzd/how-to-run-multiple-instances-of-vlc-media-player/ |
| fba2c100-79e8-42df-ae74-b592418d54f4-WOS | 从视频中截图并保存 | 使用VLC的截图功能 | 比较生成的截图与标准图片 | https://www.youtube.com/watch?v=XHprwDJ0-fU&t=436s |
| fcd3d211-80f9-53eg-bf85-c603529e65g5-1-WOS | 禁止VLC窗口自动调整大小 | 修改VLC界面设置 | 检查vlcrc配置文件中qt-video-autoresize设置是否为0 | https://superuser.com/questions/368743/how-to-prevent-vlc-from-automatically-resizing-its-window-according-to-viewed-co |

###  不可执行的测试用例

以下测试用例被标记为不可执行(infeasible):

1. INF-0d95d28a-9587-433b-a805-1fbe5467d598-WOS: 打开当前播放视频所在文件夹 (无当前播放视频)
2. INF-5ac2891a-eacd-4954-b339-98abba077adb-WOS: 防止视频结束后自动关闭VLC (功能可能仅适用于macOS)
3. INF-7882ed6e-bece-4bf0-bada-c32dc1ddae72-WOS: 播放从Google Play购买的视频 (无购买信息和DRM支持)
4. INF-a1c3ab35-02de-4999-a7ed-2fd12c972c6e-WOS: 压缩视频为MPEG-4格式 (无源视频文件)
5. INF-cb130f0d-d36f-4302-9838-b3baf46139b6-WOS: 根据房间光线自动调节亮度和对比度 (无法检测房间光线)
6. INF-d1ba14d0-fef8-4026-8418-5b581dc68ca0-WOS: 重复播放视频的前半部分 (无源视频文件)
7. INF-d70666e4-7348-42c7-a06a-664094c5df3c-WOS: 添加水印到视频右上角 (无logo文件和源视频) 

## VS Code 测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 0ed39f63-6049-43d4-ba4d-5fa2fe04a951-WOS | 将文档中所有"text"替换为"test" | 1. 下载测试文件到指定路径<br>2. 使用VS Code打开文件<br>3. 等待1秒确保窗口加载<br>4. 激活VS Code窗口 | 1. 激活VS Code窗口<br>2. 等待0.5秒<br>3. 使用Ctrl+S保存<br>4. 比较文件内容与预期结果 | https://www.quora.com/How-do-you-find-and-replace-text-in-Visual-Studio-Code |
| 4e60007a-f5be-4bfc-9723-c39affa0a6d3-2-WOS | 安装Pylance扩展 | 1. 启动VS Code<br>2. 等待2秒确保窗口加载<br>3. 激活VS Code窗口 | 使用命令行检查已安装扩展列表中是否包含ms-python.vscode-pylance | https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/best_practices/vscode_docstring_extension/vscode_docstring_extension.html |
| 4e60007a-f5be-4bfc-9723-c39affa0a6d3-WOS | 安装autoDocstring扩展 | 1. 启动VS Code<br>2. 等待2秒确保窗口加载<br>3. 激活VS Code窗口 | 使用命令行检查已安装扩展列表中是否包含njpwerner.autodocstring | https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/best_practices/vscode_docstring_extension/vscode_docstring_extension.html |
| 5e2d93d8-8ad0-4435-b150-1692aacaa994-WOS | 将项目保存为VS Code工作区 | 1. 创建项目目录结构<br>2. 下载测试文件<br>3. 启动VS Code打开项目<br>4. 等待2秒<br>5. 激活VS Code窗口 | 检查是否存在project.code-workspace文件 | https://www.youtube.com/watch?v=B-s71n0dHUk |
| 9d425400-e9b2-4424-9a4b-d4c7abac4140-WOS | 设置标签页在超出空间时换行显示 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含workbench.editor.wrapTabs: true | https://superuser.com/questions/1466771/is-there-a-way-to-make-editor-tabs-stack-in-vs-code |
| 276cc624-87ea-4f08-ab93-f770e3790175-2-WOS | 设置行长度为100字符 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含editor.wordWrapColumn: 100 | https://www.quora.com/unanswered/How-do-you-set-the-line-length-in-Visual-Studio-Code |
| 276cc624-87ea-4f08-ab93-f770e3790175-WOS | 设置行长度为50字符 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含editor.wordWrapColumn: 50 | https://www.quora.com/unanswered/How-do-you-set-the-line-length-in-Visual-Studio-Code |
| 930fdb3b-11a8-46fe-9bac-577332e2640e-WOS | 创建从终端到编辑器的快捷键Ctrl+J | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查keybindings.json中是否正确配置快捷键 | https://superuser.com/questions/1270103/how-to-switch-the-cursor-between-terminal-and-code-in-vscode |
| 982d12a5-beab-424f-8d38-d2a48429e511-2-WOS | 将颜色主题更改为Solarized Dark | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含workbench.colorTheme: "Solarized Dark" | https://www.youtube.com/watch?v=ORrELERGIHs |
| 982d12a5-beab-424f-8d38-d2a48429e511-WOS | 将颜色主题更改为Visual Studio Dark | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含workbench.colorTheme: "Visual Studio Dark" | https://www.youtube.com/watch?v=ORrELERGIHs |
| 9439a27b-18ae-42d8-9778-5f68f891805e-WOS | 调试时保持光标在调试控制台 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含debug.focusEditorOnBreak: false | https://stackoverflow.com/questions/75832474/how-to-keep-cursor-in-debug-console-when-debugging-in-visual-studio-code |
| 57242fad-77ca-454f-b71b-f187181a9f23-WOS | 创建新的Python文件test.py | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查指定路径是否存在test.py文件 | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| 70745df8-f2f5-42bd-8074-fbc10334fcc5-2-WOS | 设置自动保存延迟为1000毫秒 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含正确的自动保存配置 | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| 70745df8-f2f5-42bd-8074-fbc10334fcc5-WOS | 设置自动保存延迟为500毫秒 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含正确的自动保存配置 | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| c6bf789c-ba3a-4209-971d-b63abf0ab733-WOS | 在资源管理器中隐藏__pycache__文件夹 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否正确配置files.exclude | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| e2b5e914-ffe1-44d2-8e92-58f8c5d92bb2-WOS | 禁用Python缺失导入的错误报告 | 1. 安装Python扩展<br>2. 启动VS Code<br>3. 等待2秒<br>4. 激活VS Code窗口 | 检查settings.json中是否正确配置诊断设置 | https://superuser.com/questions/1386061/how-to-suppress-some-python-errors-warnings-in-vs-code |
| ea98c5d7-3cf9-4f9b-8ad3-366b58e0fcae-WOS | 移除资源管理器搜索的Ctrl+F快捷键 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查keybindings.json中是否正确禁用快捷键 | https://superuser.com/questions/1748097/vs-code-disable-tree-view-find-explorer-search |
| eabc805a-bfcf-4460-b250-ac92135819f6-WOS | 安装Python扩展 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 使用命令行检查已安装扩展列表中是否包含ms-python.python | https://www.youtube.com/watch?v=VqCgcpAypFQ |
| ec71221e-ac43-46f9-89b8-ee7d80f7e1c5-WOS | 增加第2-10行的缩进 | 1. 下载测试文件<br>2. 使用VS Code打开文件<br>3. 等待2秒<br>4. 激活VS Code窗口 | 1. 激活窗口<br>2. 等待0.5秒<br>3. 保存文件<br>4. 比较文件内容与预期结果 | https://stackoverflow.com/questions/47903209/how-to-shift-a-block-of-code-left-right-by-one-space-in-vscode |

### 以下是被标记为不可行(Infeasible)的测试用例：

| 测试用例ID | 测试目的 | 原因 |
|------------|----------|-------|
| INF-7aeae0e2-70ee-4705-821d-1bba5d5b2ddd-WOS | 可视化所有numpy数组 | VS Code本身不支持此功能 |
| INF-7c4cc09e-7a92-40dd-8338-b2286535c4ed-WOS | 将VS Code显示语言改为阿拉伯语 | VS Code可能不支持阿拉伯语显示 |
| INF-847a96b6-df94-4927-97e6-8cc9ea66ced7-WOS | 在同一窗口同时打开两个工作区 | VS Code不支持在单一窗口打开多个工作区 |
| INF-971cbb5b-3cbf-4ff7-9e24-b5c84fcebfa6-WOS | 设置VS Code启动时自动创建test.py | VS Code没有此类自动化功能 |
| INF-dcbe20e8-647f-4f1d-8696-f1c5bbb570e3-WOS | 更改VS Code背景为指定图片 | VS Code不支持自定义背景图片 | 

## Windows 计算器测试用例

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 28b91a24-5d97-4c2a-891c-dccbd3820c62-WOS-2 | 测试使用计算器计算两个日期之间的天数 | 1. 启动计算器应用(calc)<br>2. 等待2秒让应用加载<br>3. 计算2024年1月3日到2024年8月20日之间的天数<br>4. 将结果保存到桌面的numdays.txt文件中 | 通过exact_match函数验证:<br>1. 文件是否保存在桌面<br>2. 文件名是否为numdays.txt<br>3. 文件内容是否为"230 days" | Microsoft Corporation |
| 28b91a24-5d97-4c2a-891c-dccbd3820c62-WOS-3 | 测试使用计算器计算两个日期之间的天数 | 1. 启动计算器应用(calc)<br>2. 等待2秒让应用加载<br>3. 计算2023年1月13日到2024年8月20日之间的天数<br>4. 将结果保存到桌面的numdays.txt文件中 | 通过exact_match函数验证:<br>1. 文件是否保存在桌面<br>2. 文件名是否为numdays.txt<br>3. 文件内容是否为"585 days" | Microsoft Corporation |
| 28b91a24-5d97-4c2a-891c-dccbd3820c62-WOS | 测试使用计算器计算两个日期之间的详细时间差 | 1. 启动计算器应用(calc)<br>2. 等待2秒让应用加载<br>3. 计算1980年8月10日到2024年8月2日之间的年、月、周、日差值<br>4. 将结果保存到桌面的Differences.txt文件中 | 通过exact_match函数验证:<br>1. 文件是否保存在桌面<br>2. 文件名是否为Differences.txt<br>3. 文件内容是否为"43 years, 9 months, 3 weeks, 4 days" | Microsoft Corporation |


## 注意事项

1. 部分测试用例被标记为不可行(Infeasible)，原因包括：
   - 功能在当前版本不支持
   - 缺少必要的硬件支持
   - 依赖外部服务或资源
   - 功能仅在特定操作系统版本可用
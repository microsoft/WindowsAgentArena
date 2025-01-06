# LibreOffice Calc 测试用例总结

| 序号 | ID | 测试目的 | 用法说明 | 测试方法 | 评估方式 | 来源 |
|-----|----|--------------|--------------|--------------|--------------------|--------|
| 1 | 01b269ae-2111-4a07-81fd-3fcd711993b0-WOS | 测试空白单元格填充功能 | 用上方单元格的值填充所有空白单元格 | 1. 打开Excel文件<br>2. 选择空白单元格<br>3. 使用上方单元格值填充 | 将工作表数据与预期结果进行比较 | https://www.youtube.com/shorts/VrUzPTIwQ04 |
| 2 | 035f41ba-6653-43ab-aa63-c86d449d62e5-WOS | 测试公式计算和文本拼接 | 帮我填写毛利润列。然后在新工作表的A列（名为"Year_Profit"）中，显示工作表1中的年份列，并用"_"连接相应的毛利润值。 | 1. 计算毛利润<br>2. 创建新工作表<br>3. 拼接年份和利润值 | 比较两个工作表的数据与预期结果 | SheetCopilot@92 |
| 3 | 0a2e43bf-b26c-4631-a966-af9dfa12c9e5-WOS | 测试数据汇总和图表创建 | 在名为"Total"的新行中计算月度总销售额，然后创建折线图显示结果（x轴为月份）。 | 1. 计算月度总额<br>2. 添加Total行<br>3. 创建折线图<br>4. 设置x轴为月份 | 比较工作表数据和图表属性与预期结果 | SheetCopilot@154 |
| 4 | 0acbd372-ca7a-4507-b949-70673120190f-WOS | 测试计算和数字格式化 | 在标题为"Net Income"的新列中计算净收入，并将所有数据格式化为会计数字类型。 | 1. 添加净收入列<br>2. 计算数值<br>3. 格式化为会计数字 | 将工作表数据与预期结果进行比较 | SheetCopilot@121 |
| 5 | 0bf05a7d-b28b-44d2-955a-50b41e24012a-WOS | 测试数字前导零格式化 | 我想在'Old ID'列中的所有数字前面填充零，使其在'New 7 Digit ID'列中填充到七位数。 | 1. 添加新列<br>2. 格式化数字添加前导零<br>3. 确保7位数格式 | 将工作表数据与预期结果进行比较 | https://www.youtube.com/shorts/FPAQaDTS8VY |
| 6 | 0cecd4f3-74de-457b-ba94-29ad6b5dafb6-WOS | 测试工作表管理操作 | 将"Sheet1"重命名为"LARS Resources"。然后复制它，将副本放在"Sheet2"之前，并在其名称后附加后缀"(Backup)"（用空格连接）。同时将"Sheet2"重命名，添加后缀"(Offline)"。 | 1. 重命名Sheet1<br>2. 复制工作表<br>3. 移动副本<br>4. 重命名Sheet2 | 比较工作表名称和数据与预期结果 | https://www.libreofficehelp.com/add-insert-delete-copy-move-rename-a-worksheet-in-libreoffice-calc/ |
| 7 | 1d17d234-e39d-4ed7-b46f-4417922a4e7c-WOS | 测试单元格合并和标题创建 | 创建名为"Sheet2"的新工作表，合并单元格A1:C1以写入标题"Investment Summary"。在其下方，合并单元格A2:B2以写入"High Interest Rate"，合并单元格C2:D2以形成"Low Interest Rate"。 | 1. 创建新工作表<br>2. 合并单元格<br>3. 添加标题 | 将工作表数据与预期结果进行比较 | SheetCopilot@73 |
| 8 | 1de60575-bb6e-4c3d-9e6a-2fa699f9f197-WOS | 测试数据透视表创建和图表格式化 | 在新工作表（Sheet2）中汇总每种促销类型的总收入，将促销名称作为列标题。 | 1. 创建数据透视表<br>2. 设置促销类型为标题<br>3. 计算收入总额 | 比较数据透视表和图表属性与预期结果 | SheetCopilot@55 |
| 9 | 1e8df695-bd1b-45b3-b557-e7d599cf7597-WOS | 测试公式计算和利润分析 | 添加名为"Profit"的新列，通过从"Sales"中减去"COGS"来计算每周的利润。 | 1. 添加利润列<br>2. 计算利润值<br>3. 格式化结果 | 将工作表数据与预期结果进行比较 | SheetCopilot@203 |
| 10 | 21ab7b40-77c2-4ae6-8321-e00d3a086c73-WOS | 测试计算和条件格式化 | 请在标题为"Period Rate (%)"的新列中计算期间利率，将结果转换为数字类型，并用绿色(#00ff00)字体突出显示最高结果。 | 1. 计算期间利率<br>2. 格式化为数字<br>3. 应用条件格式 | 比较工作表数据和样式与预期结果 | SheetCopilot@124 |
| 11 | 26a8440e-c166-4c50-aef4-bfb77314b46b-WOS | 测试数据汇总和表格创建 | 在新工作表中创建一个包含两个标题（"Month"和"Total"）的表格，显示所有月份的总销售额。 | 1. 创建新工作表<br>2. 添加标题<br>3. 计算月度总额 | 将工作表数据与预期结果进行比较 | SheetCopilot@152 |
| 12 | 30e3e107-1cfb-46ee-a755-2cd080d7ba6a-WOS | 测试单元格格式化和数据透视表创建 | 创建新工作表。合并单元格A1:C1并写入"Demographic Profile"，使用蓝色(#0000ff)填充和粗体白色文本。然后创建三个数据透视表，显示性别、婚姻状况和最高学历的百分比。 | 1. 创建新工作表<br>2. 格式化合并单元格<br>3. 创建数据透视表<br>4. 计算百分比 | 比较数据透视表数据和单元格格式与预期结果 | SheetCopilot@9 |
| 13 | 39aa4e37-dc91-482e-99af-132a612d40f3-WOS | 测试工作表重命名 | 帮我将sheet1重命名为"LARS_Science_Assessment" | 1. 选择Sheet1<br>2. 重命名工作表 | 比较工作表名称与预期结果 | https://www.libreofficehelp.com/add-insert-delete-copy-move-rename-a-worksheet-in-libreoffice-calc/ |
| 14 | 4de54231-e4b5-49e3-b2ba-61a0bec721c0-WOS | 测试公式计算和文本拼接 | 计算第2行的加速度并填写B列和D列的其他行。然后将A到D列的值（包括它们的标题）拼接到一个名为"Combined Data"的新列中。保留2位小数。 | 1. 计算加速度<br>2. 填充公式<br>3. 创建组合列<br>4. 格式化小数 | 将工作表数据与预期结果进行比较 | SheetCopilot@147 |
| 15 | 4e6fcf72-daf3-439f-a232-c434ce416af6-WOS | 测试根据生日计算年龄 | 请根据员工的生日计算他们的年龄。 | 1. 添加年龄列<br>2. 计算年龄<br>3. 格式化结果 | 将工作表数据与预期结果进行比较 | https://www.youtube.com/shorts/0uxJccNCKcE |
| 21 | 8b1ce5f2-59d2-4dcc-b0b0-666a714b9a14-WOS | 测试条件单元格格式化 | 给定部分日历，请通过将单元格背景设置为红色(#ff0000)来突出显示所有周末（周六和周日）。 | 1. 识别周末<br>2. 应用条件格式<br>3. 设置背景颜色 | 比较工作表数据和单元格样式与预期结果 | https://www.youtube.com/shorts/Hbcwu6IQ1ns |
| 22 | 9ed02102-6b28-4946-8339-c028166e9512-WOS | 测试复杂计算和数据可视化 | 考虑零售价格和折扣计算每笔交易的收入。创建网站销售计数的数据透视表。绘制标题为"Sales frequency by website"的条形图，不带图例。 | 1. 计算收入<br>2. 创建数据透视表<br>3. 创建条形图<br>4. 配置图表设置 | 比较工作表数据、数据透视表和图表属性与预期结果 | SheetCopilot@0 |
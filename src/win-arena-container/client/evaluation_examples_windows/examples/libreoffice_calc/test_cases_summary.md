# LibreOffice Calc 测试用例分析

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
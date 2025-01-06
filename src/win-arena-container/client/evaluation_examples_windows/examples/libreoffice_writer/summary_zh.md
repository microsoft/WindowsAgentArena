# LibreOffice Writer 测试用例总结

| 序号 | ID | 测试目的 | 用法说明 | 测试方法 | 评估方式 | 来源 |
|------|----|---------|-----------|-----------|-----------| -----|
| 1 | 0810415c-bde4-4443-9047-d5f70165a697-WOS | 测试文档段落行距设置 | 将前两段的行距设置为双倍行距 | 1. 打开文档<br>2. 选择前两段<br>3. 设置行距为双倍 | 检查文档中前两段的行距是否为双倍行距 | https://www.youtube.com/watch?v=Q_AaL6ljudU |
| 2 | 0a0faba3-5580-44df-965d-f562a99b291c-WOS | 测试文本对齐和制表位设置 | 我想让句子的前三个词左对齐，其余部分右对齐。我基本上想在中间留出一些空白空间来添加一些照片。假设每个句子至少有三个词。你能帮我使用制表位进行对齐吗？ | 1. 打开文档<br>2. 设置制表位<br>3. 调整文本对齐 | 使用check_tabstops函数检查文本是否按要求分割和对齐 | https://stackoverflow.com/questions/64528055/how-to-make-part-of-my-sentence-left-aligned-and-rest-as-right-aligned |
| 3 | 0b17a146-2934-46c7-8727-73ff6b6483e8-WOS | 测试下标功能 | 帮我把"H2O"中的2改为下标 | 1. 打开文档<br>2. 选择数字2<br>3. 设置为下标 | 1. 比较文档内容<br>2. 检查下标是否正确应用 | https://askubuntu.com/questions/245695/how-do-you-insert-subscripts-and-superscripts-into-ordinary-non-formula-text-i |
| 4 | 0e47de2a-32e0-456c-a366-8c607ef7a9d2-WOS | 测试页码添加功能 | 在每页底部左侧添加页码 | 1. 打开文档<br>2. 插入页码<br>3. 设置位置为底部左侧 | 检查页脚中是否包含页码 | https://ask.libreoffice.org/t/how-to-start-page-numbering-on-a-certain-page/39931/4 |
| 5 | 0e763496-b6bb-4508-a427-fad0b6c3e195-WOS | 测试字体更改功能 | 将整个文本的字体改为"Times New Roman" | 1. 打开文档<br>2. 全选文本<br>3. 更改字体 | 比较字体名称是否为Times New Roman | https://ask.libreoffice.org/t/how-do-i-change-the-font-for-the-whole-document-in-writer/9220 |
| 6 | 3ef2b351-8a84-4ff2-8724-d86eae9b842e-WOS | 测试标题居中对齐功能 | 帮我在LibreOffice中将标题居中对齐 | 1. 打开文档<br>2. 选择标题<br>3. 应用居中对齐 | 检查第一行是否居中对齐 | https://askubuntu.com/questions/1066351/how-do-you-center-align-in-libreoffice |
| 7 | 41c621f7-3544-49e1-af8d-dafd0f834f75-WOS | 测试文本高亮功能 | 我在学生写的句子旁边添加了以"#"开头的注释。我想让我的注释更突出，你能把这些句子用黄色高亮显示吗？我很难一个一个地给注释上色。顺便说一下，高亮文本后记得删除#符号。谢谢！ | 1. 打开文档<br>2. 查找#开头的文本<br>3. 应用黄色高亮<br>4. 删除#符号 | 比较高亮文本是否正确 | https://superuser.com/questions/1668018/how-to-auto-format-lines-in-libre-office-writer |
| 8 | 72b810ef-4156-4d09-8f08-a0cf57e7cefe-WOS | 测试删除线功能 | 我正在同行评议朋友的课程大纲。我认为最后一段是多余的，所以我想在最后一段的文字上添加删除线。你能帮我做这个吗？ | 1. 打开文档<br>2. 选择最后一段<br>3. 应用删除线格式 | 评估最后一段是否应用了删除线 | https://superuser.com/questions/657792/libreoffice-writer-how-to-apply-strikethrough-text-formatting |
| 9 | 88fe4b2d-3040-4c70-9a70-546a47764b48-WOS | 测试段落分隔功能 | 我正在为我的课程学生制定指导方针，想要分隔第一段中的每个句子以提高可读性。请在每个句子后创建一个空行，因为我很难一个一个地分隔它们。 | 1. 打开文档<br>2. 定位句子结尾<br>3. 插入空行 | 比较文档内容和格式 | https://stackoverflow.com/questions/56554555/libreoffice-writer-how-to-create-empty-line-space-after-every-period-in-a-par |
| 10 | 936321ce-5236-426a-9a20-e0e3c5dc536f-WOS | 测试文本转表格功能 | 你能帮我把用逗号分隔的文本转换成表格吗？ | 1. 打开文档<br>2. 选择文本<br>3. 转换为表格 | 比较文档中的表格内容 | https://www.youtube.com/watch?v=l25Evu4ohKg |
| 11 | adf5e2c3-64c7-4644-b7b6-d2f0167927e7-WOS | 测试参考文献和交叉引用功能 | 帮我在参考文献列表中添加"Steinberg, F. M., Bearden, M. M., & Keen, C. L. (2003). Cocoa and chocolate flavonoids: Implications for cardiovascular health. Journal of the American Dietetic Association, 103(2), 215-223. doi: 10.1053/jada.2003.50028"，并在我标记"<add here>"的第四段添加交叉引用（使用参考文献编号）。 | 1. 打开文档<br>2. 添加参考文献<br>3. 插入交叉引用 | 比较文档内容和格式 | https://seekstar.github.io/2022/04/11/libreoffice%E5%BC%95%E7%94%A8%E6%96%87%E7%8C%AE/ |
| 12 | b21acd93-60fd-4127-8a43-2f5178f4a830-WOS | 测试多段落行距设置 | 我最近一直在练习专业写作。现在我正在写一篇要求引言、正文和结论各一段的论文，引言为单倍行距，正文为双倍行距，结论为1.5倍行距。这篇论文的字体大小是12。你能帮我处理这个吗？ | 1. 打开文档<br>2. 设置各段落行距<br>3. 确认字体大小 | 比较各段落的行距设置 | https://superuser.com/questions/1097199/how-can-i-double-space-a-document-in-libreoffice |
| 13 | d53ff5ee-3b1a-431e-b2be-30ed2673079b-WOS | 测试大小写转换功能 | 我目前正在进行文本处理，需要帮助将文档中的所有大写文本转换为小写。这种精确性对于保持统一和精致的展示至关重要。你能帮我吗？ | 1. 打开文档<br>2. 全选文本<br>3. 转换为小写 | 比较文档内容和格式 | https://ask.libreoffice.org/t/how-to-convert-all-uppercase-to-lowercase/53341 |
| 14 | e246f6d8-78d7-44ac-b668-fcf47946cb50-WOS | 测试斜体字大小调整 | 我发现斜体字很难与普通文本区分开来，因为它也是深黑色的，大小也一样。当前字体大小是12，我想把斜体字的字体大小改为14，使其更容易辨认。你能帮我吗？ | 1. 打开文档<br>2. 查找斜体文本<br>3. 调整字体大小 | 检查斜体字的字体大小是否为14 | https://ask.libreoffice.org/t/how-to-change-text-size-color-of-italic-font/77712 |
| 15 | e528b65e-1107-4b8c-8988-490e4fece599-WOS | 测试首字母大写功能 | 请帮我把每个单词的首字母改为大写 | 1. 打开文档<br>2. 全选文本<br>3. 应用首字母大写 | 比较文档内容和格式 | https://www.youtube.com/watch?v=l25Evu4ohKg |
| 16 | f178a4a9-d090-4b56-bc4c-4b72a61a035d-WOS | 测试默认字体设置 | 将Times New Roman设为默认字体 | 1. 打开文档<br>2. 修改默认字体设置 | 检查默认字体是否为Times New Roman | https://ask.libreoffice.org/t/how-do-i-make-times-new-roman-the-default-font-in-lo/64604 |
| 17 | INF-bb8ccc78-479f-4a2f-a71e-d565e439436b-WOS | 测试实时协作功能 | 与我的团队共享此文档，让我们一起实时编辑 | 不适用 - LibreOffice不支持实时协作 | 标记为不可行 | https://ask.libreoffice.org/t/can-lo-be-used-for-collaboration-multi-person-real-time-document-editing/9392/6 |

## 测试用例分析总结

1. **功能覆盖范围**：
   - 基础文本格式化：字体、大小写、对齐方式
   - 高级格式化：行距、下标、高亮、删除线
   - 文档结构：页码、表格转换、参考文献
   - 协作功能测试

2. **测试类型分布**：
   - 单一功能测试：如字体更改、首字母大写等
   - 复合功能测试：如多段落不同行距设置
   - 可行性测试：如实时协作功能

3. **评估方法特点**：
   - 文件比较：大多数测试使用文件对比
   - 特定属性检查：如字体名称、行距等
   - 功能可用性验证

4. **测试用例质量**：
   - 指令明确，步骤清晰
   - 评估标准客观
   - 包含边界情况测试

5. **改进建议**：
   - 可增加批处理操作测试
   - 建议添加文档兼容性测试
   - 可考虑添加性能相关测试 
# Chrome浏览器扩展测试用例

## 测试用例总览

| 测试目的 | 用法说明 | 测试方法 | 评估方式 |
|---------|---------|---------|----------|
| 测试Chrome字体大小设置 | "我觉得网页字体太小了,能帮我调大一些吗?" | 1. 启动Chrome浏览器<br>2. 打开Chrome设置<br>3. 调整字体大小 | func: exact_match<br>type: chrome_font_size<br>评估字体大小是否成功调整 |
| 测试Chrome标签页管理 | "请帮我打开上次关闭的标签页" | 1. 启动Chrome浏览器<br>2. 配置测试标签页<br>3. 关闭指定标签页<br>4. 重新打开关闭的标签页 | func: is_expected_tabs<br>type: open_tabs_info<br>验证标签页是否正确恢复 |
| 测试Chrome书签管理 | "把当前网页添加到书签栏" | 1. 启动Chrome浏览器<br>2. 打开测试网页<br>3. 添加书签 | func: is_expected_bookmarks<br>type: bookmarks<br>检查书签是否成功添加 |
| 测试Chrome Cookie管理 | "请删除所有来自Amazon的Cookie" | 1. 启动Chrome浏览器<br>2. 访问Amazon网站<br>3. 删除指定Cookie | func: is_cookie_deleted<br>type: cookie_data<br>验证Cookie是否被删除 |

## 测试用例设计考虑

新增测试用例主要考虑了以下几个方面：

1. 用户界面定制测试
- 字体大小调整
- 显示设置优化

2. 浏览功能测试
- 标签页管理
- 书签管理
- 浏览历史管理

3. 隐私安全测试
- Cookie管理
- 数据清理
- 隐私保护设置

4. 可用性测试
- 常用功能可访问性
- 操作便捷性 
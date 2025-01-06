# Microsoft Edge 测试用例总结

| 序号 | ID | 测试目的 | 用法说明 | 测试方法 | 评估方式 | 来源 |
|-----|----|--------------|--------------------|-------------|-------------------|---------|
| 1 | 004587f8-6028-4656-94c1-681481abbc9c-wos | 启用"请勿跟踪"功能 | 你能帮我在Edge中启用"请勿跟踪"功能来增强我的在线隐私吗？ | 1. 启动Edge浏览器<br>2. 访问隐私设置<br>3. 启用"请勿跟踪"功能 | 验证"请勿跟踪"是否已启用（期望值：1.0） | |
| 2 | 049d3788-c979-4ea6-934d-3a35c4630faf-WOS | 将当前网页添加到书签 | 你能把我正在看的这个网页保存到书签栏，这样我以后可以再回来看吗？ | 1. 启动Edge<br>2. 导航到指定URL<br>3. 添加到书签栏 | 检查URL是否存在于书签栏中 | https://www.youtube.com/watch?v=ZaZ8GcTxjXA |
| 3 | 1376d5e7-deb7-471a-9ecc-c5d4e155b0c8-wos | 清除YouTube浏览历史 | 我在找一个一个月前访问过的网站地址，但是YouTube网站占据了我几乎所有的浏览历史，这太烦人了。你能帮我先清除YouTube的浏览历史吗？ | 1. 启动Edge<br>2. 访问浏览历史<br>3. 清除YouTube相关历史 | 检查history.sqlite中的YouTube历史是否已删除 | https://superuser.com/questions/1787991/clear-browsing-history-from-specific-site-on-chrome |
| 4 | 1a1ec621-b675-4099-96a9-f702dc27afb4-wos | 更改配置文件用户名 | 最近我把英文名改成了Thomas。我想更新我的用户名。你能帮我把Edge配置文件中的用户名改成Thomas吗？ | 1. 启动Edge<br>2. 访问配置文件设置<br>3. 将用户名改为Thomas | 验证配置文件名是否为"Thomas" | |
| 5 | 1c9d2c6c-ae4b-4359-9a93-9d3c42f48417-wos | 设置关闭浏览器时自动删除站点数据 | 请帮我设置Edge在每次关闭浏览器时自动删除所有设备上的站点数据。 | 1. 启动Edge<br>2. 配置隐私设置<br>3. 启用自动删除 | 检查自动删除是否已启用（期望值：1.0） | https://www.howtogeek.com/718265/how-to-automatically-clear-browsing-data-when-you-close-microsoft-edge/ |
| 6 | 2acd62b4-a2ab-44a7-a7e3-f5227bbd8324-wos | 增加字体大小 | 我奶奶最近一直在用Edge，她说字体对她的视力来说太小了。你能帮她把默认字体设置得最大吗？ | 1. 启动Edge<br>2. 访问外观设置<br>3. 增加字体大小 | 验证字体大小是否 >= 24 | |
| 7 | 4d34ff3b-5cc8-44b2-a272-fb07927e996e-WOS | 删除亚马逊cookies | 你能帮我清理电脑，删除亚马逊可能保存的所有跟踪内容吗？ | 1. 启动Edge<br>2. 访问cookie设置<br>3. 删除亚马逊cookies | 验证.amazon.com的cookies是否已删除 | https://support.google.com/chrome/answer/95647 |
| 8 | 58f493b5-5a96-4450-99ca-7cebe144c7e5-wos | 更改下载位置 | 帮我把"msedge"中的默认下载文件夹位置改到"C:\"驱动器 | 1. 启动Edge<br>2. 访问下载设置<br>3. 更改下载路径 | 验证下载路径是否为"C:\" | https://support.microsoft.com/en-us/microsoft-edge/change-the-downloads-folder-location-in-microsoft-edge-4049e93b-0ef6-e44f-aca0-7d5f37a39294 |
| 9 | 5b46f4a4-1a78-4860-ad92-76e051fa7efc-wos | 更改默认搜索引擎 | 你能把DuckDuckGo设为我上网搜索时的主要搜索工具吗？ | 1. 启动Edge<br>2. 访问搜索设置<br>3. 设置DuckDuckGo为默认 | 验证默认搜索引擎是否为"DuckDuckGo" | |
| 10 | 98cfcec4-c74e-4faa-b70d-664fb0a1d457-wos | 启用增强安全功能 | 我希望Edge在我访问潜在有害或不安全的网站时警告我。你能启用这个安全功能吗？ | 1. 启动Edge<br>2. 访问安全设置<br>3. 启用增强安全 | 验证增强安全是否已启用（期望值：1.0） | https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-browse-safer |
| 11 | b27399ae-e91a-4055-9406-472372e0f5c7-wos | 安装PWA | 帮我在"msedge"浏览器中将"www.pwabuilder.com"安装为渐进式Web应用。 | 1. 启动Edge<br>2. 导航到网站<br>3. 安装为PWA | 验证PWA是否已安装 | https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/ux |
| 12 | bd3e9ea0-a58a-45b3-97be-b418a7e2c0fd-WOS | 创建桌面快捷方式 | 嘿，我需要一个快速回到这个网站的方法。你能在我的桌面上创建一个快捷方式吗？ | 1. 启动Edge<br>2. 为当前网站创建桌面快捷方式 | 验证桌面上是否存在具有正确URL的快捷方式 | https://www.hellotech.com/guide/for/how-to-create-a-desktop-shortcut-to-a-website |
| 13 | ccb22f83-0831-4655-b557-225144b70c71-wos | 设置主页 | 帮我在"msedge"浏览器中将"www.wikipedia.org"设为主页 | 1. 启动Edge<br>2. 访问主页设置<br>3. 设置主页 | 验证主页是否为"www.wikipedia.org" | https://support.microsoft.com/en-us/microsoft-edge/change-your-browser-home-page-a531e1b8-ed54-d057-0262-cc5983a065c6 |

## 测试用例分析总结

这些测试用例涵盖了Microsoft Edge浏览器的主要功能和常见用户需求，主要可以分为以下几个方面：

1. **隐私安全相关**
   - 启用"请勿跟踪"功能
   - 清除特定网站的浏览历史
   - 删除cookies
   - 启用增强安全功能
   - 自动删除站点数据

2. **个性化设置**
   - 更改用户配置文件
   - 调整字体大小
   - 设置默认搜索引擎
   - 设置主页

3. **便利性功能**
   - 添加书签
   - 创建桌面快捷方式
   - 安装PWA应用
   - 更改下载位置

特点分析：
1. 测试用例设计考虑了不同用户群体的需求，从普通用户到老年用户
2. 评估方式明确且可量化，便于自动化测试
3. 测试步骤清晰，易于执行
4. 涵盖了浏览器的核心功能和高级特性

建议改进：
1. 可以添加更多关于浏览器性能优化的测试用例
2. 可以增加多设备同步相关的测试场景
3. 可以补充扩展程序管理相关的测试用例
4. 建议添加更多安全相关的测试场景，如密码管理、安全浏览等 
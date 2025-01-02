# Edge浏览器测试用例总结

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

注：所有测试用例在执行后都会通过taskkill强制关闭Edge进程，并等待2秒后重新启动浏览器以确保设置生效。大部分测试都使用了远程调试端口(1337)来实现自动化操作。 
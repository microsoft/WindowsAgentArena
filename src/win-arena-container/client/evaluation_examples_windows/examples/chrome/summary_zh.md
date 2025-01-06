# Chrome浏览器测试用例总结

| ID | 测试目的 | 用法说明 | 测试方法 | 评估方式 | 来源 |
|---|---|---|---|---|---|
| 030eeff7-b492-4218-b312-701ec99ee0cc-wos | 测试启用"请勿跟踪"功能 | 能否在Chrome中启用"请勿跟踪"功能来增强我的在线隐私？ | 1. 启动Chrome浏览器<br>2. 打开设置<br>3. 启用"请勿跟踪"功能 | 检查"请勿跟踪"功能是否成功启用 | https://support.google.com/chrome/answer/2790761?hl=en&co=GENIE.Platform%3DDesktop OR settings > privacy and security > third party cookies |
| 06fe7178-4491-4589-810f-2e2bc9502122-wos | 测试恢复最近关闭的标签页 | 能否让电脑恢复我刚刚关闭的标签页？ | 1. 启动Chrome浏览器<br>2. 打开3个指定网页<br>3. 关闭其中一个标签页<br>4. 尝试恢复关闭的标签页 | 检查是否所有指定的标签页都被成功恢复 | https://www.wikihow.com/Switch-Tabs-in-Chrome |
| 121ba48f-9e17-48ce-9bc6-a4fb17a7ebba-wos | 测试在Steam购物车中添加商品 | 找到Dota 2官方原声带并添加到我的Steam购物车中。 | 1. 启动Chrome浏览器<br>2. 打开Dota 2和Steam网站<br>3. 搜索并添加原声带到购物车 | 检查Steam购物车中是否包含指定商品 | Mind2Web |
| 35253b65-1c19-4304-8aa4-6884b8218fc0-wos | 测试创建网站桌面快捷方式 | 嘿，我需要一个快速访问这个网站的方法。能帮我在桌面上创建一个快捷方式吗？ | 1. 启动Chrome浏览器<br>2. 打开指定网页<br>3. 创建桌面快捷方式 | 检查桌面上是否存在对应的网站快捷方式 | https://www.hellotech.com/guide/for/how-to-create-a-desktop-shortcut-to-a-website |
| 44ee5668-ecd5-4366-a6ce-c1c9b8d4e938-wos | 测试清除特定网站的浏览历史 | 我在寻找一个月前访问过的网站地址，但YouTube网站占据了几乎所有的浏览历史，这太烦人了。我想先删除所有YouTube的浏览历史以方便搜索。你能帮我清除YouTube的浏览历史吗？ | 1. 启动Chrome浏览器<br>2. 添加测试浏览历史数据<br>3. 清除特定网站的浏览历史 | 检查YouTube相关的浏览历史是否被清除 | https://superuser.com/questions/1787991/clear-browsing-history-from-specific-site-on-chrome |
| 480bcfea-d68f-4aaa-a0a9-2589ef319381-wos | 测试启用性能指标HUD显示 | 我想在页面上显示不同页面的性能指标，不使用任何扩展。请帮我启用这个功能。 | 1. 启动Chrome浏览器<br>2. 启用性能指标HUD显示功能 | 检查性能指标HUD是否成功启用 | https://beebom.com/enable-chromes-benchmark-hud-track-performance-metrics/ OR go to chrome://flags/#show-performance-metrics-hud > enable |
| 82bc8d6a-36eb-4d2d-8801-ef714fb1e55a-wos | 测试航班搜索功能 | 查找下周一从孟买(BOM)到斯德哥尔摩(STO)的航班。 | 1. 启动Chrome浏览器<br>2. 打开指定航空公司网站<br>3. 搜索特定航班 | 检查搜索结果是否符合指定的出发地、目的地和日期要求 | test_task_1 |
| 99146c54-4f37-4ab8-9327-5f3291665e1e-wos | 测试自动删除站点数据功能 | 请帮我设置Chrome在每次关闭浏览器时自动删除所有本地站点数据。 | 1. 启动Chrome浏览器<br>2. 配置自动删除站点数据的设置 | 检查自动删除站点数据功能是否成功启用 | https://www.youtube.com/watch?v=v0kxqB7Xa6I |
| 2ae9ba84-3a0d-4d4c-8338-3a1478dc5fe3-wos | 测试修改Chrome配置文件用户名 | 最近我把英文名改成了Thomas。我想更新我的用户名。你能帮我把Chrome配置文件中的用户名改成Thomas吗？ | 1. 启动Chrome浏览器<br>2. 修改配置文件用户名 | 检查配置文件用户名是否成功更改为Thomas | https://superuser.com/questions/1393683/how-to-change-the-username-in-google-chrome-profiles?rq=1 |
| 7a5a7856-f1b6-42a4-ade9-1ca81ca0f263-wos | 测试将网页添加到书签栏 | 你能把我正在看的这个网页保存到书签栏，这样我以后可以再回来看吗？ | 1. 启动Chrome浏览器<br>2. 打开指定网页<br>3. 将网页添加到书签栏 | 检查书签栏中是否包含指定网页 | https://www.youtube.com/watch?v=ZaZ8GcTxjXA |
| 7b6c7e24-c58a-49fc-a5bb-d57b80e5b4c3-wos | 测试删除特定网站Cookie | 你能帮我清理电脑，删除Amazon可能保存的所有跟踪内容吗？我想确保我的浏览是私密的，这些网站不会记住我。 | 1. 启动Chrome浏览器<br>2. 访问Amazon网站<br>3. 删除Amazon相关的Cookie | 检查Amazon域名相关的Cookie是否被删除 | https://support.google.com/chrome/answer/95647?hl=en&ref_topic=7438325&sjid=16867045591165135686-AP#zippy=%2Cdelete-cookies-from-a-site |
| 9656a811-9b5b-4ddf-99c7-5117bcef0626-wos | 测试启用安全浏览功能 | 我希望Chrome在我访问潜在有害或不安全的网站时警告我。你能启用这个安全功能吗？ | 1. 启动Chrome浏览器<br>2. 启用增强保护的安全浏览功能 | 检查安全浏览功能是否成功启用 | https://www.quora.com/How-do-I-set-the-security-settings-for-the-Google-Chrome-browser-for-the-best-security |
| a96b564e-dbe9-42c3-9ccf-b4498073438a-wos | 测试查找特定社区讨论帖 | 找到社区讨论页面并打开Banter讨论主题（可能是所有时间回复最多的帖子）。 | 1. 启动Chrome浏览器<br>2. 打开FlightAware网站<br>3. 导航到指定讨论帖 | 检查是否成功打开指定的讨论帖 | test_task_0 |
| af630914-714e-4a24-a7bb-f9af687d3b91-wos | 测试调整默认字体大小 | 我奶奶最近一直在使用Chrome，她说字体对她的视力来说太小了。你能把默认字体大小设置到最大吗？ | 1. 启动Chrome浏览器<br>2. 调整默认字体大小设置 | 检查字体大小是否设置在合适范围（16-99999） | https://www.howtogeek.com/680260/how-to-change-chromes-default-text-size/ |
| b070486d-e161-459b-aa2b-ef442d973b92-wos | 测试药品信息查询 | 显示Tamiflu的副作用。 | 1. 启动Chrome浏览器<br>2. 打开drugs.com网站<br>3. 搜索Tamiflu副作用信息 | 检查是否成功导航到Tamiflu副作用页面 | online_tasks |
| bb5e4c0d-f964-439c-97b6-bdb9747de3f4-wos | 测试更改默认搜索引擎 | 你能把Bing设置为我在网上搜索时的主要搜索工具吗？ | 1. 启动Chrome浏览器<br>2. 更改默认搜索引擎设置 | 检查默认搜索引擎是否成功更改为Bing | https://support.google.com/chrome/answer/95426?sjid=16867045591165135686-AP |
| e1e75309-3ddb-4d09-92ec-de869c928143-wos | 测试网页保存为PDF | 电脑，你能把我正在看的网页转换成PDF文件并保存到我的主屏幕，也就是桌面吗？将目标设置为"另存为PDF"而不是"Microsoft打印为PDF"。 | 1. 启动Chrome浏览器<br>2. 打开指定网页<br>3. 将网页保存为PDF到桌面 | 比较生成的PDF文件与预期结果是否一致 | https://in5stepstutorials.com/google-chrome/save-web-page-as-pdf-in-chrome.php |

## 测试用例统计与分析

总计测试用例数量：16个

测试用例分类分析：
1. 隐私安全相关（5个）：
   - 启用"请勿跟踪"功能
   - 删除特定网站Cookie
   - 启用安全浏览功能
   - 自动删除站点数据
   - 清除特定网站浏览历史

2. 用户界面定制（3个）：
   - 调整默认字体大小
   - 启用性能指标HUD显示
   - 更改默认搜索引擎

3. 数据管理（4个）：
   - 创建网站桌面快捷方式
   - 将网页添加到书签栏
   - 恢复关闭的标签页
   - 修改配置文件用户名

4. 功能操作（4个）：
   - 航班搜索
   - 查找社区讨论帖
   - 药品信息查询
   - 网页保存为PDF

主要特点：
1. 测试用例覆盖面广泛，包含了Chrome浏览器的主要功能模块
2. 重点关注用户隐私和安全相关的功能测试
3. 包含了常见的用户操作场景
4. 测试用例设计较为完整，包含了明确的测试步骤和评估标准

建议：
1. 可以增加更多浏览器性能相关的测试用例
2. 可以补充多标签页管理相关的测试场景
3. 建议增加浏览器扩展相关的测试用例
4. 可以考虑添加更多跨设备同步功能的测试场景 
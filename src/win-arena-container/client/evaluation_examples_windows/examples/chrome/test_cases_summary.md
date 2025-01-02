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
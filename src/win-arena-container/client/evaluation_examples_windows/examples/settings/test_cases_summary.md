# Windows 设置测试用例汇总

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 37e10fc4-b4c5-4b02-a65c-bfae8bc51d3f | 关闭系统通知 | 1. 打开系统设置<br>2. 导航到通知设置<br>3. 关闭系统通知 | 使用exact_match函数验证system_notifications的状态是否为True（已关闭） | https://support.microsoft.com/en-us/windows/change-notification-settings-in-windows-8942c744-6198-fe56-4639-34320cf9444e |
| 46adf721-2949-4426-b069-010b7c128d8f | 配置夜间模式 | 1. 打开系统设置<br>2. 启用夜间模式<br>3. 设置开启时间为晚上7点<br>4. 设置关闭时间为早上7点 | 使用exact_match函数验证night_light_state的三个参数：<br>- 是否启用<br>- 开启时间是否为7:00 PM<br>- 关闭时间是否为7:00 AM | https://support.microsoft.com/en-us/windows/set-your-display-for-night-time-in-windows-18fe903a-e0a1-8326-4c68-fd23d7aaf136 |
| 9504989a-0d6e-4017-aefb-d359f6c752aa | 更改系统时区 | 1. 打开系统设置<br>2. 导航到时间和时区设置<br>3. 将时区更改为太平洋时间 | 使用exact_match函数验证system_timezone是否设置为"(UTC-08:00) Pacific Time (US & Canada)" | https://support.microsoft.com/en-us/windows/how-to-set-your-time-and-time-zone-dfaa7122-479f-5b98-2a7b-fa0b6e01b261 |
| a659b26e-4e31-40c1-adaf-34742b6c44ac | 更改桌面背景 | 1. 打开系统设置<br>2. 导航到个性化设置<br>3. 选择纯色背景 | 使用exact_match函数验证desktop_background的更改状态是否为True | https://support.microsoft.com/en-us/windows/change-desktop-background-and-colors-176702ca-8e24-393b-15f2-b15b38f69de6 |
| e8f68f22-1f6a-4cba-a97a-ac611bb4c67b | 配置存储感知 | 1. 使用命令启动存储感知设置(ms-settings:storagesense)<br>2. 启用存储感知<br>3. 设置每周运行一次 | 使用exact_match函数验证storage_sense_run_frequency是否设置为"7"（天） | https://support.microsoft.com/en-us/windows/manage-drive-space-with-storage-sense-654f6ada-7bfc-45e5-966b-e24aded96ad5 |

注：所有测试用例都使用"base_setup"快照作为初始环境，并在settings应用中进行操作。评估采用exact_match函数进行精确匹配验证，确保设置更改符合预期结果。 
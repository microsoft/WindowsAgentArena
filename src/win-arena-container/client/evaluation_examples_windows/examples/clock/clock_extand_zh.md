# 时钟应用测试用例扩展说明

新增测试用例主要考虑了以下方面：
1. 计时器功能：覆盖了短时间（分钟级）和长时间（小时级）的计时场景
2. 世界时钟功能：覆盖了不同地理位置（欧洲、美洲、亚洲）的主要城市
3. 实用性：基于用户日常使用场景设计测试用例
4. 边界测试：包含了不同时长的计时设置

| 测试目的 | 使用说明 | 测试方法 | 评估方式 |
|---------|---------|---------|----------|
| 测试短时计时器 | 设置15分钟计时器 | 1. 使用`ms-clock://Timers`启动计时器 <br> 2. 等待1秒让应用加载 | - func: exact_match <br> - type: check_if_timer_started <br> - 参数：小时: 0, 分钟: 15, 秒: 0 |
| 测试长时计时器 | 设置4小时计时器 | 1. 使用`ms-clock://Timers`启动计时器 <br> 2. 等待1秒让应用加载 | - func: exact_match <br> - type: check_if_timer_started <br> - 参数：小时: 4, 分钟: 0, 秒: 0 |
| 测试世界时钟 - 单一城市 | 添加法国巴黎到世界时钟 | 1. 使用`ms-clock://`启动时钟应用 <br> 2. 等待1秒让应用加载 | - func: exact_match <br> - type: check_if_world_clock_exists <br> - 参数：城市: "巴黎", 国家: "法国" |
| 测试世界时钟 - 主要城市 | 添加美国纽约到世界时钟 | 1. 使用`ms-clock://`启动时钟应用 <br> 2. 等待1秒让应用加载 | - func: exact_match <br> - type: check_if_world_clock_exists <br> - 参数：城市: "纽约", 国家: "美国" |
| 测试世界时钟 - 亚洲城市 | 添加中国北京到世界时钟 | 1. 使用`ms-clock://`启动时钟应用 <br> 2. 等待1秒让应用加载 | - func: exact_match <br> - type: check_if_world_clock_exists <br> - 参数：城市: "北京", 国家: "中国" | 
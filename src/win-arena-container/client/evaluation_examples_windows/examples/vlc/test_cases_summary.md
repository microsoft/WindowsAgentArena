# VLC播放器测试用例汇总

| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 8ba5ae7a-5ae5-4eab-9fcc-5dd4fe3abf89-2-WOS | 修改VLC录制文件保存位置到Downloads文件夹 | 通过VLC配置修改录制目录路径 | 检查vlcrc配置文件中recording_file_path是否为"C:\Users\Docker\Downloads" | https://docs.videolan.me/vlc-user/desktop/3.0/en/basic/recording/playing.html#choose-your-recordings-folder |
| 8ba5ae7a-5ae5-4eab-9fcc-5dd4fe3abf89-WOS | 修改VLC录制文件保存位置到Desktop | 通过VLC配置修改录制目录路径 | 检查vlcrc配置文件中recording_file_path是否为"C:\Users\Docker\Desktop" | https://docs.videolan.me/vlc-user/desktop/3.0/en/basic/recording/playing.html#choose-your-recordings-folder |
| 8f080098-ddb1-424c-b438-4e96e5e4786e-WOS | 从视频中提取MP3音频 | 使用VLC将视频转换为MP3格式并保存 | 比较生成的MP3文件与标准音频文件的相似度 | https://medium.com/@jetscribe_ai/how-to-extract-mp3-audio-from-videos-using-vlc-media-player-beeef644ebfb |
| 215dfd39-f493-4bc3-a027-8a97d72c61bf-WOS | 禁用启动画面的锥形图标 | 修改VLC界面设置以禁用背景锥形图标 | 检查vlcrc配置文件中qt_bgcone设置是否为0 | https://superuser.com/questions/1224784/how-to-change-vlcs-splash-screen |
| 386dbd0e-0241-4a0a-b6a2-6704fba26b1c-WOS | 设置全局快捷键控制播放/暂停 | 配置VLC全局热键设置 | 检查vlcrc配置文件中global_key_play_pause设置是否为1 | https://superuser.com/questions/1708415/pause-and-play-vlc-in-background?rq=1 |
| 9195653c-f4aa-453d-aa95-787f6ccfaae9-2-WOS | 将最大音量限制为100% | 修改VLC音量设置 | 检查vlcrc配置文件中qt_max_volume是否为100 | https://superuser.com/questions/1513285/how-can-i-increase-the-maximum-volume-output-by-vlc?rq=1 |
| 9195653c-f4aa-453d-aa95-787f6ccfaae9-WOS | 将最大音量提高到200% | 修改VLC音量设置 | 检查vlcrc配置文件中qt_max_volume是否为200 | https://superuser.com/questions/1513285/how-can-i-increase-the-maximum-volume-output-by-vlc?rq=1 |
| a5bbbcd5-b398-4c91-83d4-55e1e31bbb81-WOS | 在窗口模式下隐藏底部工具栏 | 启用VLC最小化视图模式 | 检查vlcrc配置文件中qt_minimal_view设置是否为1 | https://superuser.com/questions/776056/how-to-hide-bottom-toolbar-in-vlc |
| aa4b5023-aef6-4ed9-bdc9-705f59ab9ad6-WOS | 翻转视频并保存 | 使用VLC的视频转换功能添加翻转滤镜 | 比较生成的视频文件与标准视频文件 | https://www.dedoimedo.com/computers/vlc-rotate-videos.html |
| d06f0d4d-2cd5-4ede-8de9-598629438c6e-WOS | 将音量滑块颜色改为黑色系 | 修改VLC界面颜色设置 | 检查vlcrc配置文件中滑块颜色值是否小于等于100 | https://superuser.com/questions/1039392/changing-colour-of-vlc-volume-slider |
| efcf0d81-0835-4880-b2fd-d866e8bc2294-WOS | 将当前视频帧设置为桌面背景 | 从视频中截取当前帧并设置为壁纸 | 比较设置的壁纸图片与标准图片 | https://www.youtube.com/watch?v=XHprwDJ0-fU&t=436s |
| f3977615-2b45-4ac5-8bba-80c17dbe2a37-WOS | 允许运行多个VLC实例 | 修改VLC播放列表设置 | 检查vlcrc配置文件中one_instance_when_started_from_file设置是否为0 | https://www.reddit.com/r/Fedora/comments/rhljzd/how-to-run-multiple-instances-of-vlc-media-player/ |
| fba2c100-79e8-42df-ae74-b592418d54f4-WOS | 从视频中截图并保存 | 使用VLC的截图功能 | 比较生成的截图与标准图片 | https://www.youtube.com/watch?v=XHprwDJ0-fU&t=436s |
| fcd3d211-80f9-53eg-bf85-c603529e65g5-1-WOS | 禁止VLC窗口自动调整大小 | 修改VLC界面设置 | 检查vlcrc配置文件中qt-video-autoresize设置是否为0 | https://superuser.com/questions/368743/how-to-prevent-vlc-from-automatically-resizing-its-window-according-to-viewed-co |

## 不可执行的测试用例

以下测试用例被标记为不可执行(infeasible):

1. INF-0d95d28a-9587-433b-a805-1fbe5467d598-WOS: 打开当前播放视频所在文件夹 (无当前播放视频)
2. INF-5ac2891a-eacd-4954-b339-98abba077adb-WOS: 防止视频结束后自动关闭VLC (功能可能仅适用于macOS)
3. INF-7882ed6e-bece-4bf0-bada-c32dc1ddae72-WOS: 播放从Google Play购买的视频 (无购买信息和DRM支持)
4. INF-a1c3ab35-02de-4999-a7ed-2fd12c972c6e-WOS: 压缩视频为MPEG-4格式 (无源视频文件)
5. INF-cb130f0d-d36f-4302-9838-b3baf46139b6-WOS: 根据房间光线自动调节亮度和对比度 (无法检测房间光线)
6. INF-d1ba14d0-fef8-4026-8418-5b581dc68ca0-WOS: 重复播放视频的前半部分 (无源视频文件)
7. INF-d70666e4-7348-42c7-a06a-664094c5df3c-WOS: 添加水印到视频右上角 (无logo文件和源视频) 
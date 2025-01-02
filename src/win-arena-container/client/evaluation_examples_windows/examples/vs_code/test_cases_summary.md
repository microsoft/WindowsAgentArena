| 测试用例ID | 测试目的 | 测试方法 | 评估方式 | 来源 |
|------------|----------|-----------|-----------|-------|
| 0ed39f63-6049-43d4-ba4d-5fa2fe04a951-WOS | 将文档中所有"text"替换为"test" | 1. 下载测试文件到指定路径<br>2. 使用VS Code打开文件<br>3. 等待1秒确保窗口加载<br>4. 激活VS Code窗口 | 1. 激活VS Code窗口<br>2. 等待0.5秒<br>3. 使用Ctrl+S保存<br>4. 比较文件内容与预期结果 | https://www.quora.com/How-do-you-find-and-replace-text-in-Visual-Studio-Code |
| 4e60007a-f5be-4bfc-9723-c39affa0a6d3-2-WOS | 安装Pylance扩展 | 1. 启动VS Code<br>2. 等待2秒确保窗口加载<br>3. 激活VS Code窗口 | 使用命令行检查已安装扩展列表中是否包含ms-python.vscode-pylance | https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/best_practices/vscode_docstring_extension/vscode_docstring_extension.html |
| 4e60007a-f5be-4bfc-9723-c39affa0a6d3-WOS | 安装autoDocstring扩展 | 1. 启动VS Code<br>2. 等待2秒确保窗口加载<br>3. 激活VS Code窗口 | 使用命令行检查已安装扩展列表中是否包含njpwerner.autodocstring | https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/best_practices/vscode_docstring_extension/vscode_docstring_extension.html |
| 5e2d93d8-8ad0-4435-b150-1692aacaa994-WOS | 将项目保存为VS Code工作区 | 1. 创建项目目录结构<br>2. 下载测试文件<br>3. 启动VS Code打开项目<br>4. 等待2秒<br>5. 激活VS Code窗口 | 检查是否存在project.code-workspace文件 | https://www.youtube.com/watch?v=B-s71n0dHUk |
| 9d425400-e9b2-4424-9a4b-d4c7abac4140-WOS | 设置标签页在超出空间时换行显示 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含workbench.editor.wrapTabs: true | https://superuser.com/questions/1466771/is-there-a-way-to-make-editor-tabs-stack-in-vs-code |
| 276cc624-87ea-4f08-ab93-f770e3790175-2-WOS | 设置行长度为100字符 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含editor.wordWrapColumn: 100 | https://www.quora.com/unanswered/How-do-you-set-the-line-length-in-Visual-Studio-Code |
| 276cc624-87ea-4f08-ab93-f770e3790175-WOS | 设置行长度为50字符 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含editor.wordWrapColumn: 50 | https://www.quora.com/unanswered/How-do-you-set-the-line-length-in-Visual-Studio-Code |
| 930fdb3b-11a8-46fe-9bac-577332e2640e-WOS | 创建从终端到编辑器的快捷键Ctrl+J | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查keybindings.json中是否正确配置快捷键 | https://superuser.com/questions/1270103/how-to-switch-the-cursor-between-terminal-and-code-in-vscode |
| 982d12a5-beab-424f-8d38-d2a48429e511-2-WOS | 将颜色主题更改为Solarized Dark | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含workbench.colorTheme: "Solarized Dark" | https://www.youtube.com/watch?v=ORrELERGIHs |
| 982d12a5-beab-424f-8d38-d2a48429e511-WOS | 将颜色主题更改为Visual Studio Dark | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含workbench.colorTheme: "Visual Studio Dark" | https://www.youtube.com/watch?v=ORrELERGIHs |
| 9439a27b-18ae-42d8-9778-5f68f891805e-WOS | 调试时保持光标在调试控制台 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含debug.focusEditorOnBreak: false | https://stackoverflow.com/questions/75832474/how-to-keep-cursor-in-debug-console-when-debugging-in-visual-studio-code |
| 57242fad-77ca-454f-b71b-f187181a9f23-WOS | 创建新的Python文件test.py | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查指定路径是否存在test.py文件 | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| 70745df8-f2f5-42bd-8074-fbc10334fcc5-2-WOS | 设置自动保存延迟为1000毫秒 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含正确的自动保存配置 | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| 70745df8-f2f5-42bd-8074-fbc10334fcc5-WOS | 设置自动保存延迟为500毫秒 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否包含正确的自动保存配置 | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| c6bf789c-ba3a-4209-971d-b63abf0ab733-WOS | 在资源管理器中隐藏__pycache__文件夹 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查settings.json中是否正确配置files.exclude | https://download.microsoft.com/download/8/A/4/8A48E46A-C355-4E5C-8417-E6ACD8A207D4/VisualStudioCode-TipsAndTricks-Vol.1.pdf |
| e2b5e914-ffe1-44d2-8e92-58f8c5d92bb2-WOS | 禁用Python缺失导入的错误报告 | 1. 安装Python扩展<br>2. 启动VS Code<br>3. 等待2秒<br>4. 激活VS Code窗口 | 检查settings.json中是否正确配置诊断设置 | https://superuser.com/questions/1386061/how-to-suppress-some-python-errors-warnings-in-vs-code |
| ea98c5d7-3cf9-4f9b-8ad3-366b58e0fcae-WOS | 移除资源管理器搜索的Ctrl+F快捷键 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 检查keybindings.json中是否正确禁用快捷键 | https://superuser.com/questions/1748097/vs-code-disable-tree-view-find-explorer-search |
| eabc805a-bfcf-4460-b250-ac92135819f6-WOS | 安装Python扩展 | 1. 启动VS Code<br>2. 等待2秒<br>3. 激活VS Code窗口 | 使用命令行检查已安装扩展列表中是否包含ms-python.python | https://www.youtube.com/watch?v=VqCgcpAypFQ |
| ec71221e-ac43-46f9-89b8-ee7d80f7e1c5-WOS | 增加第2-10行的缩进 | 1. 下载测试文件<br>2. 使用VS Code打开文件<br>3. 等待2秒<br>4. 激活VS Code窗口 | 1. 激活窗口<br>2. 等待0.5秒<br>3. 保存文件<br>4. 比较文件内容与预期结果 | https://stackoverflow.com/questions/47903209/how-to-shift-a-block-of-code-left-right-by-one-space-in-vscode |

以下是被标记为不可行(Infeasible)的测试用例：

| 测试用例ID | 测试目的 | 原因 |
|------------|----------|-------|
| INF-7aeae0e2-70ee-4705-821d-1bba5d5b2ddd-WOS | 可视化所有numpy数组 | VS Code本身不支持此功能 |
| INF-7c4cc09e-7a92-40dd-8338-b2286535c4ed-WOS | 将VS Code显示语言改为阿拉伯语 | VS Code可能不支持阿拉伯语显示 |
| INF-847a96b6-df94-4927-97e6-8cc9ea66ced7-WOS | 在同一窗口同时打开两个工作区 | VS Code不支持在单一窗口打开多个工作区 |
| INF-971cbb5b-3cbf-4ff7-9e24-b5c84fcebfa6-WOS | 设置VS Code启动时自动创建test.py | VS Code没有此类自动化功能 |
| INF-dcbe20e8-647f-4f1d-8696-f1c5bbb570e3-WOS | 更改VS Code背景为指定图片 | VS Code不支持自定义背景图片 | 
# 项目介绍

本项目是一个名为 "Clip-Shortcuts-Sync" 的剪贴板同步工具，它可以帮助用户在不同平台的设备上同步剪贴板内容。具体来说，用户可以通过在 iOS 设备上执行快捷指令，并通过本工具将该文本同步到 Windows 设备上，从而实现跨平台的剪贴板同步。

# 使用方法

1. 安装必要的依赖库，包括 Flask、requests、pyperclip、pystray 和 PIL。
2. 编辑clipsync-server.py与clipsync-win.py中的yourip，将youip替换为服务器ip或PC的局域网ip。
3. 在服务器或者本地电脑启动服务端程序
   运行`python clipsync-server.py`命令。
4. 在本地电脑启动客户端程序
   运行`python clipsync-win.py`命令。
5. 编辑Shortcuts文件并导入iOS设备，将youip替换为服务器ip或PC的局域网ip。
6. 在 iOS 设备上执行快捷指令，iOS设备与Windows设备上的剪贴板内容自动交换。

# 实现细节

本项目包含两个程序，一个是服务端程序 `clipsync-server.py`，另一个是客户端程序 `clipsync-win.py`。

服务端程序使用 Flask 框架实现了一个简单的 Web API，用于接收来自客户端的请求并将其存储到内存中。具体来说，服务端程序提供了两个接口：

* `/clipboard`，用于接收客户端发送的剪贴板内容并将其存储到内存中。
* `/clipboard?platform=xxx`，用于获取指定平台的剪贴板内容。

客户端程序使用 requests、pyperclip、pystray 和 PIL 库实现了一个简单的桌面应用，用于监视 iOS 设备上的剪贴板变化并将其同步到 Windows 设备上。

具体来说，客户端程序实现了以下功能：

* 监视 Windows 设备上的剪贴板变化，并将新的剪贴板内容发送到服务端。
* 从服务端获取 iOS设备上的剪贴板内容，并将其复制到本地的剪贴板中。
* 将程序最小化到系统托盘中，并在系统托盘上显示一个图标。

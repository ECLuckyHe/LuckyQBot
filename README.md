# LuckyQBot

[Mirai-API-http]: https://github.com/project-mirai/mirai-api-http  
[Mirai Console]: https://github.com/mamoe/mirai-console
[启动Mirai Console]: https://github.com/mamoe/mirai-console/blob/master/docs/Run.md
[MCDReforged]: https://github.com/Fallen-Breath/MCDReforged

LuckyQBot是一个使用Python编写、基于 [Mirai-API-http] 插件（运行于 [Mirai Console] ）的、参照 [MCDReforged] 插件模式编写的、提供简单QQ消息收发功能的、通过可自定义的插件系统执行自定义功能的简单程序。

## 使用
使用该程序前，请先启动Mirai Console和Mirai-API-http。

> 关于Mirai Console启动方法，请参阅[启动Mirai Console]。  
> 关于Mirai-API-http的加载方法，请参阅[Mirai-API-http]。

在Mirai-API-http的配置文件`net.mamoe.mirai-api-http/setting.yml`中配置的端口号`port`和授权码`authKey`将会被用于该程序中。

**注意：请妥善保管授权码，防止泄露，其他人通过连接地址、端口号、授权码可直接获取Bot消息和发送消息。**

该程序界面使用`Tkinter`编写，且**未提供命令行指令功能**，因此您可能需要有一个具有桌面程序的操作系统。

关于如何让该程序连接到Mirai以及该程序界面提供的简单功能，请参阅[选项卡](docs/tabs.md)。

## 插件开发文档
由于该程序使用Python编写，因此对于插件的开发您需要有一定的Python基础。

插件开发详见[插件开发](docs/plugins.md)。


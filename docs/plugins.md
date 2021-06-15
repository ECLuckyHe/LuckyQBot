# 插件开发

## 目录
+ [开始](##开始)
+ [相关类和对象](##相关类和对象)
    + [Group类](###Group类)
    + [Member类](###Member类)
    + [Friend类](###Friend类)
    + [MessageChain类](###MessageChain类)
    + [Message类](###Message类)
    + [Conn类](###Conn类)
    + [异常类](###异常类)
+ [开始编写插件](##开始编写插件)
    + [消息相关](###消息相关)
    + [初始化](###初始化)
    + [事件相关](###事件相关)
        + [Bot登录成功](####Bot登录成功)
        + [Bot主动离线](####Bot主动离线)
        + [Bot被挤下线](####Bot被挤下线)
        + [Bot被服务器断开或因网络问题而掉线](####Bot被服务器断开或因网络问题而掉线)
        + [Bot主动重新登录](####Bot主动重新登录)
        + [Bot在群里的权限被改变](####Bot在群里的权限被改变)
        + [Bot被禁言](####Bot被禁言)
        + [Bot被取消禁言](####Bot被取消禁言)
        + [Bot加入了一个新群](####Bot加入了一个新群)
        + [Bot主动退出一个群](####Bot主动退出一个群)
        + [Bot被踢出一个群](####Bot被踢出一个群)
        + [群消息撤回](####群消息撤回)
        + [好友消息撤回](####好友消息撤回)
        + [某个群名改变](####某个群名改变)
        + [某群入群公告改变](####某群入群公告改变)
        + [全员禁言开关](####全员禁言开关)
        + [匿名聊天开关](####匿名聊天开关)
        + [坦白说开关](####坦白说开关)
        + [允许群员邀请好友加群修改](####允许群员邀请好友加群修改)
        + [新人入群](####新人入群)
        + [成员被踢出群（该成员不是Bot）](####成员被踢出群（该成员不是Bot）)
        + [成员主动离群（该成员不是Bot）](####成员主动离群（该成员不是Bot）)
        + [群名片改动](####群名片改动)
        + [群头衔改动](####群头衔改动)
        + [成员权限改变（该成员不是Bot）](####成员权限改变（该成员不是Bot）)
        + [群成员被禁言（该成员不是Bot）](####群成员被禁言（该成员不是Bot）)
        + [群成员被取消禁言（该成员不是Bot）](####群成员被取消禁言（该成员不是Bot）)
        + [添加好友申请](####添加好友申请)
        + [用户入群申请](####用户入群申请)
        + [Bot被邀请入群申请](####Bot被邀请入群申请)

[Mirai HTTP API]: https://github.com/project-mirai/mirai-api-http/blob/master/docs/API.md
[Mirai HTTP API 消息类型]: https://github.com/project-mirai/mirai-api-http/blob/master/docs/MessageType.md

## 开始
**创建一个新的插件**：在`plugins`文件夹中创建一个`.py`文件，此文档中以`sample.py`举例。

当程序运行后，若在`插件列表`选项卡的列表中看到有名为`sample.py`的项目，则可以说明该文件已被识别到，即可开始在文件中编写内容。

## 相关类和对象
编写执行内容前，请先了解以下对象和类提供的变量和功能。

### Group类
当消息或事件来自群时，会创建此对象。

| 成员/方法 | 变量类型 | 说明 |
| ---- | ---- | ---- |
| `id` | `int` | 群号 |
| `name` | `str` | 群名 |
| `permission` | `str` | 群权限（因情况而异） |

群权限有：
+ `OWNER` - 群主
+ `ADMINISTRATOR` - 群管理员
+ `MEMBER` - 普通成员

群权限内容视情况而定。

### Member类
当消息或事件来自群时，会创建此对象。

| 成员/方法 | 变量/返回类型 | 说明 |
| ---- | ---- | ---- |
| `qq` | `int` | 成员QQ |
| `name` | `str` | 成员群名片 |
| `permission` | `str` | 成员权限（因情况而异） |
| `group` | `Group` | 所在群或操作群（因情况而异） |

### Friend类
当消息或事件来自好友时，会创建此对象。

| 成员/方法 | 变量/返回类型 | 说明 |
| ---- | ---- | ---- |
| `qq` | `int` | 发送者QQ |
| `nickname` | `str` | 发送者昵称 |
| `remark` | `str` | （没有弄清楚用处） |

### MessageChain类
该类在`utils/api/`目录下。

在Mirai-API-http中，消息内容以`messageChain`列表记录。  

假设一名普通群成员（QQ为111111）在群123456中发送了如下消息：
> @Lucky_He 你好

其中Lucky_He的QQ为673230244，则生成的`messageChain`为：
```python
messageChain = [
    {
        "type": "At",
        "target": 673230244
    },
    {
        "type": "Plain",
        "text": "你好"
    }
]
```

详细的消息类型请参见程序代码中的注释或`Mirai-API-http`提供的消息类型参考[Mirai HTTP API 消息类型]。

以上例子只是用于引入`messageChain`的概念，当插件中需要向QQ好友或群发送消息时，则需要使用该类创建对象。（**该类的对象编写插件时手动创建，程序本身不会创建该对象**）

`MessageChain`类有如下变量和方法：

| 成员/方法 | 变量/返回类型 | 说明 |
| ---- | ---- | ---- |
| `__message_chain` | `list` | `messageChain`（私有） |
| `get_message_chain()` | `list` | 返回`messageChain` |
| `add_at(member_id: int)` | `None` | 向`messageChain`添加一个群@，`member_id`为被@成员QQ，此方法仅在发送至群时有用 |
| `add_at_all()` | `None` | 向`messageChain`添加一个群@全体成员，此方法仅在发送至群时有用 |
| `add_face(face_id: int = None, name: str = None)` | `None` | 向`messageChain`添加一个表情，`face_id`为表情编号（优先于`name`，但是我没有表情编号对应表）；`name`为表情名称（经测试发现直接输入表情中文名称即可，如：斜眼笑） |
| `add_plain_text(text: str)` | `None` | （常用）向`messageChain`添加一个纯文本消息，`text`为文本消息 |
| `add_image(group_image_id: str = None, friend_image_id: str = None, url: str = None, path: str = None)` | `None` | 向`messageChain`添加一个图片，其中`friend_image_id`为好友图片id，`group_image_id`为群图片id，这两种id冲突且优先于`url`和`path`；`url`为图片的url地址，优先于`path`；`path`为本地路径 |
| `add_flash_image(group_image_id: str = None, friend_image_id: str = None, url: str = None, path: str = None)` | `None` |向`messageChain`添加一个闪照，参数与`add_image()`一致 |
| `add_voice(voice_id: str = None, url: str = None, path: str = None)` | `None` | 向`messageChain`添加一个语音，`voice_id`为语音号，优先级最高；`url`为url地址，优先级其次；`path`为本地路径 |
| `add_xml(xml: str)` | `None` | 向`messageChain`添加xml文本 |
| `add_json(json: str)` | `None` | 向`messageChain`添加json文本 |
| `add_app(app: str)` | `None` | 没弄清楚，请参照[Mirai HTTP API 消息类型] |
| `add_poke(poke: str)` | `None` | 向`messageChain`添加戳一戳，其中`poke`为戳一戳类型，类型有`"Poke"`：戳一戳，`"ShowLove"`：比心，`"Like"`：点赞，`"Heartbroken"`：心碎，`"SixSixSix"`：666，`"FangDaZhao"`：放大招 |

如果以上说明不准确，请参见程序代码中的注释或`Mirai-API-http`提供的消息类型参考[Mirai HTTP API 消息类型]。

### Message类
当程序接收到一条消息时，一个新的`Message`类对象将会被创建，该类具有的成员变量和方法如下：

| 成员/方法 | 变量/返回类型 | 说明 |
| ---- | ---- | ---- |
| `type` | `str` | 消息类型，`"GroupMessage"`为群消息，`"TempMessage"`为临时消息，`"FriendMessage"`为好友消息 |
| `message_chain` | `list` | `messageChain`本身 |
| `message_id` | `int` | 消息号（该消息的唯一标识） |
| `time` | `int` | 时间戳 |
| `is_op` | `bool` | 是否为Bot管理员发送，如果是则为`True`否则为`False` |
| `is_command` | `bool` | 消息是否以`command_head`开头 |
| `command_head` | `str` | 指令头（由程序界面传入的参数） |
| `sender_member` | `Member` | 如果为群消息或临时消息，则存在此变量，且`sender_friend`不存在 |
| `sender_friend` | `Friend` | 如果为好友消息，则存在此变量，且`sender_group`不存在 |
| `is_group_message()` | `bool` | 是否为群消息 |
| `is_temp_message()` | `bool` | 是否为临时消息 |
| `is_friend_message()` | `bool` | 是否为好友消息 |
| `get_plain_text()` | `str` | 获取该消息的纯文本消息（即`messageChain`中去除`"type"`不是`"Plain"`的所有字典，并将所有的`"text"`的值拼接起来） |
| `send_message_back(message_chain: MessageChain)` | `None` | 向消息来源方发送`message_chain`消息内容，如果为群消息则向该群发送 |

关于使用上述部分方法的一个例子：

假设`command_head`为`"#"`，现在要求Bot收到好友消息“#你好”时给发送方回复“（表情：斜眼笑）你好”，消息创建的`Message`类对象为`message`，核心代码如下：
```python
if message.get_plain_text() == message.command_head + "你好":
    mc = MessageChain()
    mc.add_face(name="斜眼笑")
    mc.add_plain_text("你好")
    message.send_message_back(mc)
```

### Conn类
Conn类提供了对Bot进行操作的所有功能，以下只列出**能用到的方法**（具体可参见程序源码），以下所有方法返回类型为`dict`，内容为执行`GET`或`POST`后得到的响应。

**注意：此类的方法全部都是静态方法。**

| 成员/方法 | 说明 |
| ---- | ---- |
| `send_friend_message(qq: int, message_chain: MessageChain, quote: int = None)` | 发送消息给好友，`qq`为接收方qq，`quote`为引用消息号，`message_chain`为消息内容 |
| `send_temp_message(qq: int, group: int, message_chain: MessageChain, quote: int = None)` | 发送临时消息，`qq`为接收方qq，`group`为接收方所在群，`message_chain`为消息内容，`quote`为引用消息号 |
| `send_group_message(group: int, message_chain: MessageChain, quote: int = None)` | 发送群消息，`group`为群号，`message_chain`为消息内容，`quote`为引用消息号 |
| `recall_message(message_id: int)` | 撤回消息，`message_id`为撤回消息号 |
| `send_image_message_by_url(urls: list, qq: int = None, group: int = None)` | 通过url发送图片（测试过程中出现了奇怪的问题，建议不要使用此方法） |
| `get_message_from_id(id: int)` | 通过消息号获取某条消息，`id`为消息号，参见[Mirai HTTP API] |
| `get_friend_list() ` | 获取好友列表，参见[Mirai HTTP API] |
| `get_group_list()` | 获取群列表，参见[Mirai HTTP API] |
| `set_mute(group: int, member_qq: int, time: int = None)` | 设置禁言，`group`为指定群号，`member_qq`为指定成员qq号，`time`为禁言时间（单位为秒） |
| `set_unmute(group: int, member_qq: int)` | 解除禁言，`group`为群号，`member_qq`为成员qq号 |
| `kick_member(group: int, member_qq: int, msg: str = None)` | 移除指定成员，`group`为群号，`member_qq`为成员qq，`msg`为移除消息（？） |
| `quit_group(group: int)` | 退出群聊，`group`为群号 |
| `mute_all(group: int)` | 禁言全体，`group`为指定群号 |
| `unmute_all(group: int)` | 解除全体禁言，`group`为群号 |
| `get_group_config(group: int)` | 获取群设置，参见[Mirai HTTP API] |
| `set_group_config(group: int, group_name: str = None, group_announcement: str = None, confess_talk: bool = None, allow_member_invite: bool = None, auto_approve: bool = None, anonymous_chat: bool = None)` | 修改群设置，`group`为群号，`group_name`为群名称，`group_announcement`为群公告，`confess_talk`为是否开启坦白说，`allow_member_invite`为是否允许群员邀请，`auto_approve`为是否开启自动审批入群，`anonymous_chat`为是否允许匿名聊天 |
| `get_member_info(group: int, member_qq: int)` | 获取群成员资料，`group`为群号，`member_qq`为成员qq号，参见[Mirai HTTP API]
| `set_member_info(group: int, member_id: int, name: str = None, special_title: str = None)` | 设置群成员信息，`group`为群号，`member_id`为成员qq号，`name`为新的群名片，`special_title`为新的群头衔 |

以下方法为部分事件的处理方法，其中`event_id`为事件唯一标识，事件相关内容将会在后面介绍：

| 成员/方法 | 说明 |
| ---- | ---- |
| `resp_new_friend_request(event_id: int, from_qq: int, group_id: int, operate: int, message: str)` | 处理添加新好友事件，`event_id`为事件号；`from_qq`为申请人qq；`group_id`为申请人所在群，为`0`表示不是从群内添加；`operate`为响应操作类型，`0`表示同意，`1`表示拒绝，`2`表示拒绝并拉黑；`message`为回复的信息 |
| `resp_member_join_request(event_id: int, from_qq: int, group_id: int, operate: int, message: str)` | 处理入群申请，`event_id`为事件号；`from_qq`为申请人qq；`group_id`为加的群号；`operate`为响应操作类型，`0`表示同意，`1`表示拒绝，`2`表示忽略，`3`表示拒绝并拉黑不再接受请求，`4`表示忽略并拉黑不再接受请求 |
| `resp_bot_invited_join_group_request_event(event_id: int, from_qq: int, group_id: int, operate: int, message: str)` | 处理被邀请入群申请，`event_id`为事件号；`from_qq`为邀请人qq；`group_id`为被邀请入群群号；`operate`为被邀请入群群名；`message`为回复的信息 |

### 异常类
这些异常类在`utils/api/`目录下。

在使用`Conn`类时，如果出现了不能操作的情况（如Bot为非群管理员，但是执行了禁言某群员操作）或Bot本身出现某些情况时，会抛出以下的异常：

| 异常类 | 异常说明 |
| ---- | ---- |
| `ResponseException` | 所有Bot异常类的父类 |
| `WrongAuthkeyException` | 错误的Authkey |
| `BotNotExistException` | 指定的Bot不存在 |
| `SessionInvalidException` | Session失效或不存在 |
| `SessionNotCertifiedException` | Session未认证（未激活） |
| `MessageReceiverNotExistException` | 发送消息目标不存在（指定对象不存在） |
| `FileNotExistException` | 指定文件不存在 |
| `NoPermissionException` | Bot没有对应的操作权限 |
| `BotSpeakNotAllowedException` | Bot当前无法向指定群发送信息 |
| `TooLongMessageException` | 消息过长 |
| `WrongAccessException` | 错误的访问 |

请参照异常说明考虑应该对哪些操作进行`try-except`语句编写。

## 开始编写插件

了解上述类和相关对象后，就可以开始编写插件了。

下面先看一个例子：  
假设我收到来自QQ号为673230244的好友消息时（无论是什么消息），调用`print("Hello World!")`，并向该好友发送消息`"你好"`，则在`sample.py`文件中添加如下函数即可：

```python
def on_friend_message(message, Conn):
    print("Hello World!")
    
    mc = MessageChain()
    mc.add_plain_text("你好")
    message.send_message_back(mc)
    # 调用该方法等同于：
    # Conn.send_friend_message(message.sender_friend.qq, mc)
```

其中，`message`类型为`Message`，为接收到的消息对象，`Conn`为`Conn`类本身。

下面提供的是此类函数的**函数名**，当对应的事件发生时，如果`sample.py`中有这些函数，则会自动调用他们。

**注意：当函数名与参数个数完全一致时，该函数才能被正确调用。**

### 消息相关
收到QQ消息时会调用的函数如下：

| 函数名 | 说明 |
| ---- | ---- |
| `on_friend_message(message, Conn)` | 当Bot收到好友消息时调用 |
| `on_group_message(message, Conn)` | 当Bot收到群消息时调用 |
| `on_temp_message(message, Conn)` | 当Bot收到临时消息时调用 |

### 初始化
当程序被启动时，`init()`将会被调用。

**注意：由于此时未连接到Mirai-API-http，故使用`Conn`类的方法可能会导致异常。**

在程序启动时输出`"Hello World!"`：
```python
def init():
    print("Hello World!")
```

### 事件相关

由于每个事件所产生的信息不同，故此处将对每个事件产生的信息进行解释。

#### Bot登录成功
当Bot登录成功时，`on_bot_online_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.qq` | `int` | 登录成功的Bot的QQ号 |

#### Bot主动离线
当Bot主动离线时，`on_bot_offline_active_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.qq` | `int` | 主动离线的QQ号 |

#### Bot被挤下线
当Bot被挤下线时，`on_bot_offline_force_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.qq` | `int` | 被挤下线的QQ号 |

#### Bot被服务器断开或因网络问题而掉线
当Bot被服务器断开或因网络问题而掉线时，`on_bot_offline_dropped_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.qq` | `int` | 被服务器断开或因网络问题而掉线的Bot的QQ号 |

#### Bot主动重新登录
当Bot主动重新登录时，`on_bot_relogin_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.qq` | `int` | 主动重新登录的QQ |

#### Bot在群里的权限被改变
当Bot在群里的权限被改变时，`on_bot_group_permission_change_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.origin` | `str` | Bot的原权限 |
| `event.new` | `str` | Bot的新权限 |
| `event.current` | `str` | Bot的新权限 |
| `event.group.id` | `int` | 群号 |
| `event.group.name` | `str` | 群名 |
| `event.group.permission` | `str` | Bot在群中的权限 |

#### Bot被禁言
当Bot在群中被禁言时，`on_bot_mute_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.duration_seconds` | `int` | 禁言时长，单位为秒 |
| `event.operator.qq` | `int` | 操作者的QQ号 |
| `event.operator.name` | `str` | 操作者的群名片 |
| `event.operator.permission` | `str` | 操作者在群中的权限 |
| `event.operator.group.id` | `int` | 群号 |
| `event.operator.group.name` | `str` | 群名 |
| `event.operator.group.permission` | `str` | Bot在群中的权限 |

#### Bot被取消禁言
当Bot在群中被取消禁言时，`on_bot_unmute_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event.operator.qq` | `int` | 操作者的QQ号 |
| `event.operator.name` |`str` | 操作者的群名片 |
| `event.operator.permission` |`str` | 操作者在群中的权限 |
| `event.operator.group.id` | `int` | 群号 |
| `event.operator.group.name` |`str` | 群名 |
| `event.operator.group.permission` |`str` | Bot在群中的权限 |

#### Bot加入了一个新群
当Bot加入了一个新群时，`on_bot_join_group_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |

#### Bot主动退出一个群
当Bot主动退出一个群时，`on_bot_leave_active_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |

#### Bot被踢出一个群
当Bot被踢出一个群时，`on_bot_leave_kick_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |

#### 群消息撤回
当群消息被撤回时，`on_group_recall_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `author_qq` | `int` | 原消息发送者的QQ号 |
| `message_id` | `int` | 原消息号 |
| `time` | `int` | 原消息发送时间 |
| `group` | `Group` | 消息撤回所在的群 |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 撤回消息的操作人，当为`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`group` |

#### 好友消息撤回
当好友消息被撤回时， `on_friend_recall_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `author_qq` | `int` | 原消息发送者的QQ号 |
| `message_id` | `int` | 原消息号 |
| `time` | `int` | 原消息发送时间 |
| `operator_qq` | `int` | 好友QQ号或BotQQ号 |

#### 某个群名改变
当某个群名改变时，`on_group_name_change_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `str` | 原群名 |
| `new` | `str` | 新群名 |
| `current` | `str` | 新群名 |
| `group` | `Group` | 群名改名的群信息 |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作的管理员或群主信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`group` |

#### 某群入群公告改变
当某群入群公告改变时，`on_group_entrance_announcement_change_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `str` | 原公告 |
| `new` | `str` | 新公告 |
| `current` | `str` | 新公告 |
| `group` | `Group` | 公告改变的群信息 |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作的管理员或群主信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`group` |

#### 全员禁言开关
当某群全员禁言或解除时，`on_group_mute_all_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `bool` | 原本是否处于全员禁言 |
| `new` | `bool` | 现在是否处于全员禁言 |
| `current` | `bool` | 现在是否处于全员禁言 |
| `group` | `Group` | 全员禁言的群信息 |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作的管理员或群主信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`group` |

#### 匿名聊天开关
当某群匿名聊天被开启或关闭时，`on_group_allow_anonymous_chat_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `bool` | 原本匿名聊天是否开启 |
| `new` | `bool` | 现在匿名聊天是否开启 |
| `current` | `bool` | 现在匿名聊天是否开启 |
| `group` | `Group` | 匿名聊天状态改变的群信息 |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作的管理员或群主信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`group` |

#### 坦白说开关
当某群坦白说被开启或关闭时，`on_group_allow_confess_talk_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `bool` | 原本坦白说是否开启 |
| `new` | `bool` | 现在坦白说是否开启 |
| `current` | `bool` | 现在坦白说是否开启 |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |
| `is_by_bot` | `bool` | 是否为Bot进行的该操作 |

#### 允许群员邀请好友加群修改
当某群进行允许群员邀请好友加群设置修改时，`on_group_allow_member_invite_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `bool` | 原本是否允许群员邀请好友加群 |
| `new` | `bool` | 现在是否允许群员邀请好友加群 |
| `current` | `bool` | 现在是否允许群员邀请好友加群 |
| `group` | `Group` | 允许群员邀请好友加群状态改变的群信息 |
| `group.id` | `int` | 群号 |
| `group.name` | `str` | 群名 |
| `group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作的管理员或群主信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`group` |

#### 新人入群
当某群有新人入群时，`on_member_join_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `member.qq` | `int` | 新人信息 |
| `member.name` | `str` | 新人的QQ号 |
| `member.permission` | `str` | 新人在群中的权限 |
| `member.group.id` | `int` | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |

#### 成员被踢出群（该成员不是Bot）
当某群成员被踢出群（该成员不是Bot）时，`on_member_leave_kick_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `member.qq` | `int` | 被踢者的QQ号 |
| `member.name` | `str` | 被踢者的群名片 |
| `member.permission` | `str` | 被踢者在群中的权限 |
| `member.group` | `Group` | 被踢者所在的群 |
| `member.group.id` | `int` | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member`  | 操作的管理员或群主信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`member.group` |

#### 成员主动离群（该成员不是Bot）
当某群成员主动离群（该成员不是Bot）时，`on_member_leave_quit_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `member.qq` | `int` | 退群群员的QQ号 |
| `member.name` | `str` | 退群群员的群名片 |
| `member.permission` | `str` | 退群群员在群中的权限 |
| `member.group.id` | `int` | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |

#### 群名片改动
当某群某人群名片被改动时，`on_member_card_change_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `str` | 原本名片 |
| `new` | `str` | 现在名片 |
| `current` | `str` | 现在名片 |
| `member.qq` | `int` | 名片改动的群员的QQ号 |
| `member.name` | `str` | 名片改动的群员的群名片 |
| `member.permission` | `str` | 名片改动的群员在群中的权限 |
| `member.group` | `Group` | 名片改动的群员所在群的信息 |
| `member.group.id` | `str`  | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作者的信息，可能为该群员自己，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`member.group` |

#### 群头衔改动
当某群某人群头衔被改动时，`on_member_special_title_change_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `str` | 原头衔 |
| `new` | `str` | 现头衔 |
| `current` | `str` | 现头衔 |
| `member.qq` | `int` | 头衔改动的群员的QQ号 |
| `member.name` | `str` | 头衔改动的群员的群名片 |
| `member.permission` | `str` | 头衔改动的群员在群中的权限 |
| `member.group.id` | `int` | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |

#### 成员权限改变（该成员不是Bot）
当某群成员权限改变（该成员不是Bot）时，`on_member_permission_change_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `origin` | `str` | 原权限 |
| `new` | `str` | 现权限 |
| `current` | `str` | 现权限 |
| `member.qq` | `int` | 权限改动的群员的QQ号 |
| `member.name` | `str` | 权限改动的群员的群名片 |
| `member.permission` | `str` | 权限改动的群员在群中的权限 |
| `member.group.id` | `int` | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |

#### 群成员被禁言（该成员不是Bot）
当某群群成员被禁言（该成员不是Bot）时，`on_member_mute_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `duration_seconds` | `int` | 禁言时长，单位为秒 |
| `member.qq` | `int` | 被禁言的群员的QQ号 |
| `member.name` | `str` | 被禁言的群员的群名片 |
| `member.permission` | `str` | 被禁言的群员在群中的权限 |
| `member.group` | `Group` | 被禁言的群员所在群的信息 |
| `member.group.id` | `int` | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作者的信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`member.group` |

#### 群成员被取消禁言（该成员不是Bot）
当群成员被取消禁言（该成员不是Bot）时，`on_member_unmute_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `member.qq` | `int` | 被取消禁言的群员的QQ号 |
| `member.name` | `str` | 被取消禁言的群员的群名片 |
| `member.permission` | `str` | 被取消禁言的群员在群中的权限 |
| `member.group` | `Group` | 被取消禁言的群员所在群的信息 |
| `member.group.id` | `int` | 群号 |
| `member.group.name` | `str` | 群名 |
| `member.group.permission` | `str` | Bot在群中的权限 |
| `operator` | `Member` | 操作者的信息，当`None`时为Bot操作 |
| `operator.qq` | `int` | 操作者的QQ号 |
| `operator.name` | `str` | 操作者的群名片 |
| `operator.permission` | `str` | 操作者在群中的权限 |
| `operator.group` | `Group` | 同`member.group` |

#### 添加好友申请
当收到添加好友申请时，`on_new_friend_request_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event_id` | `int` | 事件号，响应该事件时的标识 |
| `from_qq` | `int` | 申请人QQ号 |
| `group_id` | `int` | 申请人如果通过某个群添加好友，该项为该群群号；否则为`0` |
| `nick` | `str` | 申请人的昵称或群名片 |
| `message` | `str` | 申请消息 |

#### 用户入群申请
当收到用户入群申请时，`on_member_join_request_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event_id` | `int` | 事件号，响应该事件时的标识 |
| `from_qq` | `int` | 申请人QQ号 |
| `group_id` | `int` | 申请人申请入群的群号 |
| `group_name` | `str` | 申请人申请入群的群名称 |
| `nick` | `str` | 申请人的昵称或群名片 |
| `message` | `str` | 申请消息 |

#### Bot被邀请入群申请
当Bot收到被邀请入群的申请时，`on_bot_invited_join_group_request_event(event, Conn)`将会被调用。

| 变量 | 类型 | 说明 |
| ---- | ---- | ---- |
| `event_id` | `int` | 事件号，响应该事件时的标识 |
| `from_qq` | `int` | 邀请人（好友）的QQ号 |
| `group_id` | `int` | 被邀请进入群的群号 |
| `group_name` | `str` | 被邀请进入群的群名称 |
| `nick` | `str` | 邀请人（好友）的昵称 |
| `message` | `str` | 邀请消息 |
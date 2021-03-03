# 插件开发

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
Conn类提供了对Bot进行操作的所有功能，以下只列出**能用到的方法**（具体可参见程序源码），以下所有方法返回类型为`dict`，内容为执行`POST`后得到的响应。

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


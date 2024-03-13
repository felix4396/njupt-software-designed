## 概述

本接口用于该软件系统**管理员用户**前后端之间的数据交互。

本接口中，所有请求 ( 除了登录请求之外 )，必须在cookie中携带有登录的成功后，服务端返回的sessionid。

本接口中，所有请求、响应的消息体 均采用 UTF8 编码

除了登录请求，所有的请求消息，如果有消息体，消息体都是json格式，

所有的响应消息的消息体，都是json格式。

响应消息体json 中， `ret` 字段值为 0 表示操作成功，其它值均为操作失败。

如果操作失败， 会有 `msg` 字段，内容为字符串，表示失败原因





## 管理员登录系统

### 请求消息

```
POST  /api/mgr/signin  HTTP/1.1
Content-Type:   application/x-www-form-urlencoded
```

### 请求参数

http 请求消息 body 中参数以格式 x-www-form-urlencoded 存储

需要携带如下参数，

- username

  用户名

- password

  密码

### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果登录成功，返回如下

```
{
    "ret": 0
}
```

ret 为 0 表示登录成功

如果登录失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg":  "用户名或者密码错误"
}
```

ret 不为 0 表示登录失败， msg字段描述登录失败的原因





## 管理用户数据

### 列出所有用户

#### 请求消息

```
GET  /api/mgr/user?action=list_user  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action

  填写值为 list_customer

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
    "ret": 0,
    "retlist": [
        {
            "address": "江苏省常州武进市白云街44号",
            "id": 1,
            "name": "武进市 袁腾飞",
            "password": "xxxxxx",
            "phone_number": "13886666666"
        },

        {
            "address": "北京海淀区",
            "id": 4,
            "name": "北京海淀区代理 蔡国庆",
            "password": "xxxxxx",
            "phone_number": "13990123456"
        }
    ]              
}
```

ret 为 0 表示登录成功

retlist 里面包含了所有的用户信息列表。

每个用户信息以如下格式存储

```
{
   "address": "江苏省常州武进市白云街44号",
   "id": 1,
   "name": "武进市 袁腾飞",
   "password": "xxxxxxx",
   "phonenumber": "13886666666"
}
```

### 添加一个用户

#### 请求消息

```
POST  /api/mgr/user  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加用户的信息

消息体的格式是json，如下示例：

```
{
    "action":"add_user",
    "data":{
        "name":"武汉市桥西医院",
        "password":"xxxxxxx",
        "phonenumber":"13345679934",
        "address":"武汉市桥西医院北路"
    }
}
```

其中

`action` 字段固定填写 `add_customer` 表示添加一个用户

`data` 字段中存储了要添加的用户的信息

服务端接受到该请求后，应该在系统中增加一位这样的用户。

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id 为 添加用户的id号。

如果添加失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "用户名已经存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因



### 修改用户密码（可选）

#### 请求消息

```
PUT  /api/mgr/user  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带修改用户的信息

消息体的格式是json，如下示例：

```
{
    "action":"modify_user",
    "user_name": "采样者1",
    "newdata":{
        "password":"xxxxxxx"
    }
}
```

其中

`action` 字段固定填写 `modify_user` 表示修改一个用户的密码

`id` 字段为要修改的用户的id号

`newdata` 字段中存储了修改后的用户的密码



#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果修改失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "用户名不存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因





### 删除用户信息

#### 请求消息

```
DELETE  /api/mgr/user  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除用户的user_name

消息体的格式是json，如下示例：

```
{
    "action":"del_user",
    "user_name": "采样者1"
}
```

其中

`action` 字段固定填写 `del_user` 表示删除一个用户

`user_name` 字段为要删除的用户的账号

服务端接受到该请求后，应该在系统中尝试删除该账号对应的用户。



#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果删除成功，返回如下

```
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果删除失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "账号为xxx的用户不存在"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因





### 查看用户信息

#### 请求消息

`GET  /api/mgr/user?action=get_data&user_name=xxx  HTTP/1.1`

#### 请求参数

http 请求消息 url 中需要携带如下参数，

- action

  填写值为 get_data

- user_name

  填写值为需要查看的用户名

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
	"ret": 0,
	"retlist":[
		{
			"blood_oxygen": "98",
			"user_name": "采样者1"，
			"terminal_id": "123456",
			"time_stampe": "2024.03.13.20.38"
		}，
		......
	]
}
```

ret 为 0 表示登录成功

retlist 里面包含了用户信息列表。





# 用户登录系统

### 请求消息

```
POST  /api/user/signin  HTTP/1.1
Content-Type:   application/x-www-form-urlencoded
```

### 请求参数

http 请求消息 body 中 参数以 格式 x-www-form-urlencoded 存储

需要携带如下参数，

- username

  用户名

- password

  密码

### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果登录成功，返回如下

```
{
    "ret": 0
}
```

ret 为 0 表示登录成功

如果登录失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg":  "用户名或者密码错误"
}
```

ret 不为 0 表示登录失败， msg字段描述登录失败的原因

# 用户

### 查看信息

#### 请求消息

`GET  /api/user/data?action=get_data&user_name=xxx  HTTP/1.1`

#### 请求参数

http 请求消息 url 中需要携带如下参数，

- action

  填写值为 get_data

- user_name

  填写值为需要查看的用户名

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```
{
	"ret": 0,
	"retlist":[
		{
			"blood_oxygen": "98",
			"user_name": "采样者1"，
			"terminal_id": "123456",
			"time_stampe": "2024.03.13.20.38"
		}，
		......
	]
}
```

ret 为 0 表示登录成功

retlist 里面包含了用户信息列表。

### 控制模拟端的启停

#### 请求消息

```
POST  /api/user/control  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带

消息体的格式是json，如下示例：

```
{
    "action":"start"
}
```

其中

`action` 字段固定填写 `start` 或者 `stop`

#### 响应消息

```
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果执行失败，返回失败的原因，示例如下

```
{
    "ret": 1,    
    "msg": "链接不上模拟端"
}
```

ret 不为 0 表示失败， msg字段描述添加失败的原因
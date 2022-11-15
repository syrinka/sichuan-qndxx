# 四川省青年大学习

> 由于服务端 token 过期时间[仅约两周][1]，此项目已失去了它的作用，不再更新，仅作参考

## 部署

### docker

```bash
docker run syrinka/sichuan-qndxx --name sichuan-qndxx -e USER_ID=${your_token}
```

### docker compose

```yaml
version: '3.6'

services:
  dxx:
    image: syrinka/sichuan-qndxx
    container_name: sichuan-qndxx
    environment:
      TOKEN: ${your_token}
```

### 手动调用

```bash
pip install -r requirements.txt
export token=${your_token}; python3 main.py
```

----

> 恕不提供 Github Action 部署方法

## token 获取

需要 https 抓包。

配置好环境后进入青年大学习，找到任意发往 `https://dxx.scyol.com/api/*` 的请求，请求头中即有所需的 `token`。

## 免责声明

1. 本仓库发布的项目中涉及的任何脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。
2. 本项目内所有资源文件，禁止进行任何形式的转载、发布，禁止直接改项目名二次发布。
3. 作者对任何脚本问题概不负责，包括但不限于由脚本错误或滥用导致的任何损失或损害。
4. 请勿将本项目的任何内容用于商业或非法目的，否则后果自负。
5. 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
6. 以任何方式查看此项目的人或直接或间接使用本项目的任何脚本的使用者都应仔细阅读此声明。作者保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或本项目，则视为您已接受此免责声明。

[1]: https://github.com/syrinka/sichuan-qndxx/issues/1
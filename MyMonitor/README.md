# MyMonitor
用python写的分布式监控软件  
参考zabbix架构，前端、后端、监控插件、数据优化存储等已实现 (画图功能会添加的，前端模板已经弄完了抽空传上来哈。。)


## 启动

    python3 manage.py runserver 127.0.0.1:9000  启动监控服务web端

    python3 ServerMonitor.py start  启动监控主程序

    python3 ServerMonitor.py trigger_watch  启动报警监听程序

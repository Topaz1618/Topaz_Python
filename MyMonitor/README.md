# MyMonitor
用python写的分布式监控软件 
参考zabbix架构，后端、监控插件、数据优化存储等全部自己实现 (前端、画图还在添加中。。)


## 启动

    python3 manage.py runserver 127.0.0.1:9000  启动监控服务web端

    python3 ServerMonitor.py start  启动监控主程序

    python3 ServerMonitor.py trigger_watch  启动报警监听程序

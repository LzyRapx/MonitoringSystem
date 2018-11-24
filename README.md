# Monitoring System（Just a tutorial，Only for learning）
### Command:
启动prometheus:
```
/usr/local/share/prometheus/prometheus -config.file=/usr/local/share/prometheus/prometheus.yml
```
启动node-exporter:
```
sudo systemctl start node_exporter
```
启动Grafana:
```
sudo systemctl start grafana-server
```
## prometheus架构：
![prometheus](https://github.com/LzyRapx/MonitoringSystem/blob/master/screenshot/prometheus.png)

- 1.Prometheus server 定期从配置好的 jobs 或者 exporters 中拉 metrics，或者接收来自 Pushgateway 发过来的 metrics，或者从其他的 Prometheus server 中拉 metrics。
- 2.Prometheus server 在本地存储收集到的 metrics，并运行已定义好的 alert.rules，记录新的时间序列或者向 Alertmanager 推送警报。
- 3.Alertmanager 根据配置文件，对接收到的警报进行处理，发出告警。
- 4.在图形界面中，可视化采集数据。


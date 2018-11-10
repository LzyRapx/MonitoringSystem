# Monitoring System
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


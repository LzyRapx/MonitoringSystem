### prometheus的配置：
- prometheus.yml
  - 这是prometheus-server的标准配置
- alert.rules
  - 这是告警标准的配置
- prometheus_scrape_configs.yml
  - 这是prometheus-server的扩展配置

### alertmanager的配置：
- altermanager.yml
  - 这是告警邮件，钉钉等发送方和接受方的配置

### prometheus-webhook-dingtalk
- dingtalk部署YAML.yml
  - 这是prometheus-webhook-dingtalk的一键部署文件。
  - docker镜像为：https://hub.docker.com/r/timonwong/prometheus-webhook-dingtalk/
  - 项目为：https://github.com/timonwong/prometheus-webhook-dingtalk


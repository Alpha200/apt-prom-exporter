# APT Exporter

Prometheus exporter for available apt package updates.

## Installation

Install this pip package via `pip install apt-prom-exporter`.

### Configuration

#### Systemd

The recommended way to run this prometheus exporter is via systemd: First of all, create a file with the following content at `/etc/systemd/system/apt-prom-exporter.service`:

```
[Unit]
Description=Apt prometheus exporter

[Service]
ExecStart=/usr/local/bin/apt-prom-exporter

[Install]
WantedBy=multi-user.target
```

After that, run `sudo systemctl enable --now apt-prom-exporter.service` to enable and start the service.
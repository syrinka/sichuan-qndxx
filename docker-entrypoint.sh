#!/bin/bash
export -p > /etc/cron.env

touch /var/log/dxx.log
crontab /app/crontab
cron && tail -f /var/log/dxx.log

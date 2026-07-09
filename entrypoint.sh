#!/bin/bash

set -e

## start rsyslong so /dev/log exists otherwise isc_agent will crash

rsyslogd 

## need to write dshield.ini from environment variables since isc-agent reads a config FILE not env vars

cat > /srv/dshield/etc/dshield.ini <<EOF
[DShield]
apikey=${DSHIELD_AUTHKEY}
userid=${DSHIELD_USERID}
honeypotip=172.17.0.0/16
replacehoneypotip=auto
anonymizeip=

[plugin:tcp:http]
enable_local_logs=true
local_logs_file=/srv/log/isc-agent.out
EOF


## launch isc-agent as non-root user pointed at isc_agent directory per the README

cd /srv/web
exec gosu agent python3 ./isc_agent -c /srv/dshield/etc/dshield.ini

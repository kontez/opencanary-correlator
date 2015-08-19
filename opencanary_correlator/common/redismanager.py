import redis
redis = redis.StrictRedis(host='localhost', port=6379, db='0')
redis.DEFAULT_EXPIRY = 120

KEY_LOGS                    = 'logs'
KEY_DEVICE                  = 'device:'
KEY_INCIDENTS               = 'incidents'
KEY_FTPLOGIN                = 'incident:ftplogin:'
KEY_HTTP_LOGIN              = 'incident:httplogin:'
KEY_SSH_LOGIN               = 'incident:sshlogin:'
KEY_TELNET_LOGIN            = 'incident:telnetlogin:'
KEY_HTTPPROXY_LOGIN         = 'incident:httpproxylogin:'
KEY_MYSQL_LOGIN             = 'incident:mysqllogin:'
KEY_MSSQL_LOGIN             = 'incident:mssqllogin:'
KEY_TFTP                    = 'incident:tftp:'
KEY_NTP_MON_LIST            = 'incident:ntpmonlist:'
KEY_VNC_LOGIN               = 'incident:vnclogin:'
KEY_SNMP_LOGIN              = 'incident:snmplogin:'
KEY_RDP_LOGIN               = 'incident:rdplogin:'
KEY_SIP_LOGIN               = 'incident:siplogin:'
KEY_SMB_FILE_OPEN           = 'incident:smbfileopen:'
KEY_TRACK_HOST_PORT_SCAN    = 'scan:host:'
KEY_HOST_PORT_SCAN          = 'incident:hostportscan:'
KEY_TRACK_NETWORK_PORT_SCAN = 'scan:network:'
KEY_NETWORK_PORT_SCAN       = 'incident:networkportscan:'
KEY_USER_COUNT              = 'usercount'
KEY_USER                    = 'user:'
KEY_WHITELIST_IPS           = 'whitelist-ips:'
KEY_CONSOLE_SETTING_PREFIX  = 'console-setting:'

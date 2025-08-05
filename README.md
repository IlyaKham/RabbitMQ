rabbitmqctl set_policy ha-all ".*" '{"ha-mode":"all"}'
rabbitmqctl list_policies
rabbitmqctl cluster_status
rabbitmqadmin get queue='hello'

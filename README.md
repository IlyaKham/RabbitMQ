sudo rabbitmqctl set_policy ha-all "^" '{"ha-mode":"all","ha-sync-mode":"automatic"}'
rabbitmqctl list_policies
rabbitmqctl cluster_status
rabbitmqadmin get queue='hello'

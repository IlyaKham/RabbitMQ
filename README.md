rabbitmqctl enable_feature_flag classic_mirrored_queues
rabbitmqctl set_policy ha-all ".*" '{"ha-mode":"all"}'
rabbitmqctl list_policies
rabbitmqctl cluster_status
rabbitmqadmin get queue='hello'

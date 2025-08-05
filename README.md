sudo rabbitmqctl join_cluster rabbit@rmq01
Clustering node rabbit@Vm2 with rabbit@rmq01

15:05:54.647 [error] Feature flags: error while running:
Feature flags:   rabbit_ff_controller:running_nodes[]
Feature flags: on node `rabbit@rmq01`:
Feature flags:   exception error: {erpc,noconnection}
Feature flags:     in function  erpc:call/5 (erpc.erl, line 1376)
Feature flags:     in call from rabbit_ff_controller:rpc_call/5 (src/rabbit_ff_controller.erl, line 1613)
Feature flags:     in call from rabbit_ff_controller:list_nodes_clustered_with/1 (src/rabbit_ff_controller.erl, line 570)
Feature flags:     in call from rabbit_ff_controller:check_node_compatibility_task/3 (src/rabbit_ff_controller.erl, line 433)
Feature flags:     in call from rabbit_db_cluster:can_join/1 (src/rabbit_db_cluster.erl, line 60)
Feature flags:     in call from rabbit_db_cluster:join/2 (src/rabbit_db_cluster.erl, line 92)
Feature flags:     in call from erpc:execute_call/4 (erpc.erl, line 1250)

Error:
{:aborted_feature_flags_compat_check, {:error, {:erpc, :noconnection}}}

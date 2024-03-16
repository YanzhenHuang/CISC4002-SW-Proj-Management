from activity_node_class import ActivityNode
from requirement_table import requirement

def print_graph(graph):
    for name, val in graph.items():
        val.print_node_info()


def init_graph(req):

    activity_node_name_map = {}
    activity_node_instances = []

    for activity_node_data in req.items():
        # Initialize names and durations
        cur_name = activity_node_data[0]
        cur_dur = activity_node_data[1]['DUR']
        cur_activity_node = ActivityNode(cur_name, cur_dur, [], [])

        # Stores raw nodes
        activity_node_instances.append(cur_activity_node)
        activity_node_name_map[cur_name] = cur_activity_node

    for activity_node_data in req.items():
        cur_activity_node = activity_node_name_map[activity_node_data[0]]
        cur_previous_strings = activity_node_data[1]['PREV']
        cur_previous_nodes = []
        # Insert all the corresponding post nodes to this node's prev.
        for name in cur_previous_strings:
            this_prev_node = activity_node_name_map[name]
            cur_previous_nodes.append(this_prev_node)

        # Also, for all prev nodes, insert this node to their post.
        cur_activity_node.set_prev(cur_previous_nodes)
        for node in cur_previous_nodes:
            node.insert_to_post(cur_activity_node)

    print_graph(activity_node_name_map)

    return activity_node_name_map


def forward_pass():
    graph = init_graph(requirement)

    # For start activities, initialize
    for name, node in graph:
        if node.get_predecessors() == []:
            node.set_ES(0)
            node.set_EF(node.get_ES() + node.get_dur())

    # Pass each node, update start and end
    for name, node in graph:
        earliest_finishes = [prev_node.get_EF() for prev_node in node.get_prevs()]
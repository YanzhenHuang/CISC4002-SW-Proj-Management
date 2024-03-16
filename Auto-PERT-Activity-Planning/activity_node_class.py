
class ActivityNode:
    def __init__(self, init_name, init_dur, init_prev, init_post):
        self.name = init_name
        self.early = [0, 0]
        self.late = [0, 0]
        self.dur = init_dur
        self._float = 0
        self.prev_activities = init_prev
        self.post_activities = init_post

        if not isinstance(init_prev, list) or not isinstance(init_post, list):
            raise TypeError("Previous and Post activities must be lists.")

    # Private methods
    def _update_float(self):
        self._float = self.early[1] - self.early[0]

    # Get start and finishes
    def get_name(self):
        return self.name

    def get_dur(self):
        return self.dur

    def get_ES(self):
        return self.early[0]

    def get_EF(self):
        return self.early[1]

    def get_LS(self):
        return self.late[0]

    def get_LF(self):
        return self.late[1]

    def get_prevs(self):
        return self.prev_activities

    def get_posts(self):
        return self.post_activities

    # Set start and finishes
    def set_ES(self, val):
        if val < 0:
            raise ValueError("Time can't be negative!")
        self.early[0] = val
        self._update_float()

    def set_EF(self, val):
        if val <= self.get_ES():
            raise ValueError("Earliest finish should be later than earliest start!")
        self.early[1] = val
        self._update_float()

    def set_LS(self, val):
        if val < self.get_ES():
            raise ValueError("Latest start should be later or equal to earliest start!")
        self.late[0] = val
        self._update_float()

    def set_LF(self, val):
        if val <= self.get_LF():
            raise ValueError("Latest finish should be later than latest start!")
        self.late[1] = val
        self._update_float()

    def set_prev(self, prev):
        if not isinstance(prev, list):
            raise TypeError("Prev should be a list!")
        self.prev_activities = prev

    def insert_to_post(self, node):
        if not isinstance(node, ActivityNode):
            raise TypeError("Only node should be inserted!")
        self.post_activities.append(node)


    def print_node_info(self):
        print("Name: " + self.name)
        print("ES: " + str(self.get_ES()) + " Dur: " + str(self.get_dur()) + " EF: " + str(self.get_EF()))
        print("LF: " + str(self.get_LF()) + " Flt: " + str(self._float) + " LF: " + str(self.get_LF()))

        print("Prev: ")
        for node in self.prev_activities:
            node_name = node.get_name()
            print(node_name, end=" ")
        print("")

        print("Post: ")
        for node in self.post_activities:
            node_name = node.get_name()
            print(node_name, end=" ")
        print("\n")

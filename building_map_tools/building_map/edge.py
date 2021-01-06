import math
from .param_value import ParamValue


class Edge:
    def __init__(self, yaml_node):
        self.start_idx = int(yaml_node[0])
        self.end_idx = int(yaml_node[1])
        self.params = {}
        if len(yaml_node[2]) > 0:
            for param_name, param_yaml in yaml_node[2].items():
                self.params[param_name] = ParamValue(param_yaml)

    def calc_statistics(self, vertices):
        self.x1 = vertices[self.start_idx].x
        self.y1 = vertices[self.start_idx].y
        self.x2 = vertices[self.end_idx].x
        self.y2 = vertices[self.end_idx].y
        self.dx = self.x1 - self.x2
        self.dy = self.y1 - self.y2
        self.length = math.sqrt(self.dx*self.dx + self.dy*self.dy)
        self.x = (self.x1 + self.x2) / 2.0
        self.y = (self.y1 + self.y2) / 2.0
        self.yaw = math.atan2(self.dy, self.dx)

    def is_bidirectional(self):
        if 'bidirectional' not in self.params:
            return False
        p = self.params['bidirectional']
        if p.type != ParamValue.BOOL:
            raise ValueError('expected bidirectional param to be Boolean')
        return p.value

    def orientation(self):
        if 'orientation' not in self.params:
            return None
        return self.params['orientation'].value

    def reverse_orientation(self):
        if 'orientation' not in self.params:
            return None
        if self.params['orientation'].value == 'forward':
            return 'backward'
        elif self.params['orientation'].value == 'backward':
            return 'forward'
        else:
            return ''

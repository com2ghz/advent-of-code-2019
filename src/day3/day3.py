

def main():
    with open('input.txt', 'r') as data:
        wire1 = data.readline().split(",")
        wire2 = data.readline().split(",")
        wire_walk1 = walkwire(wire1)
        wire_walk2 = walkwire(wire2)

        intersecting = calculate_intersecting(wire_walk1, wire_walk2)

        manhattan_map = calculate_manhattan(intersecting)
        shortest_distance = min(manhattan_map.values())
        print("Part 1: Shortest distance: ", shortest_distance)

        wire1_steps = calculate_step_count(intersecting, wire_walk1)
        wire2_steps = calculate_step_count(intersecting, wire_walk2)
        sums = sum_wire_steps(wire1_steps, wire2_steps)
        print("Part 2: Least steps for the first intersection:", min(sums))


def sum_wire_steps(wire1_steps, wire2_steps):
    sums = []
    for i in range(len(wire1_steps)):
        sums.append(wire1_steps[i] + wire2_steps[i])
    return sums


def calculate_step_count(intersecting, wire_walk):
    steps = []
    for point in intersecting:
        count = wire_walk.index(point) + 1
        steps.append(count)
    return steps


def calculate_manhattan(intersecting):
    distance_map = {}
    for point in intersecting:
        distance = abs(point.x) + abs(point.y)
        distance_map.update({point: distance})
    return distance_map


def calculate_intersecting(wire_walk1, wire_walk2):
    intersecting = []
    for wireone in wire_walk1:
        for wiretwo in wire_walk2:
            if wireone.x == wiretwo.x and wireone.y == wiretwo.y:
                print("Intersecting", wireone.x, wiretwo.y)
                intersecting.append(wireone)
    return intersecting


def walkwire(actions):
    wire_walk = []
    x_pos = 0
    y_pos = 0
    for action in actions:
        direction = action[0]
        steps = int(action[1::])
        for i in range(steps):
            if direction == 'R':
                x_pos = x_pos + 1
            elif direction == "L":
                x_pos = x_pos - 1
            elif direction == "U":
                y_pos = y_pos + 1
            elif direction == "D":
                y_pos = y_pos - 1
            wire_walk.append(Point(x_pos, y_pos))
    return wire_walk


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


if __name__ == '__main__':
    main()

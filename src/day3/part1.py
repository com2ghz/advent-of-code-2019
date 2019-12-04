

def main():
    with open('input.txt', 'r') as data:
        wire1 = data.readline().split(",")
        wire2 = data.readline().split(",")
        wire_walk1 = walkwire(wire1)
        wire_walk2 = walkwire(wire2)

        intersecting = calculate_intersecting(wire_walk1, wire_walk2)

        manhattan_map = calculate_manhattan(intersecting)
        shortest_distance = min(manhattan_map.values())
        print(shortest_distance)


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
            wire_walk.append(point(x_pos, y_pos))
    return wire_walk


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


if __name__ == '__main__':
    main()

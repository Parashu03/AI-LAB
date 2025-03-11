class WaterJugState:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return (self.jug1 == other.jug1 and self.jug2 == other.jug2)

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def dfs(current_state, visited, jug1_capacity, jug2_capacity, target_volume):
    if current_state.jug1 == target_volume or current_state.jug2 == target_volume:
        if current_state.jug1 == target_volume:
            print("Jug 1 now has", target_volume, "Liters")
        else:
            print("Jug 2 now has", target_volume, "Liters")
        return True

    visited.add(current_state)

    operations = [
        ('Fill jug1', jug1_capacity, current_state.jug2),
        ('Fill jug2', current_state.jug1, jug2_capacity),
        ('Empty jug1', 0, current_state.jug2),
        ('Empty jug2', current_state.jug1, 0),
        ('Pour jug1 to jug2', 
         max(0, current_state.jug1 + current_state.jug2 - jug2_capacity), 
         min(jug2_capacity, current_state.jug1 + current_state.jug2)),
        ('Pour jug2 to jug1',
         min(jug1_capacity, current_state.jug1 + current_state.jug2),
         max(0, current_state.jug1 + current_state.jug2 - jug1_capacity))
    ]

    for action, new_jug1, new_jug2 in operations:
        new_state = WaterJugState(new_jug1, new_jug2)

        if new_state not in visited:
            print(f"Trying: {action} => ({new_jug1}, {new_jug2})")

            if dfs(new_state, visited, jug1_capacity, jug2_capacity, target_volume):
                return True

    return False

def solve_water_jug_problem(jug1_capacity, jug2_capacity, target_volume):
    initial_state = WaterJugState(0, 0)
    visited = set()

    print(f"Solving water jug problem with capacities ({jug1_capacity}, {jug2_capacity}) to measure {target_volume} liters")

    if not dfs(initial_state, visited, jug1_capacity, jug2_capacity, target_volume):
        print("Solution Not Possible")

jug1_capacity = int(input("Enter the jug1_capacity: "))
jug2_capacity = int(input("Enter the jug2_capacity: "))
target_volume = int(input("Enter the target_volume: "))

solve_water_jug_problem(jug1_capacity, jug2_capacity, target_volume)

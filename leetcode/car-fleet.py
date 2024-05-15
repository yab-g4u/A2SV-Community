class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its index and sort the pairs in ascending order of positions
        car_indices_sorted_by_position = sorted(range(len(position)), key=lambda idx: position[idx])

        # Initialize the count of car fleets and the time of the previously counted fleet
        fleet_count = 0
        previous_time = 0

        # Iterate over the cars from the one closest to the target to the furthest
        for i in car_indices_sorted_by_position[::-1]: # Reverse iteration
            # Calculate the time needed for the current car to reach the target
            time_to_reach_target = (target - position[i]) / speed[i]
            # If this time is greater than the time of the previously counted fleet,
            # it means this car cannot catch up with that fleet and forms a new fleet.
            if time_to_reach_target > previous_time:
                fleet_count += 1 # Increment fleet count
                previous_time = time_to_reach_target # Update the time of the last fleet

        # Return the total number of fleets
        return fleet_count

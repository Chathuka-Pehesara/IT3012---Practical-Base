from collections import deque
import random
import heapq

# agent.py
class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # If standing directly on food, or just wander / move towards coordinates
        pos = percept['agent_pos']
        # Simple heuristic or fallback random sweep
        return random.choice(self.actions_pool)

class SearchAgent:

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']
    
    def bfs_search(self, start_state, goal_state, get_successors):
        frontier = deque([(start_state, [])]) # here queue store state and path
        reached = set([start_state]) # this will track explored states

        while frontier: # while queue is not empty
            current_state, current_path = frontier.popleft() # get the first element

            if current_state == goal_state:
                return current_path # if goal is reached, return the path

            for action, successor in get_successors(current_state):
                if successor not in reached:
                    reached.add(successor)
                    frontier.append((successor, current_path + [action]))
        
        return []

    
    def dfs_search(self, start_state, goal_state, get_successors):
        frontier = [(start_state, [])] # Stack stores (state, path)
        reached = set()                # Track explored states (added when popped)
        while frontier:
            current_state, path = frontier.pop() # LIFO Stack
            if current_state == goal_state:
                return path
            
            if current_state not in reached:
                reached.add(current_state)
                for action, successor in get_successors(current_state):
                    if successor not in reached:
                        frontier.append((successor, path + [action]))
        return []
        
    def ucs_search(self, start_state, goal_state, get_successors, cost_function):
        frontier = []
        heapq.heappush(frontier, (0, id(start_state), start_state, [])) 
        
        reached = {start_state: 0} 
        while frontier:
            current_cost, _, current_state, path = heapq.heappop(frontier)
            if current_state == goal_state:
                return path
            for action, successor, step_cost in get_successors(current_state):
                new_cost = current_cost + step_cost
                
                if successor not in reached or new_cost < reached[successor]:
                    reached[successor] = new_cost
                    heapq.heappush(frontier, (new_cost, id(successor), successor, path + [action]))
                    
        return []
            



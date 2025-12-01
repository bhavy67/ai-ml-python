# Taking the input
num_tasks = int(input())
num_team_members = int(input())

def assign_tasks(num_tasks, num_team_members):
    if num_tasks == 0 or num_team_members == 0:
        return 0
    
    r = min(num_tasks, num_team_members)
    
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    arrangements = factorial(num_tasks) / factorial(num_tasks - r)
    return float(arrangements)

# Print the output
print(assign_tasks(num_tasks, num_team_members))
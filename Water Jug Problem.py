from collections import deque
def waterJug(capacities,targetJug,targetAmount):
    n=len(capacities)
    start=tuple([0]*n)
    queue=deque([(start,[start])])
    visited=set()
    while queue:
        state,path=queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state[targetJug]==targetAmount:
            print("\nSolution Path:")
            for step in path:
                print(step)
            print("\nGoal Achieved")
            print("Jug",targetJug+1,"contains",targetAmount,"litres.")
            return
        for i in range(n):
            newState=list(state)
            newState[i]=capacities[i]
            newState=tuple(newState)
            if newState not in visited:
                queue.append((newState,path+[newState]))
        for i in range(n):
            newState=list(state)
            newState[i]=0
            newState=tuple(newState)
            if newState not in visited:
                queue.append((newState,path+[newState]))
        for i in range(n):
            for j in range(n):
                if i!=j:
                    newState=list(state)
                    transfer=min(state[i],capacities[j]-state[j])
                    newState[i]-=transfer
                    newState[j]+=transfer
                    newState=tuple(newState)
                    if newState not in visited:
                        queue.append((newState,path+[newState]))
    print("No solution possible.")

n=int(input("Enter number of jugs: "))
capacities=[]
for i in range(n):
    capacities.append(int(input(f"Enter capacity of Jug {i+1}: ")))
targetJug=int(input("\nEnter target jug number: "))-1
targetAmount=int(input("Enter target amount: "))
waterJug(capacities,targetJug,targetAmount)

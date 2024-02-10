N = int(input())
votes = {}
for i in range(N):
    name = input()
    votes[name] = votes.get(name, 0) + 1;
elected_person = max(votes, key=votes.get)
print(elected_person)

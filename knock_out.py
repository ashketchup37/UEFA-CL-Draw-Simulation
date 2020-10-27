print("Welcome to this years edition of UEFA Champions League.")
print("The best 16 teams have qualified for the Round of 16.")
print("\n\nRules:\n\t1. No group winners will face other group winners in the round of 16.")
print("\t2. No teams will face another team from the same group or same association.")
print("\n")
print("So Let's begin.\n")
print("You'll be asked about the group winners and runners up. Please follow the given format")
print("FC Barcelona(ESP)    Atalanta(ITA)   Bayern(GER)    Liverpool(ENG)")
group_winner = []
group_runner_up = []
group_name = "ABCDEFGH"
for i in range(8):
    winner = input("The winner of group " + group_name[i] + " is: ")
    runner_up = input("The runner up of group " + group_name[i] + " is: ")
    group_winner.append(winner)
    group_runner_up.append(runner_up)


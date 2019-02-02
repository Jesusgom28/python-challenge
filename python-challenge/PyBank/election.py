import os 
import csv

electioncsv = os.path.join('..', 'resources', 'election_data.csv')

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

with open (electioncsv,newline="") as elections:
    csvreader = csv.reader(elections,delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_votes +=1
        if row[2] == "Khan":
            Khan_votes +=1
        elif row[2] == "Correy":
            Correy_votes +=1
        elif row [2] == "Li":
            Li_votes +=1
        elif row[2] == "O'Tooley":
            Otooley_votes +=1

dict_candidates_and_votes = dict(zip(candidates,votes))
        key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

Khan_percent = (Khan_votes/total_votes) * 100
Correy_percent = (Correy_votes/total_votes) * 100
Li_percent = (Li_votes/total_votes) * 100
Otooley_percent = (Otooley_votes/total_votes) * 100

print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------")
print(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
print(f"Li: {Li_percent:.3f}% ({Li_votes})")
print(f"O'Tooley: {Otooley_percent:.3f}% ({)tooley_votes})")
print(f"------------------------")
print(f"Winner: {key}")
print(f"------------------------")

output_file = Path("Python-Challenge", "PyPoll", "election_results.txt")

with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"------------------------")
    file.write("\n")
    file.write(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
    file.write("\n")
    file.write(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
    file.write("\n")
    file.write(f"Li: {Li_percent:.3f}% ({Li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_votes})")
    file.write("\n")
    file.write(f"------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"------------------------")


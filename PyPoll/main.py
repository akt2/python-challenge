import os
import csv

csvpath=os.path.join('election_data.csv')

with open(csvpath,newline='') as file:
    election=csv.reader(file,delimiter=',')
    # print(election)
    header=next(election)
    # print(header)
    rows=[]
    vid=[]
    county=[]
    cand=[]
    for row in election:
        # print(row)
        rows.append(row)
        vid.append(row[0])
        county.append(row[1])
        cand.append(row[2])

# The total number of votes cast
# print(len(vid))
total_votes=len(vid)

# A complete list of candidates who received votes
candlist=[]
for x in cand:
    if x not in candlist:
        candlist.append(x)
# print(candlist)
# print(candlist[0])

# The percentage of votes each candidate won
# The total number of votes each candidate won
khancount=cand.count(candlist[0])
correycount=cand.count(candlist[1])
licount=cand.count(candlist[2])
otooleycount=cand.count(candlist[3])
khanper=round((100*(khancount/total_votes)),5)
correyper=round((100*(correycount/total_votes)),5)
liper=round((100*(licount/total_votes)),5)
otooleyper=round((100*(otooleycount/total_votes)),5)

# The winner of the election based on popular vote.
counts=[khancount,correycount,licount,otooleycount]
counts.sort(reverse=True)
# print(counts)
if counts[0]>counts[1]:
    if counts[0]>counts[2]:
        if counts[0]>counts[3]:
            print(candlist[0])
elif counts[1]>counts[2]:
    if counts [1]>counts[3]:
        print(candlist[1])
elif counts[2]>counts[3]:
    print(candlist[2])
else:
    print(candlist[3])
# OR much more simply:
for x in candlist:
    if counts[0]==cand.count(x):
        winnerx=x
# print(winnerx)
# OR
for y in candlist:
    if max(counts)==cand.count(y):
        winnery=y
# print(winnery)

cands=[]
m=0
for w in candlist:
    for m in range(len(counts)):
        if counts[m]==cand.count(w):
            cands.append(w)
# print(cands)

# Anyways...
# my variables shouldn't be attached to candidate names, but I have to move on.
print('Election Results\n----------------------------')
print(f'Total Votes: {total_votes}\n----------------------------')
print(f'{cands[0]}: {khanper}% ({khancount})\n{cands[1]}: {correyper}% ({correycount})')
print(f'{cands[2]}: {liper}% ({licount})\n{cands[3]}: {otooleyper}% ({otooleycount})')
print(f'----------------------------\nWinner: {winnery}\n----------------------------')

txtfile=open('PyPoll.txt','w')
txtfile.write('Election Results\n----------------------------')
txtfile.write(f'\nTotal Votes: {total_votes}\n----------------------------')
txtfile.write(f'\n{cands[0]}: {khanper}% ({khancount})\n{cands[1]}: {correyper}% ({correycount})')
txtfile.write(f'\n{cands[2]}: {liper}% ({licount})\n{cands[3]}: {otooleyper}% ({otooleycount})')
txtfile.write(f'\n----------------------------\nWinner: {winnery}\n----------------------------')
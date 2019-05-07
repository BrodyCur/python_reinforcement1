doc = "David Lynch: The Art Life"
comedy = "Sorry to Bother You"
drama = "Phantom Thread"
dramedy = "The Disaster Artist"

print("Do you like Documentaries?")
doc_answer = input().lower()

if doc_answer == 'yes':
    print(f"check out {doc}")
else:
    pass

print("Do you like Comedies?")
com_answer = input().lower()

if com_answer == 'yes':
    print(f"You might like {comedy} then!")
else:
    pass

print("Do you like Dramas?")
dram_answer = input().lower()

if dram_answer == 'yes' and com_answer == 'no':
    print(f"How about {drama}?")
elif dram_answer == 'yes' and com_answer == 'yes':
    print(f"Oh, what about {dramedy}?")
else:
    print("How bout a good book instead?")
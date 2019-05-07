doc = "David Lynch: The Art Life"
comedy = "Sorry to Bother You"
drama = "Phantom Thread"
dramedy = "The Disaster Artist"


print('Please rate the following on a scale of 1-5.')
print('Documentaries')
doc_answer = int(input())
print('Comedies')
com_answer = int(input())
print('Dramas')
dram_answer = int(input())

if doc_answer >= 4 and doc_answer > com_answer and doc_answer > dram_answer:
    print(f"check out {doc}")
elif com_answer >= 4 and com_answer > doc_answer and com_answer > dram_answer:
    print(f"You might like {comedy} then!")
elif dram_answer >= 4 and dram_answer > doc_answer and dram_answer > com_answer:
    print(f"How about {drama}?")
elif dram_answer >= 4 and com_answer >= 4:
    print(f"Oh, what about {dramedy}?")
elif doc_answer and com_answer and dram_answer <= 3:
    print("How bout a good book instead?")
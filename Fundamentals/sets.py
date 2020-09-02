art_friends = {"Rolf", "Anne", "Mesut"}

art_friends.add("Rob");
print(art_friends)

art_friends.remove("Anne");
print(art_friends)

science_friends = {"Jen", "Laca", "Rolf"}

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

all_friends = art_friends.union(science_friends)
print(all_friends)
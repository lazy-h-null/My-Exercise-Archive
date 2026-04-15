# ============================================================
# Python Dictionary Methods — 10 Beginner Challenges
# Practice each one before reading the hint!
# Hints are at the bottom of the file.
# ============================================================


# --------------------------------------------------------------
# Challenge 1 — Build a Profile
# Create a dictionary for a person with keys "name", "age",
# and "city", then print each value using get().
# Method: get()
# --------------------------------------------------------------

profile = {}
# your code here
profile = {
    "name" : "Bob",
    "age" : 25,
    "city" : "vancouver"
}

print(profile.get("name"))
print(profile.get("age"))
print(profile.get("city"))


# --------------------------------------------------------------
# Challenge 2 — Safe Access
# Retrieve "email" safely — it doesn't exist, so return
# "not provided" as the default instead.
# Method: get()
# --------------------------------------------------------------

user = {"name": "Bob", "age": 25}
# your code here

u_email = user.get("email", "not provided")
print(u_email)

# --------------------------------------------------------------
# Challenge 3 — Update the Record
# Update "age" to 26 and add a new key "job" with value "Dev",
# both in a single call. Then print the updated dict.
# Method: update()
# --------------------------------------------------------------

record = {"name": "Bob", "age": 25}
# your code here
record.update(age=26, job="Dev")
print(record)


# --------------------------------------------------------------
# Challenge 4 — Set Only If Missing
# Set "theme" to "light" only if it doesn't already exist,
# then try to overwrite "lang" — it should NOT change.
# Method: setdefault()
# --------------------------------------------------------------

config = {"lang": "en", "debug": False}
# your code here
config.setdefault("theme", "light")
config.setdefault("lang", "ko")
print(config)

# --------------------------------------------------------------
# Challenge 5 — Remove and Reuse
# Pop "city" from the dict, store its value in a variable,
# then print both the removed value and the remaining dict.
# Method: pop()
# --------------------------------------------------------------

employee = {"name": "Alice", "age": 30, "city": "Toronto"}
# your code here
remove_employee = employee.pop("city")
print(remove_employee)
print(employee)

# --------------------------------------------------------------
# Challenge 6 — Inspect the Dictionary
# Print all keys, all values, and all key-value pairs of the
# dict below using the three view methods.
# Methods: keys(), values(), items()
# --------------------------------------------------------------

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
# your code here
print(inventory.keys())
print(inventory.values())
print(inventory.items())


# --------------------------------------------------------------
# Challenge 7 — Merge Preferences
# Merge defaults and user_prefs so that user_prefs values win
# on conflict. Store the result in a new dict called "final".
# Method: | operator (Python 3.9+) or {**a, **b}
# --------------------------------------------------------------

defaults   = {"theme": "light", "lang": "en", "debug": False}
user_prefs = {"theme": "dark", "lang": "fr"}
# your code here
final = defaults | user_prefs
print(final)


# --------------------------------------------------------------
# Challenge 8 — Initialize from a List
# Create a dict where each subject is a key and its default
# grade value is 0.
# Method: dict.fromkeys()
# --------------------------------------------------------------

subjects = ["math", "science", "history", "art"]
# your code here
init_subjects = dict.fromkeys(subjects, 0)
print(init_subjects)

# --------------------------------------------------------------
# Challenge 9 — Count Word Frequency
# Count how many times each word appears in the list below.
# Build the result dict using get() inside a loop.
# Method: get()
# --------------------------------------------------------------

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}
# your code here
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

# --------------------------------------------------------------
# Challenge 10 — Sort by Value
# Sort the scores dict by score from highest to lowest and
# rebuild it as a new sorted dict. Print the final result.
# Method: sorted() with key + dict()
# --------------------------------------------------------------

scores = {"Bob": 88, "Alice": 95, "Charlie": 72, "Diana": 90}
# your code here
sorted_items = sorted(scores.items(), key=lambda item: item[1], reverse=True)
sorted_scores = dict(sorted_items)
print(sorted_scores)


# ============================================================
# BONUS TIPS
# - Use get() over direct access [] when a key might be absent.
# - dict views (keys/values/items) are dynamic — they reflect
#   changes to the dict automatically.
# - dict.fromkeys() with a mutable default (like []) is tricky:
#   all keys share the SAME object. Use a comprehension instead:
#   {k: [] for k in keys}
# ============================================================


# ============================================================
# HINTS — try to solve each challenge before reading these!
# ============================================================

# Challenge 1:  get(key) returns None if missing; get(key, default) returns the fallback value.

# Challenge 2:  Pass a second argument to get() as the fallback: get("email", "not provided").

# Challenge 3:  update() accepts a dict or keyword arguments; both can be combined.

# Challenge 4:  setdefault() does nothing if the key already exists — it never overwrites.

# Challenge 5:  pop() returns the removed value; use pop(key, default) to avoid KeyError.

# Challenge 6:  Use a for loop with items() to unpack key and value in the same iteration.

# Challenge 7:  The right-hand side wins when both dicts share a key: defaults | user_prefs.

# Challenge 8:  fromkeys(iterable, value) sets the same default value for every key.

# Challenge 9:  count.get(word, 0) + 1 is the classic frequency-counting pattern.

# Challenge 10: Sort items() by the second element of each tuple: key=lambda item: item[1].

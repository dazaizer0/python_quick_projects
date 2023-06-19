import random
import time

import matplotlib.pyplot as plt


def average(tab):
    suma = sum(tab)
    tab_len = len(tab)
    to_ret = suma / tab_len
    return to_ret


results = []
max_range = 6
repeats = 5000

start_time = time.time()
while len(results) != repeats:

    los_nrs = random.choices(range(1, max_range), k=6)
    to_los_nrs = random.choices(range(1, max_range), k=6)
    counter = 0

    while sorted(to_los_nrs) != sorted(los_nrs):
        print(len(results), " <<<<", counter, " << ", los_nrs, " --- ", to_los_nrs)
        to_los_nrs = random.choices(range(1, max_range), k=6)
        counter += 1

    print(counter, "finish << results: ", los_nrs, "==", to_los_nrs)
    results.append(counter)

    counter = 0
    los_nrs.clear()
    to_los_nrs.clear()

print("> in_result: 1-", max_range, ":: ", average(results), "t.rials")

end_time = time.time()
print("> program time duration:: ", end_time - start_time)

# GRAF
fig, ax = plt.subplots()
ax.plot(range(1, repeats + 1), results, label="results")

text = "> data << results: {r}, max_range: {mr}, repeats: {rp}".format(r=results, mr=max_range, rp=repeats)
text2 = "After how many votes cast, you could probably win: {sr}".format(sr=average(results))

ax.text(0.5, 0.5, text2, ha='left', va='top', fontsize=8, color='red')
ax.set_title('average(results)')

# window settings
ax.set_title(text, fontsize=8)
ax.set_ylabel(repeats)

# start
ax.legend()
plt.show()

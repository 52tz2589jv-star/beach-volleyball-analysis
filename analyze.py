import pandas as pd
from scipy import stats

df = pd.read_csv("data.csv", encoding="latin-1", low_memory=False)

print(df.shape)
print(df.head())
print(df.info())

stats_columns = [
    "w_p1_tot_hitpct", "w_p2_tot_hitpct", "l_p1_tot_hitpct", "l_p2_tot_hitpct",
    "w_p1_tot_errors", "w_p2_tot_errors", "l_p1_tot_errors", "l_p2_tot_errors"
]
df_with_stats = df.dropna(subset=stats_columns)
print(df_with_stats.shape)

df_with_stats["w_team_hitpct"] = df_with_stats[["w_p1_tot_hitpct", "w_p2_tot_hitpct"]].mean(axis=1)
df_with_stats["l_team_hitpct"] = df_with_stats[["l_p1_tot_hitpct", "l_p2_tot_hitpct"]].mean(axis=1)
print(df_with_stats["w_team_hitpct"].mean())
print(df_with_stats["l_team_hitpct"].mean())

winner_hitpct = df_with_stats["w_team_hitpct"]
loser_hitpct = df_with_stats["l_team_hitpct"]
hitpct_test = stats.ttest_ind(winner_hitpct, loser_hitpct)
print(hitpct_test)

df_with_stats["w_team_kills"] = df_with_stats[["w_p1_tot_kills", "w_p2_tot_kills"]].mean(axis=1)
df_with_stats["l_team_kills"] = df_with_stats[["l_p1_tot_kills", "l_p2_tot_kills"]].mean(axis=1)
print(df_with_stats["w_team_kills"].mean())
print(df_with_stats["l_team_kills"].mean())

winner_kills = df_with_stats["w_team_kills"]
loser_kills = df_with_stats["l_team_kills"]
kills_test = stats.ttest_ind(winner_kills, loser_kills)
print(kills_test)

df_with_stats["w_team_digs"] = df_with_stats[["w_p1_tot_digs", "w_p2_tot_digs"]].mean(axis=1)
df_with_stats["l_team_digs"] = df_with_stats[["l_p1_tot_digs", "l_p2_tot_digs"]].mean(axis=1)
print(df_with_stats["w_team_digs"].mean())
print(df_with_stats["l_team_digs"].mean())

winner_digs = df_with_stats["w_team_digs"]
loser_digs = df_with_stats["l_team_digs"]
digs_test = stats.ttest_ind(winner_digs, loser_digs)
print(digs_test)

df_with_stats["w_team_blocks"] = df_with_stats[["w_p1_tot_blocks", "w_p2_tot_blocks"]].mean(axis=1)
df_with_stats["l_team_blocks"] = df_with_stats[["l_p1_tot_blocks", "l_p2_tot_blocks"]].mean(axis=1)
print(df_with_stats["w_team_blocks"].mean())
print(df_with_stats["l_team_blocks"].mean())

winner_blocks = df_with_stats["w_team_blocks"]
loser_blocks = df_with_stats["l_team_blocks"]
blocks_test = stats.ttest_ind(winner_blocks, loser_blocks)
print(blocks_test)

df_with_stats["w_team_aces"] = df_with_stats[["w_p1_tot_aces", "w_p2_tot_aces"]].mean(axis=1)
df_with_stats["l_team_aces"] = df_with_stats[["l_p1_tot_aces", "l_p2_tot_aces"]].mean(axis=1)
print(df_with_stats["w_team_aces"].mean())
print(df_with_stats["l_team_aces"].mean())

winner_aces = df_with_stats["w_team_aces"]
loser_aces = df_with_stats["l_team_aces"]
aces_test = stats.ttest_ind(winner_aces, loser_aces)
print(aces_test)

df_with_stats["w_team_errors"] = df_with_stats[["w_p1_tot_errors", "w_p2_tot_errors"]].mean(axis=1)
df_with_stats["l_team_errors"] = df_with_stats[["l_p1_tot_errors", "l_p2_tot_errors"]].mean(axis=1)
print(df_with_stats["w_team_errors"].mean())
print(df_with_stats["l_team_errors"].mean())

winner_errors = df_with_stats["w_team_errors"]
loser_errors = df_with_stats["l_team_errors"]
errors_test = stats.ttest_ind(winner_errors, loser_errors)
print(errors_test)

import matplotlib.pyplot as plt

stat_names = ["Kills", "Digs", "Blocks", "Aces", "Errors"]
winner_counts = [df_with_stats["w_team_kills"].mean(), df_with_stats["w_team_digs"].mean(), df_with_stats["w_team_blocks"].mean(), df_with_stats["w_team_aces"].mean(), df_with_stats["w_team_errors"].mean()]
loser_counts = [df_with_stats["l_team_kills"].mean(), df_with_stats["l_team_digs"].mean(), df_with_stats["l_team_blocks"].mean(), df_with_stats["l_team_aces"].mean(), df_with_stats["l_team_errors"].mean()]

x = range(len(stat_names))
plt.bar([i - 0.2 for i in x], winner_counts, width=0.4, label="Winners")
plt.bar([i + 0.2 for i in x], loser_counts, width=0.4, label="Losers")
plt.xticks(x, stat_names)
plt.legend()
plt.title("Winner vs Loser Stats (Beach Volleyball)")
plt.savefig("winner_vs_loser_chart.png")

plt.figure()
plt.bar(["Winners", "Losers"], [df_with_stats["w_team_hitpct"].mean(), df_with_stats["l_team_hitpct"].mean()])
plt.title("Winner vs Loser Hitting Percentage")
plt.savefig("hitpct_chart.png")

import numpy as np
all_hitpct = pd.concat([winner_hitpct, loser_hitpct]).reset_index(drop=True)
won = pd.concat([pd.Series(np.ones(len(winner_hitpct))), pd.Series(np.zeros(len(loser_hitpct)))]).reset_index(drop=True)
correlation_hitpct = all_hitpct.corr(won)
print("correlation_hitpct:", correlation_hitpct)

all_kills = pd.concat([winner_kills, loser_kills]).reset_index(drop=True)
won = pd.concat([pd.Series(np.ones(len(winner_kills))), pd.Series(np.zeros(len(loser_kills)))]).reset_index(drop=True)
correlation_kills = all_kills.corr(won)
print("correlation_kills:", correlation_kills)

all_digs = pd.concat([winner_digs, loser_digs]).reset_index(drop=True)
won = pd.concat([pd.Series(np.ones(len(winner_digs))), pd.Series(np.zeros(len(loser_digs)))]).reset_index(drop=True)
correlation_digs = all_digs.corr(won)
print("correlation_digs:", correlation_digs)

all_blocks = pd.concat([winner_blocks, loser_blocks]).reset_index(drop=True)
won = pd.concat([pd.Series(np.ones(len(winner_blocks))), pd.Series(np.zeros(len(loser_blocks)))]).reset_index(drop=True)
correlation_blocks = all_blocks.corr(won)
print("correlation_blocks:", correlation_blocks)

all_aces = pd.concat([winner_aces, loser_aces]).reset_index(drop=True)
won = pd.concat([pd.Series(np.ones(len(winner_aces))), pd.Series(np.zeros(len(loser_aces)))]).reset_index(drop=True)
correlation_aces = all_aces.corr(won)
print("correlation_aces:", correlation_aces)

all_errors = pd.concat([winner_errors, loser_errors]).reset_index(drop=True)
won = pd.concat([pd.Series(np.ones(len(winner_errors))), pd.Series(np.zeros(len(loser_errors)))]).reset_index(drop=True)
correlation_errors = all_errors.corr(won)
print("correlation_errors:", correlation_errors)
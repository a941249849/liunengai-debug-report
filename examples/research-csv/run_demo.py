from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

source = Path("example.csv")
if not source.is_file():
    raise FileNotFoundError("Open the notebook from the folder containing example.csv.")
raw = pd.read_csv(source, dtype=str, keep_default_na=False)
required = {"sample_id", "group", "signal"}
if not required.issubset(raw.columns):
    raise ValueError("CSV must contain sample_id, group and signal columns.")
if raw["sample_id"].eq("").any() or raw["sample_id"].duplicated().any():
    raise ValueError("Sample IDs must be present and unique.")
if not raw["group"].isin(["control", "treatment"]).all():
    raise ValueError("Unknown or missing group: check the input before analysis.")
values = pd.to_numeric(raw["signal"], errors="coerce")
# Only the two documented missing markers are accepted; stop on unexpected text.
known_missing = raw["signal"].isin(["", "not_measured"])
if (values.isna() & ~known_missing).any():
    raise ValueError("Unexpected non-numeric signal: check the source data.")
if values.isin([float("inf"), -float("inf")]).any():
    raise ValueError("Signal must be finite.")
clean = raw.assign(signal=values)
excluded = clean.loc[known_missing, ["sample_id", "group"]].copy()
excluded["reason"] = "signal_missing"
valid = clean.loc[~known_missing].copy()
summary = valid.groupby("group")["signal"].agg(n="count", mean="mean").reindex(["control", "treatment"])
if summary["n"].isna().any() or summary["n"].eq(0).any():
    raise ValueError("Each group needs at least one valid observation.")
assert len(raw) == len(valid) + len(excluded)
print(f"Input={len(raw)}; included={len(valid)}; excluded={len(excluded)}")
print(summary.to_string())
print("Excluded rows:\n" + excluded.to_string(index=False))
summary.to_csv("summary.csv")
excluded.to_csv("excluded.csv", index=False)
fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)
for x, group in enumerate(summary.index):
    ys = valid.loc[valid["group"].eq(group), "signal"].to_numpy()
    offsets = [(i - (len(ys)-1)/2)*0.08 for i in range(len(ys))]
    ax.scatter([x+v for v in offsets], ys, color="#2563eb", label="Observed" if x == 0 else None)
    ax.hlines(summary.loc[group, "mean"], x-.2, x+.2, colors="#0f172a", label="Mean" if x == 0 else None)
ax.set_xticks([0, 1], [f"{g} (n={int(summary.loc[g, 'n'])})" for g in summary.index])
ax.set_ylabel("Signal (arbitrary units)")
ax.set_title("Synthetic data: observations and means")
ax.legend(frameon=False)
fig.savefig("result.png", dpi=160)
plt.close(fig)

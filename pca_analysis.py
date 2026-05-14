import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Load files
# -----------------------------
class_data = pd.read_csv("data/class.tsv", sep="\t", header=None)

gene_data = pd.read_csv("data/filtered.tsv.gz", sep="\t")
gene_data.columns = gene_data.columns.astype(str).str.strip()

columns_data = pd.read_csv(
    "data/columns.tsv.gz",
    sep="\t",
    comment="#",
    header=None,
    engine="python"
)

# Flatten class labels
labels = class_data.iloc[:, 0].values

# -----------------------------
# Find gene IDs
# -----------------------------
columns_data[1] = columns_data[1].astype(str).str.strip()

xbp1_row = columns_data[
    columns_data.astype(str).apply(
        lambda row: row.str.contains("XBP1", case=False, na=False).any(),
        axis=1
    )
]

gata3_row = columns_data[
    columns_data.astype(str).apply(
        lambda row: row.str.contains("GATA3", case=False, na=False).any(),
        axis=1
    )
]

if xbp1_row.empty:
    raise ValueError("XBP1 not found")

if gata3_row.empty:
    raise ValueError("GATA3 not found")

xbp1_id = str(xbp1_row.iloc[0, 0])
gata3_id = str(gata3_row.iloc[0, 0])

print("XBP1 ID:", xbp1_id)
print("GATA3 ID:", gata3_id)

# -----------------------------
# Extract gene expressions
# -----------------------------
print("Available columns sample:")
print(gene_data.columns[:20])

xbp1 = gene_data[str(xbp1_id)]
gata3 = gene_data[str(gata3_id)]

# -----------------------------
# Figure 1a
# -----------------------------
plt.figure(figsize=(10, 7))

for label, color, name in zip(
    [0, 1],
    ['red', 'blue'],
    ['ER-', 'ER+']
):
    idx = labels == label
    plt.scatter(
        gata3[idx],
        xbp1[idx],
        c=color,
        label=name,
        alpha=0.7
    )

plt.xlabel("GATA3 Expression")
plt.ylabel("XBP1 Expression")
plt.title("Figure 1a: XBP1 vs GATA3")
plt.legend()
plt.grid(True)

plt.show()
plt.close()

# -----------------------------
# PCA
# -----------------------------
scaled = StandardScaler().fit_transform(gene_data)

pca = PCA(n_components=2)
pc = pca.fit_transform(scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)

# -----------------------------
# Figure 1c
# -----------------------------
plt.figure(figsize=(10, 7))

for label, color, name in zip(
    [0, 1],
    ['red', 'blue'],
    ['ER-', 'ER+']
):
    idx = labels == label
    plt.scatter(
        pc[idx, 0],
        pc[idx, 1],
        c=color,
        label=name,
        alpha=0.7
    )

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Figure 1c: PCA Projection")
plt.legend()
plt.grid(True)

plt.show()
plt.close()

print("Analysis completed successfully.")
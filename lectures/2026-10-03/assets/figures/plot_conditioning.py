"""Reproduce the supplemental conditioning plot for the 2026-10-03 notes."""

from pathlib import Path
from math import gcd
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    out = Path(__file__).resolve().parent
    size = 720
    frequencies = np.arange(1, size)
    rows = []
    for length in range(1, 61):
        invertible = gcd(size, length) == 1
        condition = None
        if invertible:
            # The omitted zero frequency has eigenvalue exactly one.
            magnitudes = np.abs(
                np.sin(np.pi * length * frequencies / size)
                / (length * np.sin(np.pi * frequencies / size))
            )
            condition = 1.0 / min(1.0, float(magnitudes.min()))
        rows.append((size, length, invertible, condition))

    with (out / "conditioning.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["N", "k", "invertible", "condition_2"])
        writer.writerows(rows)

    xs = [row[1] for row in rows if row[2]]
    ys = [row[3] for row in rows if row[2]]
    plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 10})
    fig, ax = plt.subplots(figsize=(6.6, 2.9), layout="constrained")
    ax.scatter(xs, ys, color="#244c76", s=21, zorder=3)
    ax.set_xlabel("Длина целочисленного смаза $k$")
    ax.set_ylabel(r"$\mathrm{cond}_2(S)$")
    ax.set_title(r"$N=720$, $\gcd(N,k)=1$")
    ax.set_xlim(0, 61)
    ax.set_ylim(bottom=0)
    ax.grid(color="#dddddd", linewidth=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(out / "conditioning.pdf")
    fig.savefig(out / "conditioning.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main()

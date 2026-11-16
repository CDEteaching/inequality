import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
out = sys.argv[1]
INK="#222322"; INK2="#6B685F"; GRID="#D8D5CE"; OLIVE="#869E2F"; PURPLE="#9E6CB4"; NAVY="#003A70"
plt.rcParams.update({"font.family":"Arial","font.size":11})
# Illustrative decile income shares (%), not real data
A = np.array([3,4,5,6,8,9,11,13,16,25])      # more equal society
B = np.array([1,2,3,4,5,6,8,11,17,43])       # more unequal society
def lorenz(s): c=np.cumsum(s)/s.sum(); return np.r_[0,np.arange(1,11)/10], np.r_[0,c]
def gini(s):
    x,y=lorenz(s); return 1-np.sum((x[1:]-x[:-1])*(y[1:]+y[:-1]))
def palma(s): return s[9]/s[:4].sum()
fig,ax=plt.subplots(figsize=(7,5.6),dpi=300)
ax.plot([0,1],[0,1],color=INK2,lw=1.2,ls="--")
xa,ya=lorenz(A); xb,yb=lorenz(B)
ax.fill_between(xb,xb,yb,color=PURPLE,alpha=0.15,lw=0)
ax.plot(xa,ya,color=OLIVE,lw=2.5,marker="o",ms=4)
ax.plot(xb,yb,color=PURPLE,lw=2.5,marker="o",ms=4)
ax.text(0.27,0.31,"Line of perfect equality",rotation=38,color=INK2,fontsize=10,ha="center")
ax.annotate(f"Society A\nGini {gini(A):.2f}, Palma {palma(A):.1f}",xy=(0.6,0.35),xytext=(0.04,0.72),color=OLIVE,fontsize=10,fontweight="bold",arrowprops=dict(arrowstyle="->",color=OLIVE,lw=1.2))
ax.text(0.80,0.17,f"Society B\nGini {gini(B):.2f}, Palma {palma(B):.1f}",color=PURPLE,fontsize=10,fontweight="bold",ha="center")
ax.text(0.46,0.35,"area A\n(for B)",color=PURPLE,fontsize=9,ha="center")
ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.set_xticks(np.arange(0,1.01,0.2)); ax.set_yticks(np.arange(0,1.01,0.2))
ax.set_xticklabels([f"{int(v*100)}%" for v in ax.get_xticks()]); ax.set_yticklabels([f"{int(v*100)}%" for v in ax.get_yticks()])
ax.set_xlabel("Cumulative share of population (poorest to richest)",color=INK2)
ax.set_ylabel("Cumulative share of income",color=INK2)
for s in ["top","right"]: ax.spines[s].set_visible(False)
for s in ["left","bottom"]: ax.spines[s].set_color(GRID)
ax.tick_params(colors=INK2); ax.grid(axis="y",color=GRID,lw=0.6)
ax.set_title("Two Lorenz curves (illustrative data)",loc="left",color=NAVY,fontsize=13,fontweight="bold")
fig.tight_layout(); fig.savefig(out,facecolor="white")
print("Gini A",gini(A),"B",gini(B),"Palma A",palma(A),"B",palma(B))

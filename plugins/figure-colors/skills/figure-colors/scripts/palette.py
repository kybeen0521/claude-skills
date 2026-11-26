"""figure-colors 팔레트: 그림 색의 단일 출처.

그림 코드는 hex 값을 직접 적지 말고 이 파일을 불러 쓴다.

    import sys; sys.path.insert(0, "<이 폴더 경로>")
    import palette as P
    ax.plot(x, y, color=P.CAT3[0])
    ax.contourf(X, Y, Z, levels=lev, cmap=P.teal_steps(5))

견본 그림:  python palette.py --swatch out.png
"""

# ---------------------------------------------------------------- 범주형(데이터 클래스가 다를 때)
# 기본 3색: Paul Tol high-contrast. 세 범주용으로 설계됐고 밝기가 어둠, 밝음, 중간이라 흑백에서도 갈린다.
CAT3 = ["#004488", "#DDAA33", "#BB5566"]

# 점·무리 구분: Paul Tol vibrant. 앞 셋이 발표 자료에서 쓴 순서, 뒤 넷은 4개 이상일 때 이 순서로 늘린다.
VIBRANT = ["#009988", "#EE7733", "#EE3377", "#0077BB", "#33BBEE", "#CC3311", "#BBBBBB"]

# 순서가 있는 무리(단계, 각도, 수준): Paul Tol iridescent 23단계 중 12, 16, 20, 23번째. 밝음 -> 어둠.
ORDINAL4 = ["#81C4E7", "#9398D2", "#906388", "#46353A"]

# 요구 조건, 목표선, 강조 하나
ACCENT = "#C00000"

# 글자, 축, 검은 선
INK = "#1A1A1A"

# ---------------------------------------------------------------- 크기(데이터 클래스가 같을 때)
# 청록 계열: 흰색 -> #628FA2 -> #014460.
TEAL_BASE = ["#FFFFFF", "#628FA2", "#014460"]
TEAL_2D_RANGE = (0.00, 0.70)   # 2D 맵: 밝은 쪽 70 %만(위에 그린 검은 선이 묻히지 않게)
TEAL_3D_RANGE = (0.20, 0.85)   # 3D 곡면: 더 진하게(낮은 곳이 흰 바탕에 묻히지 않게)
TEAL_3D_ALPHA = 0.85
# 2D 5단계(단계 가운데 값의 색), 발표 자료 16쪽과 같음
TEAL_STEPS5 = ["#EAF0F3", "#BED0D8", "#91B1BE", "#6591A4", "#497B91"]
# 막대 하나, 단색 채움
TEAL_SOLID = "#497B91"


def _base():
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list("teal_base", TEAL_BASE)


def teal_cmap(kind="2d"):
    """연속 색 지도. kind = "2d" 또는 "3d"."""
    import numpy as np
    from matplotlib.colors import ListedColormap
    lo, hi = TEAL_2D_RANGE if kind == "2d" else TEAL_3D_RANGE
    return ListedColormap(_base()(np.linspace(lo, hi, 256)), name=f"teal_{kind}")


def teal_steps(n=5):
    """2D 맵·색 막대용 n 단계. 각 단계는 2D 연속 지도에서 단계 가운데 값의 색."""
    import numpy as np
    from matplotlib.colors import ListedColormap
    if n == 5:
        return ListedColormap(TEAL_STEPS5, name="teal_steps5")
    c = teal_cmap("2d")
    return ListedColormap([c((i + 0.5) / n) for i in range(n)], name=f"teal_steps{n}")


def categorical(n, ordered=False):
    """n 개 범주의 색. ordered=True 면 순서형(4개까지)."""
    if ordered:
        if n > len(ORDINAL4):
            raise ValueError("순서형은 4단계까지 정해져 있다. 더 필요하면 teal_steps(n) 이나 표식 모양을 함께 쓴다.")
        return ORDINAL4[:n] if n == 4 else [ORDINAL4[i] for i in _spread(n, 4)]
    if n <= 3:
        return CAT3[:n]
    if n <= len(VIBRANT):
        return VIBRANT[:n]
    raise ValueError("범주가 7개를 넘는다. 색을 줄이고 표식 모양으로 나눈다.")


def _spread(n, m):
    return [round(i * (m - 1) / (n - 1)) for i in range(n)] if n > 1 else [m - 1]


def _swatch(path):
    import matplotlib.pyplot as plt
    rows = [("CAT3 (Tol high-contrast)", CAT3), ("VIBRANT (Tol vibrant)", VIBRANT),
            ("ORDINAL4 (Tol iridescent)", ORDINAL4), ("TEAL_STEPS5", TEAL_STEPS5),
            ("ACCENT / INK / TEAL_SOLID", [ACCENT, INK, TEAL_SOLID])]
    fig, axes = plt.subplots(len(rows) + 2, 1, figsize=(8, 0.62 * (len(rows) + 2)))
    for ax, (name, cols) in zip(axes, rows):
        for i, c in enumerate(cols):
            ax.add_patch(plt.Rectangle((i, 0), 0.95, 1, color=c))
            ax.text(i + 0.475, -0.18, c, ha="center", va="top", fontsize=7)
        ax.set_xlim(0, 7); ax.set_ylim(-0.6, 1); ax.axis("off")
        ax.set_title(name, loc="left", fontsize=8.5, pad=2)
    import numpy as np
    g = np.linspace(0, 1, 256)[None, :]
    for ax, k in zip(axes[len(rows):], ("2d", "3d")):
        ax.imshow(g, aspect="auto", cmap=teal_cmap(k), extent=(0, 7, 0, 1))
        ax.set_xlim(0, 7); ax.set_ylim(-0.6, 1); ax.axis("off")
        ax.set_title(f"teal_cmap('{k}')", loc="left", fontsize=8.5, pad=2)
    fig.tight_layout(); fig.savefig(path, dpi=200); plt.close(fig)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "--swatch":
        _swatch(sys.argv[2]); print(sys.argv[2])
    else:
        print(__doc__)

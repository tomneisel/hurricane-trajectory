import pandas as pd
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature

def plot_hurricane(data: pd.DataFrame, plt_title: str):

    fig = plt.figure(figsize = (12,8))
    ax = plt.axes(projection = ccrs.PlateCarree())

    ax.set_extent([-100, -70, 15, 45], crs=ccrs.PlateCarree())

    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
    ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)

    ax.plot(
    data["LON"],
    data["LAT"],
    marker="o",
    markersize=4,
    linewidth=2,
    transform=ccrs.PlateCarree(),
    label=plt_title
)

    ax.scatter(
        data["LON"].iloc[0],
        data["LAT"].iloc[0],
        marker="o",
        s=100,
        transform=ccrs.PlateCarree(),
        label="Start"
    )

    ax.scatter(
        data["LON"].iloc[-1],
        data["LAT"].iloc[-1],
        marker="X",
        s=120,
        transform=ccrs.PlateCarree(),
        label="Ende"
    )

    gl = ax.gridlines(draw_labels=True, alpha=0.4)
    gl.top_labels = False
    gl.right_labels = False

    plt.title(plt_title, fontsize=16)
    plt.legend()
    plt.show()
import pandas as pd
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature

def plot_hurricane(observed_data: pd.DataFrame, predicted_data: pd.DataFrame):

    lon_lower = min([observed_data["LON"].min(), predicted_data["LON"].min()])
    lon_upper = max([observed_data["LON"].max(), predicted_data["LON"].max()])
    lat_lower = min([observed_data["LAT"].min(), predicted_data["LAT"].min()])
    lat_upper = max([observed_data["LAT"].max(), predicted_data["LAT"].max()])

    if observed_data.iloc[0]["NAME"] != "UNNAMED":
        hurricane_name = observed_data.iloc[0]["NAME"].capitalize()
    else:
        hurricane_name = observed_data.iloc[0]["SID"]

    fig = plt.figure(figsize = (12,8))
    ax = plt.axes(projection = ccrs.PlateCarree())

    ax.set_extent([lon_lower -8, lon_upper + 8, lat_lower - 8, lat_upper + 8], crs=ccrs.PlateCarree())

    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
    ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)

    ax.scatter(
        observed_data["LON"].iloc[0],
        observed_data["LAT"].iloc[0],
        marker="o",
        c="black",
        s=100,
        transform=ccrs.PlateCarree(),
        label="Start of storm"
    )

    ax.plot(
        observed_data["LON"],
        observed_data["LAT"],
        marker="o",
        c="blue",
        markersize=4,
        linewidth=2,
        transform=ccrs.PlateCarree(),
        label="Observed trajectory of hurricane " + hurricane_name
    )

    ax.scatter(
        observed_data["LON"].iloc[-1],
        observed_data["LAT"].iloc[-1],
        marker="X",
        c="blue",
        s=120,
        transform=ccrs.PlateCarree(),
        label="Observed end of storm"
    )

    ax.plot(
        predicted_data["LON"],
        predicted_data["LAT"],
        marker="o",
        c="orange",
        markersize=4,
        linewidth=2,
        transform=ccrs.PlateCarree(),
        label="Predicted trajectory of hurricane " + hurricane_name
    )

    ax.scatter(
        predicted_data["LON"].iloc[-1],
        predicted_data["LAT"].iloc[-1],
        marker="X",
        c="orange",
        s=120,
        transform=ccrs.PlateCarree(),
        label="Predicted end of storm"
    )

    gl = ax.gridlines(draw_labels=True, alpha=0.4)
    gl.top_labels = False
    gl.right_labels = False

    plt.title("Hurricane " + hurricane_name, fontsize=16)
    plt.legend()
    plt.show()
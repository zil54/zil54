import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import os

# Capital coordinates
capital_coords = {
    "Guatemala City": (-90.5133, 14.6349),
    "Belmopan": (-88.7769, 17.2514),
    "San Salvador": (-89.1890, 13.6929),
    "Tegucigalpa": (-87.2169, 14.0723),
    "Managua": (-86.2514, 12.1364),
    "San Jose": (-84.0907, 9.9281),
    "Panama City": (-79.5199, 8.9824),
    "Bogota": (-74.0721, 4.7110),
    "Caracas": (-66.9036, 10.4806),
    "Quito": (-78.4678, -0.1807),
    "Lima": (-77.0428, -12.0464),
    "La Paz": (-68.1193, -16.5000),
    "Asuncion": (-57.5759, -25.2637),
    "Santiago": (-70.6483, -33.4569),
    "Buenos Aires": (-58.4173, -34.6118),
    "Montevideo": (-56.1645, -34.9011),
    "Brasília": (-47.8825, -15.7942),
    "Georgetown": (-58.1551, 6.8013),
    "Paramaribo": (-55.2038, 5.8520),
    "Cayenne": (-52.3333, 4.9333)
}

# Country-capital pairs
country_capitals = {
    "Guatemala": "Guatemala City",
    "Belize": "Belmopan",
    "El Salvador": "San Salvador",
    "Honduras": "Tegucigalpa",
    "Nicaragua": "Managua",
    "Costa Rica": "San Jose",
    "Panama": "Panama City",
    "Colombia": "Bogota",
    "Venezuela": "Caracas",
    "Ecuador": "Quito",
    "Peru": "Lima",
    "Bolivia": "La Paz",
    "Paraguay": "Asuncion",
    "Chile": "Santiago",
    "Argentina": "Buenos Aires",
    "Uruguay": "Montevideo",
    "Brazil": "Brasília",
    "Guyana": "Georgetown",
    "Suriname": "Paramaribo",
    "French Guiana": "Cayenne"
}

# Load Natural Earth shapefile manually
shapefile_path = os.path.join("data", "ne_110m_admin_0_countries", "ne_110m_admin_0_countries.shp")
world = gpd.read_file("data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")





def generate_country_map(country, label, save_path, capital_coords=None):
    country_shape = world[world["ADMIN"] == country]
    if country_shape.empty:
        print(f"❌ Country '{country}' not found.")
        return

    ax = country_shape.plot(color="lightgreen", edgecolor="black", figsize=(6, 6))
    plt.axis("off")

    centroid = country_shape.geometry.centroid
    plt.text(centroid.x, centroid.y, label, ha="center", va="center", fontsize=14, weight="bold")

    if capital_coords:
        cap_point = Point(capital_coords[0], capital_coords[1])
        plt.plot(cap_point.x, cap_point.y, "ro", markersize=8)
        plt.text(cap_point.x, cap_point.y, label, fontsize=12, ha="left", va="bottom", color="red")

    os.makedirs("images", exist_ok=True)
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"✅ Saved {save_path}")

# Generate all 41 images
#for country, capital in country_capitals.items():
#    generate_country_map(country, country, f"images/{country.lower().replace(' ', '_')}_country.png")
#    coords = capital_coords.get(capital)
#    generate_country_map(country, capital, f"images/{country.lower().replace(' ', '_')}_capital.png", capital_coords=coords)

# Special case: French Guiana (part of France)
generate_country_map("France", "French Guiana", "images/french_guiana_country.png")
generate_country_map("France", "Cayenne", "images/french_guiana_capital.png", capital_coords=(-52.3333, 4.9333))
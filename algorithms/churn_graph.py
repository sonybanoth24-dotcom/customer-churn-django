import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os
from django.conf import settings

def generate_churn_graph():
    ages = [20, 25, 30, 35, 40, 45, 50]
    churn = [5, 10, 18, 25, 30, 35, 40]

    plt.figure(figsize=(6, 4))
    plt.plot(ages, churn, marker='o')
    plt.title("Customer Churn vs Age")
    plt.xlabel("Age")
    plt.ylabel("Churn %")
    plt.grid(True)

    # 🔥 FORCE STATIC DIR
    static_dir = os.path.join(settings.BASE_DIR, "static")
    os.makedirs(static_dir, exist_ok=True)

    image_path = os.path.join(static_dir, "churn_graph.png")
    plt.savefig(image_path)
    plt.close()

    print("GRAPH SAVED AT:", image_path)
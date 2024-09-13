import pandas as pd

def generate_response(filtered_houses):
    if not isinstance(filtered_houses, pd.DataFrame) or filtered_houses.empty:
        return "No houses found matching the criteria."

    top_houses = filtered_houses.head(10)
    house_names = top_houses['house_Name'].tolist()

    response = f"Here are choices for houses you are very likely to get into based on your criteria:\n"
    for i, house in enumerate(house_names, 1):
        response += f"{i}. {house}\n"

    return response
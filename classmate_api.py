
import requests

URL = "https://balcenajessicaann.onrender.com/student"

def get_classmate_data():
    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as error:
        print("Classmate API connection failed:", error)
        return None

    except ValueError:
        print("Invalid JSON response from Classmate API.")
        return None


if __name__ == "__main__":
    data = get_classmate_data()

    if data is not None:
        print("Classmate API Data:")
        print(data)

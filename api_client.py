
import requests

URL = "https://kleinjasperagrabio.onrender.com/course"

def get_course_data():
    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()

        data = response.json()

        print("Course Code:", data.get("course_code", "N/A"))
        print("Course Name:", data.get("course_name", "N/A"))
        print("Instructor:", data.get("instructor", "N/A"))

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)

    except ValueError:
        print("Invalid JSON response.")


if __name__ == "__main__":
    get_course_data()

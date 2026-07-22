# Safe API Parsing with Python Dataclasses

A lightweight Python project demonstrating how to safely parse nested API responses using **Python dataclasses**. Instead of scattering multiple `.get()` chains throughout your codebase, this project centralizes parsing logic into a single, reusable parser.

---

## 📌 Problem

Third-party APIs often return nested JSON responses with optional or missing fields. Accessing these values directly can lead to repetitive code like this:

```python
city = response.get("address", {}).get("city", "Unknown")
zipcode = response.get("address", {}).get("zipcode", "Unknown")
```

As your application grows, these repeated dictionary lookups become harder to maintain and more error-prone.

---

## ✅ Solution

Parse the API response once and convert it into a structured Python object using a **dataclass**.

```python
user = UserParser.from_dict(response)

print(user.city)
print(user.zipcode)
```

Your application now works with clean, typed Python objects instead of raw dictionaries.

---

## 🚀 Features

- Fetches data from a real public REST API
- Uses Python `@dataclass` for structured models
- Centralizes API parsing in one place
- Safely handles missing nested fields using sensible defaults
- Includes unit tests for the parser
- Clean, beginner-friendly project structure

---

## 📂 Project Structure

```text
python-api-parser/
│
├── tests/
│   └── test_parser.py      # Unit tests
│
├── api.py                  # Fetches data from the public API
├── models.py               # Dataclass model
├── parser.py               # Converts JSON into Python objects
├── main.py                 # Runs the example
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd python-api-parser
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

### Example Output

```text
UserProfile(
    id=1,
    username='Bret',
    email='Sincere@april.biz',
    city='Gwenborough',
    zipcode='92998-3874'
)

Username : Bret
Email    : Sincere@april.biz
City     : Gwenborough
Zip Code : 92998-3874
```

---

## 🧪 Running the Tests

```bash
python -m unittest discover tests
```

---

## 💡 Why This Pattern?

Instead of accessing nested dictionaries throughout your application, parse the response once and work with structured Python objects.

### Benefits

- ✔ Cleaner and more readable code
- ✔ Centralized parsing logic
- ✔ Easier maintenance when API responses change
- ✔ Sensible default values for optional fields
- ✔ Better separation of concerns
- ✔ Improved code reusability

---

## 🌐 Public API Used

This project uses the free **JSONPlaceholder** REST API.

**Endpoint:**

```
https://jsonplaceholder.typicode.com/users/1
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you have ideas to improve the project, feel free to open an issue or submit a pull request.

---

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub if it helped you learn a new Python pattern.

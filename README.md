# Safe API Parsing with Python Dataclasses

A lightweight Python project demonstrating how to safely parse nested API responses using **dataclasses** instead of scattering multiple `.get()` chains throughout your code.

---

## 📌 Problem

When working with third-party APIs, responses often contain nested JSON objects with optional or missing fields.

This usually leads to code like:

```python
city = response.get("address", {}).get("city", "Unknown")
zipcode = response.get("address", {}).get("zipcode", "Unknown")
```

As your application grows, these repeated dictionary lookups become difficult to maintain.

---

## ✅ Solution

Convert the API response into a structured Python object using a **dataclass** and a centralized parser.

```python
user = UserParser.from_dict(response)

print(user.city)
print(user.zipcode)
```

Now your application works with clean Python objects instead of raw dictionaries.

---

## 🚀 Features

- Fetches data from a real public REST API
- Uses Python `@dataclass` for structured models
- Centralizes API parsing in one place
- Safely handles missing nested fields with sensible defaults
- Includes unit tests for the parser
- Beginner-friendly and easy to extend

---

## 📂 Project Structure

```
python-api-parser/
│
├── api.py              # Fetches data from the public API
├── models.py           # Dataclass model
├── parser.py           # Converts JSON into Python objects
├── main.py             # Demo application
├── test_parser.py      # Unit tests
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

Clone the repository:

```bash
git clone <repository-url>
cd python-api-parser
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

Example Output:

```
UserProfile(
    id=1,
    username='Bret',
    email='Sincere@april.biz',
    city='Gwenborough',
    zipcode='92998-3874'
)
```

---

## 🧪 Run Tests

```bash
python test_parser.py
```

---

## 💡 Why Use This Pattern?

Instead of accessing nested dictionaries throughout your application, parse the response once and work with typed Python objects.

**Benefits:**

- Cleaner and more readable code
- Centralized parsing logic
- Easier maintenance when APIs change
- Sensible default values for optional fields
- Better separation between API responses and business logic

---

## 🌐 Public API Used

This project uses the free **JSONPlaceholder** API for demonstration purposes.

https://jsonplaceholder.typicode.com/users/1

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

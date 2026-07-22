# Safe API Parsing with Python Dataclasses

A lightweight Python project demonstrating how to safely parse nested API responses using **Python dataclasses**. Instead of scattering multiple `.get()` chains throughout your codebase, this project centralizes parsing logic into a single, reusable parser.

---

## 📌 Problem

Third-party APIs often return nested JSON responses with optional or missing fields. This usually leads to repetitive code like:

```python
city = response.get("address", {}).get("city", "Unknown")
zipcode = response.get("address", {}).get("zipcode", "Unknown")
```

As applications grow, these repeated dictionary lookups become harder to maintain and update.

---

## ✅ Solution

Parse the API response once and convert it into a structured Python object using a **dataclass**.

```python
user = UserParser.from_dict(response)

print(user.city)
print(user.zipcode)
```

Now the rest of your application works with clean Python objects instead of raw dictionaries.

---

## 🚀 Features

- Fetches data from a real public REST API
- Uses Python `@dataclass` for structured models
- Centralizes API parsing logic
- Safely handles missing nested fields with sensible defaults
- Includes unit tests
- Simple, beginner-friendly project structure

---

## 📂 Project Structure

```text
python-api-parser/
│
├── tests/
│   └── test_parser.py
│
├── api.py
├── models.py
├── parser.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/dshyleshkarthik7-hue/python-api-parser.git
cd python-api-parser
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

### Example Output

```text
UserProfile(
    id=1,
    username='test',
    email='test@example.com',
    city='Bengaluru',
    zipcode='560001'
)

Username : test
Email    : test@example.com
City     : Bengaluru
Zip Code : 560001
```

---

## 🧪 Run the Tests

```bash
python -m unittest discover tests
```

---

## 💡 Why This Pattern?

Instead of repeatedly accessing nested dictionaries across your application, parse the response once and work with structured Python objects.

### Benefits

- ✅ Cleaner and more readable code
- ✅ Centralized parsing logic
- ✅ Easier maintenance when API responses change
- ✅ Sensible default values for optional fields
- ✅ Better separation of concerns
- ✅ Improved code reusability

---

## 🌐 Public API Used

This project uses the free **JSONPlaceholder** REST API for demonstration purposes.

**Endpoint:**

```text
https://jsonplaceholder.typicode.com/users/1
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

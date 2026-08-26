# 🔀 Combination Generator

A simple Python command-line tool that generates **all possible combinations** from multiple categories of user-provided options.

The program asks you to enter options such as names, father's names, nicknames, cities, or any other categories. It then uses Python's `itertools.product()` to generate every possible combination and saves the results to a `combinations.txt` file.

## ✨ Features

* 🖥️ Simple terminal-based interface
* 📋 Supports any number of categories
* ✍️ Enter multiple options separated by commas
* 🔄 Generates all possible combinations automatically
* 🧹 Handles empty or invalid input
* 📄 Saves combinations to `combinations.txt`
* 🔢 Displays the total number of combinations generated
* 🐍 Uses Python's built-in `itertools.product()`

## 📁 Project Structure

```text
combination-generator/
│
├── combination_generator.py
├── combinations.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rook-jpg/COMBINATION.git
```

### 2. Open the project directory

```bash
cd combination
```

### 3. Run the program

```bash
python combination_generator.py
```

If your system uses `python3`, run:

```bash
python3 combination_generator.py
```

## 💻 How It Works

The program asks you to enter options for each category.

For example:

```text
Enter options for Category 1, separated by commas: Ali, Ahmed
Add another category? y/n: y

Enter options for Category 2, separated by commas: Khan, Shah
Add another category? y/n: y

Enter options for Category 3, separated by commas: Sunny, Sonu
Add another category? y/n: n
```

The program then generates every possible combination.

With:

* 2 names
* 2 father names
* 2 nicknames

The total number of combinations is:

```text
2 × 2 × 2 = 8
```

The output is saved in:

```text
combinations.txt
```

Example:

```text
Ali - Khan - Sunny
Ali - Khan - Sonu
Ali - Shah - Sunny
Ali - Shah - Sonu
Ahmed - Khan - Sunny
Ahmed - Khan - Sonu
Ahmed - Shah - Sunny
Ahmed - Shah - Sonu
```

At the end, the program displays:

```text
Done! 8 combinations saved to combinations.txt
```

## 🧠 Technology Used

* **Python 3**
* **itertools.product()**
* File handling with Python's built-in `open()` function

No external Python packages are required.

## 📌 Example Categories

You can use the tool for many different types of data, for example:

```text
Name
Father Name
Nickname
City
Country
Company
Username
Product
Color
Model
```

The program does not require specific category names. You can enter any options you want.

## ⚠️ Important Note

The number of combinations can become very large as you add more options or categories.

For example:

```text
10 options × 10 options × 10 options × 10 options
= 10,000 combinations
```

With larger inputs, the generated `combinations.txt` file can become very large.

## 📄 Output

All generated combinations are stored in:

```text
combinations.txt
```

Each combination is written on a separate line using:

```text
 -
```

as the separator.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

## 📜 License

This project is open source and available under the MIT License.

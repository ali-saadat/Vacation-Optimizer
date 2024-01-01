
# Vacation-Optimizer

Welcome to the Vacation-Optimizer repository! I've developed this Python-based tool to help individuals and professionals efficiently plan their vacations by combining public holidays with adjacent weekends. The goal is simple: maximize your time off with minimal vacation days used.

## Features

- **Smart Vacation Planning**: Automatically identifies the best times to take leave based on public holidays and weekends.
- **Customizable**: Works with any country's public holidays by simply adjusting the country code.
- **User-Friendly**: Easy to understand output, showing the start and end of each vacation period, along with the number of vacation days used.

## Getting Started

To use this tool, you'll need Python installed on your system and the `holidays` package. 

### Prerequisites

- Python 3.x
- holidays package (`pip install holidays`)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Vacation-Optimizer.git
   ```
2. Navigate to the cloned directory.

### Usage

Modify the `country_code` and `year` in the script to match your desired location and year. Run the script, and it will output the optimized vacation periods.

Example:
```python
country_code = 'CZ'  # Change to your country's code
year = 2024          # Change to your desired year

optimized_vacations = extended_vacation_optimization(country_code, year)
print(optimized_vacations)
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/Vacation-Optimizer/issues) if you want to contribute.

## Author

- **ali saadat** - *Initial work* - [Your Medium Profile](https://medium.com/@ali.saadat81)

## License

This project is licensed under the MIT License - see the [MIT](LICENSE) file for details.

## Acknowledgments

- Inspired by initial works by [@kryptonite0](https://github.com/kryptonite0/python-long-weekends) and [@jezrael](https://stackoverflow.com/users/2901002/jezrael) on GitHub and StackOverflow.
- Special thanks to the `python-long-weekends` library for the foundational concept.

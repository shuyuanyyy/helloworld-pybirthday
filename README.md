![Python test](https://github.com/software-students-spring2025/3-python-package-helloworld/actions/workflows/ci.yml/badge.svg)

# The `pybirthday` Package 🎉🎂

`pybirthday` is a Python package that lets users generate festive birthday-themed visuals!  

*[Package Page on PyPI](https://pypi.org/project/pybirthday/0.1.1/)*

Currently, the package offers four functions:

1. `cake()` 🍰: returns a birthday cake with a personalized name and a custom message.  
   - **Syntax**: `pybirthday.cake(name, words)`  
   - **Parameters**:  
     - `name`: Optional. A string (up to 15 characters) to be displayed on the cake. If no name is provided or invalid, the cake will display a blank space.
     - `words`: Optional. A string with a custom message to be printed below the cake. Defaults to "Hope all your birthday wishes come true!"

2. `candle()` 🕯️: returns an image of a candle from various styles.  
   - **Syntax**: `pybirthday.candle(style)`  
   - **Parameter**:
     - `style`: Optional. Values of 0–4 each specify a candle style. If out of range, style #4 is returned. Defaults to random.

3. `balloon()` 🎈: returns an image of birthday balloons from various styles.  
   - **Syntax**: `pybirthday.balloon(style)`  
   - **Parameter**:
     - `style`: Optional. Specifies a balloon style. Defaults to random.

4. `teddy()` 🧸: returns a cute teddy bear bringing you a birthday greeting!  
   - **Syntax**: `pybirthday.teddy(age, name)`  
   - **Parameters**:  
     - `age`: Optional. Includes age in the greeting. Specify in ordinal format (e.g., "20th", "2nd"). Can take integers or strings of no more than 10 characters.
     - `name`: Optional. Includes name in the greeting. Can take strings of no more than 10 characters.
     - Invalid parameters are ignored!

## Installation ⚙️

Install the package via pip:
```bash
pip install pybirthday


## Usage
```python
from pybirthday import cake, candle, balloon, teddy

mycake = cake("Alice", "Happy 20th Birthday!")
print(mycake) # Prints cake with "Alice" written on cake, and "Happy 20th Birthday!" at the bottom

myteddy = teddy("20th", "Bob")
print(myteddy) # Prints teddy bear saying "HAPPY 20TH BIRTHDAY BOB"

mycandle_1 = candle()
mycandle_2 = candle(2)
print(mycandle_1) # Prints a random candle
print(mycandle_2) # Prints candle style #3

myballoon_1 = balloon()
myballoon_2 = balloon(2)
print(myballoon_1) # Prints random balloons
print(myballoon_2) # Prints balloon style #3
```

## How to Contribute 🤝
1. Fork this repository and then clone it to your local machine:
   ```sh
   git clone https://github.com/software-students-spring2025/3-python-package-helloworld
   cd 3-python-package-helloworld
   ```
2. Set up a virtual environment
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Create your own feature branch
   ```sh
   git checkout -b your_branch_name
   ```
4. Make your change and commit
   ```sh
   git add .
   git commit -m "Add feature from ***"
   git push # Need to push to your own feature branch
   ```
5. Create a pull request and wait for code review!

## Testing ✅
Unit tests are included within the tests directory. To run these tests:
1. Install pytest into the virtual environment
   ```sh
   pipenv install pytest
   ```
2. Run the tests from the main project directory: 
   ```sh
   python -m pytest
   ```

## Team ✨
- [Eric Xu](https://github.com/EricXu1244)
- [Frank Fang](https://github.com/FrankFangH)
- [Lauren Zhou](https://github.com/laurenlz)
- [Shuyuan Yang](https://github.com/shuyuanyyy)


## References 🔖
1. [ASCII Art](https://asciiart.website/index.php) - The ASCII arts used in the functions were obtained from this website.

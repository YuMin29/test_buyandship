This project automates switching to all regions on the Buy&Ship TW website using Python, Selenium, pytest, pytest-html, and Chrome (version 126.0.6478.62).
1. Go to the [Buy&Ship TW](https://www.buyandship.com.tw/).
2. Click the region element
3. Switch to all regions and generate a report.
4. The report contains 2 failed test cases and 13 passed test cases.

# Installation
[Python](https://www.python.org/downloads/)

pytest
```bash
pip install pytest
```
pytest-html
```bash
pip install pytest-html
```
selenium
```bash
pip install selenium
```
Update/Download Chrome
```bash
version 126.0.6478.62
```

# Usage
clone the project
```bash
git clone https://github.com/YuMin29/test_buyandship.git
```

go to the folder and execute pytest：
```bash
cd test_buyandship

python3.x -m pytest .\test_buyandship.py -v --html=report.html
```
report generated in:
```bash
report.html
```

# Report
![image](https://github.com/user-attachments/assets/5e117377-0e4a-4103-96f4-b6444378f171)
# Excute result
![image](https://github.com/user-attachments/assets/c93b1249-2bed-4728-8f66-f58925c72c61)


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate and provide a brief description of the project's purpose.

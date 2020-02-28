@echo off

python -m pip install --upgrade pip && python -m venv myenv && .\myenv\Scripts\activate.bat && echo "activated venv!" && pip install pytest && py.test tests\test_add.py --junit-xml=report.xml && py.test tests\test_subtract.py --junit-xml=report.xml

echo "Done!!!!!!!"

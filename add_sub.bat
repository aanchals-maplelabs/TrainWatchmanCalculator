@echo off

python -m pip install --upgrade pip && python -m venv myenv && .\myenv\Scripts\activate.bat && echo "activated venv!" && pip install pytest && py.test tests\test_add.py tests\test_subtract.py --junit-xml=reports\report.xml && python reports\xml_to_json.py

echo "Done!!!!!!!"

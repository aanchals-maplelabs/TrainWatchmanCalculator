@echo off

python -m pip install --upgrade pip && python -m venv myenv && .\myenv\Scripts\activate.bat && echo "activated venv!" && pip install pytest && py.test tests\test_add.py tests\test_subtract.py tests\test_multiply.py tests\test_divide.py tests\test_modulo.py tests\test_powerof.py --junit-xml=report.xml && python -m pip install --upgrade pip && pip install xmltodict && python reports\xml_to_json.py

echo "Done!!!!!!!"

@echo off

python -m pip install --upgrade pip && python -m venv myenv && .\myenv\Scripts\activate.bat && echo "activated venv!" && pip install pytest && py.test tests\test_multiply.py tests\test_divide.py --junit-xml=report.xml && python -m pip install --upgrade pip && pip install xmltodict && python reports\xml_to_json.py


echo "Done!!!!!!!"

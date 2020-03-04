@echo off

python -m pip install --upgrade pip && python -m venv myenv && .\myenv\Scripts\activate.bat && echo "activated venv!" && pip install pytest && py.test tests\test_add.py tests\test_subtract.py --junit-xml=report.xml && python -m pip install --upgrade pip && pip install xmltodict && python reports\xml_to_json.py && pip install pymongo && python reports\mongotrial.py


echo "Done!!!!!!!"

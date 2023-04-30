
echo " BUILD START"
pip install -r requirements.txt
pip install --upgrade pip
pip install --upgrade setuptools
python3.9 manage.py collectstatic
echo " BUILD END"

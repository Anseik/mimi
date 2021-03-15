## 팀장님만세

**Backend**

```sh
anaconda 20.11version 설치 (python 3.8.5)
python -m venv env - 가상환경 설치
source ./env/Scrupts/activate - 가상환경 실행
cd sub2/backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

**Frontend**

```sh
cd sub2/frontend
npm install
npm run serve
```




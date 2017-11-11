# pyenv
## "Simple Python Version Management"
### 로컬에 다양한 파이썬 버전을 설치하고 사용. 파이썬 버전에 대한 의존성 해결.

- pyenv 설치(ubuntu)
#### 의존성 패키지 설치
>$sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm

- pyenv installer로 설치
>$curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

-  .bashrc에 하기 내용 추가
>$echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc <br/>
>$echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc <br/>
>$echo 'eval "$(pyenv init -)"' >> ~/.bashrc <br/>

- 파이썬 3.6.2 버전을 pyenv로 설치
>$pyenv update
>$pyenv install 3.6.2

- 지금 사용하고 있는 파이썬 버전확인
>$pyenv versions

- 설치된 파이썬 리스트 및 파이썬 개발환경 리스트 출력
>$pyenv install --list

- 설치한 파이썬 버전을 사용하고 싶다면
>$pyenv shell 3.6.2
>$python --version #현재 버전 확인.

- 설치한 파이썬 버전삭제
>$~/.env/versions/ 아래에서 해당버전 삭제(rm -rmf ~/.pyenv/versions/django-dev)

# virtualenv
## "Virtual Python Environment Builder"
### 로컬에 다양한 파이썬 환경울 구축. pip install 을 통해서 설치하는 패키지들에 대한 의존성을 해결.
- 가상환경 생성 & 프로젝트 폴더에 세팅
#pyenv virtualenv PYTHON_VERSION VIRTUAL_ENV_NAME
>$pyenv install 3.5.3<br/>
>$pyenv virtualenv 3.5.3 django_server
#프로젝트 폴더로 이동...
>$pyenv local django_server
#폴더 엑세스하면 바로 가상환경에 접속하도록 세팅함.
#### 생성한 개발환경은 pyenv shell로 사용할 수 있음.
>$pyenv versions
>$pyenv activate VIRTUAL_ENV_NAME #가상환경 접속.
>$pyenv deactivate #가상환경 빠져나오기.

# 구축한 개발환경 공유방법
>user$ pip list > requirements.txt
>other-user$ pip install -r requirements.txt  

# pip
## 파이썬 패키지 관리
### pip는 Python 2.7.9 또는 Python 3.4 이상 버전을 설치하게 되면 설치되어 있음.
- pip 기본 upgrade
>$pip install --upgrade pip
>$pip install --upgrade setuptools

## 패키지 의존 리스트 공유
1. 패키지 리스트 내보내기 : pip freeze > requirements.txt
2. 패키지 리스트 불러오고 설치하기 : pip install -r requiremenets.txt

## 패키지 리스트를 development, production 환경을 분리하여 관리하는 방법
1. 프로젝트에서 requirements-dev.txt에 
2. "-r requirements.txt"를 추가.
3. development 환경으로 설정 : pip install -r requirements-dev.txt
4. production 환경으로 설정 : pip install -r requirements.txt 으로 쉘 명령 하나로 환경 설정


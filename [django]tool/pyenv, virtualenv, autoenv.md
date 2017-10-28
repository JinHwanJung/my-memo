# pyenv
## "Simple Python Version Management"
### 로컬에 다양한 파이썬 버전을 설치하고 사용. 파이썬 버전에 대한 의존성 해결.

- pyenv 설치(ubuntu)
#### 의존성 패키지 설치
>$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm

- pyenv installer로 설치
>$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

-  .bashrc에 하기 내용 추가
>$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
<br/>
$ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
<br/>
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc

- 파이썬 3.6.2 버전을 pyenv로 설치
>pyenv update
<br/>
pyenv install 3.6.2

- 지금 사용하고 있는 파이썬 버전확인
>$ pyenv versions
- 설치된 파이썬 리스트 및 파이썬 개발환경 리스트 출력
> $ pyenv install --list

- 설치한 파이썬 버전을 사용하고 싶다면
> $ pyenv shell 3.6.2
<br/>
python --version #현재 버전 확인.
# virtualenv
## "Virtual Python Environment Builder"
### 로컬에 다양한 파이썬 환경울 구축. pip install 을 통해서 설치하는 패키지들에 대한 의존성을 해결.



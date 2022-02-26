# Інструкція як автоматично скаржитись на хуйловські телеграм-канали:
1. Необхідно отримати api_id та api_hash через один з варіантів: 1) інструкція за [посиланням](https://docs.telethon.dev/en/latest/basic/signing-in.html), 2) через телеграм-бот "TG API EXTRACTOR BOT"
2. Мають бути встановлені: 1) Git 2) Docker або python3 з pip 
3. У файл dicks.txt можна додавати посилання на інші хуйловські телеграм-канали
4. Два варіанти запуску:

# Docker
* Install Docker Desktop for your platform:
  - [Windows](https://docs.docker.com/desktop/windows/install)
  - [Linux](https://docs.docker.com/engine/install/ubuntu/)
  - [Mac](https://docs.docker.com/desktop/mac/install)
* Через CLI:`git clone  https://github.com/ftishko/de_d-mosk_l.git`
в Dockerfile, який знаходиться в клонованому проекті, додати отримані api_id та api_hash.

Приклад: 
```
ENV API_ID=1192049
ENV API_HASH=28314e02454cd413456a78e692f56b55
```
* Запуск

`docker build -t de_d-mosk_l .`

`torsocks docker run --rm -it de_d-mosk_l` - якщо встановлено тор

`docker run —rm -it de_d-mosk_l`

# Run from CLI/sources
Python 3

```
git clone https://github.com/ftishko/de_d-mosk_l.git
cd de_d-mosk_l
pip3 install -r requirements.txt
python3 runner.py

# win
pip install -r requirements.txt
python runner.py

```

Слава Україні! Смерть ворогам!
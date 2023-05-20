# Home work 12

Кешування у Django

## Розгортаня проекту (команди для Windows)

1. Склонувати репозиторій
    ```bash    
    git clone https://github.com/AtamanAA/hillel_py_pro_home_work_12.git  
    ```
2. Запустити [Redis](https://redis.io) (переконатися що [Docker Desktop](https://www.docker.com/products/docker-desktop/) запущений )
    ```bash
    docker run -p 6379:6379 redis    
    ```
3. Встановити venv та активувати його
    ```bash
    python -m venv venv
   .\venv\Scripts\activate    
    ```
4. Інсталювати сторонні пакети у venv
    ```bash
    python -m pip install -r requirements.txt    
    ```
5. Перейти до осноної дерикторії проекту та згенерувати тестові публікації (за замовчуванням створиться 100 шт.)
    ```bash
    cd cache_project
    py manage.py generate_blog     
    ```
6. Виконати запуск основного web-серверу
    ```bash
    python manage.py runserver   
    ```
7. В браузері перейти на сторінку публікації за її id
    http://127.0.0.1:8000/blog/<publication_id>



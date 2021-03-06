## Lab_5: Автоматизація за допомогою Makefile VS Docker Compose

1. Прочитав про `docker-compose`;
2. Прочитав про бібліотеку `Flask`; 
3. Моє завдання: за допомогою Docker автоматизувати розгортання веб сайту з усіма супутніми процесами:
    - за допомогою `Makefile`;
    - за допомогою `docker-compose.yaml`;
4. Першим розглянув варіант з `Makefile`, але для цього створимо робочий проект. 
5. Створив папку `my_app` в якій буде знаходитись мій проект. Створив папку `tests` де будуть тести на перевірку працездатності проекту. Ознайомтесь із вмістом кожного з файлів;
6. Щоб спробувати чи проект є працездатним виконала команди записані нижче:
    ```bash
    pipenv --python 3.8
    pipenv install -r requirements.txt
    pipenv run python app.py
    ```
    - так само можна ініціалузувати середовище для тестів у іншій вкладці шелу та запустити їх командою (вкажіть чи тести пройшли успішно?):
    ```bash
    pipenv run pytest test_app.py --url http://localhost:5000
    ```
   ![image](img/1.jpg)
   Тести пройшли успішно
    - перевірив роботу сайту перейшовши на кожну із сторінок.    
7. Видалив файли які постворювались після тестового запуску. Створив два `Dockerfile` та `Makefile` який допоможе автоматизувати процес розгортання;
8. Ознайомився із вмістом `Dockerfile` та `Makefile` та його директивами.
    run - директива Make ініціалізація та запуск імеджів.
    test-app- директива Make запуск процесу тестування.
    docker-prune- директива Make очищає середовище docker.


9. Використовуючи команду `make` створив Docker імеджі для додатку та для тестів. Запустив додаток та перейшовши в іншу вкладку шелу запустила тести.
    Тести успішно працюють;
    ![image](img/7.jpg)
    - перевірив роботу веб-сайту.
    ![image](img/3.jpg)
    
    ![image](img/2.jpg)
    
    ![image](img/4.jpg)
10. Зупинив проект натиснувши `Ctrl+C` та почистив всі ресурси Docker за допомогою `make`.
11. Створив директиву в `Makefile` для завантаження створених імеджів у Ваш Docker Hub репозиторій. 
12. Також видалив створені та закачані імеджі.
13. Для цього створив файл у кореновій папці проекту та заповнив вмістом з прикладу;
    У браузері потрібно зайти на адресу localhost:80.
14. Перевірив чи Docker-compose встановлений та працює у системі, а далі просто запустив `docker-compose`;  
    ```bash
    docker-compose version
    docker-compose -p lab5 up
    ```
15. Веб-сайт працює.localhost:80
16. Перевірив чи компоуз створив докер імеджі.
17. Зупинив проект натиснувши `Ctrl+C` і почистив ресурси створені компоуз `docker-compose down`;
18. Завантажив створені імеджі до Docker Hub репозиторієм за допомого команди:
    ```bash
    docker-compose push
    ```
19. У розробці під докер інструмент docker-compose має перевагу над Makefile.
20. Створення docker-compose для Django проекту.
    Запуск Django проекту: docker-compose -p Django up.
    Перевірка імеджів: docker images.
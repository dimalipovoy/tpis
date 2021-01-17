# LAB 4

## Хід роботи

1) Ознайомився з документацією докер.
2) Виконав команди, перенаправив вивід 
цих команд у файл my_work.log та закомітив
його до репозиторію.

        docker -vmy_work.log
        docker -hmy_work.log
        docker run dockerwhalesay cowsay Docker is funmy_work.log
3) Ознайомився з документацією.
4) Використав команду щоб завантажити 
базовий імедж з репозиторію , 
створив Dockerfile та закомітив його   
        
         sudo docker pull python3.8-slim
         sudo docker images
         sudo docker inspect python3.8-slim
5) Створив реаозиторій на Docker Hub 
6) Виконав білд (build) Docker імеджа та завантажив 
його до репозиторію.
[Репозиторій](https://hub.docker.com/repository/docker/dmytrolypovyi/devops_course)
[Імедж](https://hub.docker.com/layers/dmytrolypovyi/devops_course/django/images/sha256-40c95d98f8fd87b6451b5797db2ba5b2f6bff1c3fc493bc15e2605b379da7320?context=explore)
        
          sudo docker build -t dmytrolypovyidjango .
          sudo docker images
          sudo docker push dmytrolypovyidjango
7) Запустив сайт (все працює)
    
          sudo docker run -it --rm -p 80008000 dmytrolypovyidjango 
8) Cтворив Dockerfile.monitor. Виконав білд (build) Docker імеджа 
 з моніторингом та завантажив його до репозиторію.
[Імедж](https://hub.docker.com/layers/dmytrolypovyi/devops_course/django/images/sha256-40c95d98f8fd87b6451b5797db2ba5b2f6bff1c3fc493bc15e2605b379da7320?context=explore)

          sudo docker build -t dmytrolypovyimonitoring --file Dockerfile.monitor .
          sudo docker images
          sudo docker push dmytrolypovyimonitoring
    Запустив обидва імеджі.
    
          sudo docker run -it --rm -p 80008000 dmytrolypovyidjango
          sudo docker run --net=host --rm -it dmytrolypovyimonitoring
9) Для того щоб отримати логи я використав  docker exec

          sudo docker ps
    Знайшов необхідний ID (8787641e0fe7) 
    
          sudo docker exec -it 8787641e0fe7 binbash   
          cat server.log
Частина з виведедених даних

        INFO 2020-11-24 175914,697 root  Ключ client_info, Значення python-requests2.22.0
        INFO 2020-11-24 180014,723 root  Сервер доступний. Час на сервері 24112020 160014
        INFO 2020-11-24 180014,724 root  Запитувана сторінка  httplocalhost8000health
        INFO 2020-11-24 180014,724 root  Відповідь сервера містить наступні поля
        INFO 2020-11-24 180014,724 root  Ключ date, Значення 24112020 160014
        INFO 2020-11-24 180014,724 root  Ключ current_page, Значення httplocalhost8000health
        INFO 2020-11-24 180014,724 root  Ключ server_info, Значення ['Linux', 'DIMA-VirtualBox', '5.4.0-52-generic', '#57-Ubuntu SMP Thu Oct 15 105700 UTC 2020', 'x86_64']
        INFO 2020-11-24 180014,724 root  Ключ client_info, Значення python-requests2.22.0
        INFO 2020-11-24 180114,737 root  Сервер доступний. Час на сервері 24112020 160114
        INFO 2020-11-24 180114,738 root  Запитувана сторінка  httplocalhost8000health
        INFO 2020-11-24 180114,738 root  Відповідь сервера містить наступні поля
        INFO 2020-11-24 180114,738 root  Ключ date, Значення 24112020 160114
        INFO 2020-11-24 180114,738 root  Ключ current_page, Значення httplocalhost8000health
# Chapter 3 - создание образов контейнеров из Dockerfile

### Python server - пример маленького сервера, который запускается в контейнере

#### `docker build -t python_server .` - собрать образ из Dockerfile в текущей директории с именем *python_server*

### `docker run --rm -dt -p <port-outside-container.>:<port-in-container> python_server` - запустить контейнер в фоновом режиме из образа *python_server*  
ключи:
- -dt - запустить контейнер в фоновом режиме
- --rm после остановки конейнер сразу же удалится
- --p <port-outside-container.>:<port-in-container> позволяет прокинуть порт наружу, привязывая <port-outside-container> к <port-in-container>, что позволяет 
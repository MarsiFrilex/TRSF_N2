# Система контроля

## Серверная часть приложения, построенная с помощью микросервисной архитектуры

### Схематичная визуализация архитектура системы
<img width="1169" height="489" alt="image" src="https://github.com/user-attachments/assets/1cb1b235-7cbb-4208-87f3-b0ba75368625" />

### Схема отношения сущностей в базе данных
<img width="1299" height="1092" alt="image" src="https://github.com/user-attachments/assets/54c122dc-6099-4327-bd21-2f2299802d39" />

### Маршруты микросервиса авторизации
<img width="1468" height="557" alt="image" src="https://github.com/user-attachments/assets/ea48446a-3dfa-4672-b57b-fe53c72ab271" />

### Маршруты микросервиса заказов
<img width="1468" height="786" alt="image" src="https://github.com/user-attachments/assets/ce579689-6d1e-4d07-abb3-f8ae7677b385" />

## Запуск проекта

Проект соберет и запустит docker-compose на порту 8000
```
docker-compose up -d --build
```

### Документация (swagger)
Станет доступна после запуска проекта по адресу:
http://localhost:8000/docs

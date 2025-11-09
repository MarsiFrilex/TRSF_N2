# Система контроля

## Серверная часть приложения, построенная с помощью микросервисной архитектуры

### Схематичная визуализация архитектура системы
<img width="1169" height="489" alt="image" src="https://github.com/user-attachments/assets/1cb1b235-7cbb-4208-87f3-b0ba75368625" />

### Схема отношения сущностей в базе данных
<img width="1299" height="1092" alt="image" src="https://github.com/user-attachments/assets/54c122dc-6099-4327-bd21-2f2299802d39" />

## Запуск проекта

Проект соберет и запустит docker-compose на порту 8000
```
docker-compose up -d --build
```

### Документация (swagger)
http://localhost:8000/docs

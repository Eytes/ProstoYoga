# ProstoYoga

## Описание приложения

WEB сервис для автоматизации управления и отслеживания данных о активностях пользователей, а также для записи на
практики йоги

## Возможности

> Пользователь - человек, посещающий практики и оплачивающий их

- Пользователь
    - [ ] Регистрация
    - [ ] Вход / Выход
    - [ ] Просмотр абонемента (профиль пользователя)
        - [ ] История посещений
        - [ ] Состояние абонемента
        - [ ] Оставшиеся посещения
        - [ ] Дата последнего занятия
        - [ ] Дата начала действия абонемента
        - [ ] Оплатить абонемент
            - [ ] Выбор из вариантов абонементов
    - [ ] Просмотр расписания практик
    - [ ] Просмотреть данные практике
    - [ ] Записаться на практику
    - [ ] Отменить запись на практику

---

> Мастер - специалист, проводящий практики

- Мастер
    - [ ] Вход / Выход
    - [ ] Просмотр расписания практик
    - [ ] Запрос на изменение параметров практики (перенос на другой день, отмена и прочее)

---

> Администратор - человек, имеющий высшие полномочия в системе. Владелец системы

- Администратор
  - [ ] Вход / Выход
  - [ ] Создание _Мастера_
  - [ ] Удаление _Мастера_
  - [ ] Блокировка пользователей
  - [ ] Просмотр абонементов (профилей пользователей)
    - [ ] История посещений
    - [ ] Состояние абонемента
    - [ ] Оставшиеся посещения
    - [ ] Дата последнего занятия
    - [ ] Дата начала действия абонемента
  - [ ] Просмотр расписания практик
  - [ ] Изменение расписания практик
  - [ ] Изменение данных практик
  
    - [ ] Вход / Выход
    - [ ] Создание _Мастера_
    - [ ] Удаление _Мастера_
    - [ ] Блокировка пользователей
    - [ ] Просмотр абонементов (профилей пользователей)
        - [ ] История посещений
        - [ ] Состояние абонемента
        - [ ] Оставшиеся посещения
        - [ ] Дата последнего занятия
        - [ ] Дата начала действия абонемента
    - [ ] Просмотр расписания практик
    - [ ] Изменение расписания практик
    - [ ] Изменение данных практик
## Абонемент пользователя

### Описание

Выступает в качестве профиля пользователя, через который можно просматривать активность и баланс

### Структура

- ФИО пользователя
- Номер телефона
- История посещений
- Состояние абонемента (Оплачен, не оплачен, заблокирован)
- Оставшиеся посещения
- Дата последнего занятия
- Дата начала действия абонемента
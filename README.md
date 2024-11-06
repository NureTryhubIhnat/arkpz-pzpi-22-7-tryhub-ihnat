ПЗПІ-22-7

Тригуб Ігнат

Тема: Програмна система інтелектуального моніторингу стану здоров'я людини з нагадуванням про
профілактичні обстеження

Опис теми:
Система збирає та аналізує дані про здоров'я користувача (пульс, рівень активності, сон, стрес) та за допомогою алгоритмів прогнозування визначає оптимальний час для профілактичних візитів,обстежень.
Також система може нагадувати необхідність прийому ліків, записів на огляди і підтримувати історію здоров'я користувача.

Основна функціональність:
Програмна система інтегрує функціонал збору даних зі здоров'я користувача, надає зручний інтерфейс для перегляду історії показників та рекомендацій, а також сповіщає про потребу у профілактичних заходах.

Складові проєкту:

1. Back-end
Back-end обробляє та зберігає дані користувача, забезпечує захист персональних даних і підтримує логіку аналітики.
Його функціонал включає:
- Збір даних з IoT-пристроїв (серцебиття, рівень активності, сон тощо).
- Обробка даних: алгоритми прогнозування, які аналізують дані для створення рекомендацій.
- Надсилання повідомлень: сповіщення про необхідність звернення до лікаря або прийому ліків.
- Інтернаціоналізація: підтримка різних мов, систем мір і форматів часу.
- Захист даних: шифрування інформації, обмеження доступу до конфіденційної інформації користувача.

2. Front-end
Front-end надає зручний інтерфейс для перегляду даних про стан здоров'я, аналізу показників і доступу
до рекомендацій. Основні елементи: - Особистий кабінет користувача: профіль з історією стану здоров'я,
де зібрані основні показники (серцебиття, сон, рівень стресу).
- Інформаційна панель з рекомендаціями щодо здорового способу життя.
- Нагадування: відображення повідомлень про прийом ліків, запис на огляд або профілактичні заходи.
- Графіки та звіти: візуалізація даних про здоров'я користувача для простішого розуміння динаміки.
- Підтримка двох мов (українська та англійська) для інтерфейсу.

3. IoT 
IoT-пристрої для збору інформації про стан здоров'я користувача:
- Датчики здоров'я: зчитують дані про частоту серцевих скорочень, артеріальний тиск, рівень активності, температуру тіла.
- Синхронізація з мобільними пристроями (фітнес-браслети, розумні годинники): автоматичний збір даних про здоров'я в реальному часі.
- Контроль показників: система порівнює поточні дані з допустимими значеннями та відправляє оповіщення у разі відхилень.
- Віддалене оновлення: можливість оновлення прошивки для підтримки нових функцій та сенсорів.

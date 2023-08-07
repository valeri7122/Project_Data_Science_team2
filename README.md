# Згорткова нейронна мережа для класифікації зображень (CIFAR-10)

![Image](https://raw.githubusercontent.com/SSP0d/source/main/logo.webp)
Цей проєкт представляє собою згорткову нейронну мережу для класифікації зображень з використанням датасету CIFAR-10. Метою проєкту є навчання моделі розпізнавати 10 класів зображень (літаки, автомобілі, птахи, коти, олені, собаки, жаби, коні, кораблі та вантажівки) та реалізація веб-інтерфейсу для її використання.

## Встановлення

1. Клонуйте репозиторій:

```
git clone https://github.com/valeri7122/Project_Data_Science_team2.git
```

2. Перейдіть до директорії проєкту:

```
cd Project_Data_Science_team2
```

3. Встановіть необхідні залежності:

```
pip install -r requirements.txt
```

4. Запустіть веб-інтерфейс:

```
python main.py
```

## Використання

Відкрийте браузер та перейдіть до:

```
http://localhost:8000
```

Завантажте зображення, натиснувши на кнопку **"Choose File"**

Після завантаження зображення, натисніть кнопку **"Classify"** для класифікації.

Результат класифікації буде показаний під зображенням.

## Архітектура використаної нейронної мережі

Згорткова нейронна мережа з методом виділення ознак має наступну архітектуру:

- Згортковий шар з 32 фільтрами розміром (3, 3) та функцією активації ReLU.
- Шар підвибірки з максимальним зведенням з розміром підвибірки (2, 2).
- Згортковий шар з 64 фільтрами розміром (3, 3) та функцією активації ReLU.
- Шар підвибірки з максимальним зведенням з розміром підвибірки (2, 2).
- Згортковий шар з 128 фільтрами розміром (3, 3) та функцією активації ReLU.
- Повнозв'язний шар з 512 нейронами та функцією активації ReLU.
- Випадковий Dropout (0.2) для зменшення перенавчання.
- Повнозв'язний шар з 256 нейронами та функцією активації ReLU.
- Випадковий Dropout (0.2).
- Повнозв'язний шар з 10 нейронами та функцією активації softmax для класифікації.

#

Згорткова нейронна мережа з методом донавчання має наступну архітектуру:

- Згортковий шар з 32 фільтрами розміром (3, 3) та функцією активації ReLU.
- Шар підвибірки з максимальним зведенням з розміром підвибірки (2, 2).
- Згортковий шар з 64 фільтрами розміром (3, 3) та функцією активації ReLU.
- Шар підвибірки з максимальним зведенням з розміром підвибірки (2, 2).
- Згортковий шар з 128 фільтрами розміром (3, 3) та функцією активації ReLU.
- Повнозв'язний шар з 256 нейронами та функцією активації ReLU.
- Повнозв'язний шар з 10 нейронами та функцією активації softmax для класифікації.

- Включенні у донавчання шари block4_conv1, block5_conv1 мережі VGG16

## Результати

Графік точності  
![Image](https://github.com/SSP0d/source/blob/main/Accuracy.jpeg)

Графік втрат  
![Image](https://github.com/SSP0d/source/blob/main/Loss.jpeg)

Результати роботи моделі на тестових даних
![Image](https://github.com/valeri7122/Project_Data_Science_team2/blob/main/model/VGG16_evaluation.jpg)

Графіки показують точність та втрати моделі на тренувальних, тестових та валідаційних даних протягом навчання.

Покриття тестами 
![Image](https://github.com/SSP0d/source/blob/main/Test_result.png)

## Контейнеризація

Даний проєкт є контейнеризованим в Docker. Ви можете побудувати контейнерний образ самостійно за допомогою команди:

```
docker build -t your-dockerhub-username/your-image-name:tag .
```

Або завантажити готовий образ з DockerHub:

```
docker pull sunriseuk/dsteamworkweb:final
```

Для запуску контейнера:

```
docker run -p 8000:8000 sunriseuk/dsteamworkweb:final
```

## Telegram бот

Для зручності використання додана можливість використання Telegram бота.

Перейдіть за посиланням

```
https://t.me/PicRec_AI_bot
```

Завантажте зображення та отримайте результат класиіфкації

Також ви маєте можливість налаштувати ваш бот для роботи з моделью.  

Для цого вкажіть API вашого бота у файлі congig.py

Післяцого запустіть

```
python telegram_bot.py
```

## Вкладення

### Проєкт містить:

- main.py: Веб-інтерфейс для класифікації зображень
- model.ipynb: Ноутбук з кодом нейромережі та навчанням
- weights.h5: Збережені ваги навченої моделі
- requirements.txt: Залежності проєкту
- telegram_bot.py Telegram бот
- README.md: Цей файл

## Автори

**Валерій Третяков**  
GitHub: [Valeri](https://github.com/valeri7122)  
LinkedIn: [Валерій Третяков](https://www.linkedin.com/in/валерій-третяков-512a9a275/)

**Сергій Підкопай**  
GitHub: [SSP0d](https://github.com/SSP0d)  
LinkedIn: [Serhii Pidkopai](https://www.linkedin.com/in/serhii-pidkopai-1734b7243/)

**Микола Присташ**
Mykola Prystash  
GitHub: [Sunriseuk](https://github.com/Sunriseuk)  
LinkedIn: [Mykola Prystash](https://www.linkedin.com/in/mykola-prystash-5bb18b287/)

**Василь Глущенко**  
GitHub: [Vasyl-Hlushchenko](https://github.com/Vasyl-Hlushchenko)  
LinkedIn: [Vasiliy Hlushchenko](https://www.linkedin.com/in/vasiliy-hlushchenko/)

## Ліцензія

Цей проєкт має ліцензію MIT - дивись LICENSE файл для деталей.

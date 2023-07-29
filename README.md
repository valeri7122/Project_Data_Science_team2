# Згорткова нейронна мережа для класифікації зображень (CIFAR-10)

![Image](https://raw.githubusercontent.com/SSP0d/source/main/applsci-12-12873-g001.webp)
Цей проєкт представляє собою згорткову нейронну мережу для класифікації зображень з використанням датасету CIFAR-10. Метою проєкту є навчання моделі розпізнавати 10 класів зображень (літаки, автомобілі, птахи, коти, олені, собаки, жаби, коні, кораблі та вантажівки) та реалізація веб-інтерфейсу для її використання.

## Встановлення

1. Клонуйте репозиторій:

```
git clone https://github.com/your-username/cifar-10-cnn.git
```

2. Перейдіть до директорії проєкту:

```
cd cifar-10-cnn
```

3. Встановіть необхідні залежності:

```
pip install -r requirements.txt
```

4. Запустіть веб-інтерфейс:

```
python app.py
```

## Використання

Відкрийте браузер та перейдіть до:

```
http://localhost:5000
```

Завантажте зображення, натиснувши на кнопку **"Choose File"**

Після завантаження зображення, натисніть кнопку **"Classify"** для класифікації.

Результат класифікації буде показаний під зображенням.

## Архітектура нейронної мережі

Використана згорткова нейронна мережа має наступну архітектуру:

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

## Результати

Графік точності та втрат

--тут повинен бути графік---

Графік показує точність та втрати моделі на тренувальних, тестових та валідаційних даних протягом навчання.

## Контейнеризація

Даний проєкт є контейнеризованим в Docker. Ви можете побудувати контейнерний образ самостійно за допомогою команди:

```
docker build -t cifar-10-cnn .
```

Або завантажити готовий образ з DockerHub:

```
docker pull username/cifar-10-cnn
```

Для запуску контейнера:

```
docker run -p 5000:5000 cifar-10-cnn
```

## Вкладення

### Проєкт містить:

- app.py: Веб-інтерфейс для класифікації зображень
- cifar10_cnn.ipynb: Ноутбук з кодом нейромережі та навчанням
- weights.h5: Збережені ваги навченої моделі
- requirements.txt: Залежності проєкту
- README.md: Цей файл

## Автори

**Сергій Підкопай**  
GitHub: [SSP0d](https://github.com/SSP0d)  
LinkedIn: [Serhii Pidkopai](https://www.linkedin.com/in/serhii-pidkopai-1734b7243/)

**Сергій Підкопай**  
GitHub: [SSP0d](https://github.com/SSP0d)  
LinkedIn: [Serhii Pidkopai](https://www.linkedin.com/in/serhii-pidkopai-1734b7243/)

**Микола Присташ**
Mykola Prystash  
GitHub: [Sunriseuk](https://github.com/Sunriseuk)  
LinkedIn:

## Ліцензія

Цей проєкт має ліцензію MIT - дивись LICENSE файл для деталей.

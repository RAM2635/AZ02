import pandas as pd

# 1. Создание DataFrame с данными
students_data = {
    'Имя': ['Ань', 'Бинь', 'Чанг', 'Зунг', 'Хан', 'Куанг', 'Линь', 'Минь', 'Нам', 'Тхи'],
    'Математика': [8, 9, 7, 6, 8, 9, 7, 5, 6, 8],
    'КиберСпорт': [7, 8, 9, 6, 7, 8, 6, 9, 8, 7],
    'Магия': [6, 7, 8, 9, 5, 6, 7, 8, 9, 6],
    'Зельеварение': [8, 9, 6, 7, 8, 9, 7, 6, 8, 7],
    'Драконоведение': [9, 8, 7, 6, 9, 8, 7, 9, 8, 6]
}

# Создание DataFrame
df = pd.DataFrame(students_data)

# Сохранение DataFrame в отдельный файл CSV
df.to_csv('students_grades.csv', index=False)

# 2. Вывод первых нескольких строк DataFrame для проверки данных
print("Первые несколько строк DataFrame:")
print(df.head())

# 3. Вычисление средней оценки по каждому предмету
average_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(average_scores.to_string(index=True))

# 4. Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores.to_string(index=True))

# 5. Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nQ1 и Q3 для оценок по математике:")
print(f"Q1: {Q1_math}, Q3: {Q3_math}, IQR: {IQR_math}")

# 6. Вычисление стандартного отклонения
std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение для оценок по каждому предмету:")
print(std_dev.to_string(index=True))

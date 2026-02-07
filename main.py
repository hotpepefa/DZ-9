import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Чтобы графики отображались корректно
plt.style.use('default')

# Загрузка данных из JSON
with open('events.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Преобразуем список событий в DataFrame
df = pd.DataFrame(data['events'])

print("Первые 5 строк данных:")
print(df.head())
print("\nИнформация о данных:")
print(df.info())

# Уникальные типы событий
print("\nУникальные типы событий:")
print(df['signature'].unique())

# Подсчет количества каждого типа события
signature_counts = df['signature'].value_counts()

print("\nРаспределение событий по типам:")
print(signature_counts)

# Визуализация (по сигнатурам)
plt.figure(figsize=(8, 10))
sns.countplot(data=df, x='signature')
plt.title('Распределение типов событий информационной безопасности')
plt.xlabel('Тип события (signature)')
plt.ylabel('Количество событий')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

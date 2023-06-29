from sklearn.linear_model import LinearRegression
import pandas as pd
from loguru import logger
import os
import config

logger.add(config.GEN_LOG_FILE_PATH, format="{time} - {level} - {extra[a]}  - {extra[b]} - {message}", level='INFO', rotation="00:00")

def fc(df: pd.DataFrame):
    
    # Удаляем предыдущий файл лога, если он существует
    if os.path.isfile(config.LOG_FILE_PATH):
        os.remove(config.LOG_FILE_PATH)

    handler = logger.add(config.LOG_FILE_PATH, format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {function} - {extra[a]}  - {extra[b]} - {message}", level='INFO')
    logger.configure(extra={'a': 'a', 'b': 'b'})
    logger.info(f"df.shape: {df.shape}")
    # Разделим данные на обучающую и тестовую выборки по значению в колонке partition
    train_data = df[df['partition'] == 'train']
    test_data = df[df['partition'] == 'test']

    # Логируем информацию
    logger.info('Вызов функции lr')
    # Выделим целевую переменную и признаки
    target_col = 'target'
    feature_cols = ['feature1', 'feature2']

    X_train, y_train = train_data[feature_cols], train_data[target_col]
    X_test, y_test = test_data[feature_cols], test_data[target_col]

    # Создадим объект модели линейной регрессии
    model = LinearRegression()

    # Обучим модель на обучающей выборке
    model.fit(X_train, y_train)

    # Сделаем прогноз на тестовой выборке
    y_pred = model.predict(X_test)
    logger.remove(handler)
    return y_pred


def add(a, b):
    # Удаляем предыдущий файл лога, если он существует
    if os.path.isfile(config.LOG_FILE_PATH):
        os.remove(config.LOG_FILE_PATH)

    handler = logger.add(config.LOG_FILE_PATH, format="{time} - {level} - {extra[a]} - {extra[b]} - {message}", level='INFO')
    
    logger.info(f"Вызов функции add с параметрами a={a}, b={b}")
    logger.remove(handler)
    return a + b

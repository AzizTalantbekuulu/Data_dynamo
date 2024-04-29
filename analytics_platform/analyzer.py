# analyzer.py

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from string import punctuation

# Загрузка необходимых ресурсов для nltk
nltk.download('punkt')
nltk.download('stopwords')

def analyze_text_data(data):
    """
    Функция для анализа текстовых данных.
    Принимает объект Data и возвращает результаты анализа.
    """
    # Получение текстовых данных из объекта Data
    text = data.description.lower()

    # Токенизация текста на слова
    words = word_tokenize(text)

    # Удаление стоп-слов (стоп-слова - это общие слова, которые не несут смысловой нагрузки)
    stop_words = set(stopwords.words('english') + list(punctuation))
    filtered_words = [word for word in words if word not in stop_words]

    # Подсчет частоты встречаемости слов
    word_freq = FreqDist(filtered_words)

    # Выделение наиболее часто встречающихся слов
    most_common_words = word_freq.most_common(5)

    # Токенизация текста на предложения
    sentences = sent_tokenize(text)

    # Подсчет количества предложений
    num_sentences = len(sentences)

    # Составление результата анализа
    analysis_result = {
        'most_common_words': most_common_words,
        'num_sentences': num_sentences
    }

    return analysis_result

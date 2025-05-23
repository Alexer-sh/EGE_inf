"""
Автоматическая камера производит растровые изображения размером 600 х 400 пикселей.
Для кодирования цвета каждого пикселя используется одинаковое целое количество байт, коды пикселей записываются в файл один за другим без промежутков.
Объем файла с изображением не может превышать 350 Кбайт без учета размера заголовка файла. Какое максимальное количество цветов можно использовать в палитре.
1) Найдем объем файла в байтах: 350Кбайт = 350 * 1024 байт = 358400 байт
2) Найдем количество байт на пиксель:  358400/(600*400) = 1,493... так как используется одинаковое целое количество байт, то получаем 1 байт на пиксель
3) Так как на 1 пиксель используется 1 байт  = 8 бит, то максимальное количество цветов равно 28=256
"""
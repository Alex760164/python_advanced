Для запуска приложения на новом компьютере нужно выполнить следующее:

1.Установка Git
    - проверяем наличие утилиты Git командой (git --version) 
    - команда установки для Linux Ubuntu (sudo apt update && sudo apt install git)
    
2.Выполняем проверку на наличие в системе менеджера пакетов pip
    - pip --version или pip3 --version
	Если менеджер пакетов pip не установлен, то устанавливаем его
    - sudo apt-get install python3-pip
		
3.Устанавливаем виртуальное окружение используя pip3
	- pip3 install virtualenv 
	
4.Склонировать репозиторий в рабочую папку, выполнив команду 
    - git clone https://gitlab.com/Alex760164/python_lesson.git

5.Устанавливаем недостающие пакеты согласно списку пакетов из файла requirements.txt
    - Проверяем список установленных пакетов с помощью команды pip list
    - pip install package_name (установка недостающих пакета(ов))
    Если есть необходимость установить весь перечень библиотек из файла requirements.txt в 
    текущее окружение, то нужно выполнить следующую команду:
    - pip3 install -r requirements.txt

6.В папке проекта создаем виртуальное окружение
	- virtualenv имя_виртуального_окружения

7.Инициализируем виртуальное окружение
	- source имя_виртуального_окружения/bin/activate
	или
	- python3 -m venv имя_виртуального_окружения    
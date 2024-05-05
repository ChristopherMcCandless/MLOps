# LAB4

## Скрипты
- создание датасета - data_creation.py
- модификация существующих файлов - step1_modify.py
- добавления новых файлов - step2_create_new_files.py

## Remote storage
Ссылка на удаленное хранилище файлов [gdrive](https://drive.google.com/drive/folders/1z8Wtd19T11QWqL7rDPYIjWw2749yMgdX)

## Работа с dvc

### Инициализация:
- `dvc init`
- `dvc add lab4/datasets/`
- `dvc remote add "lab4" gdrive://<folder_uid>`

### При внесении изменений:
- `dvc push`
- `dvc push -r lab4`

### Переключение между версиями
- `git checkout <commit_uid>|<master>`
- `dvc pull`



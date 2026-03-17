from appstore import get_top_apps

# Получаем топ-приложения
apps = get_top_apps()

# Показываем первые 5 приложений
for app in apps[:5]:
    print(app["name"], "-", app["artistName"], "-", app["id"])
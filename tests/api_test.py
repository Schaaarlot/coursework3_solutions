from run import app

# Сперва тестируем все посты
class TestAPI:

    def test_app_all_posts_status_code(self):
        """ Проверяем, получили ли нормальный список"""
        response = app.test_client().get('/api/posts', follow_redirects=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "Статус  код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_one_post_status_code(self):
        """ Проверяем, получен ли нужный пост"""
        response = app.test_client().get('/api/posts/1', follow_redirects=True)

        print(response.status_code)
        print(response.mimetype)

        assert response.status_code == 200, "Статус  код запроса поста неверный"
        assert response.mimetype == "application/json", "Получен не JSON"


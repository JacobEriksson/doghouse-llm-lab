import unittest
from types import SimpleNamespace
from unittest.mock import patch

from app import create_app


class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.update(TESTING=True)
        self.client = self.app.test_client()

    def test_pages_load_without_openai_api_key(self):
        for path in ('/', '/products', '/about', '/chatbot', '/designer'):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_chat_rejects_an_empty_message(self):
        response = self.client.post('/api/chat', json={'message': '  '})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'A non-empty message is required.'})

    def test_chat_rejects_a_non_string_message(self):
        response = self.client.post('/api/chat', json={'message': 123})

        self.assertEqual(response.status_code, 400)

    @patch('doghouse.chatbot.get_openai_client')
    def test_chat_returns_openai_response(self, get_openai_client):
        response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content='Welcome!'))]
        )
        get_openai_client.return_value.chat.completions.create.return_value = response

        result = self.client.post('/api/chat', json={'message': 'Hello'})

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.get_json(), {'response': 'Welcome!'})

    @patch('doghouse.routes.generate_doghouse_suggestion')
    def test_designer_confirmation_redirects_to_result(self, generate_suggestion):
        generate_suggestion.return_value = ('A cozy doghouse', 'https://example.com/image.png')

        response = self.client.post(
            '/confirm',
            data={'style': 'classic', 'size': 'small', 'color': 'blue'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn('/result?', response.location)
        self.assertIn('image_url=', response.location)


if __name__ == '__main__':
    unittest.main()

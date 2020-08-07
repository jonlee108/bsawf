from flask import url_for
from bs4 import BeautifulSoup


class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_faq(self, client):
        """FAQ page should respond with a success 200. """
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200
        
    def test_faq_title_exists(self, client):
        """FAQ page should have a <title> tag"""
        response = client.get(url_for('page.faq'))
        soup = BeautifulSoup(response.data, 'html.parser')
        assert soup.title.text
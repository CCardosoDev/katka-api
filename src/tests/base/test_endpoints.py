from django.urls import reverse


class TestHealth:

    def test_health(self, client):
        endpoint = reverse('health:index')
        resp = client.get(endpoint)
        assert resp.status_code == 200
        assert 'date' in resp.json()

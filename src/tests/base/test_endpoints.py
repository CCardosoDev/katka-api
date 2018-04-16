from django.urls import reverse

from pytest import raises


class TestHealth:

    def test_health(self, client):
        endpoint = reverse('health:index')
        resp = client.get(endpoint)
        assert resp.status_code == 200
        assert 'date' in resp.json()


class TestError:

    def test_error_index(self, client):
        endpoint = reverse('error:index')
        resp = client.get(endpoint)
        assert resp.status_code == 200

    def test_error_any(self, client):
        # test that an exception is raised when calling any error
        # TODO update this test to overwrite RAISE_EXCEPTIONS setting to be False
        endpoint = reverse('error:any')
        with raises(Exception) as ex:
            client.get(endpoint)

        assert str(ex.value) == 'Any exception'

    def test_error_silent(self, client):
        # test that no exception is raised on silent mode
        endpoint = reverse('error:silent')
        resp = client.get(endpoint)
        assert resp.status_code == 400

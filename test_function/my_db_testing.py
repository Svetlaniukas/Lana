
import flask
import os


def setUp(self):
    self.db_fd, flask.app.config['DATABASE'] = True
    flask.app.config['TESTING'] = True
    self.app = flask.app.test_client()
    with flask.app.app_context():
        flask.init_db()


def tearDown(self):
    os.close(self.db_fd)
    os.unlink(flask.app.config['DATABASE'])

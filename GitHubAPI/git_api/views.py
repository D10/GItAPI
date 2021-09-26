import requests
import datetime
import logging


from GitHubAPI.settings import BASE_DIR
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404

logger = logging.getLogger('mailings')


class GitApiViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny, ]

    def __init__(self):
        self.params = ['', '/pulls', '/forks', '/issues', '/unmerged_pulls']

    def get_kwargs_params(self):
        """Достаем путь ссылки из kwargs"""
        account = self.kwargs.get('account')
        repo = self.kwargs.get('repo')
        param = self.kwargs.get('param', '')
        if param:
            param = f'/{param}'
        return account, repo, param

    def get_params(self):
        """делаем валидацию пути запроса и url путь"""
        account, repo, param = self.get_kwargs_params()
        if param not in self.params:
            raise Http404
        if param == '/unmerged_pulls':
            days = datetime.timedelta(days=14)
            today = datetime.datetime.today()
            date = (today - days).strftime("%Y-%m-%d")
            link = f'search/issues?q=is:pr+is:unmerged+created:<={date}+repo:{account}/{repo}'
        else:
            link = f'repos/{account}/{repo}{param}'
        return link

    def get_response(self):
        """Получаем необходимые параметры из пути запроса,
        собираем ссылку github api и отдаем json из get запроса по этой сслыке"""
        link_param = self.get_params()
        link = f'https://api.github.com/' + link_param
        response = requests.get(link, data={'Accept': 'application/vnd.github.v3+json'}).json()
        return response

    @action(detail=True, methods=['get', ])
    def get_repo_details(self, *args, **kwargs):
        """Получаем запрос и из функции get_response получаем и отдаем ответ"""
        account, repo, param = self.get_kwargs_params()
        logger.info(f'GET api/repo_detal/{account}/{repo}{param}')
        repo_detail = self.get_response()
        return Response(repo_detail)

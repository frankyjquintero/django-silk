# -*- coding: utf-8 -*-
import factory
import factory.fuzzy

from silk.models import RequestSkill, Response, SQLQuery


HTTP_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'HEAD', 'OPTIONS']
STATUS_CODES = [200, 201, 300, 301, 302, 401, 403, 404]


class SQLQueryFactory(factory.django.DjangoModelFactory):

    query = factory.Sequence(lambda num: u'SELECT foo FROM bar WHERE foo=%s' % num)
    traceback = factory.Sequence(lambda num: u'Traceback #%s' % num)

    class Meta:
        model = SQLQuery


class RequestMinFactory(factory.django.DjangoModelFactory):

    path = factory.Faker('uri_path')
    method = factory.fuzzy.FuzzyChoice(HTTP_METHODS)

    class Meta:
        model = RequestSkill


class ResponseFactory(factory.django.DjangoModelFactory):
    request = factory.SubFactory(RequestMinFactory)
    status_code = factory.fuzzy.FuzzyChoice(STATUS_CODES)

    class Meta:
        model = Response

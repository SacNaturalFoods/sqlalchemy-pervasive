
from unittest import TestCase
from mock import Mock

from sqlalchemy.exc import InvalidRequestError

from sqlalchemy_pervasive import base


class PervasiveCompilerTests(TestCase):

    def compiler(self):
        return base.PervasiveCompiler(dialect=Mock(paramstyle='named'), statement=Mock())

    def test_get_select_precolumns(self):
        compiler = self.compiler()

        select = Mock(_distinct=None, _limit=None, _offset=None)
        self.assertEqual(compiler.get_select_precolumns(select), '')

        select._distinct = True
        self.assertEqual(compiler.get_select_precolumns(select), 'DISTINCT ')

        select._distinct = False
        select._limit = 10
        self.assertEqual(compiler.get_select_precolumns(select), 'TOP 10 ')

        select._limit = None
        select._offset = 10
        self.assertRaises(InvalidRequestError, compiler.get_select_precolumns, select)

    def test_limit_clause(self):
        compiler = self.compiler()
        self.assertEqual(compiler.limit_clause(Mock()), '')

    def test_visit_true(self):
        compiler = self.compiler()
        self.assertEqual(compiler.visit_true(Mock()), '1')

    def test_visit_false(self):
        compiler = self.compiler()
        self.assertEqual(compiler.visit_false(Mock()), '0')

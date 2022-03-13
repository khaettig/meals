from django import forms
from django.test import TestCase

from core.mixins import FormExceptionHandlerMixin


class NonFieldException(Exception):
    pass


class FieldException(Exception):
    pass


class NotHandledException(Exception):
    pass


class DummyForm(FormExceptionHandlerMixin, forms.Form):
    handled_exceptions = {
        NonFieldException: (None, "Something is wrong!"),
        FieldException: ("some_field", "Some field is wrong!"),
    }

    some_field = forms.CharField()


class FormExceptionHandlerMixinTest(TestCase):
    def setUp(self):
        super().setUp()
        self.form = DummyForm({"some_field": "data"})

    def test_no_exceptions_raised(self):
        with self.form.handles_specified_exceptions():
            pass

        self.assertEqual(0, len(self.form.errors))

    def test_non_field_exception_raised(self):
        with self.form.handles_specified_exceptions():
            raise NonFieldException

        self.assertEqual({"__all__": ["Something is wrong!"]}, self.form.errors)

    def test_field_exception_raised(self):
        with self.form.handles_specified_exceptions():
            raise FieldException

        self.assertEqual({"some_field": ["Some field is wrong!"]}, self.form.errors)

    def test_not_handled_exception_raised(self):
        with self.assertRaises(NotHandledException):
            with self.form.handles_specified_exceptions():
                raise NotHandledException

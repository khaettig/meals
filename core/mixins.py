class FormExceptionHandlerMixin:
    handled_exceptions = {}

    def handles_specified_exceptions(self):
        return FormExceptionHandlerContextManager(self)

    def handle_exception(self, exception_type):
        self.add_error(*self.handled_exceptions[exception_type])


class FormExceptionHandlerContextManager:
    def __init__(self, form):
        self._form = form

    def __enter__(self):
        pass

    def __exit__(self, exception_type, *args):
        if exception_type in self._form.handled_exceptions:
            self._form.handle_exception(exception_type)
            return True

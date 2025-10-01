class NoopSession:
    class NoopBind:
        class NoopConnect:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                pass

        def connect(self):
            return self.NoopConnect()

    bind = NoopBind()

    def add(self, *args, **kwargs):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def execute(self, *args, **kwargs):  # noqa: ARG002
        return None

    def query(self, *args, **kwargs):  # noqa: ARG002
        return []

    def close(self):
        pass

    def refresh(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass

    def get(self, *args, **kwargs):  # noqa: ARG002
        return None

    def exec(self, *args, **kwargs):  # noqa: ARG002
        class _NoopResult:
            def first(self):
                return None

            def all(self):
                return []

            def one_or_none(self):
                return None

        return _NoopResult()

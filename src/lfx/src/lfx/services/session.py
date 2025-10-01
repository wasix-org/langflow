"""Lightweight session implementations for lfx package."""


class NoopSession:
    """No-operation session mirroring a synchronous SQLAlchemy/SQLModel session.

    Methods are implemented as no-ops to allow calling code to run without
    a real database. Useful for testing or when DB is disabled.
    """

    class NoopBind:
        class NoopConnect:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                pass

        def connect(self):
            return self.NoopConnect()

    bind = NoopBind()

    # CRUD-like APIs
    def add(self, *args, **kwargs):  # noqa: ARG002
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

    def refresh(self, *args, **kwargs):  # noqa: ARG002
        pass

    def delete(self, *args, **kwargs):  # noqa: ARG002
        pass

    def get(self, *args, **kwargs):  # noqa: ARG002
        return None

    # SQLModel-style API
    def exec(self, *args, **kwargs):  # noqa: ARG002
        class _NoopResult:
            def first(self):
                return None

            def all(self):
                return []

            def one_or_none(self):
                return None

        return _NoopResult()

    # Context manager helpers
    @property
    def no_autoflush(self):
        """Context manager that disables autoflush (no-op implementation)."""
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass

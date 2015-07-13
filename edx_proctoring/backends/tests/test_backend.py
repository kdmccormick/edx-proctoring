"""
Tests for backend.py
"""

from django.test import TestCase
from edx_proctoring.backends.backend import ProctoringBackendProvider
from edx_proctoring.backends.null import NullBackendProvider


class TestBackendProvider(ProctoringBackendProvider):
    """
    Implementation of the ProctoringBackendProvider that does nothing
    """

    def register_exam_attempt(self, exam, time_limit_mins, attempt_code,
                              is_sample_attempt, callback_url):
        """
        Called when the exam attempt has been created but not started
        """
        return 'testexternalid'

    def start_exam_attempt(self, exam, attempt):
        """
        Method that is responsible for communicating with the backend provider
        to establish a new proctored exam
        """
        return None

    def stop_exam_attempt(self, exam, attempt):
        """
        Method that is responsible for communicating with the backend provider
        to establish a new proctored exam
        """
        return None


class PassthroughBackendProvider(ProctoringBackendProvider):
    """
    Implementation of the ProctoringBackendProvider that just calls the base class
    """

    def register_exam_attempt(self, exam, time_limit_mins, attempt_code,
                              is_sample_attempt, callback_url):
        """
        Called when the exam attempt has been created but not started
        """
        return super(PassthroughBackendProvider, self).register_exam_attempt(
            exam,
            time_limit_mins,
            attempt_code,
            is_sample_attempt,
            callback_url
        )

    def start_exam_attempt(self, exam, attempt):
        """
        Method that is responsible for communicating with the backend provider
        to establish a new proctored exam
        """
        return super(PassthroughBackendProvider, self).start_exam_attempt(
            exam,
            attempt
        )

    def stop_exam_attempt(self, exam, attempt):
        """
        Method that is responsible for communicating with the backend provider
        to establish a new proctored exam
        """
        return super(PassthroughBackendProvider, self).stop_exam_attempt(
            exam,
            attempt
        )


class TestBackends(TestCase):
    """
    Miscelaneous tests for backends.py
    """

    def test_raises_exception(self):
        """
        Makes sure the abstract base class raises NotImplementedError
        """

        provider = PassthroughBackendProvider()

        with self.assertRaises(NotImplementedError):
            provider.register_exam_attempt(None, None, None, None, None)

        with self.assertRaises(NotImplementedError):
            provider.start_exam_attempt(None, None)

        with self.assertRaises(NotImplementedError):
            provider.stop_exam_attempt(None, None)

    def test_null_provider(self):
        """
        Assert that the Null provider does nothing
        """

        provider = NullBackendProvider()

        self.assertIsNone(provider.register_exam_attempt(None, None, None, None, None))
        self.assertIsNone(provider.start_exam_attempt(None, None))
        self.assertIsNone(provider.stop_exam_attempt(None, None))
from django.test import TestCase
from rest_framework import serializers


class DRFSerializerTest(TestCase):
    def test_empty_serializer(self):
        class EmptySerializer(serializers.Serializer):
            pass

        serializer = EmptySerializer()

        assert serializer.data == {}

    def test_serializer_empty_data(self):
        class MySerializer(serializers.Serializer):
            name = serializers.CharField()

        serializer = MySerializer()

        assert serializer.data == {'name': ''}


class SerializerInstanceTest(TestCase):
    # Serializer 객체 생성시, data 인자에 값을 넘겨서 생성한 경우 테스트
    def setUp(self):
        class MySerializer(serializers.Serializer):
            name = serializers.CharField()

        self.serializer = MySerializer(data={'name': 'test'})

    def test_data_property(self):
        # `.data` 접근시 에러발생
        error_msg = (
            'When a serializer is passed a `data` keyword argument'
            ' you must call `.is_valid()`'
            ' before attempting to access the serialized `.data` representation.'
            '\n'
            'You should either call `.is_valid()` first, or access `.initial_data` instead.'
        )
        with self.assertRaisesMessage(AssertionError, error_msg):
            assert self.serializer.data

    def test_errors_property(self):
        error_msg = 'You must call `.is_valid()` before accessing `.errors`.'
        with self.assertRaisesMessage(AssertionError, error_msg):
            assert self.serializer.errors

    def test_initial_data_property(self):
        assert self.serializer.initial_data == {'name': 'test'}

    def test_is_valid_method(self):
        assert self.serializer.is_valid() is True
        # is_valid() 호출 후 .data 도 접근가능해짐
        assert self.serializer.data == {'name': 'test'}


class SerializerInstanceTest2(TestCase):
    # Serializer 객체 생성시, data 인자에 값을 넘기지 않은 경우 테스트
    def setUp(self):
        class MySerializer(serializers.Serializer):
            name = serializers.CharField()

        self.serializer = MySerializer({'name': 'test'})  # 첫 번째 인자(instance 인자)에 만 값을 넘김. data 인자로는 값을 넘기지 않음

    def test_data_property(self):
        assert self.serializer.data == {'name': 'test'}

    def test_errors_property(self):
        error_msg = 'You must call `.is_valid()` before accessing `.errors`.'
        with self.assertRaisesMessage(AssertionError, error_msg):
            assert self.serializer.errors

    def test_initial_data_property(self):
        with self.assertRaises(AttributeError):
            assert self.serializer.initial_data

    def test_is_valid_method(self):
        error_msg = 'Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.'
        # 번역 : serializer 인스턴스를 인스턴스화 할 때`data =`키워드 인수가 전달되지 않았으므로`.is_valid ()`를 호출 할 수 없습니다.
        with self.assertRaisesMessage(AssertionError, error_msg):
            self.serializer.is_valid()

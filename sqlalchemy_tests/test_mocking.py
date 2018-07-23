from mock import Mock
import pytest
import mocking

@pytest.fixture
def mock_originalClass():
    return Mock(spec=mocking.originalClass)

@pytest.fixture(params=[('a',1,2),('a','b')])
def parameterized_fixture(request):
    return request.param

def test_oc_call(mock_originalClass):
    a = mock_originalClass.someMethod(1,2,3)
    mock_originalClass.someMethod.assert_any_call(1,2,3)

def test_oc_wrong_parameter(parameterized_fixture):
    a = mocking.originalClass()
    with pytest.raises(TypeError):
        a.someMethod(parameterized_fixture)

def test_mock_returns(mock_originalClass):
    mock_originalClass.someMethod.return_value = 5
    b = mock_originalClass.someMethod()
    assert b == 5
    
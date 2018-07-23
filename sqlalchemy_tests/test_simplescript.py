import simplescript
import pytest

@pytest.fixture(scope='function', params = [(1,2,3),(-4,7,3),(-3,-6,-9),(2,-2,0), ('ab','cd','abcd')])
def someFixture(request):
    def fin():
        print('\n\nthe end')
    request.addfinalizer(fin)
    return request.param


def test_add(someFixture):
    print('\nstarting the test\n')
    x, y, z = someFixture
    print('expected: ' + str(z))
    print('found: ' + str(x + y) + '\n')
    assert x + y == z
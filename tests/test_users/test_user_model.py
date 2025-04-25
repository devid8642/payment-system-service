from payment_system_service.users.models import User


def test_user_str_representation():
    user = User(
        name='João',
        email='joao@example.com',
        document='12345678900',
        type='COMMON',
    )
    assert str(user) == 'João (joao@example.com)'


def test_set_password():
    user = User(
        name='Maria',
        email='maria@example.com',
        document='09876543210',
        type='COMMON',
    )
    user.set_password('senha_segura_123')

    assert user.password_hash != 'senha_segura_123'
    assert user.password_hash.startswith('md5$')   # MD5 used in tests


def test_check_password_correct():
    user = User(
        name='Carlos',
        email='carlos@example.com',
        document='11223344556',
        type='COMMON',
    )
    user.set_password('senha_teste')
    assert user.check_password('senha_teste') is True


def test_check_password_incorrect():
    user = User(
        name='Ana',
        email='ana@example.com',
        document='66554433221',
        type='MERCHANT',
    )
    user.set_password('senha_certa')
    assert user.check_password('senha_errada') is False

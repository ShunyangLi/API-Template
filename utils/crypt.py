"""
用于数据加密
"""
import jwt
from app import app
from flask_restplus import abort
# serializer for JWT
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# exceptions for JWT
from itsdangerous import SignatureExpired


def encryption(data, expires_in=3600):
    """
    加密json
    :param data: 需要加密的数据
    :param expires_in: 过期时间
    :return: 返回加密的str
    """
    s = Serializer(app.config['SECRET_KEY'], expires_in=expires_in)
    return s.dumps(data).decode("utf-8")


def decryption(token):
    """
    解密token到json数据
    :param token: 密文
    :return: 解密的数据
    """
    s = Serializer(app.config['SECRET_KEY'])

    try:
        data = s.loads(token)
        return data
    except SignatureExpired:
        abort(403, 'Token expired')
    except:
        abort(403, 'Unknown error')


def encode_token(payload):
    """
    官网：https://pyjwt.readthedocs.io/en/latest/usage.html
    {'a': 'b'}的形式
    :param payload: dict 需要加密的信息
    """
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token.decode("utf-8")


def decode_token(token):
    """
    decode token get payload
    :param token: token
    """
    try:
        return jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
    except jwt.ExpiredSignatureError:
        # 时间过期了
        abort(400, 'token expired')
    except jwt.exceptions.InvalidTokenError:
        # token 错误
        abort(400, 'incorrect token')
    except jwt.exceptions.DecodeError:
        # something error
        pass
    return None
    
    
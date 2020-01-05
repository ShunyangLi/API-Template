from flask import request
from flask_restful import reqparse
from flask_restplus import abort
from werkzeug.datastructures import FileStorage


"""
This file contain all the functions which need to be used
when get the request args, header and files
"""


def get_request_args(arg_name, arg_type=str, required=True):
    """
    It will get the argument value according to the name.
    And it will check whether required
    :param arg_name: the argument name
    :param arg_type: the argument type
    :param required: whether necessary
    :return: the argument value
    """

    parser = reqparse.RequestParser()
    parser.add_argument(arg_name, type=arg_type)
    args = parser.parse_args()

    res = args.get(arg_name)

    if res is None and required:
        abort(400, "Can not the arg: %s" % arg_name)

    return res


# get the header token
def get_header(req, required=True, header_name='Authorization'):
    """
    get the result from header
    :param req: the request object
    :param required: check whether the header required.
    :param header_name: the arg name
    :return: the result can from header
    """

    res = req.headers.get(header_name, None)
    if not res and required:
        abort(400, "Can not find the arg: %s in the header" % header_name)

    return res


def get_request_file(arg_name, required=True):
    """
    Get files in the requests according to file name
    :param arg_name: the files name
    :return: list of files or None
    """
    parser = reqparse.RequestParser()
    parser.add_argument(arg_name, location='files', type=FileStorage, action='append')
    args = parser.parse_args()
    files = args.get(arg_name)

    if files is None and required:
        abort(400, "Can not the arg: %s" % arg_name)

    return files

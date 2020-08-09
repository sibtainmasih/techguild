import argparse
from contactbook.handlers import add_contact, search_contacts


def __set_add_contact_parser(parser_obj):
    parser_obj.set_defaults(handler_func=add_contact)
    parser_obj.add_argument(
        "-n", "--name", type=str, required=True, action="store", dest="contact_name"
    )
    parser_obj.add_argument(
        "-a",
        "--address",
        type=str,
        required=True,
        action="store",
        dest="contact_address",
    )
    parser_obj.add_argument(
        "-c", "--city", type=str, required=True, action="store", dest="contact_city"
    )
    parser_obj.add_argument(
        "-p", "--phone", type=str, required=True, action="store", dest="contact_phone",
    )
    parser_obj.add_argument(
        "-e", "--email", type=str, required=False, action="store", dest="contact_email"
    )


def __set_search_contact_parser(parser_obj):
    parser_obj.set_defaults(handler_func=search_contacts)
    parser_obj.add_argument(
        "-k",
        "--key",
        type=str,
        required=True,
        action="store",
        dest="search_field",
        help="Name of the field to search on",
    )
    parser_obj.add_argument(
        "-v",
        "--value",
        type=str,
        required=True,
        action="store",
        dest="search_field_value",
        help="Value to match against the field",
    )


def get_parser():
    parser = argparse.ArgumentParser(description="Contact Book Application")

    sub_parser = parser.add_subparsers(help="Operations of Contact Book")

    add_contact_parser = sub_parser.add_parser("add")
    __set_add_contact_parser(add_contact_parser)

    search_contacts_parser = sub_parser.add_parser("search")
    __set_search_contact_parser(search_contacts_parser)

    # TODO - Add parsers for update and delete

    return parser

import logging

from .models import setup_database, save_contact, get_contacts

logger = logging.getLogger(__name__)


def storage_setup(arguments):
    """
    Handles storage setup for application.
    """
    logger.info("Setting storage structure.")
    setup_database()
    logger.info("Storage setup successful.")


def add_contact(arguments):
    """
    Handles storing of a new client record
    """
    # TODO - Add validation for arguments
    record_id = save_contact(
        arguments.contact_name,
        arguments.contact_address,
        arguments.contact_city,
        arguments.contact_phone,
        arguments.contact_email,
    )
    logger.info("Contact added successfully.")
    logger.debug(f"New record id = {record_id}")


def update_contacts(arguments):
    print("update_contacts invoked")
    print(arguments)
    # raise NotImplementedError("Implement Update Functionality")


def search_contacts(arguments):
    get_contacts(arguments.search_field, arguments.search_field_value)


def delete_contacts(arguments):
    print("delete_contacts invoked")
    print(arguments)
    # raise NotImplementedError("Implement Delete Functionality")

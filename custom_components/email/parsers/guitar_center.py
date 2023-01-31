import logging

from bs4 import BeautifulSoup
from ..const import EMAIL_ATTR_BODY


_LOGGER = logging.getLogger(__name__)
ATTR_GUITAR_CENTER = 'guitar_center'
EMAIL_DOMAIN_GUITAR_CENTER = 'guitarcenter.com'


def parse_guitar_center(email):
    """Parse Guitar Center tracking numbers."""
    tracking_numbers = []

    soup = BeautifulSoup(email[EMAIL_ATTR_BODY], 'html.parser')
    elements = [element for element in soup.find_all('td')]
    for element in elements:
        _LOGGER.error(element.text)
        if 'Tracking:' in element.text:
            tracking_link = element.find("a", recursive=False)
            tracking_number = tracking_link.text
            _LOGGER.error(tracking_number)
            if tracking_number not in tracking_numbers:
                tracking_numbers.append(tracking_number)

    return tracking_numbers

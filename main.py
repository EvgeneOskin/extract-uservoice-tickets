import json
import logging
from itertools import count
import uservoice


def main():
    logging.basicConfig(level=logging.INFO)
    client = uservoice_client()
    with client.login_as_owner() as owner:
        tickets = extract_all_tickets(owner)
        echo(list(tickets))


def extract_all_tickets(owner):
    for page in count(1):
        page = extract_tickets(owner, page)
        tickets_page = page['tickets']

        for i in tickets_page:
            yield i
        if not tickets_page:
            break


def extract_tickets(owner, page):
    url = "/api/v1/tickets.json?per_page=500&page={}".format(page)
    tickets_page = owner.get(url)
    logging.info('Page %s', tickets_page['response_data']['page'])
    return tickets_page


def echo(item):
    print(json.dumps(item))


def uservoice_client():
    subdomain_name = 'serverauditor'
    api_key = 'kFrl5U0ECy6vK7nL4AJQ'
    api_secret = 'xEb2AG8A84jbeCZBUiBoEQLmSSGzS9AbeTXWRXeCjE'
    return uservoice.Client(subdomain_name, api_key, api_secret)


if __name__ == '__main__':
    main()

import json
import logging
import uservoice


def main():
    logging.basicConfig(level=logging.INFO)
    client = uservoice_client()
    with client.login_as_owner() as owner:
        extract_all_tickets(owner)


def extract_all_tickets(owner):
    tickets = []
    last_page = 1

    page = extract_tickets(owner, last_page)

    tickets_page = page['tickets']
    last_page = page['response_data']['page']

    tickets += tickets_page
    echo(tickets)


def extract_tickets(owner, page):
    url = "/api/v1/tickets.json?per_page=2&page={}".format(page)
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

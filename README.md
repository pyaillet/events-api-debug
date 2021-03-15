# Injector and connector to debug Akeneo PIM Events API

## How to use ?

Clone the repo.
Launch `pip3 install -r requirements.txt`.

Configure a connector for injection in the PIM.
Configure the injector `client.py` with your `client_id`, `secret`, `username`, `password`, `host`.

Configure a connector for the webhook configuration.

## Launch

Launch the connector with `python3 ./serve.py`.
The connector will log the requests received and total requests and events count.

Launch the injector with `python3 ./client.py`.
The injector will retrieve the 100 first product identifier and cycle between 
enabling/disabling them to trigger events.

## Tips

When using from a computer without a public IP, you can use [ngrok](https://ngrok.com/)
to make it accessible.

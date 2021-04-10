from discogs_client import DiscogsClient


if __name__ == "__main__":
    cli = DiscogsClient()
    token, token_secret = cli.get_token()
    print(cli.search("nirvana", token=token_secret))

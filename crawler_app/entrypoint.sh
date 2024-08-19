#!/bin/bash

# Run scrapyd-deploy to deploy the Scrapy project without building an egg file
scrapyd-deploy

# Start any other commands if needed
exec "$@"
# Twitter sliding window

Script that deletes tweets (and likes) older than a specified age, effectively creating a sliding window personal timeline

## Getting Started

Everything is very basic, and leaves the running part to you so some programming knowledge is required, you can
run the script on a server if you have access to one, or simply create a cron job in a machine you use regularly.

### Prerequisites

You only need python 3.7 or above, and [pipenv](https://pipenv.readthedocs.io/en/latest/) installed (and your [twitter access tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens))

### Installing

After downloading the code, you need to rename `config_template.ini` to `config.ini` and adjust the values.

In the `twitter` section you need to fill the 4 values required to use the api, you must follow the instructions here to get them: https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens

In the `application` section simply input the time you want your tweets and likes deleted under the `age` entry, the following formats are accepted:

|Character|Meaning|Example
|---|---|---
|s|Seconds|'60s' -> 60 Seconds
|m|Minutes|'5m'  -> 5 Minutes
|h|Hours|'24h' -> 24 Hours
|d|Days|'7d'  -> 7 Days

After that, simply run:

```
pipenv run python run.py
```

If you want to execute the code once every hour (the frequency depends on the _age_ granularity in the config file and
where you have the code running) you can add the following line to your cron file (adjust accordinlgy)

```
0 * * * * cd /git/twitter-sliding-window && ./execute.sh
```

**WARNING**: This will delete all the tweets older than the specified age, if you followed all the steps and get it running I assume you know what you're doing,
but maybe you'd want to request [your archive](https://twitter.com/settings/account) before doing it

Also be aware that the twitter api only let's you access the latest 3200 tweets, so if you have more than that you'd need to initially delete them some other way
(there are paid services that do it), after that just ensure that you don't tweet more than 3200 times in the age window you set in this script.

## Running the tests

Tests pending

## Authors

**Juan Manuel Formoso** - *Initial work* - [juanformoso](https://github.com/juanformoso)


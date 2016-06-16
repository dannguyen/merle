# merle
A command-line tool for getting meta information from a URL


# Todo:

- [x] Create a Document class so that dates can be parsed from URLs
- [?] Integrate newspaper egg
-  [x] `title = list(extract_element('title', f).values())[0]`
- [ ] FetchedResource to Dictionary
- [ ] image url fetcher
- [ ] Make source list
- [ ] Turn into CLI


# Current state of usage:

```sh
$ python merle/cli.py 'http://www.nytimes.com/2016/06/16/sports/olympics/world-anti-doping-agency-russia-cheating.html?hp&action=click&pgtype=Homepage'
```

Result:

```yaml
slug: even-with-confession-of-cheating-worlds-doping-watchdog-did-nothing-www-nytimes-com
url: http://www.nytimes.com/2016/06/16/sports/olympics/world-anti-doping-agency-russia-cheating.html?hp&action=click&pgtype=Homepage
title: Even With Confession of Cheating, World’s Doping Watchdog Did Nothing
description: Even With Confession of Cheating, World’s Doping Watchdog Did Nothing
fetched_at: 2016-06-15 22:26:18.723174
published_at: '2016-06-16'
authors:
- Rebecca R. Ruiz
- Juliet Macur
- Ian Austen
word_count: 3180
excerpt: 'Dr. Ljungqvist, vice president of WADA from 2008 to 2013, said he repeatedly
  raised concerns about Russia. The agency considered penalties against the nation,
  but in the end, he said, the inherent conflicts of interests within WADA and the
  Olympic movement won: The matter was set aside because “it was too politically infected,”
  he said. “You could say I was ...'
```

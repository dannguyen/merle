# merle

A command-line tool for getting meta information from a URL

Uses the [newspaper3k](https://pypi.python.org/pypi/newspaper3k) package and some custom HTML parsing to extract attributes.


# Current state of usage:

```sh
$ pip install merle
$ merle http://www.newyorker.com/magazine/1988/11/07/counting-votes
```

Result:

```yaml
slug: counting-votes-new-yorker-www-newyorker-com
fetched_at: 2016-06-16 11:51:14.707606
url: http://www.newyorker.com/magazine/1988/11/07/counting-votes
title: Counting Votes - The New Yorker
description: |
  Counting Votes - The New Yorker
published_at: 1988-11-07
authors:
  - Richard Brody
  - Gilad Edelman
  - Josephine Livingstone
  - Jason Adam Katzenstein
  - Farid Farid
  - Louis Menand
  - Margaret Talbot
  - Sarah Hutto
word_count: 20691
excerpt: |
  During the past quarter of a century, with hardly anyone noticing, the inner workings of democracy have been computerized. All our elections, from mayor to President, are counted locally, in about ten thousand five hundred political jurisdictions, and gradually, since 1964, different kinds of computer-based voting systems have been installed in town after town, city after city, county after county. ...
```



# Todo:

- [x] Create a Document class so that dates can be parsed from URLs
- [?] Integrate newspaper egg
- [X] `title = list(extract_element('title', f).values())[0]`
- [ ] FetchedResource to Dictionary
- [ ] image url fetcher
- [X] Turn into CLI
- [ ] Make source list in data/publiushers.txt

# Broken URLs

- http://www.stanforddaily.com/2013/09/17/transfer-student-experience-offers-rewards-challenges/

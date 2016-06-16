# merle
A command-line tool for getting meta information from a URL


# Todo:

- [x] Create a Document class so that dates can be parsed from URLs
- [?] Integrate newspaper egg
- [X] `title = list(extract_element('title', f).values())[0]`
- [ ] FetchedResource to Dictionary
- [ ] image url fetcher
- [ ] Make source list
- [X] Turn into CLI


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

## Reference
### Setup

1. Add your site and author details in `_config.yml`.
2. Add your Google Analytics and Disqus keys to `_config.yml`.
3. Get a workflow going to see your site's output (with [CloudCannon](https://app.cloudcannon.com/) or Jekyll locally).

### Develop

Frisco was built with [Jekyll](http://jekyllrb.com/) version 3.3.1, but should support newer versions as well.  
Install the dependencies with [Bundler](http://bundler.io/):

~~~bash
$ bundle install
~~~

~~~bash
$ bundle exec jekyll serve
~~~

### Posts

* Add, update or remove a post in the *Posts* collection.
* The **Staff Author** field links to members in the **Staff Members** collection.
* Documentation pages are organised in the navigation by category, with URLs based on the path inside the `_docs` folder.
* Change the defaults when new posts are created in `_posts/_defaults.md`.

### Contact Form

* Preconfigured to work with CloudCannon, but easily changed to another provider (e.g. [FormSpree](https://formspree.io/)).

### Staff

* Reused around the site to save multiple editing locations.

### Footer

* Exposed as a data file to give clients better access.
* Set in the *Data* / *Navigation* section.

### Footer

* Exposed as a data file to give clients better access.
* Set in the *Data* / *Footer* section.


### Hosting

- https://domains.google/

```bash
$ dig ailever.github.io +nostats +nocomments +nocmd
```

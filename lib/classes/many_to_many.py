class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        author_articles = {}
        for article in self.articles():
            author_articles[article.author] = author_articles.get(article.author, 0) + 1
        return [author for author, count in author_articles.items() if count > 2]

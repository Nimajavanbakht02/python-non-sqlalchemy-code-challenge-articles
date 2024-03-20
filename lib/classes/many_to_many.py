class Article:
    #! An all class attribute to store all instances of the Article class.
    all = []
    #! Python's class constructor
    def __init__(self, author, magazine, title):
    #! An __init__ method to initialize the author, magazine, and title attributes of an article instance.
    #! Setter methods for the title, author, and magazine attributes with validation checks.
    #! Getter methods as well for the corresponding attributes
        self.author = author
        self.magazine = magazine
        self.title = title
    #! IMPORTANT to always use type(self) instead of the class name
        type(self).all.append(self)

    
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    #! Checking if the title is a string and that it is between 5-50 characters
    def title(self, new_title):
            if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
                self._title = new_title
            else:
                raise ValueError("Title must be a string and between 5 and 50 characters!!")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    #! Checking if the author being passed through is an instance of the Author class
    def author(self, author):
            if isinstance(author, Author):
                self._author = author
            else:
                raise ValueError("Author must be an instance of the Author class!!")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    #! Checking if the magazine being passed through is an instance of the Magazine class
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of the Magazine class!!")
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    #! Getter method that returns the value of the _name attribute
    def name(self):
        return self._name 
    
    @name.setter
    #! Checking if the author name is a class string and ensures that the field cannot be empty
    def name(self, name):
        if isinstance(name, str) and name != "" and not hasattr(self, 'name'):
            self._name = name
        else:
            raise ValueError("Author name must be a string and cannot be empty!!")

    def articles(self):
    #! Defines the articles method and uses list comprehension to iterate all of the articles in Article.all list
        return [article for article in Article.all if article.author == self]

    def magazines(self):
    #! Uses set comprehension instead to iterate over the articles returned by the articles method
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
    #! The method creates a new Article object with the author, magazine, and title provided as arguments
        return Article(self, magazine, title)
    
    def add_magazine(self, magazine):
    #! The method returns a list containing the instance of the class and the provided magazine argument
        return [self, magazine]

    def topic_areas(self):
    #! The method returns a list of unique topic areas of the articles written by the author. 
    #! If the author has no articles, it returns None.
        if self.articles():
            return list(set(article.magazine.category for article in self.articles()))
        else:
            return None

class Magazine:
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    #! The setter method checks if the provided name is a string and has a length between 2 and 16 characters.
    #! If the conditions are met, it assigns the name to the private attribute _name.
    #! If not, it raises a ValueError with an appropriate error message.
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string and between 2 and 16 characters!!")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    #! The setter method checks if the provided category is a string and that it has more than 0 characters
    #! If the conditions are met, if assigns the category to the private attribute _category
    #! If not, it raises the ValueError
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a string and greater than 0 characters!!")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
    #! The method checks if the instance has any articles by calling the articles method.
    #! If there are articles, it uses list comphrension to iterate over the articles and extract the title attribute
    #! It returns the list of titles, returns None if there are no articles
        if self.articles():
            return [article.title for article in self.articles()]
        else:
            return None

    def contributing_authors(self):
    #! contributing_authors first initializes an empty dictionary called author_article_count
    #! It then iterates over the articles associated with the instance and checks
    #! if the author of each article is an instance of the Author class.
    #! If so, it updates the count of articles for that author in the author_article_count dictionary.
    #! After that, it creates a list of authors who have contributed more than 2 articles
    #! by filtering the author_article_count dictionary.
    #! Lastly, it returns the list of contributing authors or None if there are no contributing authors.
        author_article_count = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                if article.author in author_article_count:
                    author_article_count[article.author] += 1
                else:
                    author_article_count[article.author] = 1
        contributing_article_authors = [author for author, count in author_article_count.items() if count > 2]        
        
        if contributing_article_authors:
            return contributing_article_authors
        else:
            return None
    
    @classmethod
    def top_publisher(cls):
    #! It creates a list called magazines_with_articles by iterating 
    #! over all the magazines associated with the class and filtering out the magazines that have articles
    #! f there are magazines with articles, it returns the magazine
    #! with the most articles based on the length of the articles list.
    #! If there are no magazines with articles, it returns None.
        magazines_with_articles = [magazine for magazine in cls.all if magazine.articles()]
        
        if magazines_with_articles:
            return max(magazines_with_articles, key=lambda magazine: len(magazine.articles()))
        else:
            return None
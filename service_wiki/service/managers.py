from django.db import models


class ContentManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, title):
        try:
            obj = self.get(title=title)
            if obj:
                return obj
        except Exception:
            query = self.filter(title__icontains=title)
            for elem in query:
                if title.lower() == elem.title.lower():
                    return elem

    def create_content(self, data):
        obj = self.model(create_timestamp=data['create_timestamp'], timestamp=data['timestamp'],
                         language=data['language'], wiki=data['wiki'],
                         category=data['category'],
                         title=data['title'], auxiliary_text=data['auxiliary_text'])
        obj.save()
        return obj


class CategoryManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, category_name):
        try:
            obj = self.get(category_name=category_name)
            if obj:
                return self.get(category_name=category_name)
        except Exception:
            query = self.filter(category_name__icontains=category_name)
            for elem in query:
                if category_name.lower() == elem.category_name.lower():
                    return elem


    def create_category(self, name):
        try:
            obj = self.get(category_name=name)
            return obj
        except Exception as err:
            string = self.model(category_name=name)
            string.save()
            return string


class CategoryContentManager(models.Manager):
    use_in_migrations = True

    def create_ship(self, category, content):
        try:
            obj = self.get(category=category, content=content)
            return obj
        except Exception as err:
            string = self.model(category=category, content=content)
            string.save()
            return string

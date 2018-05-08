from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.mary=Editor(first_name='Maryanne',last_name='Njeri',email='m@gmail.com')

    #testing instance checking instance is created
    def test_instance(self):
        self.assertTrue(isinstance(self.mary,Editor))
    #testing save method
    def test_save(self):
        self.mary.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)
#inherits from the testcase class
class TagsTestClass(TestCase):
    def setUp(self):
        self.tag=tags(name='numberone')
    def test_tag_instance(self):
        self.assertTrue(isinstance(self.tag,tags))
    def t_save(self):
        self.tag.save_tag()
        tag=tags.objects.all()
        self.assertTrue(len(tag) >0)
class ArtcleTestClass(TestCase):
    def setUp(self):
        self.mary=Editor(first_name='Mary',last_name='Njeri',email='t@gmail.com')
        self.mary.save_editor()
        #creating a new tag and saving it
        self.new_tag=tags(name='testing')
        self.new_tag.save()
        self.new_article=Article(title='Test Article',post='This is a random article',editor=self.mary)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)
    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    def test_get_news_today(self):
        today_news=Article.todays_news()
        self.assertTrue(len(today_news)>0)

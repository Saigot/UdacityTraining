import handler
from google.appengine.ext import db
import cgi

#----------------Assignment03--------------------#


class BlogEntry(db.Model):
	title = db.StringProperty(required = True)
	body = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

class Assignment03(handler.Handler):
    def get(self):
        #front Page
		b = db.GqlQuery("SELECT * FROM BlogEntry ORDER BY created DESC")
		self.render("A03.html",Blog = b)
		pass
        
class PostHandler(handler.Handler):
    def get(self, id):
		#permalinks go here
		b = BlogEntry.get_by_id(int(id))
		a = b
		self.render("A03PermaLink.html",title=a.title, body=a.body, date="{:%d, %b %Y}".format(a.created))
		
class NewPost(handler.Handler):
	def renderFront(self, title="",body="",error=""):
		self.render("A03NewPost.html",title = title, body=body,error=error)
	def get(self):
		self.renderFront()
	def post(self):
		title = self.request.get("subject")
		body = self.request.get("content")
		if title and body:
			a = BlogEntry(title=title,body=body)
			a.put()
			url = "/A03Blog/"+str(a.key().id())
			self.redirect(url)
		else:
			self.renderFront(title,body,"You need a subject and content")
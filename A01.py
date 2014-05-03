import webapp2
import cgi

formA01="""<form method="post">
	<p> Enter some Text in ROT13 </p>
	<textarea name="text">%(text)s</textarea>
	<input type="submit" name="submit">
	<p> <a href="/"> Home </a></p>
</form>"""
#----------------Assignment01--------------------#
class Assignment01(webapp2.RequestHandler):
    def get(self):
        string = ""
        self.response.write(formA01 %{"text":string})
    def Rot13(self,text):
        newstring =""
        i =0
        while i < len(text):
            if((ord(text[i]) <= ord('z') - 13 and ord(text[i]) >= ord('a')) or (ord(text[i]) <= ord('Z') - 13 and ord(text[i]) >= ord('A'))):
                newstring += chr(ord(text[i]) + 13)
            elif (ord(text[i]) in range(ord('z') - 12, ord('z') +1)):
                newstring += chr(ord('a') + (12 - (ord('z') - ord(text[i]))))
            elif (ord(text[i]) in range(ord('Z') - 12, ord('Z')+1)):
                newstring += chr(ord('A') + (12 - (ord('Z') - ord(text[i]))))
            else:
                newstring += text[i]
            i = i+1
        return cgi.escape(newstring)
    
    def post(self):
        Text = self.request.get("text")
        Text = self.Rot13(Text)
        self.response.write(formA01 %{"text":Text})

import web

urls = (
       '/','index')

movies = [
    {
        'title': 'Forrest Gump',
        'year': 1994,
    },
    {
        'title': 'Titanic',
        'year': 1997,
    }
]

class index:
    def GET(self):
        page = ''
        for m in movies:
            page += '%s (%d)\n' % (m['title'], m['year'])
        return page
    
if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()
import web

db = web.database(dbn='sqlite',db='MovieSite.db')
render = web.template.render('templates/')

urls = (
        '/','index',
        '/movie/(\d+)','movie',
        )
#shiyong list
# movies = [
#          {'title':'Terminator',
#           'year':1984,
#           },
#          {'title':'Judgment Day',
#           'year':1991,
#           }
#          ]

class index:
    def GET(self):
#         page = ''
#         for m in movies:
#             page += '%s(%d)\n'%(m['title'],m['year']) 
#         return page
        movies = db.select('movie')
#         return render.index(movies)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie')[0]['COUNT']
        return render.index(movies, count, None)
    
    def POST(self):
        data = web.input()
        condition = r'title like "%' + data.title + r'%"'
        movies = db.select('movie',where=condition)
#         return render.index(movies)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies, count, data.title)
     
        
    
        
        

class movie:
    def GET(self,movie_id):
        movie_id = int(movie_id)
        movie = db.select('movie',where='id=$movie_id',vars=locals())[0]
#         condition = 'id=' + movie_id
#         movie = db.select('movie',where=condition)[0]
        
        return render.movie(movie)
        
    
if __name__=='__main__':
    app = web.application(urls,globals())
    app.run()
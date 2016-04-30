#coding:utf8
import web

db = web.database(dbn='sqlite', db='MovieSite.db')
render = web.template.render('templates/')

#页面跳转
urls = (
    '/', 'index',
    '/movie/(.*)', 'movie',
    '/cast/(.*)', 'cast',
    '/director/(.*)', 'director',
)


#index页面的请求
class index:
    
    def GET(self):
        movies = db.select('movie')
        return render.index(movies)
#         movies = db.select('movie')
#         count = db.query('SELECT COUNT(*) AS COUNT FROM movie')[0]['COUNT']
#         return render.index(movies, count, None)
    
#     #首页的电影标题搜索   
#     def POST(self):
#         data = web.input()
#         condition = r'TITLE LIKE "%' + data.title + r'%"'
#         movies = db.select('movie', where=condition)
#         count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
#         return render.index(movies, count, data.title)

# #处理请求的类movie
# class movie:
#     def GET(self, movie_id):
#         movie = db.select('movie', where='id=$int(movie_id)', vars=locals())[0]
#         return render.movie(movie)

# #通过主演信息连接电影
# class cast:
#     def GET(self, cast_name):
#         condition = r'CASTS LIKE "%' + cast_name + r'%"'
#         movies = db.select('movie', where=condition)
#         count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
#         return render.index(movies, count, cast_name)

# #通过导演信息连接电影
# class director:
#     def GET(self, director_name):
#         condition = r'DIRECTORS LIKE "%' + director_name + r'%"'
#         movies = db.select('movie', where=condition)
#         count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
#         return render.index(movies, count, director_name)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

class TravelBlog:
    total_blogs = 0

tb1 = TravelBlog()

tb1.name = 'Франция'
tb1.days = 6

tb2 = TravelBlog()

tb2.name = 'Италия'
tb2.days = 5

TravelBlog.total_blogs += 2

print(TravelBlog.total_blogs)
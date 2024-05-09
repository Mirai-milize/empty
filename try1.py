views = [
    {'video_genre': 1, 'rating': 7.226},
    {'video_genre': 3, 'rating': 2.442},
    {'video_genre': 2, 'rating': 8.683},
    {'video_genre': 2, 'rating': 9.676},
    {'video_genre': 3, 'rating': 4.213},
    {'video_genre': 2, 'rating': 3.724},
    {'video_genre': 2, 'rating': 5.553},
    {'video_genre': 4, 'rating': 9.155},
    {'video_genre': 3, 'rating': 4.667},
    {'video_genre': 5, 'rating': 5.972},
    {'video_genre': 5, 'rating': 6.374},
    {'video_genre': 1, 'rating': 3.826},
    {'video_genre': 2, 'rating': 1.732},
    {'video_genre': 1, 'rating': 7.945},
    {'video_genre': 2, 'rating': 1.337},
]

acc = 0
for i in views:
    print(i)
    acc += i['rating']

print(acc/len(views))
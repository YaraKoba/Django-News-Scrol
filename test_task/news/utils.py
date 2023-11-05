

def update_likes(news, data):
    if data.get('action') == 'plus' and data.get('type') in ['likes', 'dislikes']:
        if data['type'] == 'likes':
            news.likes += 1
        else:
            news.dislikes += 1
    elif data.get('action') == 'minus' and data.get('type') in ['likes', 'dislikes']:
        if data['type'] == 'likes':
            news.likes -= 1
        else:
            news.dislikes -= 1

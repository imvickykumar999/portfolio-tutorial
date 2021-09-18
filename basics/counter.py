
def callviews(user):
    from multivicks import crud

    obj = crud.vicks('@Hey_Vicks', link = 'https://new-project-ab9c7-default-rtdb.firebaseio.com/')
    pageviews = obj.pull(child = f'{user}/views')

    if pageviews == None:
        obj.push(data = 1, child = f'{user}/views')
    else:
        obj.push(data = pageviews+1, child = f'{user}/views')

    return pageviews

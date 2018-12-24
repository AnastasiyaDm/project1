from git import Repo

class Shop(object):
    name = 'My Pizza shop!'


def shop_processor(request):
    shop = Shop()
    repo = Repo('.')
    branch_name = repo.active_branch.name
    return {'shop': shop,'branch_name':branch_name}

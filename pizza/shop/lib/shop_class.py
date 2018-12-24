class Shop(object):
    name = 'My Pizza shop!'

from git import Repo

def shop_processor(request):
    shop = Shop()
    repo = Repo('.')
    branch_name = repo.active_branch.name
    return {'shop': shop, 'branch_name': branch_name}

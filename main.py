import os
import requests as rq


def good_or_raise(resp):
    if resp['code'] != 200:
        raise RuntimeError(resp)
    else:
        return resp['data']


def fuckdxx(token=None):
    h = {'token': token}

    resp = rq.post(
        'https://dxx.scyol.com/api/student/studyHostory',
        json={'pageNo': 1, 'pageSize': 1},
        headers=h
    ).json()
    data = good_or_raise(resp)
    id = data[0]['id']
    stage = data[0]['stageId']

    resp = rq.post(
        'https://dxx.scyol.com/api/student/showStudyStageOrg',
        params={'stageId': stage, 'id': id},
        headers=h
    ).json()
    data = good_or_raise(resp)
    payload = {
        i: data[i] for i in \
            ('name', 'tel', 'org', 'lastOrg', 'orgName', 'allOrgName')
    }

    resp = rq.post(
        'https://dxx.scyol.com/api/student/commit',
        json=payload,
        headers=h
    ).json()
    good_or_raise(resp)


if __name__ == '__main__':
    token = os.getenv('TOKEN')
    if token is None:
        print('no token given, abort!')
        exit(1)
    else:
        try:
            fuckdxx(token)
        except RuntimeError as e:
            print(e.args[0])
            exit(1)
        else:
            print('打卡成功')

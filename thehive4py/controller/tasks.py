from typing import List

from .abstract import AbstractController
from ..models import Task
from ..query import *


class TasksController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/task', api)

    def find_all(self, query, **kwargs) -> List[Task]:
        return self._wrap(self._find_all(query, **kwargs), Task)

    def find_one_by(self, query, **kwargs) -> Task:
        return self._wrap(self._find_one_by(query, **kwargs), Task)

    def get_by_id(self, org_id) -> Task:
        return self._wrap(self._get_by_id(org_id), Task)

    def of_case(self, case_id, query={}, **kwargs) -> List[Task]:
        parent_expr = ParentId('case', case_id)

        if query is not None and len(query) is not 0:
            return self.find_all(And(parent_expr, query), **kwargs)
        else:
            return self.find_all(parent_expr, **kwargs)

    def get_waiting(self, query={}, **kwargs) -> List[Task]:
        if query is not None and len(query) is not 0:
            return self.find_all(And({'status': 'Waiting'}, query), **kwargs)
        else:
            return self.find_all({'status': 'Waiting'}, **kwargs)

    def get_by_user(self, user_id, query={}, **kwargs) -> List[Task]:
        if query is not None and len(query) is not 0:
            return self.find_all(And({'owner': user_id}, query), **kwargs)
        else:
            return self.find_all({'owner': user_id}, **kwargs)

    def get_logs(self, task_id, query, **kwargs):
        # TODO
        pass

    def add_log(self, task_id, task_log):
        # TODO
        pass

    def flag(self, task_id, flag):
        # TODO
        pass

    def close(self, task_id):
        # TODO
        pass

    def start(self, task_id):
        # TODO
        pass

    def assign(self, task_id, user_id):
        # TODO
        pass

    def cancel(self, task_id):
        # TODO
        pass